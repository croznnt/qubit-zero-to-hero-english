# Sources and how they are used

The original edition consulted these sources on October 18, 2026. The lessons, exercises, toy models, and source code in this repository are independent implementations. The links below provide API and tool references; they do not imply endorsement of the course by upstream authors.

1. [QuTiP: installation](https://qutip.readthedocs.io/en/stable/installation.html), installation guidance. The course version is pinned through package metadata and the test environment, not inferred from the latest documentation branch.
2. [QuTiP: quantum objects](https://qutip.readthedocs.io/en/stable/guide/guide-basics.html), ket and operator objects.
3. [QuTiP: tensor products and partial traces](https://qutip.readthedocs.io/en/stable/guide/guide-tensor.html), composite-system structure.
4. [QuTiP: dynamics and Lindblad solver](https://qutip.readthedocs.io/en/stable/guide/dynamics/dynamics-master.html), the sesolve and mesolve APIs and open-system assumptions.
5. [QuTiP package on PyPI](https://pypi.org/project/qutip/5.3.1/), the version pinned in this project.
6. [SciPy minimize](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html), the classical optimization API.
7. [OpenQuantumComputing/QAOA](https://github.com/OpenQuantumComputing/QAOA), a related tool for a follow-up project, not a dependency.
8. [QAOA training pipeline](https://github.com/qiskit-community/qaoa_training_pipeline), an external parameter-training tool, not a dependency.

Execution evidence and verification status are recorded in [VALIDATION.md](VALIDATION.md). The capstone proposals have no results yet and require independent testing.
