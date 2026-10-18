"""Starter for rabi. Return exactly the fields described in README.md.

Run with: python -m qubit_course.labs check rabi
"""
import numpy as np
import qutip as qt


def solve(seed=42):
    time_us = np.linspace(0, 4, 401)
    omega = np.pi
    zero, one = qt.basis(2, 0), qt.basis(2, 1)
    # TODO 1: Read the numbered tasks in this folder's README.md.
    # TODO 2: Build the Hamiltonian and return the numerical sesolve population.
    # TODO 3: Return the documented dictionary of actual objects/arrays.
    # Keep seed in this interface even when the calculation is deterministic.
    raise NotImplementedError("Complete the rabi tasks before checking your solution.")
