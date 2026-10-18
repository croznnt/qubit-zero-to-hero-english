# Hands-on exercises with starter code and reference solutions

Each directory contains starter.py for your implementation, solution.py for reference, and a README.md guide. The exercises progress from building states to validating a small QAOA model, using the same QuTiP framework as the rest of the course.

| Order | Exercise | Main skills |
| :--- | :--- | :--- |
| 01 | [basics](basics/README.md) | Kets, probabilities, Bloch coordinates, and sampling |
| 02 | [gates](gates/README.md) | Unitaries, rotations, and global phase |
| 03 | [rabi](rabi/README.md) | Hamiltonians and analytic solutions |
| 04 | [noise](noise/README.md) | Lindblad dynamics, T1, and T2 |
| 05 | [entanglement](entanglement/README.md) | Tensor products, partial traces, and coherence |
| 06 | [control](control/README.md) | Piecewise propagation and gate objectives |
| 07 | [robustness](robustness/README.md) | Uncertainty grids and worst-case performance |
| 08 | [leakage](leakage/README.md) | Three-level models and population conservation |
| 09 | [convergence](convergence/README.md) | Solver tolerances and independent reference checks |
| 10 | [assignment](assignment/README.md) | Penalties, bit ordering, and one QAOA layer |

## Start an exercise

From the repository root, using the environment with the editable installation:

```console
python -m qubit_course.labs list
python -m qubit_course.labs check basics
```

The second command initially reports UNFINISHED with exit code 1 because the starter has no solution yet. Open basics/starter.py and complete its TODOs using the guide. Each file needs a solve(seed=42) function returning a dictionary that satisfies the exercise contract. Rerun the checker until you understand and fix the cause of each failure.

## Compare with the reference solution

```console
python -m qubit_course.labs check basics --solution
python -m qubit_course.labs check all --solution
```

The checker does not import the reference solution to grade your work. It uses analytic solutions, independent mathematics, or physical-state checks appropriate to each exercise. It provides learning feedback; it is not a secure grader for untrusted code or a system that prevents hardcoded answers.

## Work on a copy

You can keep the starter unchanged and create your own Python file elsewhere:

```powershell
New-Item -ItemType Directory -Path runs -Force | Out-Null
Copy-Item exercises/basics/starter.py runs/my-basics.py
python -m qubit_course.labs check basics --file runs/my-basics.py --seed 7
```

On Ubuntu Bash, the copy workflow is:

```bash
mkdir -p runs
cp exercises/basics/starter.py runs/my-basics.py
./.venv/bin/python -m qubit_course.labs check basics --file runs/my-basics.py --seed 7
```

The shorter `python` commands in this guide assume an activated environment. See the [Windows](../docs/WINDOWS.md) or [Ubuntu](../docs/UBUNTU.md) walkthrough for explicit interpreter paths.

Do not combine --file with --solution or all. The runner executes Python code from your selected file; only run submissions and source code you trust.

## Save feedback

```console
python -m qubit_course.labs check all --solution --report runs/lab-feedback.json
```

The runner refuses to overwrite an existing report. Choose a new name for the next run. The report only confirms exercise checks; it does not replace the research metadata and artifacts produced by the experiment CLI.

Continue with the [guided lab workflow](../docs/GUIDED_LABS.md).
