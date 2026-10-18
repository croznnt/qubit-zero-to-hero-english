"""Starter for convergence. Return exactly the fields described in README.md.

Run with: python -m qubit_course.labs check convergence
"""
import numpy as np
import qutip as qt


def solve(seed=42):
    time_us = np.linspace(0, 4, 401)
    tolerances = [1e-6, 1e-10]
    omega = np.pi
    # TODO 1: Read the numbered tasks in this folder's README.md.
    # TODO 2: Run both solver tolerances and compute errors against the analytic curve.
    # TODO 3: Return the documented dictionary of actual objects/arrays.
    # Keep seed in this interface even when the calculation is deterministic.
    raise NotImplementedError("Complete the convergence tasks before checking your solution.")
