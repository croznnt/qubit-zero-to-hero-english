"""Starter for basics. Return exactly the fields described in README.md.

Run with: python -m qubit_course.labs check basics
"""
import numpy as np
import qutip as qt


def solve(seed=42):
    zero, one = qt.basis(2, 0), qt.basis(2, 1)
    theta, phi = np.pi / 3, np.pi / 4
    shots = 2000
    # TODO 1: Read the numbered tasks in this folder's README.md.
    # TODO 2: Construct state, compute Born probabilities and Bloch coordinates, then sample counts.
    # TODO 3: Return the documented dictionary of actual objects/arrays.
    # Keep seed in this interface even when the calculation is deterministic.
    raise NotImplementedError("Complete the basics tasks before checking your solution.")
