"""Reference: build gates and preserve their operator meaning."""
import numpy as np
import qutip as qt


def solve(seed=42):
    hadamard = (qt.sigmax() + qt.sigmaz()) / np.sqrt(2)
    # The factor one half matters: this is -iX, equivalent to X up to phase.
    rx_pi = (-0.5j * np.pi * qt.sigmax()).expm()
    after_hh = hadamard * hadamard * qt.basis(2, 0)
    return {'hadamard': hadamard, 'rx_pi': rx_pi, 'after_hh': after_hh}
