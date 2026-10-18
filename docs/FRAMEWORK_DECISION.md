# One quantum framework throughout

## Decision

Use QuTiP 5.3.1 for every quantum object: kets, density matrices, operators, tensor products, Schrödinger evolution, Lindblad evolution, and QAOA states. NumPy handles data, SciPy performs classical optimization, and Matplotlib produces plots. This is one quantum framework supported by scientific computing libraries.

This choice prioritizes the dynamics, pulse design, and quantum control direction of the [original research catalog](https://github.com/croznnt/quantum-inspire-python-matlab). The required operations are documented in the [QuTiP guide](https://qutip.readthedocs.io/en/stable/guide/guide-basics.html). The final QAOA lesson is built directly with QuTiP operators to preserve the same state representation.

## Tradeoffs

| Criterion | Course decision |
| :--- | :--- |
| Learning kets, operators, and Hamiltonians | QuTiP represents these objects directly |
| Noise and open systems | Use mesolve with collapse operators |
| Pulse control | Use QuTiP for propagation and SciPy for optimization |
| Small QAOA circuits | Implement cost and mixer layers with QuTiP |
| Circuit compilation or hardware execution | Leave these to a follow-up project |
| UAV search-and-rescue simulation | Use a dedicated simulator in another project that consumes assignment results |
| MATLAB | Use it to cross-check equations if needed; it is not required for the course |

Qiskit is worth considering when the main objective shifts to circuit compilation, transpilation, or the surveyed QAOA ecosystem. This course does not require Qiskit and does not claim binary compatibility with those QAOA libraries.

## Implementation boundaries

The pulse optimizer uses bounded parameter optimization with L-BFGS-B and piecewise matrix exponentials. It is not an implementation of GRAPE, GOAT, CRAB, or Krotov. After completing the course, you can start a separate project with qutip-qtrl or qutip-qoc and verify dependencies against their documentation.

QuTiP does not eliminate exponential state-space growth. A statevector contains 2^n elements; a full density matrix contains 4^n elements. The six-qubit QAOA example is chosen so that exhaustive verification is possible, not to demonstrate quantum advantage.
