"""List and independently check editable course exercises from a source checkout."""
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import uuid

from .lab_checks import validate
from .lab_registry import LABS, exercise_root


def check_submission(name, path, seed=42):
    """Execute an explicitly selected local Python submission; do not sandbox it."""
    module_name = '_qubit_lab_' + uuid.uuid4().hex
    try:
        path = Path(path)
        if not path.is_file():
            return {'lab': name, 'status': 'error', 'message': f'File not found: {path}. Use a source checkout or --file PATH.'}
        spec = importlib.util.spec_from_file_location(module_name, path)
        if spec is None or spec.loader is None:
            return {'lab': name, 'status': 'error', 'message': 'Select a Python .py file.'}
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        solve = getattr(module, 'solve', None)
        if not callable(solve):
            return {'lab': name, 'status': 'error', 'message': 'Define a callable solve(seed=42).'}
        data = solve(seed=seed)
        validate(name, data)
        return {'lab': name, 'status': 'passed', 'message': 'Documented object contracts and physical checks passed.'}
    except NotImplementedError as error:
        return {'lab': name, 'status': 'unfinished', 'message': str(error) or 'Complete the TODOs in solve().'}
    except SyntaxError as error:
        return {'lab': name, 'status': 'error', 'message': f'Syntax error at line {error.lineno}: {error.msg}'}
    except KeyError as error:
        return {'lab': name, 'status': 'failed', 'message': f'Missing return key: {error.args[0]}'}
    except (Exception, SystemExit) as error:
        return {'lab': name, 'status': 'failed', 'message': f'{type(error).__name__}: {error}'}
    finally:
        sys.modules.pop(module_name, None)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('list', help='Show available exercises in learning order.')
    check = commands.add_parser('check', help='Execute and validate a trusted local exercise file.')
    check.add_argument('lab', choices=[*LABS, 'all'])
    check.add_argument('--solution', action='store_true', help='Check the reference instead of the starter.')
    check.add_argument('--file', type=Path, help='Check your own copy; only for one lab, not all.')
    check.add_argument('--seed', type=int, default=42)
    check.add_argument('--report', type=Path, help='Save JSON feedback to a new file; never overwrite.')
    args = parser.parse_args(argv)
    if args.command == 'list':
        for name, (title, _) in LABS.items():
            print(f'{name:14} {title}')
        return 0
    if args.file and (args.lab == 'all' or args.solution):
        parser.error('--file requires a single lab and cannot be combined with --solution.')
    if args.report and args.report.exists():
        parser.error('Report already exists; choose a new path.')
    names = list(LABS) if args.lab == 'all' else [args.lab]
    feedback = []
    for name in names:
        path = args.file if args.file else exercise_root() / name / ('solution.py' if args.solution else 'starter.py')
        result = check_submission(name, path, seed=args.seed)
        feedback.append(result)
        print(f"{name}: {result['status'].upper()} | {result['message']}")
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        # Exclusive creation also protects against a concurrent writer.
        with args.report.open('x', encoding='utf-8') as stream:
            json.dump({'seed': args.seed, 'reference': args.solution, 'results': feedback}, stream, indent=2)
            stream.write('\n')
    return 0 if all(item['status'] == 'passed' for item in feedback) else 1


if __name__ == '__main__':
    raise SystemExit(main())
