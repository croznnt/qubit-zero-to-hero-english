# Leakage into a third level

## Prerequisites

Lessons 03 and 08. Know ladder operators and rotating frames. Read the [theory lesson](../../lessons/08_validation.md) and [conventions](../../docs/CONVENTIONS.md) if you are unsure about units or tensor ordering.

## Physics question

Does the two-level model pi pulse still transfer all population to |1> when level |2> is present?

The quantum model uses QuTiP. Time is measured in microseconds, angular frequency in radians per microsecond, and hbar is 1. The UAV assignment cost instead uses abstract units.

## Getting started

Open [starter.py](starter.py), keep the solve(seed=42) function, and replace the TODOs with your calculations. You do not need to repeat installation if you have completed lesson 00. From the repository root, run:

```console
python -m qubit_course.labs check leakage
```

The untouched starter intentionally reports UNFINISHED with exit code 1. This means the exercise is incomplete, rather than indicating an environment error. Only PASSED confirms that the exercise checks passed.

## Tasks

1. Build projectors for all three levels.
2. Build H = -alpha*|2><2| + omega*(a+a.dag())/2.
3. Solve with sesolve starting from the three-dimensional |0>, setting atol and rtol to 1e-10.
4. Return p0,p1,p2 so that total population can be checked.

## Output contract

solve returns a dictionary with the following keys and shapes. Do not only print the results. Keep QuTiP objects in the fields that require them rather than replacing them with NumPy matrices.

```text
time_us: numeric array (301,), from 0 to 1
p0: numeric array (301,)
p1: numeric array (301,)
p2: numeric array (301,)
```

seed controls sampling where applicable; deterministic exercises retain this parameter to use the shared runner. Changing the seed may not change the result of an exercise that performs no sampling.

## Expected results

p0+p1+p2 equals 1 within numerical error. The final p2 is about 0.007475 and the final p1 is about 0.988683.

### Hint 1

qt.destroy(3) includes the sqrt(n) factors; this differs from simply using two equal couplings.

### Hint 2

e_ops can be a list of three projectors. A small final p2 does not imply that there was no leakage during the evolution.

## Checks and reference solution

After working through the exercise, rerun the checker. For a missing-key error, compare your dictionary with the output contract. For a shape error, check vector dimensions and the number of time points. For a physics mismatch, check signs, factors of 1/2, and operator ordering before relaxing tolerances.

You can inspect [solution.py](solution.py) and validate the reference solution:

```console
python -m qubit_course.labs check leakage --solution
python -m qubit_course.cli leakage --output runs/lab-leakage-experiment
```

The second command runs the full course experiment and saves its data; the checker only checks your exercise implementation. Choose a new output directory if you have run it before.

## Completion criteria

1. Your implementation returns the required output contract and the checker reports PASSED.
2. You can explain how the formulas and QuTiP operations answer the physics question.
3. You deliberately introduce an incorrect change and understand why the reference checks detect it.

The checker provides learning feedback. It is neither an anti-cheating system nor a guarantee of correctness for every parameter choice. A hardcoded answer may pass some checks without meeting the learning objectives.

## Extension

Extend to four and five levels, and check cutoff convergence before drawing conclusions about an oscillator.
