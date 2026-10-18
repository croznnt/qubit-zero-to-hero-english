# Suggested study plan

The durations below are suggestions, not commitments. If you are new to Python, allow extra time for variables, functions, loops, imports, NumPy arrays, and reading tracebacks.

| Stage | Lessons | Suggested workload | Checkpoint |
| :--- | :--- | :--- | :--- |
| Getting started | 00 | One to two sessions | Run the environment and read JSON |
| Optional preparation | 00b | Two to four sessions | Python functions, complex numbers, and matrix multiplication |
| Foundations | 01 and 02 | Three to four sessions | Calculate probabilities and single-qubit gates yourself |
| Dynamics | 03 and 04 | Four to six sessions | Compare solvers with Rabi, T1, and T2 analytical solutions |
| Composite systems | 05 | Two sessions | Explain tensor products and entanglement |
| Project structure | 06 | Two sessions | Add an experiment with a test |
| Control | 07 and 08 | Four to six sessions | Evaluate nominal and robust pulses and leakage |
| Combinatorial optimization | 09 | Three to four sessions | Decode solutions and check penalties yourself |
| Research | 10 | One to several weeks | Produce a report with baselines and artifacts |

Each session should include three parts: predict by hand, run the code, and explain differences. Do not move on merely because the program runs successfully. Use the completion criteria at the end of each lesson to assess your understanding.

## Pair lessons with exercises

After each lesson, open the corresponding [exercise](../exercises/README.md): basics, gates, rabi, noise, entanglement, control, robustness, leakage, convergence, or assignment. Attempt the starter yourself, use checker feedback to diagnose errors, and only then compare with the solution.

Do not confuse running an experiment with completing your own implementation. python -m qubit_course.cli runs complete example code; python -m qubit_course.labs check evaluates your implementation file. See the [lab guide](GUIDED_LABS.md) for exit codes and ways to save feedback.
