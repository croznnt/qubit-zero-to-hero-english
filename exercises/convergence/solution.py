"""Reference: compare actual numerical solves at two tolerances."""
import numpy as np
import qutip as qt


def solve(seed=42):
    time_us = np.linspace(0, 4, 401)
    hamiltonian = np.pi * qt.sigmax() / 2
    curves = []
    for tolerance in [1e-6, 1e-10]:
        result = qt.sesolve(hamiltonian, qt.basis(2, 0), time_us,
                           e_ops=[qt.basis(2, 1).proj()],
                           options={'atol': tolerance, 'rtol': tolerance})
        curves.append(np.real(result.expect[0]))
    reference = np.sin(np.pi * time_us / 2) ** 2
    return {'time_us': time_us, 'loose_p1': curves[0], 'tight_p1': curves[1],
            'loose_max_error': float(np.max(abs(curves[0] - reference))),
            'tight_max_error': float(np.max(abs(curves[1] - reference)))}
