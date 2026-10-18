# T1, Tphi, and the density matrix

## Prerequisites

Lesson 04. Know mixed states, traces, and collapse operators. Read the [theory lesson](../../lessons/04_noise.md) and [conventions](../../docs/CONVENTIONS.md) if you are unsure about units or tensor ordering.

## Physics question

How do relaxation and pure dephasing jointly determine T2?

The quantum model uses QuTiP. Time is measured in microseconds, angular frequency in radians per microsecond, and hbar is 1. The UAV assignment cost instead uses abstract units.

## Getting started

Open [starter.py](starter.py), keep the solve(seed=42) function, and replace the TODOs with your calculations. You do not need to repeat installation if you have completed lesson 00. From the repository root, run:

```console
python -m qubit_course.labs check noise
```

The untouched starter intentionally reports UNFINISHED with exit code 1. This means the exercise is incomplete, rather than indicating an environment error. Only PASSED confirms that the exercise checks passed.

## Tasks

1. Build LOWER = |0><1| and collapse operators containing the square roots of the rates.
2. Run relaxation from the density matrix |1><1| and measure P1.
3. Run coherence decay from the density matrix |+><+| and measure X, using the same collapse operators.
4. Store the final relaxation state using store_states=True and return it as rho_final.

## Output contract

solve returns a dictionary with the following keys and shapes. Do not only print the results. Keep QuTiP objects in the fields that require them rather than replacing them with NumPy matrices.

```text
time_us: numeric array (241,), from 0 to 24
p1: numeric array (241,)
sx: numeric array (241,)
rho_final: Qobj density operator (2,2), final relaxation state
```

seed controls sampling where applicable; deterministic exercises retain this parameter to use the shared runner. Changing the seed may not change the result of an exercise that performs no sampling.

## Expected results

P1 follows exp(-t/8), while the X expectation follows exp(-t/T2). rho_final must have trace one, be Hermitian, and have no significantly negative eigenvalues.

### Hint 1

L1 = sqrt(1/t1)*zero*one.dag(); Lphi = sqrt(1/(2*tphi))*Z.

### Hint 2

qt.mesolve accepts c_ops and e_ops as keyword arguments. T2 satisfies 1/T2 = 1/(2*T1)+1/Tphi.

## Checks and reference solution

After working through the exercise, rerun the checker. For a missing-key error, compare your dictionary with the output contract. For a shape error, check vector dimensions and the number of time points. For a physics mismatch, check signs, factors of 1/2, and operator ordering before relaxing tolerances.

You can inspect [solution.py](solution.py) and validate the reference solution:

```console
python -m qubit_course.labs check noise --solution
python -m qubit_course.cli noise --output runs/lab-noise-experiment
```

The second command runs the full course experiment and saves its data; the checker only checks your exercise implementation. Choose a new output directory if you have run it before.

## Completion criteria

1. Your implementation returns the required output contract and the checker reports PASSED.
2. You can explain how the formulas and QuTiP operations answer the physics question.
3. You deliberately introduce an incorrect change and understand why the reference checks detect it.

The checker provides learning feedback. It is neither an anti-cheating system nor a guarantee of correctness for every parameter choice. A hardcoded answer may pass some checks without meeting the learning objectives.

## Extension

Evaluate the control exercise pulse under noise. Choose a state or channel metric; do not apply unitary overlap to a density matrix.
