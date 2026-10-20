"""S02 reference. Attempt starter.py before reading this file."""
import numpy as np
import starter


def projector(v):
    v = np.asarray(v, dtype=complex)
    if v.ndim != 1:
        raise ValueError('Expected a one-dimensional vector')
    norm = np.linalg.norm(v)
    if norm == 0:
        raise ValueError('The zero vector has no normalized direction')
    u = v/norm
    return np.outer(u, u.conj())


def x_rotation(theta):
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    return np.cos(theta/2)*np.eye(2)-1j*np.sin(theta/2)*X


if __name__ == '__main__':
    starter.projector = projector
    starter.x_rotation = x_rotation
    starter.check()
