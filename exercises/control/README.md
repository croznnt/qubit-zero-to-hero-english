# Piecewise pulses and the X-gate objective

## Prerequisites

Lessons 03 and 07. Know propagation and gate_overlap. Read the [theory lesson](../../lessons/07_control.md) and [conventions](../../docs/CONVENTIONS.md) if you are unsure about units or tensor ordering.

## Physics question

Can a pulse with piecewise-varying amplitude still produce the correct total rotation angle?

The quantum model uses QuTiP. Time is measured in microseconds, angular frequency in radians per microsecond, and hbar is 1. The UAV assignment cost instead uses abstract units.

## Getting started

Open [starter.py](starter.py), keep the solve(seed=42) function, and replace the TODOs with your calculations. You do not need to repeat installation if you have completed lesson 00. From the repository root, run:

```console
python -m qubit_course.labs check control
```

The untouched starter intentionally reports UNFINISHED with exit code 1. This means the exercise is incomplete, rather than indicating an environment error. Only PASSED confirms that the exercise checks passed.

## Tasks

1. Keep pulse_xy as six segments with columns ux,uy, each lasting duration_us/6.
2. Initialize unitary to I and build each segment Hamiltonian as (ux*X+uy*Y)/2.
3. Multiply each new segment unitary on the left of the accumulated product.
4. Calculate infidelity = 1-gate_overlap(unitary,X).

## Output contract

solve returns a dictionary with the following keys and shapes. Do not only print the results. Keep QuTiP objects in the fields that require them rather than replacing them with NumPy matrices.

```text
pulse_xy: real numeric array (6,2), abs amplitude <= 2*pi
unitary: Qobj operator (2,2)
infidelity: finite scalar
```

seed controls sampling where applicable; deterministic exercises retain this parameter to use the shared runner. Changing the seed may not change the result of an exercise that performs no sampling.

## Expected results

Infidelity is below 1e-7. The checker validates propagation using an independent NumPy eigendecomposition.

### Hint 1

Do not replace the product of unitary matrices with their sum.

### Hint 2

With uy=0, the total angle is the sum of ux multiplied by 1/6. The example segments add up to an angle of pi.

## Checks and reference solution

After working through the exercise, rerun the checker. For a missing-key error, compare your dictionary with the output contract. For a shape error, check vector dimensions and the number of time points. For a physics mismatch, check signs, factors of 1/2, and operator ordering before relaxing tolerances.

You can inspect [solution.py](solution.py) and validate the reference solution:

```console
python -m qubit_course.labs check control --solution
python -m qubit_course.cli control --output runs/lab-control-experiment
```

The second command runs the full course experiment and saves its data; the checker only checks your exercise implementation. Choose a new output directory if you have run it before.

## Completion criteria

1. Your implementation returns the required output contract and the checker reports PASSED.
2. You can explain how the formulas and QuTiP operations answer the physics question.
3. You deliberately introduce an incorrect change and understand why the reference checks detect it.

The checker provides learning feedback. It is neither an anti-cheating system nor a guarantee of correctness for every parameter choice. A hardcoded answer may pass some checks without meeting the learning objectives.

## Extension

Add a Y control channel so the segments do not commute, and reuse the loss function from the optimization lesson. Run the control experiment to see the complete optimization loop.
