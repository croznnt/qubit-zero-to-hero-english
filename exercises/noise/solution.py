"""Reference: two independent initial preparations under the same noise model."""
import numpy as np
import qutip as qt


def solve(seed=42):
    zero, one = qt.basis(2, 0), qt.basis(2, 1)
    plus = (zero + one).unit()
    time_us = np.linspace(0, 24, 241)
    # Explicit computational lowering avoids spin-label convention mistakes.
    collapse = [np.sqrt(1 / 8) * zero * one.dag(), np.sqrt(1 / 24) * qt.sigmaz()]
    options = {'atol': 1e-10, 'rtol': 1e-10, 'store_states': True}
    relaxation = qt.mesolve(0 * qt.sigmaz(), one.proj(), time_us, c_ops=collapse,
                          e_ops=[one.proj()], options=options)
    coherence = qt.mesolve(0 * qt.sigmaz(), plus.proj(), time_us, c_ops=collapse,
                         e_ops=[qt.sigmax()], options=options)
    return {'time_us': time_us, 'p1': np.real(relaxation.expect[0]),
            'sx': np.real(coherence.expect[0]), 'rho_final': relaxation.states[-1]}
