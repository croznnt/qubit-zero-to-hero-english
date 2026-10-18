# Bell states and classical correlations

## Prerequisites

Lesson 05. Know tensor products and partial traces. Read the [theory lesson](../../lessons/05_entanglement.md) and [conventions](../../docs/CONVENTIONS.md) if you are unsure about units or tensor ordering.

## Physics question

Must two states with identical Z measurement statistics also have identical coherence?

The quantum model uses QuTiP. Time is measured in microseconds, angular frequency in radians per microsecond, and hbar is 1. The UAV assignment cost instead uses abstract units.

## Getting started

Open [starter.py](starter.py), keep the solve(seed=42) function, and replace the TODOs with your calculations. You do not need to repeat installation if you have completed lesson 00. From the repository root, run:

```console
python -m qubit_course.labs check entanglement
```

The untouched starter intentionally reports UNFINISHED with exit code 1. This means the exercise is incomplete, rather than indicating an environment error. Only PASSED confirms that the exercise checks passed.

## Tasks

1. Build the Bell ket from |00> and |11>, normalizing with unit().
2. Obtain reduced using bell.ptrace(0).
3. Calculate entropy_vn of reduced with base=2.
4. Build the classical mixture of |00> and |11>; measure X tensor X for both states.

## Output contract

solve returns a dictionary with the following keys and shapes. Do not only print the results. Keep QuTiP objects in the fields that require them rather than replacing them with NumPy matrices.

```text
bell: two-qubit Qobj ket (4,1)
reduced: Qobj density operator (2,2)
entropy_bits: finite scalar
bell_xx: finite scalar
classical_xx: finite scalar
```

seed controls sampling where applicable; deterministic exercises retain this parameter to use the shared runner. Changing the seed may not change the result of an exercise that performs no sampling.

## Expected results

The reduced state is I/2 and its entropy is 1 bit. Bell XX is 1; classical-mixture XX is 0.

### Hint 1

qt.tensor(zero,zero) preserves two tensor sites. Do not replace it with a four-dimensional ket that loses the dims information.

### Hint 2

The mixture is a weighted sum of projectors; the Bell state is a sum of kets before forming its projector.

## Checks and reference solution

After working through the exercise, rerun the checker. For a missing-key error, compare your dictionary with the output contract. For a shape error, check vector dimensions and the number of time points. For a physics mismatch, check signs, factors of 1/2, and operator ordering before relaxing tolerances.

You can inspect [solution.py](solution.py) and validate the reference solution:

```console
python -m qubit_course.labs check entanglement --solution
python -m qubit_course.cli entanglement --output runs/lab-entanglement-experiment
```

The second command runs the full course experiment and saves its data; the checker only checks your exercise implementation. Choose a new output directory if you have run it before.

## Completion criteria

1. Your implementation returns the required output contract and the checker reports PASSED.
2. You can explain how the formulas and QuTiP operations answer the physics question.
3. You deliberately introduce an incorrect change and understand why the reference checks detect it.

The checker provides learning feedback. It is neither an anti-cheating system nor a guarantee of correctness for every parameter choice. A hardcoded answer may pass some checks without meeting the learning objectives.

## Extension

Change the relative sign of the Bell ket and predict XX. Do not use subsystem entropy to infer entanglement for an arbitrary mixed joint state.
