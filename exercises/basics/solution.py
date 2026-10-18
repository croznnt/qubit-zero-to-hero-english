"""Reference: prepare a qubit and sample independent computational-basis shots."""
import numpy as np
import qutip as qt


def solve(seed=42):
    zero, one = qt.basis(2, 0), qt.basis(2, 1)
    theta, phi = np.pi / 3, np.pi / 4
    state = np.cos(theta / 2) * zero + np.exp(1j * phi) * np.sin(theta / 2) * one
    # Each expectation is a Born probability, not a complex amplitude.
    probabilities = np.array([qt.expect(ket.proj(), state) for ket in [zero, one]])
    bloch = np.array([qt.expect(pauli, state) for pauli in [qt.sigmax(), qt.sigmay(), qt.sigmaz()]])
    count_one = np.random.default_rng(seed).binomial(2000, probabilities[1])
    counts = np.array([2000 - count_one, count_one])
    return {'state': state, 'probabilities': probabilities, 'bloch': bloch, 'counts': counts}
