# Windows walkthrough (PowerShell)

This guide covers a native Windows installation. Use PowerShell for the commands below. You do not need WSL, a GPU, a cloud account, or a quantum computer for the included examples.

## 1. Install Python and Git

Install Python 3.13 from [python.org](https://www.python.org/downloads/windows/) and Git from [git-scm.com](https://git-scm.com/downloads/win). Open a new PowerShell window after installation.

```powershell
py -3.13 --version
git --version
```

If the `py` launcher is unavailable, check `python --version`. You can use `python` instead of `py -3.13` below if it identifies the intended Python installation. The package requires Python 3.11 or newer; this walkthrough targets 3.13, while CI covers 3.12 and 3.13.

## 2. Clone the English edition

```powershell
git clone https://github.com/croznnt/qubit-zero-to-hero-english.git
cd qubit-zero-to-hero-english
```

Keep paths containing spaces inside quotes when using `cd`. Commands below assume you are in the repository root, where `pyproject.toml` is located.

## 3. Create an isolated environment

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -c "import sys, qutip; print(sys.executable); print(qutip.__version__)"
```

The interpreter path should point inside this checkout's `.venv`, and the QuTiP version should be `5.3.1`. Calling the interpreter directly avoids activation-policy problems. Never copy a `.venv` from another checkout or from Ubuntu; create it again at the destination.

Optional activation:

```powershell
.\.venv\Scripts\Activate.ps1
```

After successful activation, `python` is shorthand for this environment's interpreter. Later lessons use that shorthand. If activation is blocked, continue using `.\.venv\Scripts\python.exe`; no system-wide policy change is needed.

## 4. Run the first experiment

```powershell
.\.venv\Scripts\python.exe -m qubit_course.cli basics --seed 42 --output runs/windows-first
Get-Content runs/windows-first/basics/metrics.json
```

The output folder contains `metrics.json`, `metadata.json`, `arrays.npz`, and `figure.png`. Open the image in File Explorer. Choose a new `--output` directory for each completed run; the CLI protects existing results.

## 5. Complete a guided exercise

```powershell
.\.venv\Scripts\python.exe -m qubit_course.labs list
.\.venv\Scripts\python.exe -m qubit_course.labs check basics
```

The second command intentionally reports `UNFINISHED` and exits with code 1 before you implement the starter. Read [the basics task](../exercises/basics/README.md), edit its `starter.py`, and rerun the command. This expected unfinished result is not a failed installation.

To work on a copy:

```powershell
New-Item -ItemType Directory -Path runs -Force | Out-Null
Copy-Item exercises/basics/starter.py runs/my-basics.py
.\.venv\Scripts\python.exe -m qubit_course.labs check basics --file runs/my-basics.py
```

Check the supplied answers separately:

```powershell
.\.venv\Scripts\python.exe -m qubit_course.labs check all --solution --report runs/windows-reference-feedback.json
```

All ten references should report `PASSED`. The runner executes the selected Python file in the same process, so use only trusted submissions.

## 6. Verify the course and run the full examples

```powershell
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m qubit_course.cli all --seed 42 --output runs/windows-full
```

The current test suite contains 157 cases. Full examples include bounded pulse optimization and a six-qubit QAOA assignment problem. Review optimizer success flags and feasibility metrics rather than interpreting completion as proof of an optimal solution.

## Troubleshooting

| Symptom | Check or action |
| :--- | :--- |
| `python` opens the Store or identifies another version | Use `py -3.13`, or inspect the installed interpreter and its path |
| `Activate.ps1` is blocked | Call `.\.venv\Scripts\python.exe` directly |
| `No module named qubit_course` | Install editable from the repository root using the same interpreter |
| `ensurepip` fails while creating the environment | Repair Python with pip, or use the fallback below if your base Python already has pip |
| Pytest cannot create its temporary directory | Use a dedicated writable path such as `--basetemp=runs/pytest-windows`; pytest clears that directory, so never point it at valuable files |
| A report or run already exists | Select a new report filename or output directory |
| Package installation needs a compiler unexpectedly | Check Python version and wheel availability; use a supported Python version rather than silently changing the physics dependency |

Fallback for an environment without pip:

```powershell
py -3.13 -m venv --without-pip .venv
py -3.13 -m pip --python .venv/Scripts/python.exe install -e ".[dev]"
```

This fallback requires pip in the base interpreter. It does not download a replacement Python installation.

## Next steps

Continue with [Lesson 00](../lessons/00_setup.md), [the learning path](../README.md#-learning-path), and [the exercise index](../exercises/README.md). See [validation](VALIDATION.md) for measured verification status; a documented command is distinct from a successful run on a particular machine.

Reference: [Python virtual environments](https://docs.python.org/3/library/venv.html).
