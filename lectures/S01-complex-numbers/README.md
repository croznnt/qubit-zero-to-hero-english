# S01: Complex numbers and phase

The second lecture after [S00](../S00-orientation/README.md), written in English for learners starting with real-number arithmetic. Allow 75 to 90 minutes, including the practice tasks.

1. [PowerPoint](deck.pptx), with editable text, formulas, commands and embedded instructor notes
2. [PDF slides](deck.pdf), rendered for consistent viewing
3. [Slide source and copyable code](content.md)
4. [Detailed instructor notes and answers](notes.md)

## Content

The deck has 20 core slides and 4 appendix slides. It introduces the imaginary unit, Cartesian arithmetic, conjugates, squared magnitude, normalization, polar coordinates, radians, Euler's formula and phase multiplication. Three worked examples show conversion to polar form, a probability contribution, and a phase rotation. Scientific figures show the complex plane, unit circle and an analytic interference probability. A QuTiP calculation independently checks the interference formula.

Appendices provide worked practice answers, global versus relative phase, the optional power-series derivation of Euler's formula, and platform-specific run commands. Vectors, matrices and formal basis transformations follow in S02.

## Run the examples

Use the virtual environment created in S00. Run from the repository root. No additional packages are required.

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe lectures/S01-complex-numbers/examples.py
.\.venv\Scripts\python.exe lectures/S01-complex-numbers/starter.py
.\.venv\Scripts\python.exe lectures/S01-complex-numbers/solution.py
```

Ubuntu Bash:

```bash
./.venv/bin/python lectures/S01-complex-numbers/examples.py
./.venv/bin/python lectures/S01-complex-numbers/starter.py
./.venv/bin/python lectures/S01-complex-numbers/solution.py
```

`examples.py` should finish with `S01 examples: PASSED`. The untouched starter intentionally raises `NotImplementedError`. Complete its three functions, then rerun it to obtain `S01 exercises: PASSED`. Run the reference solution separately after attempting the exercise. These are standalone lecture exercises, not additional entries in `qubit_course.labs`.

The examples use tolerances for floating-point comparisons. A result such as `0.5000000000000001` represents the expected numerical approximation to one half.

## Authoring and sources

`build.mjs` exports `writeSources()` and `build(presentation)` for an empty 1280 × 720 Artifact Session canvas. The Markdown files preserve selectable commands and formula text. The PDF contains rendered slide images; use the PowerPoint or Markdown for editing and copying. Scientific figures are embedded images with reproducible source in `plot_figures.py`. Rebuild them with the same Python environment.

Course sources: [Python and math preparation](../../lessons/00b_python_math.md), [states](../../lessons/01_states.md), and the `basics` experiment in [experiments.py](../../src/qubit_course/experiments.py). Instructor notes identify assumptions and explain the derivations. QuTiP remains the simulation framework used in later lectures.
