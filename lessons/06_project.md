# Lesson 06. Build a verifiable simulation project

## From a code snippet to a project

An attractive plot is not enough for research. You need to know which model ran, its units, the code version, its dependencies, and which checks can detect errors.

1. models.py holds definitions of states, operators, pulses, and the assignment problem. Do not put machine-specific paths here.
2. experiments.py combines models, solvers, parameters, and measurements into experiments returning metrics and arrays.
3. cli.py accepts an experiment name, seed, and output location, then saves artifacts. It does not change the physical equations.
4. tests/test_physics.py checks results against analytical limits or independent representations.

## A run with a record

```console
python -m qubit_course.cli rabi --seed 17 --output runs/project-v1
python -m pytest
```

Open metadata.json to inspect versions and the commit. A commit identifies the code accurately only if the checkout has no uncommitted changes. Before a formal benchmark, record git status and save the diff or commit all relevant changes. runs is not automatically committed because its contents may be large.

```python
import json
import numpy as np
from pathlib import Path
folder = Path('runs/project-v1/rabi')
metrics = json.loads((folder / 'metrics.json').read_text())
arrays = np.load(folder / 'arrays.npz', allow_pickle=False)
print(metrics['max_analytic_error'])
print(arrays['time_us'].shape)
```

## Write meaningful tests

Do more than check whether the program returns data. Check relaxation from |1> toward |0>, the correct coherence-decay coefficient, the Rabi period, tensor ordering, and whether the assignment penalty produces the correct solution. A sign error can still produce smooth data and normalized probabilities.

## Exercises

1. Add a Z-precession experiment initialized in |+>, and check the X expectation against cos(delta*t).
2. Save raw data alongside the plot and add a test against an analytical formula.
3. Run with a new output location and write five sentences describing the model, method, reference comparison, result, and limitations.

You are finished when another person can rerun the command and understand the result without needing a notebook left open on your machine.
