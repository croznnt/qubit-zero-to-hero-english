"""Starter for robustness. Return exactly the fields described in README.md.

Run with: python -m qubit_course.labs check robustness
"""
import numpy as np
import qutip as qt
from qubit_course.models import gate_overlap, pulse_unitary


def solve(seed=42):
    pulse = np.column_stack([np.full(6, np.pi), np.zeros(6)])
    detunings = [-0.5, -0.2, 0.2, 0.5]
    calibrations = [-0.1, -0.04, 0.04, 0.1]
    # TODO 1: Read the numbered tasks in this folder's README.md.
    # TODO 2: Evaluate every held-out pair and report mean and worst gate overlap.
    # TODO 3: Return the documented dictionary of actual objects/arrays.
    # Keep seed in this interface even when the calculation is deterministic.
    raise NotImplementedError("Complete the robustness tasks before checking your solution.")
