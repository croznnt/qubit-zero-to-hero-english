# Ubuntu walkthrough (Bash)

This guide targets Ubuntu 24.04 LTS with its system Python, or another Ubuntu release providing Python 3.11 or newer. Ubuntu 22.04's default Python 3.10 does not satisfy this project's minimum; use an appropriate supported Python installation before continuing. CI covers Ubuntu 24.04 with Python 3.12 and 3.13.

The included examples run on a CPU. You do not need CUDA, a desktop session, a cloud account, or quantum hardware. Plotting uses a noninteractive backend and saves PNG files.

## 1. Install development prerequisites

Open Terminal and run:

```bash
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip
python3 --version
git --version
```

Confirm that Python is at least 3.11 before proceeding. Keep distribution-managed Python packages separate from project dependencies; use a virtual environment for this course.

## 2. Clone the English edition

```bash
git clone https://github.com/croznnt/qubit-zero-to-hero-english.git
cd qubit-zero-to-hero-english
```

All following commands assume the repository root contains `pyproject.toml` and the `exercises` directory. Linux paths are case-sensitive: `README.md` and `readme.md` are different names.

## 3. Create an isolated environment

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/python -m pip install -e ".[dev]"
./.venv/bin/python -c "import sys, qutip; print(sys.executable); print(qutip.__version__)"
```

The interpreter should be inside this checkout's `.venv`, and QuTiP should report `5.3.1`. No `sudo pip` is needed. Do not copy an environment from Windows or another checkout: recreate it for this interpreter and location.

Optional activation:

```bash
source .venv/bin/activate
```

After activation, the later lessons' `python` commands refer to this environment. You can always use `./.venv/bin/python` explicitly instead.

## 4. Run and inspect the first experiment

```bash
./.venv/bin/python -m qubit_course.cli basics --seed 42 --output runs/ubuntu-first
cat runs/ubuntu-first/basics/metrics.json
ls runs/ubuntu-first/basics
```

The folder contains `metrics.json`, `metadata.json`, `arrays.npz`, and `figure.png`. On a desktop, open the image using your file manager. On a headless machine, transfer the saved image using your normal file-transfer workflow; interactive display is not required to run the simulations.

Choose a new output directory for later completed runs. The program deliberately refuses to overwrite an existing completed result.

## 5. Complete a guided exercise

```bash
./.venv/bin/python -m qubit_course.labs list
./.venv/bin/python -m qubit_course.labs check basics
```

An untouched starter reports `UNFINISHED` with exit code 1. Read [the basics task](../exercises/basics/README.md), implement its `starter.py`, and rerun. The expected unfinished result is not an installation failure.

To work on a copy:

```bash
mkdir -p runs
cp exercises/basics/starter.py runs/my-basics.py
./.venv/bin/python -m qubit_course.labs check basics --file runs/my-basics.py
```

Check the supplied answers separately:

```bash
./.venv/bin/python -m qubit_course.labs check all --solution --report runs/ubuntu-reference-feedback.json
```

All ten references should report `PASSED`. The runner executes Python code from the selected file; use only submissions you trust.

## 6. Verify and run all examples

```bash
./.venv/bin/python -m pytest -q
./.venv/bin/python -m qubit_course.cli all --seed 42 --output runs/ubuntu-full
```

The current test suite has 157 cases. Exact floating-point outputs and optimizer termination can differ across platforms. Compare physically meaningful errors, tolerances, and feasibility rather than expecting every byte of an output file to match Windows.

## Troubleshooting

| Symptom | Check or action |
| :--- | :--- |
| `ensurepip` or virtual-environment creation fails | Install the `python3-venv` package matching the interpreter; for a separately installed Python, use that installation's matching venv support |
| `externally-managed-environment` | Use `./.venv/bin/python -m pip`; do not install into system Python or bypass its management policy |
| `No module named qubit_course` | Reinstall editable from the repository root using this environment's interpreter |
| File or directory not found | Check the current working directory and filename capitalization |
| No display is available | The experiment CLI already uses a noninteractive plotting backend; inspect saved figures later |
| Pytest cannot write temporary files | Use a dedicated writable directory with `--basetemp=runs/pytest-ubuntu`; pytest clears it, so keep other data elsewhere |
| A report or run already exists | Use a new filename or output directory |
| A dependency starts compiling | Check interpreter/platform wheel availability; native build dependencies may be required, and source-build support is not verified by these instructions |

On WSL, follow this Ubuntu guide inside the Linux terminal and create a separate Linux `.venv`. Do not invoke the Windows environment's executable from the Linux workflow.

## Next steps

Continue with [Lesson 00](../lessons/00_setup.md), [the learning path](../README.md#-learning-path), and [the exercise index](../exercises/README.md). See [validation](VALIDATION.md) for the distinction between local checks and remote Ubuntu CI results.

References: [Ubuntu Python environment setup](https://ubuntu.com/developers/docs/howto/python-setup/), [Python virtual environments](https://docs.python.org/3/library/venv.html).
