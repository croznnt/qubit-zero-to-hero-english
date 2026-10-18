"""Physical conventions: hbar=1, time in microseconds, frequency in rad/us."""
import itertools

import numpy as np
import qutip as qt

ZERO, ONE = qt.basis(2, 0), qt.basis(2, 1)
PLUS = (ZERO + ONE).unit()
P1 = ONE.proj()
LOWER = ZERO * ONE.dag()  # Explicit |0><1|; do not infer from spin labels.


def rotation(axis, angle):
    pauli = {'x': qt.sigmax(), 'y': qt.sigmay(), 'z': qt.sigmaz()}[axis]
    return (-0.5j * angle * pauli).expm()


def state_probability(state, target=ONE):
    return float(np.real(qt.expect(target.proj(), state)))


def gate_overlap(unitary, target):
    """Squared trace overlap for full unitaries, NOT average gate fidelity."""
    return float(abs((target.dag() * unitary).tr()) ** 2 / target.shape[0] ** 2)


def collapse_operators(t1, tphi):
    if t1 <= 0 or tphi <= 0:
        raise ValueError('Relaxation and pure-dephasing times must be positive.')
    return [np.sqrt(1 / t1) * LOWER, np.sqrt(1 / (2 * tphi)) * qt.sigmaz()]


def density_checks(rho):
    if rho.isket:
        rho = rho.proj()
    return {
        'trace_error': float(abs(rho.tr() - 1)),
        'hermiticity_error': float((rho - rho.dag()).norm()),
        'minimum_eigenvalue': float(np.linalg.eigvalsh(rho.full()).min()),
        'purity': float(np.real((rho * rho).tr())),
    }


def pulse_unitary(amplitudes, duration=1.0, detuning=0.0, calibration=0.0):
    """Piecewise-constant X/Y amplitudes, chronological right-to-left products."""
    amplitudes = np.asarray(amplitudes, dtype=float).reshape(-1, 2)
    if duration <= 0 or len(amplitudes) == 0:
        raise ValueError('Positive duration and at least one pulse slot required.')
    step = duration / len(amplitudes)
    unitary = qt.qeye(2)
    for ux, uy in amplitudes:
        h = 0.5 * (detuning * qt.sigmaz() + (1 + calibration) * (ux * qt.sigmax() + uy * qt.sigmay()))
        unitary = (-1j * step * h).expm() * unitary
    return unitary


def assignment_problem():
    """Two UAVs, three sectors; tensor site 0 is the leftmost/MSB bit."""
    costs = np.array([[1., 4., 6.], [3., 1., 5.]])
    bits = np.array(list(itertools.product([0, 1], repeat=6)), dtype=int)
    assignments = bits.reshape(-1, 2, 3)
    row_penalty = ((assignments.sum(axis=2) - 1) ** 2).sum(axis=1)
    duplicate_penalty = (assignments[:, 0] * assignments[:, 1]).sum(axis=1)
    travel = (assignments * costs).sum(axis=(1, 2))
    energies = travel + 8 * row_penalty + 8 * duplicate_penalty
    feasible = (row_penalty == 0) & (duplicate_penalty == 0)
    return bits, energies, feasible, travel


def qaoa_state(angles, energies):
    """Angles [gamma_1,beta_1,...], minimizing diagonal energy with X mixer."""
    n = int(np.log2(len(energies)))
    if 2 ** n != len(energies) or len(angles) % 2:
        raise ValueError('Power-of-two energy dimension and paired angles required.')
    state = qt.tensor([PLUS] * n)
    for gamma, beta in np.asarray(angles).reshape(-1, 2):
        phase = qt.Qobj(np.diag(np.exp(-1j * gamma * energies)), dims=[[2] * n, [2] * n])
        mixer = qt.tensor([(-1j * beta * qt.sigmax()).expm()] * n)
        state = mixer * phase * state
    return state
