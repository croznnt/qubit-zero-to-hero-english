# Learning through exercises with feedback

## Two practice tracks

Experiments through qubit_course.cli are complete simulations for observing phenomena and generating data. Exercises through qubit_course.labs let you implement the calculations you have studied and then verify the results. Both tracks use the same framework, but they do not share grading state or automatically replace each other's code.

| Component | Command | Purpose |
| :--- | :--- | :--- |
| Experiment | python -m qubit_course.cli rabi | Run a complete simulation and save artifacts |
| Your implementation | python -m qubit_course.labs check rabi | Check the starter you have edited |
| Reference | python -m qubit_course.labs check rabi --solution | Verify the included reference solution |

## Workflow for each exercise

1. Read the physics question and predict the result before running code.
2. Read the output contract to identify the required objects, arrays, scalars, and shapes.
3. Open starter.py, implement each calculation, and replace NotImplementedError with the result dictionary.
4. Run the checker. Read its specific feedback before changing the formulas.
5. If you get stuck, read the first hint and then the second. Consult solution.py only after attempting the exercise yourself.
6. Run the corresponding experiment to inspect the full data rather than relying only on PASSED.
7. Complete the extension and record any conditions that the checker does not cover.

## Contracts and exit codes

Every implementation exposes solve(seed=42). Its output dictionary depends on the scientific objective and is documented in each exercise directory's README. Do not merely print the result or replace the interface with a function that does not accept seed.

| Status | Meaning | Exit code when at least one requested exercise has this status |
| :--- | :--- | :--- |
| PASSED | The exercise passes its contract and physics checks | 0 if all requested exercises pass |
| UNFINISHED | solve still raises NotImplementedError | 1 |
| FAILED | Incorrect result, missing data, or runtime failure | 1 |
| ERROR | The implementation cannot be loaded, a callable is missing, or syntax is invalid | 1 |
| CLI argument error | Unknown exercise name or invalid flag | 2 |

check all continues after unsuccessful exercises so you can inspect all feedback. UNFINISHED is the expected result when running check all on untouched starters. Automated tests in tests/test_labs.py verify this behavior, so the test suite can pass even while the starters remain incomplete.

## Independent checks

| Exercise group | Reference checks |
| :--- | :--- |
| State, gates | Amplitude formulas, Born probabilities, unitarity, and global phase |
| Rabi, noise | Analytical Rabi solutions and T1/T2 decay |
| Entanglement | Bell coherence, partial trace, and entropy in bits |
| Control | Operator products computed independently through NumPy eigendecomposition |
| Robustness | Trace-overlap formula for a constant drive |
| Leakage | Spectral propagation of the three-level Hamiltonian |
| Convergence | Direct comparison with the analytical solution at two tolerances |
| Assignment | Bitstring enumeration and the exponential of the full mixer Hamiltonian |

The checker does not use solution.py as its answer key. These checks are still finite: they do not prove correctness for every parameter, assess a learner's reasoning, or prevent hardcoding. If an exercise requires a numerical solver, actually call the solver instead of returning an analytical curve just to pass.

## Runtime scope

The labs require a source checkout with an exercises directory alongside src. From the repository root, use the Python environment prepared according to the [README](../README.md), then install:

```console
python -m pip install -e ".[dev]"
```

If you only have a wheel package without the exercises directory, use --file with a separately saved implementation or obtain a source checkout. Do not assume the package includes every lesson file. See the [ten-exercise index](../exercises/README.md) to select the correct instructions and starter.

Importing qubit_course.labs does not run checks or edit files. When you invoke check, the runner executes the selected Python file in the same process without system isolation. Run only code you trust. KeyboardInterrupt still lets you stop the program.

## Connection to research projects

The control exercise teaches propagation and an objective function; it does not perform optimization. The robustness exercise evaluates a baseline under uncertainty; it is not a multi-seed benchmark. The assignment exercise checks one QAOA layer at fixed angles; it does not claim that a quantum algorithm finds the optimum. The full optimization loops in experiments.py and the capstone are the next step.

## Historical exercise validation

On October 18, 2026, the original edition passed 157 tests: 149 exercise tests and eight original physics tests. All ten reference solutions passed, and all ten existing complete experiments still ran. The source also passed Python compilation checks and wheel building. These are historical results from the original edition, not verification results for this English edition. See [validation](VALIDATION.md) for the evidence and the verification status of this edition.

The seed42 results in evidence and the earlier validation record are retained as historical evidence. New verification of this edition must be distinguished from those earlier results.
