"""Reference: enumerate an assignment model and propagate one QAOA layer."""
import itertools

import numpy as np
import qutip as qt


def solve(seed=42):
    bits = np.array(list(itertools.product([0, 1], repeat=6)))
    assignments = bits.reshape(64, 2, 3)
    travel = (assignments * np.array([[1, 4, 6], [3, 1, 5]])).sum(axis=(1, 2))
    row_error = ((assignments.sum(axis=2) - 1) ** 2).sum(axis=1)
    duplicates = (assignments[:, 0] * assignments[:, 1]).sum(axis=1)
    feasible = (row_error == 0) & (duplicates == 0)
    energies = travel + 8 * row_error + 8 * duplicates
    plus = (qt.basis(2, 0) + qt.basis(2, 1)).unit()
    initial = qt.tensor([plus] * 6)
    phase = qt.Qobj(np.diag(np.exp(-0.12j * energies)), dims=[[2] * 6, [2] * 6])
    mixer = qt.tensor([(-0.23j * qt.sigmax()).expm()] * 6)
    state = mixer * phase * initial
    return {'bits': bits, 'energies': energies, 'feasible': feasible,
            'exact_optimum': float(travel[feasible].min()),
            'zero_angle_probabilities': abs(initial.full().ravel()) ** 2,
            'probabilities': abs(state.full().ravel()) ** 2}
