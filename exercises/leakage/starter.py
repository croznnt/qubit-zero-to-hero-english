"""Starter for leakage. Return exactly the fields described in README.md.

Run with: python -m qubit_course.labs check leakage
"""
import numpy as np
import qutip as qt


def solve(seed=42):
    time_us = np.linspace(0, 1, 301)
    alpha, omega = 8*np.pi, np.pi
    a = qt.destroy(3)
    # TODO 1: Read the numbered tasks in this folder's README.md.
    # TODO 2: Construct the three-level Hamiltonian and return all numerical populations.
    # TODO 3: Return the documented dictionary of actual objects/arrays.
    # Keep seed in this interface even when the calculation is deterministic.
    raise NotImplementedError("Complete the leakage tasks before checking your solution.")
