# Integration error and reliability

## Prerequisites

Lessons 03 and 08. Know the analytic Rabi solution. Read the [theory lesson](../../lessons/08_validation.md) and [conventions](../../docs/CONVENTIONS.md) if you are unsure about units or tensor ordering.

## Physics question

Does changing solver tolerance change the error against an independent reference?

The quantum model uses QuTiP. Time is measured in microseconds, angular frequency in radians per microsecond, and hbar is 1. The UAV assignment cost instead uses abstract units.

## Getting started

Open [starter.py](starter.py), keep the solve(seed=42) function, and replace the TODOs with your calculations. You do not need to repeat installation if you have completed lesson 00. From the repository root, run:

```console
python -m qubit_course.labs check convergence
```

The untouched starter intentionally reports UNFINISHED with exit code 1. This means the exercise is incomplete, rather than indicating an environment error. Only PASSED confirms that the exercise checks passed.

## Tasks

1. Build the same Rabi model for both runs.
2. Run sesolve separately for each tolerance, setting both atol and rtol.
3. Calculate the analytic formula only as a reference; do not substitute it for the solver output.
4. Calculate loose_max_error and tight_max_error using max(abs(curve-reference)).

## Output contract

solve returns a dictionary with the following keys and shapes. Do not only print the results. Keep QuTiP objects in the fields that require them rather than replacing them with NumPy matrices.

```text
time_us: numeric array (401,)
loose_p1: numeric array (401,)
tight_p1: numeric array (401,)
loose_max_error: finite scalar
tight_max_error: finite scalar
```

seed controls sampling where applicable; deterministic exercises retain this parameter to use the shared runner. Changing the seed may not change the result of an exercise that performs no sampling.

## Expected results

The tight error is below 1e-7 and no greater than the loose error in this fixed example. This does not require every solver to improve monotonically on every problem.

### Hint 1

Keep time_us, the initial state, and the Hamiltonian fixed; change only the tolerances.

### Hint 2

Increasing the number of plotting points does not necessarily reduce an adaptive solver's internal integration step size.

## Checks and reference solution

After working through the exercise, rerun the checker. For a missing-key error, compare your dictionary with the output contract. For a shape error, check vector dimensions and the number of time points. For a physics mismatch, check signs, factors of 1/2, and operator ordering before relaxing tolerances.

You can inspect [solution.py](solution.py) and validate the reference solution:

```console
python -m qubit_course.labs check convergence --solution
python -m qubit_course.cli convergence --output runs/lab-convergence-experiment
```

The second command runs the full course experiment and saves its data; the checker only checks your exercise implementation. Choose a new output directory if you have run it before.

## Completion criteria

1. Your implementation returns the required output contract and the checker reports PASSED.
2. You can explain how the formulas and QuTiP operations answer the physics question.
3. You deliberately introduce an incorrect change and understand why the reference checks detect it.

The checker provides learning feedback. It is neither an anti-cheating system nor a guarantee of correctness for every parameter choice. A hardcoded answer may pass some checks without meeting the learning objectives.

## Extension

Change integration methods for a model with widely separated time scales, then compare accuracy and runtime.
