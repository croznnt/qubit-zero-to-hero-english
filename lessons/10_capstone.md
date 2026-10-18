# Lesson 10. Capstone: from simulation to a research question

## Choose a focused question

Choose one of the three capstones below. These are proposed extensions, not completed software features in this repository.

| Direction | Question | Reference comparisons | Results to save |
| :--- | :--- | :--- | :--- |
| A. Robust control | Does ensemble control improve gate overlap on held-out uncertainty settings? | Pi pulse and nominal optimization | Metric distributions across multiple seeds, worst case, runtime |
| B. Leakage | Do an additional Y channel and a leakage penalty reduce population outside the computational space? | Pulse from the two-level model | Final and maximum leakage, cutoff convergence, target population |
| C. UAV assignment | How do small QAOA instances compare with classical methods in feasibility and solution quality? | Exhaustive enumeration or an exact solver, greedy method | Cost, feasibility, shots, total computation time |

## Implementation plan

1. Write one page defining the question, Hamiltonian or cost function, units, limitations, and a falsifiable hypothesis.
2. Fix the baseline, training set, validation set, and budget before running. Do not revise validation after seeing the results and still call it an independent evaluation.
3. Add the model to models.py or a new module, keeping the CLI and outputs consistent.
4. Write at least one analytical or exact check for the new model and one failure-case check.
5. Run multiple seeds, retaining error logs, evaluation counts, and environment information. A fixed seed does not guarantee bitwise-identical results across every platform.
6. Generate tables and figures from saved data rather than manually entering numbers into plots.
7. Write a report covering methods, reference comparisons, results, uncertainty, and limitations. Distinguish simulation results from hardware feasibility.

## Completion criteria

| Criterion | Requirement |
| :--- | :--- |
| Model | Units, basis, signs, and assumptions are defined |
| Verification | An independent exact or analytical case is available |
| Reproducibility | Code commit, dependencies, run commands, and artifacts are recorded |
| Comparison | Methods use the same problem, metrics, and a reasonable budget |
| Reporting | Failures, uncertainty, and untested scope are included |

Meeting all five criteria is the hero level within this course: independently building a small, verifiable simulation study. It does not replace specialist training or scientific peer review.
