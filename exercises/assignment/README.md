# QAOA for assigning two UAVs

## Prerequisites

Lessons 05 and 09. Know bitstrings, constraints, and cost/mixer layers. Read the [theory lesson](../../lessons/09_qaoa_assignment.md) and [conventions](../../docs/CONVENTIONS.md) if you are unsure about units or tensor ordering.

## Physics question

How can you check penalty energies and operator ordering before optimizing QAOA?

The quantum model uses QuTiP. Time is measured in microseconds, angular frequency in radians per microsecond, and hbar is 1. The UAV assignment cost instead uses abstract units.

## Getting started

Open [starter.py](starter.py), keep the solve(seed=42) function, and replace the TODOs with your calculations. You do not need to repeat installation if you have completed lesson 00. From the repository root, run:

```console
python -m qubit_course.labs check assignment
```

The untouched starter intentionally reports UNFINISHED with exit code 1. This means the exercise is incomplete, rather than indicating an environment error. Only PASSED confirms that the exercise checks passed.

## Tasks

1. Enumerate all 64 six-bit strings in MSB order, then reshape them into 2 UAVs and 3 sectors.
2. Calculate travel, the penalty for violating exactly one sector per UAV, and the penalty for assigning both UAVs to the same sector.
3. Build the feasible mask and find exact_optimum by exhaustive enumeration of the cost without penalties.
4. Initialize the tensor product of six |+> states and calculate zero_angle_probabilities.
5. Apply exp(-i*gamma*Hcost), then the mixer exp(-i*beta*sum(X)); return probabilities.

## Output contract

solve returns a dictionary with the following keys and shapes. Do not only print the results. Keep QuTiP objects in the fields that require them rather than replacing them with NumPy matrices.

```text
bits: numeric array (64,6)
energies: numeric array (64,)
feasible: boolean array (64,)
exact_optimum: finite scalar
zero_angle_probabilities: numeric array (64,)
probabilities: numeric array (64,)
```

seed controls sampling where applicable; deterministic exercises retain this parameter to use the shared runner. Changing the seed may not change the result of an exercise that performs no sampling.

## Expected results

There are six feasible assignments and the exact optimal cost is 2. The chosen nonzero angles produce a nonuniform distribution; zero angles give probability 1/64 for every bitstring. The checker validates the QAOA layer using the matrix exponential of the full mixer Hamiltonian.

### Hint 1

The row penalty is sum((sum_sector(x)-1)**2); the shared-sector penalty is sum(x[0]*x[1]).

### Hint 2

The diagonal cost phase uses exp(-1j*gamma*energies). The mixer factorizes into six exp(-1j*beta*X) factors, with no additional factor of 1/2.

## Checks and reference solution

After working through the exercise, rerun the checker. For a missing-key error, compare your dictionary with the output contract. For a shape error, check vector dimensions and the number of time points. For a physics mismatch, check signs, factors of 1/2, and operator ordering before relaxing tolerances.

You can inspect [solution.py](solution.py) and validate the reference solution:

```console
python -m qubit_course.labs check assignment --solution
python -m qubit_course.cli assignment --output runs/lab-assignment-experiment
```

The second command runs the full course experiment and saves its data; the checker only checks your exercise implementation. Choose a new output directory if you have run it before.

## Completion criteria

1. Your implementation returns the required output contract and the checker reports PASSED.
2. You can explain how the formulas and QuTiP operations answer the physics question.
3. You deliberately introduce an incorrect change and understand why the reference checks detect it.

The checker provides learning feedback. It is neither an anti-cheating system nor a guarantee of correctness for every parameter choice. A hardcoded answer may pass some checks without meeting the learning objectives.

## Extension

Change the cost matrix and recheck the penalties. Then compare the optimizer with the exact optimum before exporting assignments to a SAR simulator.
