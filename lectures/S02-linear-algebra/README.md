# S02: Vectors, matrices and operators

The third lecture deck, following [S01](../S01-complex-numbers/README.md). It has 38 slides in English: 28 original core slides, 6 visual explanations and 4 appendices. Suggested delivery: two sessions of approximately 70 minutes, with a break after slide 17.

Six numerical illustrations explain component normalization, orthogonal projection, a real unitary rotation, eigenvectors of Pauli X, matrix versus elementwise exponentiation, and X-rotation probabilities. They follow the corresponding derivations. `plot_illustrations.py` reproduces the figures using the course environment. The notes distinguish real-plane examples from complex-vector examples.

1. [PowerPoint with speaker notes](deck.pptx)
2. [PDF slides](deck.pdf)
3. [Slide content with LaTeX expressions](content.md)
4. [Detailed instructor notes and answers](notes.md)
5. [Compilable LaTeX formula source](formulas.tex)

## Learning sequence

The lecture develops vectors and matrix shapes, adjoints, complex inner products, norms and outer products. Four worked examples cover normalization, orthogonality, a rank-one projector and the spectrum of Pauli X. Hermitian and unitary operators lead to spectral decomposition, matrix functions and a step-by-step derivation of an X rotation from the exponential series.

The final section explains dimensionless Hamiltonian exponents, noncommuting matrices and independent numerical checks. NumPy/SciPy and QuTiP implementations are compared with an analytic reference. Appendices provide notation, the orthogonality proof, practice answers and platform-specific commands. The next deck, S03, applies this mathematics to qubit states and Bloch coordinates.

## LaTeX equations

The displayed mathematical formulas are compiled from actual LaTeX using AMS mathematics packages. They include matrix brackets, fractions, sums, bras, kets and superscripts. PowerPoint embeds high-resolution equation images, with the original LaTeX in each slide's notes and in `formulas.tex`. Slide text and code remain editable. Editing an equation means changing its LaTeX and rebuilding the image; these are not native PowerPoint equation objects.

The PDF contains rendered slides for consistent viewing. Use the Markdown or `.tex` source to copy formulas, and the Python files to copy runnable code. Viewing the slides and running the exercises do not require LaTeX.

## Run the learning examples

Use the same environment created in S00. From the repository root:

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe lectures/S02-linear-algebra/examples.py
.\.venv\Scripts\python.exe lectures/S02-linear-algebra/starter.py
.\.venv\Scripts\python.exe lectures/S02-linear-algebra/solution.py
```

Ubuntu Bash:

```bash
./.venv/bin/python lectures/S02-linear-algebra/examples.py
./.venv/bin/python lectures/S02-linear-algebra/starter.py
./.venv/bin/python lectures/S02-linear-algebra/solution.py
```

The examples print reference errors and finish with `S02 examples: PASSED`. The untouched starter intentionally raises `NotImplementedError`. Implement its projector and analytic X rotation, then rerun it. Check the supplied reference separately to obtain `S02 exercises: PASSED`. These are standalone lecture tasks, not additional entries in `qubit_course.labs`.

## Rebuild the equations and slides

`build.mjs` exports `writeSources()` and `build(presentation)`. First regenerate the Markdown and `.tex` sources with `writeSources()`. Then compile and rasterize the equations with `render_formulas.py`. Finally call `build(presentation)` on an empty 1280 × 720 Artifact Session presentation canvas and export the deck.

Authoring requires a TeX distribution providing `pdflatex`, the `amsmath`, `amssymb`, `xcolor`, `geometry` and `fix-cm` packages, Poppler's `pdftoppm`, and the Python packages `pdfplumber` and `pypdf`. These authoring dependencies are separate from the course's simulation dependencies. `equation-map.json` maps the 27 formula pages to their slide numbers. Temporary compiler files go into `runs/s02-tex/` by default. Example, using an environment containing the authoring packages:

```bash
python lectures/S02-linear-algebra/render_formulas.py
```

The renderer preserves a common page width while cropping vertical whitespace, so equations keep a consistent type scale. Rebuild the slide deck after regenerating assets.

Course sources include [Python and mathematics preparation](../../lessons/00b_python_math.md), [states](../../lessons/01_states.md), [dynamics](../../lessons/03_dynamics.md) and [models.py](../../src/qubit_course/models.py). Instructor notes specify the Hermitian, finite-dimensional and time-independent assumptions used in each derivation.
