# Solving Rabi oscillations

## Prerequisites

Lesson 03 and the unit conventions. Know how projector expectations give populations. Read the [theory lesson](../../lessons/03_dynamics.md) and [conventions](../../docs/CONVENTIONS.md) if you are unsure about units or tensor ordering.

## Physics question

Does the numerical solver agree with the analytic solution for a resonantly driven qubit?

The quantum model uses QuTiP. Time is measured in microseconds, angular frequency in radians per microsecond, and hbar is 1. The UAV assignment cost instead uses abstract units.

## Getting started

Open [starter.py](starter.py), keep the solve(seed=42) function, and replace the TODOs with your calculations. You do not need to repeat installation if you have completed lesson 00. From the repository root, run:

```console
python -m qubit_course.labs check rabi
```

The untouched starter intentionally reports UNFINISHED with exit code 1. This means the exercise is incomplete, rather than indicating an environment error. Only PASSED confirms that the exercise checks passed.

## Tasks

1. Build the Hamiltonian omega*X/2.
2. Call qt.sesolve starting from zero, with the projector onto one as e_ops.
3. Set both atol and rtol to 1e-10.
4. Return the solver data in p1; do not replace it with the analytic formula.

## Output contract

solve returns a dictionary with the following keys and shapes. Do not only print the results. Keep QuTiP objects in the fields that require them rather than replacing them with NumPy matrices.

```text
time_us: numeric array (401,), from 0 to 4
p1: numeric array (401,)
```

seed controls sampling where applicable; deterministic exercises retain this parameter to use the shared runner. Changing the seed may not change the result of an exercise that performs no sampling.

## Expected results

P1 is close to 1 at t=1 microsecond and close to 0 at t=2. The maximum error against the analytic solution is below 1e-7.

### Hint 1

e_ops=[one.proj()] produces one expectation series in result.expect[0].

### Hint 2

Use np.real(result.expect[0]); check it independently against sin(omega*time_us/2)**2.

## Checks and reference solution

After working through the exercise, rerun the checker. For a missing-key error, compare your dictionary with the output contract. For a shape error, check vector dimensions and the number of time points. For a physics mismatch, check signs, factors of 1/2, and operator ordering before relaxing tolerances.

You can inspect [solution.py](solution.py) and validate the reference solution:

```console
python -m qubit_course.labs check rabi --solution
python -m qubit_course.cli rabi --output runs/lab-rabi-experiment
```

The second command runs the full course experiment and saves its data; the checker only checks your exercise implementation. Choose a new output directory if you have run it before.

## Completion criteria

1. Your implementation returns the required output contract and the checker reports PASSED.
2. You can explain how the formulas and QuTiP operations answer the physics question.
3. You deliberately introduce an incorrect change and understand why the reference checks detect it.

The checker provides learning feedback. It is neither an anti-cheating system nor a guarantee of correctness for every parameter choice. A hardcoded answer may pass some checks without meeting the learning objectives.

## Extension

Add detuning, derive or look up the general solution, and add an independent reference check.
