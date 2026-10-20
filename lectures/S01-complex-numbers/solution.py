"""Reference functions for S01. Attempt starter.py before reading this file."""
import numpy as np
import starter


def squared_magnitude(z):
    return float(z.real*z.real + z.imag*z.imag)


def from_polar(radius, phase):
    return radius*(np.cos(phase) + 1j*np.sin(phase))


def rotate_phase(z, phase):
    return z*np.exp(1j*phase)


if __name__ == '__main__':
    starter.squared_magnitude = squared_magnitude
    starter.from_polar = from_polar
    starter.rotate_phase = rotate_phase
    starter.check()
