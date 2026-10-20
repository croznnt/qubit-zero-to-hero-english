"""Numerical counterparts to S01. Run with the environment created in S00."""
import numpy as np
import qutip as qt


def main():
    z = 3 + 4j
    print('Cartesian:', z.real, z.imag)
    print('Conjugate:', np.conjugate(z))
    print('Magnitude and squared magnitude:', abs(z), abs(z)**2)
    print('Phase in radians:', np.angle(z))
    assert np.isclose(abs(z)**2, 25.0)
    assert np.isclose(abs(z) * np.exp(1j*np.angle(z)), z)

    a = (1 + 1j) / 2
    b = 1 / np.sqrt(2)
    print('Square versus squared magnitude:', a**2, abs(a)**2)
    assert np.isclose(a**2, 0.5j)
    assert np.isclose(abs(a)**2, 0.5)
    rotated = np.exp(1j*np.pi/2) * a
    assert np.isclose(rotated, (-1 + 1j)/2)
    assert np.isclose(abs(rotated)**2, abs(a)**2)

    zero, one = qt.basis(2, 0), qt.basis(2, 1)
    psi = a*zero + b*one
    p0 = qt.expect(zero.proj(), psi)
    assert np.isclose(psi.norm(), 1.0)
    assert np.isclose(p0, abs(a)**2)
    print('QuTiP probability for outcome zero:', p0)

    # Independent QuTiP check of the analytic interference curve.
    plus = (zero + one).unit()
    for phase in [0, np.pi/2, np.pi, 2*np.pi]:
        state = (zero + np.exp(1j*phase)*one)/np.sqrt(2)
        p_plus = qt.expect(plus.proj(), state)
        assert np.isclose(p_plus, (1 + np.cos(phase))/2)
        print('Phase, plus-basis probability:', phase, p_plus)
    print('S01 examples: PASSED')


if __name__ == '__main__':
    main()
