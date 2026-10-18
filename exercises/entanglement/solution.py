"""Reference: compare a coherent Bell state with a classical mixture."""
import qutip as qt


def solve(seed=42):
    zero, one = qt.basis(2, 0), qt.basis(2, 1)
    zz, oo = qt.tensor(zero, zero), qt.tensor(one, one)
    bell = (zz + oo).unit()
    reduced = bell.ptrace(0)
    classical = 0.5 * zz.proj() + 0.5 * oo.proj()
    xx = qt.tensor(qt.sigmax(), qt.sigmax())
    return {'bell': bell, 'reduced': reduced, 'entropy_bits': float(qt.entropy_vn(reduced, base=2)),
            'bell_xx': float(qt.expect(xx, bell)), 'classical_xx': float(qt.expect(xx, classical))}
