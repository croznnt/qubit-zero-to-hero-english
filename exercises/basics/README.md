# Qubit states and measurement sampling

## Prerequisites

Lessons 00b and 01. Know complex numbers, norms, and squared magnitudes. Read the [theory lesson](../../lessons/01_states.md) and [conventions](../../docs/CONVENTIONS.md) if you are unsure about units or tensor ordering.

## Physics question

How do complex amplitudes determine measurement probabilities and Bloch coordinates?

The quantum model uses QuTiP. Time is measured in microseconds, angular frequency in radians per microsecond, and hbar is 1. The UAV assignment cost instead uses abstract units.

## Getting started

Open [starter.py](starter.py), keep the solve(seed=42) function, and replace the TODOs with your calculations. You do not need to repeat installation if you have completed lesson 00. From the repository root, run:

```console
python -m qubit_course.labs check basics
```

The untouched starter intentionally reports UNFINISHED with exit code 1. This means the exercise is incomplete, rather than indicating an environment error. Only PASSED confirms that the exercise checks passed.

## Tasks

1. Build state = cos(theta/2)|0> + exp(i*phi)sin(theta/2)|1>. Preserve the relative phase.
2. Calculate probabilities using the projector for each basis state, ordered as 0 then 1.
3. Calculate bloch in X, Y, Z order.
4. Use numpy.random.default_rng(seed) to draw 2000 independent shots and count the outcomes in counts.

## Output contract

solve returns a dictionary with the following keys and shapes. Do not only print the results. Keep QuTiP objects in the fields that require them rather than replacing them with NumPy matrices.

```text
state: Qobj ket (2,1)
probabilities: numeric array (2,)
bloch: numeric array (3,)
counts: nonnegative integer array (2,), total 2000
```

seed controls sampling where applicable; deterministic exercises retain this parameter to use the shared runner. Changing the seed may not change the result of an exercise that performs no sampling.

## Expected results

The probabilities are [0.75,0.25]; the Bloch vector has norm 1. The shot frequencies fluctuate around these probabilities and need not equal 0.25 exactly.

### Hint 1

The amplitude b needs the factor exp(1j*phi); its probability is abs(b)**2.

### Hint 2

qt.expect(ket.proj(), state) gives the probability. Use rng.binomial(shots, p1), then obtain the number of 0 outcomes by subtraction.

## Checks and reference solution

After working through the exercise, rerun the checker. For a missing-key error, compare your dictionary with the output contract. For a shape error, check vector dimensions and the number of time points. For a physics mismatch, check signs, factors of 1/2, and operator ordering before relaxing tolerances.

You can inspect [solution.py](solution.py) and validate the reference solution:

```console
python -m qubit_course.labs check basics --solution
python -m qubit_course.cli basics --output runs/lab-basics-experiment
```

The second command runs the full course experiment and saves its data; the checker only checks your exercise implementation. Choose a new output directory if you have run it before.

## Completion criteria

1. Your implementation returns the required output contract and the checker reports PASSED.
2. You can explain how the formulas and QuTiP operations answer the physics question.
3. You deliberately introduce an incorrect change and understand why the reference checks detect it.

The checker provides learning feedback. It is neither an anti-cheating system nor a guarantee of correctness for every parameter choice. A hardcoded answer may pass some checks without meeting the learning objectives.

## Extension

Change phi while keeping theta fixed, and compare Z measurements with X measurements. Add a check for global-phase invariance.
