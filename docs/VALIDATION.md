# English-edition validation

## Verified Windows and Ubuntu CI

On October 19, 2026, [GitHub Actions run 39176530736](https://github.com/croznnt/qubit-zero-to-hero-english/actions/runs/39176530736) completed successfully for source commit `b42b285a86f20bcc14f2321e199df4a3131c88c5`:

| Operating system | Python | Result |
| :--- | :--- | :--- |
| Windows (`windows-latest`) | 3.12 | Passed |
| Windows (`windows-latest`) | 3.13 | Passed |
| Ubuntu 24.04 | 3.12 | Passed |
| Ubuntu 24.04 | 3.13 | Passed |

Each job installed the pinned dependencies and editable package, ran the full test suite, checked all ten reference solutions, ran all ten complete experiments, and uploaded the run artifacts. The machine-readable record is [ci-result.json](../evidence/english-edition/ci-result.json).

These CI jobs validate the Python package workflow on clean hosted runners. They use actions/setup-python rather than manually provisioning Python with Ubuntu apt or the Windows installer. The platform guides document those separate user setup steps. No local native Ubuntu machine was used.

Fresh local verification on October 18, 2026: **157 tests passed**, including eight original physics tests and 149 guided-lab cases. All ten reference solutions passed the actual feedback CLI. Python compilation checks completed successfully.

Verification reused the original course's isolated environment (Windows, Python 3.13.6, QuTiP 5.3.1), with `PYTHONPATH` explicitly set to this edition's `src`. Neither the original repository nor its installed dependencies were modified. A new clone should create its own virtual environment using this repository's README.

Equivalent commands from an activated environment in this edition are:

```console
python -m pytest -q
python -m qubit_course.labs check all --solution --report runs/english-reference-feedback.json
python -m compileall -q src exercises
```

The sandbox required an explicit writable pytest temporary directory. The primary verification run passed in 6.17 seconds; this is execution evidence, not a performance benchmark. The completed remote CI result is recorded above, separately from this local run.

Scientific Python source, exercise starters and solutions, tests, project dependencies, and historical evidence are byte-identical to the original local course at commit `b5d4fbc`. See the [SHA-256 equivalence record](../evidence/english-edition/source-equivalence.json) and [source provenance](SOURCE_PROVENANCE.md).

On October 19, 2026, explicit Windows and Ubuntu walkthroughs were added. CI was intentionally extended to Windows and Ubuntu 24.04 with Python 3.12 and 3.13, so the workflow is excluded from byte-equivalence claims. No native Ubuntu session was executed locally; the completed remote Ubuntu jobs are documented above.

The archived seed42 outputs below come from the original course. Their metadata refers to the original local implementation commit, not a commit in this independent English repository. Translation does not turn those historical outputs into newly generated simulations.

---

# Preserved original-course validation record

Verified on October 18, 2026, on Windows with Python 3.13.6 and QuTiP 5.3.1. Exact dependency versions are in [requirements-lock.txt](../requirements-lock.txt). These are local results, not yet evidence of Linux CI success or cross-platform equivalence.

## Commands executed

```console
python -m pytest -q
python -m qubit_course.cli all --seed 42 --output runs/verified-seed42
```

The eight physics tests passed. All ten CLI experiments completed and produced metrics, metadata, raw arrays, and a PNG. The source code for this evidence run is commit `9519295084867d0f05d01ed0634e1ed214952ed6`; the recorded working tree was clean. Later documentation and evidence commits do not alter these archived run outputs.

## Measured results for seed 42

| Check | Recorded value | Interpretation |
| :--- | :--- | :--- |
| Rabi maximum analytic error | 6.946e-10 | Numerical population agrees with analytic reference |
| T1 relaxation maximum error | 2.317e-10 | Explicit lowering convention and rate agree with reference |
| Coherence maximum error | 4.115e-10 | Includes both T1 and pure dephasing |
| Density-matrix trace error | 2.220e-16 | Maximum across recorded noise trajectories |
| Bell reduced purity | 0.500000 | Mixed subsystem of a pure entangled pair |
| Nominal control training infidelity | 1.175e-09 | Nominal X-gate objective, not robust performance |
| Baseline mean validation overlap | 0.971390 | Analytic pi pulse on held-out uncertainty grid |
| Robust mean validation overlap | 0.984665 | One seed on one finite uncertainty grid |
| Robust worst validation overlap | 0.971263 | Minimum on that grid, not a continuous-domain guarantee |
| Three-level final leakage | 0.007475 | Two-level pulse transferred to the three-level model |
| QAOA feasible probability | 0.435972 | Most probability mass is still infeasible |
| QAOA sampled feasible fraction | 0.431000 | Finite 2000-shot sample |
| Exact assignment optimum | 2.0 | Obtained by exhaustive enumeration |
| Best sampled feasible cost | 2.0 | Sample included an optimal assignment |

The nominal optimizer's mean held-out overlap (0.971203) is slightly below the analytic baseline. Nominal convergence does not imply robust improvement. The robust example improves this particular grid, but one seed is not a statistical study.

## Evidence and scope

The full local output snapshot is in [evidence/seed42](../evidence/seed42/). A combined metrics file is [evidence/summary.json](../evidence/summary.json). Run metadata records versions, units, seed, source commit, and working-tree state. The JSON metrics and raw arrays are authoritative; the figures summarize them.

Rabi and QAOA plots were visually inspected. Tests cover analytic Rabi dynamics, T1/T2 decay, density physicality, Bell correlations, rotation phase conventions, tensor ordering, QAOA layer equivalence, and exhaustive assignment enumeration.

No hardware, MATLAB runtime, cloud backend, external QAOA library adapter, or UAV simulator was run. The three-level example has not been validated against larger Hilbert cutoffs. Pulse optimization is bounded numerical parameter optimization, not GRAPE. QAOA performance on this toy instance does not demonstrate quantum advantage. The CI workflow is supplied for remote verification; its result must be checked after publication.
