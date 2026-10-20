# S00 instructor notes

Suggested session: approximately 60 minutes, with installation time allowed to vary. Slides 1–12 form the core lesson; 13–14 are reference material.

## 1. Your first qubit simulation

Introduce the course as a numerical simulation course using QuTiP. No quantum hardware or cloud account is required for the included examples. The sphere is an abstract illustration, not a device or a calibrated Bloch-sphere plot. This session establishes the computing workflow before S01 introduces complex numbers. Allow about 60 minutes including installation; network and installation time can vary. Ask learners to keep their operating-system guide open. Source: README.md; docs/WINDOWS.md; docs/UBUNTU.md. Cover illustration generated with OpenAI image generation.

## 2. Course map and S00 outcomes

Explain that one framework, QuTiP, carries the numerical work through the course. NumPy and SciPy support arrays and optimization. The research bridge connects to discrete assignment problems relevant to UAV task allocation; a qubit simulation alone is not a swarm simulator. QAOA examples do not establish quantum advantage. Success today means a working local interpreter, four output files and an explanation of probability versus sampled frequency. Source: README.md; lessons/; src/qubit_course/experiments.py.

## 3. The local toolchain

Walkthrough: Windows uses Python 3.13; Ubuntu 24.04 uses its distribution Python 3.12. CI covers Python 3.12 and 3.13 on both operating systems. The package declaration permits Python >=3.11, which is broader than the CI matrix. Verify git --version and the intended Python version. A repository holds source files; a virtual environment holds an interpreter and installed dependencies. Do not copy a virtual environment between computers or operating systems. Source: pyproject.toml; .github/workflows/ci.yml; docs/WINDOWS.md; docs/UBUNTU.md; https://docs.python.org/3/library/venv.html

## 4. Windows setup · PowerShell

Code walkthrough 1. Use native Windows PowerShell. Install Python 3.13 and Git first, then open a new terminal. Explain each line: clone creates a checkout, cd selects it, venv creates a local environment, pip upgrade prepares the installer, editable installation links the package to this checkout. The dev extra includes development tools such as pytest. The commands deliberately call the environment interpreter directly. If py is unavailable, use python only after verifying it is the intended Python installation. Quote paths containing spaces. Do not paste commands into the Python >>> prompt. Source: docs/WINDOWS.md; pyproject.toml.

## 5. Ubuntu setup · Bash

Code walkthrough 1, Ubuntu alternative. Target Ubuntu 24.04. System packages need sudo; the pip command inside the project environment does not. Python3-venv supplies environment creation support. Learners on a different Ubuntu release should verify Python >=3.11 and availability of wheels for the pinned dependencies. Do not use sudo pip or bypass externally-managed-environment protection. The clone command is run once in a chosen parent directory. If the repository already exists, cd into that checkout instead of cloning inside it. Source: docs/UBUNTU.md; https://ubuntu.com/developers/docs/howto/python-setup/; https://docs.python.org/3/library/venv.html

## 6. Interpreter and dependency check

Ask each learner to run only their operating-system command. To inspect the interpreter too, use -c "import sys; print(sys.executable)" with the same executable prefix. Its path must point into this checkout’s .venv. Optional activation is .\.venv\Scripts\Activate.ps1 on Windows and source .venv/bin/activate on Ubuntu. After activation, later lessons use python as shorthand. If PowerShell blocks Activate.ps1, keep the explicit executable path; no machine-wide execution-policy change is needed. If import fails, install with that same interpreter. Source: docs/WINDOWS.md; docs/UBUNTU.md; requirements.txt.

## 7. Repository map

Open the checkout in an editor and locate pyproject.toml, lessons, exercises and src. Show exercises/basics/README.md and starter.py without solving the exercise. Editable installation means changes to src are used by the environment; changes in another checkout are not. Runs are generated locally and ignored by Git. A clean source checkout and a separate output directory make it easier to identify what changed. Written task 1: record the absolute repository path and interpreter path in a personal lab log. Source: repository directory structure; .gitignore; exercises/basics/README.md.

## 8. The four experiment artifacts

