"""Reference: evaluate an analytic baseline on a held-out uncertainty grid."""
import numpy as np
import qutip as qt

from qubit_course.models import gate_overlap, pulse_unitary


def solve(seed=42):
    pulse = np.column_stack([np.full(6, np.pi), np.zeros(6)])
    validation_grid = np.array([(d, e) for d in [-0.5, -0.2, 0.2, 0.5]
                                for e in [-0.1, -0.04, 0.04, 0.1]])
    scores = np.array([gate_overlap(pulse_unitary(pulse, detuning=d, calibration=e), qt.sigmax())
                       for d, e in validation_grid])
    return {'validation_grid': validation_grid, 'scores': scores,
            'mean_overlap': float(scores.mean()), 'worst_overlap': float(scores.min())}
