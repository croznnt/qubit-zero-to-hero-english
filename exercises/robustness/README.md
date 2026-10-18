# Evaluation on a held-out uncertainty grid

## Prerequisites

Lessons 07 and 08. Know detuning, calibration, and overlap. Read the [theory lesson](../../lessons/08_validation.md) and [conventions](../../docs/CONVENTIONS.md) if you are unsure about units or tensor ordering.

## Physics question

Does an ideal pi pulse retain its quality when parameters deviate from their nominal values?

The quantum model uses QuTiP. Time is measured in microseconds, angular frequency in radians per microsecond, and hbar is 1. The UAV assignment cost instead uses abstract units.

## Getting started

Open [starter.py](starter.py), keep the solve(seed=42) function, and replace the TODOs with your calculations. You do not need to repeat installation if you have completed lesson 00. From the repository root, run:

```console
python -m qubit_course.labs check robustness
```

The untouched starter intentionally reports UNFINISHED with exit code 1. This means the exercise is incomplete, rather than indicating an environment error. Only PASSED confirms that the exercise checks passed.

## Tasks

1. Build validation_grid as a Cartesian product, with detuning in the outer loop.
2. Use pulse_unitary for each detuning and calibration pair.
3. Calculate scores using the squared trace overlap with X.
4. Calculate mean_overlap and worst_overlap over all 16 pairs, without discarding poor results.

## Output contract

solve returns a dictionary with the following keys and shapes. Do not only print the results. Keep QuTiP objects in the fields that require them rather than replacing them with NumPy matrices.

```text
validation_grid: real numeric array (16,2), columns detuning/calibration
scores: real numeric array (16,)
mean_overlap: finite scalar
worst_overlap: finite scalar
```

seed controls sampling where applicable; deterministic exercises retain this parameter to use the shared runner. Changing the seed may not change the result of an exercise that performs no sampling.

## Expected results

The baseline has a mean overlap of about 0.97139 and a worst overlap of about 0.94978. The checker computes its reference using the analytic solution for a constant rotation.

### Hint 1

Use [(d,e) for d in detunings for e in calibrations].

### Hint 2

Worst overlap is min(scores), not max. Do not reuse the training points {-0.4,0,0.4} and {-0.08,0,0.08}.

## Checks and reference solution

After working through the exercise, rerun the checker. For a missing-key error, compare your dictionary with the output contract. For a shape error, check vector dimensions and the number of time points. For a physics mismatch, check signs, factors of 1/2, and operator ordering before relaxing tolerances.

You can inspect [solution.py](solution.py) and validate the reference solution:

```console
python -m qubit_course.labs check robustness --solution
python -m qubit_course.cli robustness --output runs/lab-robustness-experiment
```

The second command runs the full course experiment and saves its data; the checker only checks your exercise implementation. Choose a new output directory if you have run it before.

## Completion criteria

1. Your implementation returns the required output contract and the checker reports PASSED.
2. You can explain how the formulas and QuTiP operations answer the physics question.
3. You deliberately introduce an incorrect change and understand why the reference checks detect it.

The checker provides learning feedback. It is neither an anti-cheating system nor a guarantee of correctness for every parameter choice. A hardcoded answer may pass some checks without meeting the learning objectives.

## Extension

Run the robustness experiment, read pulse_xy from arrays.npz, and replace the baseline pulse to compare both pulses on exactly the same grid.
