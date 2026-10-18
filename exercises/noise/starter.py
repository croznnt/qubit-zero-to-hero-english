"""Starter for noise. Return exactly the fields described in README.md.

Run with: python -m qubit_course.labs check noise
"""
import numpy as np
import qutip as qt


def solve(seed=42):
    time_us = np.linspace(0, 24, 241)
    t1, tphi = 8.0, 12.0
    zero, one = qt.basis(2, 0), qt.basis(2, 1)
    # TODO 1: Read the numbered tasks in this folder's README.md.
    # TODO 2: Define physical collapse operators and solve both relaxation and coherence.
    # TODO 3: Return the documented dictionary of actual objects/arrays.
    # Keep seed in this interface even when the calculation is deterministic.
    raise NotImplementedError("Complete the noise tasks before checking your solution.")
