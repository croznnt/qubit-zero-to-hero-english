# Lesson 00. Start with a machine that has no project yet

## Learning objectives

Understand that a terminal is where you enter commands, a project folder holds your code, Python runs that code, and a virtual environment keeps the project's libraries separate. You do not need a quantum computer or a cloud account.

For full platform-specific instructions, choose [Windows PowerShell](../docs/WINDOWS.md) or [Ubuntu Bash](../docs/UBUNTU.md). The examples below call each environment directly.

## Preparation

1. Install Python from [python.org](https://www.python.org/downloads/) and Git from [git-scm.com](https://git-scm.com/downloads). On Windows, check python --version in PowerShell. If your machine only provides py, use py to create the environment, then call the Python executable inside that environment directly.
2. Clone the repository and enter the correct folder as described in the README. Do not type the delimiters surrounding code blocks.
3. Create .venv. Installing libraries may require Internet access, but the simulations run locally after installation.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -c "import qutip; print(qutip.__version__)"
.\.venv\Scripts\python.exe -m qubit_course.cli basics --output runs/lesson00
```

### Ubuntu equivalent

Install Git and Python venv support as shown in the Ubuntu guide, then run from the cloned repository:

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install -e ".[dev]"
./.venv/bin/python -c "import qutip; print(qutip.__version__)"
./.venv/bin/python -m qubit_course.cli basics --output runs/lesson00
```

After activating the environment, you can use the shorter `python` command shown in later lessons. On Windows use `.\.venv\Scripts\Activate.ps1`; on Ubuntu use `source .venv/bin/activate`. If you skip activation, keep calling the full environment interpreter path.

## Read the results

Open runs/lesson00/basics/metrics.json. probability_one is the theoretical probability; measured_fraction_one is the fraction obtained by simulated sampling. Open figure.png to view the plot. arrays.npz stores numerical data, and metadata.json records the execution environment. Running a second time with the same output location is blocked to prevent overwriting.

## Troubleshooting

1. If PowerShell blocks Activate.ps1, call .venv/Scripts/python.exe directly as in the example. You do not need to change the system-wide execution policy.
2. If environment creation reports an ensurepip error, try the commands below. The Python used to invoke pip must already have pip available. Otherwise, use an official Python installation with pip or repair the installation.

```powershell
python -m venv --without-pip .venv
python -m pip --python .venv/Scripts/python.exe install -e ".[dev]"
```

3. If importing qubit_course fails, check that you are using the correct interpreter and have installed the project in editable mode from the folder containing pyproject.toml.
4. If the network cannot download a dependency, fix the connection or proxy for your environment. Do not change versions at random to bypass the error.

## Exercises and completion criteria

1. Run basics with seed 7 and a new output location. Compare the theoretical probability with the measured fraction.
2. Run python -m pytest to execute the existing verification tests.
3. Explain the difference between installing a package and running a program. You are finished when you can create all four output files, read the QuTiP version, and run the tests.

References: [QuTiP installation](https://qutip.readthedocs.io/en/stable/installation.html), [venv](https://docs.python.org/3/library/venv.html).

If Python or vectors are unfamiliar, read the [Python and mathematics preparation lesson](00b_python_math.md) before moving on to lesson 01.
