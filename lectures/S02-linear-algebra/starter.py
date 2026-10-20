"""Complete two functions, then run this file with the S00 environment."""
import numpy as np
from scipy.linalg import expm


def projector(v):
    """Return the orthogonal projector onto nonzero 1D complex vector v.

    The input need not have norm one. Raise ValueError for a zero vector.
    """
    raise NotImplementedError('Implement projector using conjugation and an outer product')


def x_rotation(theta):
    """Return exp(-i theta X/2) for real theta, using sine and cosine.

    Use the closed form derived in the slides, not expm, in this function.
    """
    raise NotImplementedError('Implement x_rotation using the analytic formula')


def check():
    vector = np.array([1, 1j], dtype=complex)
    expected = np.array([[1, -1j], [1j, 1]])/2
    P = projector(vector)
    assert np.asarray(P).shape == (2, 2)
    assert np.allclose(P, expected)
    assert np.allclose(projector(3*np.exp(0.7j)*vector), expected)
    assert np.allclose(P@vector, vector)
    assert np.allclose(P@np.array([1j, 1]), 0)
    assert np.allclose(P@P, P)
    try:
        projector(np.zeros(2, dtype=complex))
    except ValueError:
        pass
    else:
        raise AssertionError('The zero vector must raise ValueError')
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    for theta in [0, 0.7, -1.3, np.pi, 2*np.pi]:
        actual = x_rotation(theta)
        assert np.allclose(actual, expm(-1j*theta*X/2), atol=1e-12)
    assert np.allclose(x_rotation(np.pi)@np.array([1, 0]), [0, -1j])
    print('S02 exercises: PASSED')


if __name__ == '__main__':
    check()
