"""Complete these scalar functions. Use only trusted local exercise files."""
import numpy as np


def squared_magnitude(z):
    """Return the real, nonnegative squared magnitude of a complex scalar."""
    raise NotImplementedError('Implement squared_magnitude')


def from_polar(radius, phase):
    """Return a complex scalar. radius >= 0 and phase is in radians."""
    raise NotImplementedError('Implement from_polar')


def rotate_phase(z, phase):
    """Multiply z by a unit phase factor with phase in radians."""
    raise NotImplementedError('Implement rotate_phase')


def check():
    # Check distinct quadrants, zero, and two nontrivial rotations.
    for value, expected in [(3+4j,25),(-3+4j,25),(0j,0),(0.5-0.5j,0.5)]:
        actual = squared_magnitude(value)
        assert np.isrealobj(actual), 'Return a real scalar'
        assert np.isclose(actual, expected)
    assert np.isclose(from_polar(2,np.pi/3),1+np.sqrt(3)*1j)
    assert np.isclose(from_polar(5,np.arctan2(4,-3)),-3+4j)
    assert np.isclose(from_polar(0,0.7),0)
    assert np.isclose(rotate_phase((1+1j)/2,np.pi/2),(-1+1j)/2)
    assert np.isclose(rotate_phase(2-3j,np.pi),-2+3j)
    for angle in [-2.1,0,0.7,4.2]:
        assert np.isclose(squared_magnitude(rotate_phase(0.3-0.4j,angle)),0.25)
    print('S01 exercises: PASSED')


if __name__ == '__main__':
    check()
