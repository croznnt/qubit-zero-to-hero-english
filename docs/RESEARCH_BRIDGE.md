# Connection to the research directions discussed

## Dynamics and optimal control

The [Quantum Dynamics & Optimal Control repository](https://github.com/croznnt/quantum-inspire-python-matlab) catalogs tools and references. This course provides a consistent QuTiP practice path to prepare for that catalog's benchmarks.

| Original benchmark | Foundation implemented here | Further development |
| :--- | :--- | :--- |
| B01 and B02 | Rabi dynamics and bounded X-gate optimization | Dedicated state transfer and comparisons with specialized control algorithms |
| B03 | Ensemble optimization and separate validation | Multiple seeds, larger ensembles, and bandwidth constraints |
| B04 | T1/T2 checks using Lindblad dynamics | Direct optimization of an objective under noise |
| B05 | Bell state and tensor operations | Construct an entangler using an interaction Hamiltonian and controls |
| B06 | Three-level leakage model | Optimize leakage and increase the cutoff |
| B07 | Not implemented | Conditional stochastic dynamics, measurement records, and feedback |

Keep the same equations and metrics when moving to qutip-qtrl or qutip-qoc. The course's SciPy optimizer is a parameter-optimization baseline, not a replacement for those libraries' gradients or algorithms. Create separate environments if their dependencies differ.

## QAOA, UAV assignment, and SAR

The [UAV SAR repository](https://github.com/croznnt/uav-swarm-sar-resources) distinguishes mission simulators, flight simulators, path planning, and quantum optimization. Lesson 09 here provides only a small discrete assignment layer.

1. For OpenQuantumComputing/QAOA, reconcile the natural objective, energy, and optimization sign. Use the same six-bit instance to compare energy values at identical parameters before comparing optimizers.
2. For qaoa_training_pipeline, explicitly convert angle ordering and maximize/minimize conventions. Use an exact statevector to verify that the two evaluators calculate the same quantity.
3. For the PSO repository, use assignments to select sectors or goals, then generate paths separately. Assignment cost is not total path length unless the cost model explicitly represents that quantity.
4. For SWAN, investigate the trajectory-coordination layer if needed, but do not use choreography as a victim-observation model.
5. For DSSE or SwarmSAR, develop a separate adapter for sector IDs, mission timing, sensor information, and UAV state. Do not give the solver access to hidden victim locations that the agents are not allowed to know.

These steps are proposals. This repository currently has no adapters for these tools. No API key or cloud account is needed to complete the local lessons.

## MATLAB and Quantum Inspire

You can convert arrays.npz to a MATLAB-readable format to cross-check calculations or create plots. Verify reshape operations, tensor ordering, and fidelity conventions. The course does not run MATLAB or validate toolbox compatibility.

Quantum Inspire requires a separate circuit or backend integration step; it does not automatically provide waveform control for an arbitrary device. Before submitting circuits, check the supported gates, shot count, and result mapping. Do not describe a local QuTiP simulation as a hardware run.
