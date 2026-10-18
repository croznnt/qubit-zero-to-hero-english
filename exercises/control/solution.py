"""Reference: compose six bounded pulse slots and evaluate an X-gate objective."""
import numpy as np
import qutip as qt

from qubit_course.models import gate_overlap


def solve(seed=42):
    pulse_xy = np.zeros((6, 2))
    pulse_xy[:, 0] = np.pi * np.array([0.8, 1.1, 0.9, 1.2, 1.0, 1.0])
    unitary = qt.qeye(2)
    for ux, uy in pulse_xy:
        hamiltonian = (ux * qt.sigmax() + uy * qt.sigmay()) / 2
        # A later operator acts on the left of all earlier operators.
        unitary = (-1j * hamiltonian / 6).expm() * unitary
    infidelity = 1 - gate_overlap(unitary, qt.sigmax())
    return {'pulse_xy': pulse_xy, 'unitary': unitary, 'infidelity': infidelity}
