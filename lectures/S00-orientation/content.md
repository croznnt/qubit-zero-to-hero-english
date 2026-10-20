# S00: Your first qubit simulation

12 core slides and 2 appendix slides. All commands run from the repository root.

## 01. Your first qubit simulation

S00 · Course orientation
Windows and Ubuntu setup





## 02. Course map and S00 outcomes



* **Foundations**: Complex numbers, vectors, qubit states and gates
* **Dynamics**: Hamiltonians, time evolution, noise and validation
* **Research bridge**: Pulse control and a small QAOA assignment example
* **Today**: Create an environment, run basics, explain its outputs



## 03. The local toolchain



* **Git + repository**: Download and track the course source
* **Python + .venv**: Run code in an isolated project environment
* **QuTiP 5.3.1**: Represent quantum states and solve dynamics
* **Terminal + editor**: Run commands and edit exercise files

Install Git and Python first. The package requires Python 3.11 or newer.

## 04. Windows setup · PowerShell



```text
git clone https://github.com/croznnt/qubit-zero-to-hero-english.git
cd qubit-zero-to-hero-english
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
```



Run from the repository root, where pyproject.toml is located.

## 05. Ubuntu setup · Bash



```text
sudo apt update
sudo apt install git python3 python3-venv python3-pip
git clone https://github.com/croznnt/qubit-zero-to-hero-english.git
cd qubit-zero-to-hero-english
python3 -m venv .venv
./.venv/bin/python -m pip install -e ".[dev]"
```



Use a native Ubuntu terminal. Keep pip installations inside .venv.

## 06. Interpreter and dependency check



### Windows · PowerShell

```text
.\.venv\Scripts\python.exe -c "import qutip; print(qutip.__version__)"
```

### Ubuntu · Bash

```text
./.venv/bin/python -c "import qutip; print(qutip.__version__)"
```


Expected QuTiP version: 5.3.1. Activation is optional with these paths.

## 07. Repository map



* **lessons/**: Concept explanations and worked examples
* **exercises/**: Tasks, starters and reference solutions
* **src/qubit_course/**: Reusable models, experiments and command line tools
* **tests/**: Automated checks of numerical behavior
* **runs/**: Generated experiment outputs

Edit source files in the checkout. Treat .venv as disposable.

## 08. The four experiment artifacts



* **metrics.json**: Summary values used to judge the result
* **metadata.json**: Versions, source commit, platform and units
* **arrays.npz**: Compressed NumPy arrays for further analysis
* **figure.png**: A saved visual summary to open locally

Example run directory: runs/first/basics/
The random seed is recorded in metrics.json.

## 09. A reproducible run record



* **Source**: Record the commit and whether the working tree is dirty
* **Environment**: Keep Python and package versions with the result
* **Randomness**: Record the seed and the number of simulated shots
* **Output**: Choose a fresh output directory for each completed run

A fixed seed alone does not guarantee identical results across environments.

## 10. First experiment · basics



### Windows · PowerShell

```text
.\.venv\Scripts\python.exe -m qubit_course.cli basics `
  --seed 42 --output runs/first
```

### Ubuntu · Bash

```text
./.venv/bin/python -m qubit_course.cli basics \
  --seed 42 --output runs/first
```


Choose one operating system. Output: runs/first/basics/

## 11. Probability and sampled frequency



* **probability_one ≈ 0.25**: The state’s probability for outcome 1
* **Measured fraction = 0.262**: Observed fraction in the seed 42 reference run
* **shots = 2000**: Number of simulated binary measurements
* **bloch_norm ≈ 1**: A consistency check for this pure state

Finite samples fluctuate. A different frequency does not by itself mean a bug.

## 12. Readiness checkpoint



* **Question 1**: How does a repository differ from a virtual environment?
* **Question 2**: Why can 0.262 be consistent with probability 0.25?
* **Question 3**: Does an untouched starter reporting UNFINISHED mean setup failed?
* **Task 1**: Record your checkout, interpreter and four artifact paths.
* **Task 2**: Run seed 7 in runs/second and compare the metrics.

Next: S01 introduces complex numbers and the notation behind qubit states.

## 13. Appendix · Windows checks



```text
.\.venv\Scripts\python.exe -m qubit_course.labs check basics
.\.venv\Scripts\python.exe -m qubit_course.labs check basics --solution
.\.venv\Scripts\python.exe -m pytest -q
```

* **UNFINISHED**: Expected for the untouched learner starter
* **No module named qubit_course**: Reinstall editable with this same interpreter
* **Activate.ps1 blocked**: Continue with the explicit python.exe path



## 14. Appendix · Ubuntu checks



```text
./.venv/bin/python -m qubit_course.labs check basics
./.venv/bin/python -m qubit_course.labs check basics --solution
./.venv/bin/python -m pytest -q
```

* **venv creation fails**: Install python3-venv for the selected Python
* **Externally managed environment**: Use .venv/bin/python for pip installation
* **No graphical display**: Open the saved figure.png in an image viewer

