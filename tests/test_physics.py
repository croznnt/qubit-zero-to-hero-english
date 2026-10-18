import numpy as np
import qutip as qt

from qubit_course.models import (ZERO, ONE, PLUS, LOWER, rotation, density_checks,
                                  gate_overlap, pulse_unitary, assignment_problem, qaoa_state)
from qubit_course.experiments import rabi, noise, entanglement


def test_computational_lowering_convention():
    assert (LOWER * ONE - ZERO).norm() < 1e-12
    assert (LOWER * ZERO).norm() < 1e-12


def test_rotation_global_phase_and_gate_metric():
    unitary = rotation('x', np.pi)
    assert abs(ONE.overlap(unitary * ZERO)) ** 2 > 1 - 1e-12
    assert abs(gate_overlap(unitary, qt.sigmax()) - 1) < 1e-12
    assert abs(gate_overlap(pulse_unitary([[np.pi, 0]]), qt.sigmax()) - 1) < 1e-12


def test_rabi_matches_analytic_population():
    metrics, _ = rabi(42)
    assert metrics['max_analytic_error'] < 1e-7


def test_relaxation_dephasing_and_density_physicality():
    metrics, _ = noise(42)
    assert metrics['max_relaxation_error'] < 1e-7
    assert metrics['max_coherence_error'] < 1e-7
    assert metrics['max_trace_error'] < 1e-9
    assert metrics['minimum_eigenvalue'] > -1e-8


def test_bell_is_not_a_classically_correlated_mixture():
    metrics, _ = entanglement(42)
    assert abs(metrics['reduced_purity'] - 0.5) < 1e-12
    assert abs(metrics['entanglement_entropy_bits'] - 1) < 1e-12
    assert abs(metrics['bell_xx'] - 1) < 1e-12
    assert abs(metrics['classical_xx']) < 1e-12


def test_assignment_feasible_optimum_and_penalty_separation():
    bits, energies, feasible, travel = assignment_problem()
    assert feasible.sum() == 6
    assert travel[feasible].min() == 2
    assert np.array_equal(bits[np.argmin(energies)], [1, 0, 0, 0, 1, 0])
    assert energies[~feasible].min() > energies[feasible].min()


def test_qaoa_zero_angles_and_independent_tensor_order_reference():
    _, energies, _, _ = assignment_problem()
    state = qaoa_state([0, 0], energies)
    assert np.allclose(abs(state.full().ravel()) ** 2, np.full(64, 1 / 64))
    gamma, beta = 0.12, 0.23
    hcost = qt.Qobj(np.diag(energies), dims=[[2] * 6, [2] * 6])
    hmix = sum(qt.tensor([qt.sigmax() if site == i else qt.qeye(2) for site in range(6)]) for i in range(6))
    reference = (-1j * beta * hmix).expm() * (-1j * gamma * hcost).expm() * qt.tensor([PLUS] * 6)
    assert (reference - qaoa_state([gamma, beta], energies)).norm() < 1e-11
    assert abs(state.norm() - 1) < 1e-12


def test_purity_diagnostic():
    checks = density_checks(qt.qeye(2) / 2)
    assert checks['purity'] == 0.5
    assert checks['trace_error'] == 0
