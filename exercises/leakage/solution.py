"""Reference: evolve three levels and retain every population."""
import numpy as np
import qutip as qt


def solve(seed=42):
    time_us = np.linspace(0, 1, 301)
    a = qt.destroy(3)
    projectors = [qt.basis(3, k).proj() for k in range(3)]
    hamiltonian = -8 * np.pi * projectors[2] + np.pi / 2 * (a + a.dag())
    result = qt.sesolve(hamiltonian, qt.basis(3, 0), time_us,
                       e_ops=projectors, options={'atol': 1e-10, 'rtol': 1e-10})
    return {'time_us': time_us, 'p0': np.real(result.expect[0]),
            'p1': np.real(result.expect[1]), 'p2': np.real(result.expect[2])}
