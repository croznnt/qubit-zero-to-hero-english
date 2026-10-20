"""S02: compare hand-derived linear algebra with NumPy, SciPy and QuTiP."""
import numpy as np
import qutip as qt
from scipy.linalg import expm


def main():
    identity = np.eye(2, dtype=complex)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Z = np.diag([1, -1]).astype(complex)
    u = np.array([1, 1j])/np.sqrt(2)
    v = np.array([1j, 1])/np.sqrt(2)
    assert np.isclose(np.vdot(u, v), 0)
    assert np.isclose(np.vdot(u, u), 1)
    P = np.outer(u, u.conj())
    expected = np.array([[1, -1j], [1j, 1]])/2
    assert np.allclose(P, expected)
    assert np.allclose(P.conj().T, P)
    assert np.allclose(P@P, P)
    assert np.allclose(P@u, u)
    assert np.allclose(P@v, 0)
    assert np.allclose(X@Z-Z@X, -2j*Y)

    theta = 0.7
    values, Q = np.linalg.eigh(X)
    U = expm(-1j*theta*X/2)
    U_spec = Q@np.diag(np.exp(-1j*theta*values/2))@Q.conj().T
    U_analytic = np.cos(theta/2)*identity-1j*np.sin(theta/2)*X
    Uq = (-1j*theta*qt.sigmax()/2).expm()
    zero = qt.basis(2, 0)
    final = Uq*zero
    p1 = qt.expect(qt.basis(2, 1).proj(), final)
    errors = {
        'unitarity_frobenius': np.linalg.norm(U.conj().T@U-identity, 'fro'),
        'analytic_frobenius': np.linalg.norm(U-U_analytic, 'fro'),
        'spectral_frobenius': np.linalg.norm(U-U_spec, 'fro'),
        'qutip_frobenius': np.linalg.norm(U-Uq.full(), 'fro'),
        'eigenpair_residual': np.linalg.norm(X@Q-Q@np.diag(values), 'fro'),
    }
    for name, error in errors.items():
        print(f'{name}: {error:.3e}')
        assert error < 1e-12
    assert np.isclose(p1, np.sin(theta/2)**2)
    assert np.allclose(expm(-1j*np.pi*X/2)@np.array([1, 0]), [0, -1j])
    # A matrix exponential differs from elementwise np.exp.
    assert not np.allclose(np.exp(-1j*theta*X/2), U)

    # Exercise the spectral argument on a nontrivial complex Hermitian matrix.
    rng = np.random.default_rng(42)
    M = rng.normal(size=(3, 3))+1j*rng.normal(size=(3, 3))
    A = (M+M.conj().T)/2
    lam, V = np.linalg.eigh(A)
    assert np.allclose(A, V@np.diag(lam)@V.conj().T, atol=1e-12)
    assert np.allclose(expm(-1j*A), V@np.diag(np.exp(-1j*lam))@V.conj().T,
                       atol=1e-12)
    print('Outcome-one probability:', p1)
    print('S02 examples: PASSED')


if __name__ == '__main__':
    main()
