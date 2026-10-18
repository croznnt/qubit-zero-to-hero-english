"""Reference: solve the Hamiltonian, rather than returning the analytic curve."""
import numpy as np
import qutip as qt


def solve(seed=42):
    time_us = np.linspace(0, 4, 401)
    hamiltonian = np.pi * qt.sigmax() / 2
    result = qt.sesolve(hamiltonian, qt.basis(2, 0), time_us,
                       e_ops=[qt.basis(2, 1).proj()], options={'atol': 1e-10, 'rtol': 1e-10})
    return {'time_us': time_us, 'p1': np.real(result.expect[0])}
