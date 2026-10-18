"""Regression tests for learner execution, physics feedback, and the lab CLI."""
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest
import qutip as qt

from qubit_course import labs
from qubit_course.lab_checks import validate
from qubit_course.lab_registry import LABS, exercise_root


@pytest.fixture
def submission(tmp_path):
    def write(source):
        path = tmp_path / 'submission.py'
        path.write_text(source, encoding='utf-8')
        return path
    return write


def solution_data(name):
    spec = importlib.util.spec_from_file_location('reference_' + name, exercise_root() / name / 'solution.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.solve(seed=42)


@pytest.mark.parametrize('name', LABS)
def test_reference_passes_independent_physics(name):
    result = labs.check_submission(name, exercise_root() / name / 'solution.py')
    assert result['status'] == 'passed', result
    assert result['lab'] == name


@pytest.mark.parametrize('name', LABS)
def test_untouched_starter_is_unfinished(name):
    result = labs.check_submission(name, exercise_root() / name / 'starter.py')
    assert result['status'] == 'unfinished', result
    assert result['message']


@pytest.mark.parametrize(('source', 'status', 'diagnostic'), [
    ('answer = 42', 'error', 'callable solve'),
    ('solve = 42', 'error', 'callable solve'),
    ('def solve(seed=42): return {}', 'failed', 'Missing return key: state'),
    ('def solve(seed=42): return []', 'failed', 'dictionary'),
    ('def solve(: pass', 'error', 'Syntax error at line 1'),
    ('import nonexistent_qubit_course_test_dependency', 'failed', 'ModuleNotFoundError'),
    ('def solve(seed=42): raise RuntimeError("student failure")', 'failed', 'RuntimeError: student failure'),
    ('def solve(seed=42): raise SystemExit(7)', 'failed', 'SystemExit: 7'),
    ('raise SystemExit(3)', 'failed', 'SystemExit: 3'),
    ('def solve(seed=42): raise NotImplementedError("finish task")', 'unfinished', 'finish task'),
])
def test_submission_failures_are_actionable(submission, source, status, diagnostic):
    before = {key for key in sys.modules if key.startswith('_qubit_lab_')}
    result = labs.check_submission('basics', submission(source))
    assert result['status'] == status
    assert diagnostic in result['message']
    assert {key for key in sys.modules if key.startswith('_qubit_lab_')} == before


def test_missing_file_and_non_python_extension(tmp_path):
    assert labs.check_submission('basics', tmp_path / 'missing.py')['status'] == 'error'
    path = tmp_path / 'submission.txt'
    path.write_text('anything', encoding='utf-8')
    assert 'Python .py' in labs.check_submission('basics', path)['message']


@pytest.mark.parametrize(('field', 'value', 'diagnostic'), [
    ('probabilities', np.array([np.nan, .25]), 'NaN or infinity'),
    ('probabilities', np.array([np.inf, .25]), 'NaN or infinity'),
    ('probabilities', np.array([[.75, .25]]), 'expected shape'),
    ('probabilities', np.array(['a', 'b']), 'numeric array'),
    ('probabilities', np.array([.5, .5]), 'squared amplitude'),
    ('state', qt.basis(3, 0), 'expected shape'),
    ('state', np.array([1, 0]), 'QuTiP Qobj'),
    ('state', qt.basis(2, 0), 'Relative phase'),
    ('state', 2 * qt.basis(2, 0), 'Normalize'),
    ('counts', np.array([1500.5, 499.5]), 'nonnegative integers'),
    ('counts', np.array([1500, 400]), 'sum to 2000'),
    ('counts', np.array([0, 2000]), 'Shot frequencies'),
])
def test_basics_rejects_invalid_data(field, value, diagnostic):
    data = solution_data('basics')
    data[field] = value
    with pytest.raises(ValueError, match=diagnostic):
        validate('basics', data)


@pytest.mark.parametrize(('name', 'field', 'value'), [
    ('gates', 'hadamard', qt.qeye(2)),
    ('rabi', 'p1', np.zeros(401)),
    ('noise', 'sx', np.ones(241)),
    ('entanglement', 'classical_xx', 1),
    ('control', 'unitary', qt.qeye(2)),
    ('robustness', 'worst_overlap', 0),
    ('leakage', 'p2', np.zeros(301)),
    ('convergence', 'tight_max_error', 1),
    ('assignment', 'exact_optimum', 0),
])
def test_each_other_lab_rejects_wrong_physics(name, field, value):
    data = solution_data(name)
    data[field] = value
    with pytest.raises(ValueError):
        validate(name, data)


@pytest.mark.parametrize('argv', [
    [], ['check'], ['check', 'unknown'], ['check', 'basics', '--seed', 'not-an-int'],
    ['check', 'all', '--file', 'x.py'],
    ['check', 'basics', '--file', 'x.py', '--solution'],
])
def test_cli_rejects_invalid_arguments(argv):
    with pytest.raises(SystemExit) as error:
        labs.main(argv)
    assert error.value.code == 2


def test_list_learning_order(capsys):
    assert labs.main(['list']) == 0
    assert [line.split()[0] for line in capsys.readouterr().out.splitlines()] == list(LABS)


def test_custom_file_seed_and_report(submission, tmp_path):
    path = submission('def solve(seed=42):\n    raise NotImplementedError(f"seed={seed}")\n')
    report = tmp_path / 'nested' / 'feedback.json'
    assert labs.main(['check', 'basics', '--file', str(path), '--seed', '73', '--report', str(report)]) == 1
    payload = json.loads(report.read_text(encoding='utf-8'))
    assert payload == {'seed': 73, 'reference': False, 'results': [
        {'lab': 'basics', 'status': 'unfinished', 'message': 'seed=73'}]}
    before = report.read_bytes()
    with pytest.raises(SystemExit) as error:
        labs.main(['check', 'basics', '--report', str(report)])
    assert error.value.code == 2
    assert report.read_bytes() == before


def test_all_solutions_report(tmp_path):
    report = tmp_path / 'references.json'
    assert labs.main(['check', 'all', '--solution', '--report', str(report)]) == 0
    payload = json.loads(report.read_text(encoding='utf-8'))
    assert payload['reference'] is True
    assert [item['lab'] for item in payload['results']] == list(LABS)
    assert all(item['status'] == 'passed' for item in payload['results'])


def test_all_continues_after_failed_submission(monkeypatch, capsys):
    called = []
    def check(name, path, seed=42):
        called.append(name)
        return {'lab': name, 'status': 'failed' if len(called) == 1 else 'passed', 'message': 'feedback'}
    monkeypatch.setattr(labs, 'check_submission', check)
    assert labs.main(['check', 'all']) == 1
    assert called == list(LABS)
    assert len(capsys.readouterr().out.splitlines()) == 10


def test_module_entry_point():
    result = subprocess.run([sys.executable, '-m', 'qubit_course.labs', 'list'],
                            text=True, capture_output=True, check=False)
    assert result.returncode == 0, result.stderr
    assert 'assignment' in result.stdout

@pytest.mark.parametrize('name', LABS)
def test_each_lab_rejects_missing_fields(name):
    with pytest.raises(KeyError):
        validate(name, {})


def test_all_starters_exit_nonzero_and_report_every_lab(tmp_path):
    report = tmp_path / 'starters.json'
    assert labs.main(['check', 'all', '--report', str(report)]) == 1
    results = json.loads(report.read_text(encoding='utf-8'))['results']
    assert len(results) == 10
    assert all(item['status'] == 'unfinished' for item in results)


def test_unknown_validator_name():
    with pytest.raises(ValueError, match='Unknown lab'):
        validate('nonexistent', {})

SCALAR_FIELDS = [
    ('entanglement', 'entropy_bits'),
    ('entanglement', 'bell_xx'),
    ('entanglement', 'classical_xx'),
    ('control', 'infidelity'),
    ('robustness', 'mean_overlap'),
    ('robustness', 'worst_overlap'),
    ('convergence', 'loose_max_error'),
    ('convergence', 'tight_max_error'),
    ('assignment', 'exact_optimum'),
]


@pytest.mark.parametrize(('name', 'field'), SCALAR_FIELDS)
@pytest.mark.parametrize('shape', [(1,), (1, 1)])
def test_scalar_fields_reject_broadcastable_wrapped_values(name, field, shape):
    data = solution_data(name)
    data[field] = np.asarray(data[field]).reshape(shape)
    with pytest.raises(ValueError, match=f'{field}: expected a scalar'):
        validate(name, data)


@pytest.mark.parametrize(('name', 'field'), SCALAR_FIELDS)
@pytest.mark.parametrize('value', [np.nan, np.inf, -np.inf, 1 + 0j, True, '1'])
def test_scalar_fields_require_finite_real_numeric_values(name, field, value):
    data = solution_data(name)
    data[field] = value
    with pytest.raises(ValueError, match=field):
        validate(name, data)


def test_feasible_mask_requires_boolean_dtype():
    data = solution_data('assignment')
    data['feasible'] = data['feasible'].astype(float)
    with pytest.raises(ValueError, match='feasible: return a boolean array'):
        validate('assignment', data)


def test_relaxation_final_density_rejects_unphysical_generated_coherence():
    data = solution_data('noise')
    # Still Hermitian, trace one, positive, and with the correct population.
    # Such coherence cannot be generated by relaxation from the excited state.
    rho = data['rho_final'] + 0.1 * qt.sigmax()
    assert np.linalg.eigvalsh(rho.full()).min() > 0
    assert np.isclose(rho.tr(), 1)
    data['rho_final'] = rho
    with pytest.raises(ValueError, match='rho_final'):
        validate('noise', data)
