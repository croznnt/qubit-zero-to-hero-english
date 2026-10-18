"""Stable exercise names, progression, and learner-file locations."""
from pathlib import Path

LABS = {
    'basics': ('01. State and measurement', '01_states.md'),
    'gates': ('02. Gates and global phase', '02_gates_measurement.md'),
    'rabi': ('03. Rabi evolution', '03_dynamics.md'),
    'noise': ('04. Relaxation and dephasing', '04_noise.md'),
    'entanglement': ('05. Bell correlations', '05_entanglement.md'),
    'control': ('06. Piecewise pulse objective', '07_control.md'),
    'robustness': ('07. Held-out pulse evaluation', '08_validation.md'),
    'leakage': ('08. Three-level leakage', '08_validation.md'),
    'convergence': ('09. Solver convergence', '08_validation.md'),
    'assignment': ('10. Assignment energy and QAOA', '09_qaoa_assignment.md'),
}


def exercise_root():
    """Guided source files live in the course checkout, not installed wheels."""
    return Path(__file__).resolve().parents[2] / 'exercises'
