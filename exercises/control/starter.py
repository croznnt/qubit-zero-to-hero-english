"""Starter for control. Return exactly the fields described in README.md.

Run with: python -m qubit_course.labs check control
"""
import numpy as np
import qutip as qt
from qubit_course.models import gate_overlap


def solve(seed=42):
    pulse_xy = np.zeros((6, 2))
    pulse_xy[:, 0] = np.pi * np.array([0.8, 1.1, 0.9, 1.2, 1.0, 1.0])
    duration_us = 1.0
    # TODO 1: Read the numbered tasks in this folder's README.md.
    # TODO 2: Compose slot propagators chronologically and evaluate full-gate infidelity.
    # TODO 3: Return the documented dictionary of actual objects/arrays.
    # Keep seed in this interface even when the calculation is deterministic.
    raise NotImplementedError("Complete the control tasks before checking your solution.")