Clarify the actual schema: metrics.json contains the random seed and wall time alongside experiment metrics. Metadata contains UTC time, experiment name, Python/platform, source_commit, working_tree_dirty, package versions, units and solver settings where applicable. arrays.npz contains raw arrays; basics includes amplitudes, Bloch coordinates and simulated binary shots. figure.png is a convenience view. Its basics summary mixes numerical metrics with different meanings, so read metrics.json for interpretation. The output argument names the parent directory; the CLI adds basics. Source: src/qubit_course/cli.py; src/qubit_course/experiments.py.

## 9. A reproducible run record

The CLI records working_tree_dirty using git status --porcelain, which can include untracked files as well as tracked edits. A commit hash cannot reconstruct uncommitted changes; preserve those separately when reporting a result. metadata.json may contain null source fields if Git is unavailable. Units describe the course conventions; basics has no time evolution. A fixed seed controls this experiment’s generator but numerical libraries, versions and platforms still matter. wall_seconds is performance information, not a scientific target. The CLI refuses a run when metrics.json already exists in the experiment directory. Source: src/qubit_course/cli.py; docs/CONVENTIONS.md.

## 10. First experiment · basics

Code walkthrough 2. Explain the interpreter prefix, -m module execution, basics experiment selection, seed and output parent. The Windows backtick and Bash backslash continue a command onto the next line; put no trailing spaces after either. The source guide also provides a one-line command. Run once, wait for the printed metrics path, then inspect all four files. Windows: Get-Content runs/first/basics/metrics.json. Ubuntu: cat runs/first/basics/metrics.json. Reusing a completed path is intentionally rejected; use runs/second for another run. Source: docs/WINDOWS.md; docs/UBUNTU.md; src/qubit_course/cli.py.

## 11. Probability and sampled frequency

Read the actual metrics file. The mathematical probability is one quarter; floating-point serialization may show 0.24999999999999994. The supplied reference with seed 42 yields measured_fraction_one 0.262 and 2000 shots. This is 524 outcomes equal to one. Do not require exact equality between the two fractions. Here the code samples a binomial distribution independently; these are simulated measurements, not hardware observations. A norm near one is appropriate for this pure-state example; mixed states introduced later can lie inside the Bloch sphere. Ask: if the seed changes, which quantities should remain approximately or exactly the same? Source: src/qubit_course/experiments.py, basics; reproducible reference metrics accompanying this deck.

## 12. Readiness checkpoint

Give learners five minutes and discuss answers. Q1: the repository is versioned source; .venv is an isolated interpreter/dependency environment that can be recreated. Q2: only 2000 simulated shots were sampled, so the empirical frequency need not equal the underlying probability. Q3: no; the unfinished starter intentionally exits with code 1 until implemented. Task 1 passes when the interpreter is inside the intended checkout and the four artifacts are present under the experiment subdirectory. Task 2 uses --seed 7 --output runs/second; probability and pure-state norm stay effectively unchanged, the seed changes, and the sampled fraction may differ. Do not grade against a hard-coded new fraction. If setup is blocked, use the appendix and platform guides before S01. Source: exercises/basics/README.md; docs/GUIDED_LABS.md; src/qubit_course/experiments.py.

## 13. Appendix · Windows checks

Run the starter command to demonstrate the distinction between an unfinished exercise and environment failure. The reference command checks the supplied solution separately; it does not complete the learner’s starter. Pytest checks the course, not the learner’s progress. If pytest temporary storage is blocked, consult docs/WINDOWS.md for a dedicated writable --basetemp path; pytest clears that directory, so use an expendable location. If a run already exists, select a fresh --output. If py is missing, verify the intended python executable before creating the environment. Source: docs/WINDOWS.md; docs/GUIDED_LABS.md.

## 14. Appendix · Ubuntu checks

The experiment CLI configures Matplotlib with the noninteractive Agg backend and writes figure.png, so an interactive plotting window is not required. An untouched starter reporting UNFINISHED is expected; the supplied reference should pass. Keep apt for OS packages and pip inside the virtual environment for course packages. Never copy the Windows .venv here. If the selected Python has no compatible package wheels, consult the pinned dependency requirements and use a supported interpreter rather than silently changing QuTiP. Source: docs/UBUNTU.md; src/qubit_course/cli.py; https://qutip.readthedocs.io/en/stable/installation.html