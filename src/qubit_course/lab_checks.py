"""Independent checks of submitted objects, not comparisons to solution files."""
import itertools

import numpy as np
import qutip as qt


def require(condition, message):
    if not condition:
        raise ValueError(message)


def array(data, key, shape):
    value = np.asarray(data[key])
    require(value.shape == shape, f'{key}: expected shape {shape}, received {value.shape}.')
    require(np.issubdtype(value.dtype, np.number) or value.dtype == bool,
            f'{key}: return a numeric array.')
    require(np.isfinite(value).all(), f'{key}: NaN or infinity is not allowed.')
    return value


def qobject(data, key, shape):
    value = data[key]
    require(isinstance(value, qt.Qobj), f'{key}: return a QuTiP Qobj.')
    require(value.shape == shape, f'{key}: expected shape {shape}, received {value.shape}.')
    require(np.isfinite(value.full()).all(), f'{key}: nonfinite quantum object.')
    return value


def scalar(data, key):
    value = np.asarray(data[key])
    require(value.shape == (), f'{key}: expected a scalar, received shape {value.shape}.')
    require(np.issubdtype(value.dtype, np.number) and np.isrealobj(value),
            f'{key}: return a real numeric scalar.')
    require(np.isfinite(value).item(), f'{key}: NaN or infinity is not allowed.')
    return float(value)


def close(actual, expected, message, atol=1e-7):
    require(np.allclose(actual, expected, atol=atol, rtol=0), message)


def validate(name, data):
    """Raise a targeted diagnostic for a broken contract or physical invariant."""
    require(isinstance(data, dict), 'solve(seed=42) must return a dictionary.')
    zero, one = qt.basis(2, 0), qt.basis(2, 1)
    if name == 'basics':
        state = qobject(data, 'state', (2, 1))
        expected = np.cos(np.pi / 6) * zero + np.exp(1j * np.pi / 4) * np.sin(np.pi / 6) * one
        close(state.norm(), 1, 'Normalize the state.')
        close(abs(expected.overlap(state)) ** 2, 1, 'Relative phase or amplitudes are incorrect.')
        close(array(data, 'probabilities', (2,)), [0.75, 0.25], 'Use squared amplitude magnitudes.')
        close(array(data, 'bloch', (3,)), [np.sqrt(3 / 8), np.sqrt(3 / 8), 0.5],
              'Bloch coordinates must be expectations of X, Y, Z.')
        counts = array(data, 'counts', (2,))
        require(np.isrealobj(counts) and np.all(counts >= 0) and np.all(counts == np.floor(counts)),
                'Counts must be nonnegative integers.')
        require(counts.sum() == 2000, 'Counts must sum to 2000 shots.')
        require(abs(counts[1] / 2000 - 0.25) < 0.08, 'Shot frequencies are inconsistent with the state.')
    elif name == 'gates':
        hadamard = qobject(data, 'hadamard', (2, 2))
        rx = qobject(data, 'rx_pi', (2, 2))
        after = qobject(data, 'after_hh', (2, 1))
        close(hadamard.full(), np.array([[1, 1], [1, -1]]) / np.sqrt(2), 'Hadamard matrix is incorrect.')
        close((rx.dag() * rx).full(), np.eye(2), 'The rotation must be unitary.')
        close(abs((qt.sigmax().dag() * rx).tr()) ** 2 / 4, 1,
              'Rx(pi) must match X up to a global phase.')
        close(after.full(), zero.full(), 'Apply H twice to |0>.')
    elif name == 'rabi':
        t = array(data, 'time_us', (401,))
        close(t, np.linspace(0, 4, 401), 'Use the documented time grid.')
        close(array(data, 'p1', (401,)), np.sin(np.pi * t / 2) ** 2,
              'Rabi population disagrees with sin²(Omega*t/2).', atol=1e-7)
    elif name == 'noise':
        t = array(data, 'time_us', (241,))
        close(t, np.linspace(0, 24, 241), 'Use the documented time grid.')
        close(array(data, 'p1', (241,)), np.exp(-t / 8), 'T1 decay has wrong direction or rate.')
        close(array(data, 'sx', (241,)), np.exp(-t * (1 / 16 + 1 / 12)),
              'Check both T1 and the factor 1/(2*Tphi) in the Z collapse operator.')
        rho = qobject(data, 'rho_final', (2, 2))
        close(rho.tr(), 1, 'The final density matrix must have trace one.')
        close(rho.full(), rho.dag().full(), 'The density matrix must be Hermitian.')
        require(np.linalg.eigvalsh(rho.full()).min() >= -1e-8, 'The density matrix is not positive.')
        close(rho.full(), np.diag([1 - np.exp(-3), np.exp(-3)]),
              'rho_final must be the relaxation run at 24 us, with no generated coherence.')
    elif name == 'entanglement':
        state = qobject(data, 'bell', (4, 1))
        require(state.dims == [[2, 2], [1]], 'Keep two-qubit tensor dimensions on the Bell ket.')
        expected = (qt.tensor(zero, zero) + qt.tensor(one, one)).unit()
        close(abs(expected.overlap(state)) ** 2, 1, 'Construct the coherent Bell superposition.')
        reduced = qobject(data, 'reduced', (2, 2))
        close(reduced.full(), state.ptrace(0).full(), 'Return the actual partial trace.')
        close(reduced.full(), np.eye(2) / 2, 'The Bell subsystem must be maximally mixed.')
        close(scalar(data, 'entropy_bits'), 1, 'Use entropy in bits, not natural-log units.')
        close(scalar(data, 'bell_xx'), 1, 'Bell XX correlation must be one.')
        close(scalar(data, 'classical_xx'), 0, 'The incoherent mixture has zero XX correlation.')
    elif name == 'control':
        pulse = array(data, 'pulse_xy', (6, 2))
        require(np.isrealobj(pulse) and np.max(abs(pulse)) <= 2 * np.pi + 1e-10,
                'Pulse amplitudes must be real and respect the bound.')
        unitary = qobject(data, 'unitary', (2, 2))
        # Independent dense eigendecomposition, not the course pulse helper.
        reference = np.eye(2, dtype=complex)
        for ux, uy in pulse:
            h = 0.5 * np.array([[0, ux - 1j * uy], [ux + 1j * uy, 0]])
            vals, vecs = np.linalg.eigh(h)
            reference = (vecs @ np.diag(np.exp(-1j * vals / 6)) @ vecs.conj().T) @ reference
        close(unitary.full(), reference, 'Pulse propagation or chronological order is incorrect.')
        score = abs(np.trace(np.array([[0, 1], [1, 0]]) @ reference)) ** 2 / 4
        infidelity = scalar(data, 'infidelity')
        close(infidelity, 1 - score, 'Report squared unitary trace overlap, not state probability.')
        require(infidelity < 1e-7, 'The resonant pi pulse should realize X.')
    elif name == 'robustness':
        grid = array(data, 'validation_grid', (16, 2))
        expected_grid = np.array([(d, e) for d in [-0.5, -0.2, 0.2, 0.5] for e in [-0.1, -0.04, 0.04, 0.1]])
        close(grid, expected_grid, 'Keep the specified held-out grid and ordering.')
        # Analytic constant-drive gate overlap, independent of propagation.
        detuning, calibration = grid.T
        omega = np.pi * (1 + calibration)
        rate = np.sqrt(omega ** 2 + detuning ** 2)
        expected = (omega / rate * np.sin(rate / 2)) ** 2
        scores = array(data, 'scores', (16,))
        close(scores, expected, 'Evaluate the baseline pi pulse on each uncertainty pair.')
        close(scalar(data, 'mean_overlap'), expected.mean(), 'Mean must include every validation pair.')
        close(scalar(data, 'worst_overlap'), expected.min(), 'Worst overlap means minimum, not maximum.')
    elif name == 'leakage':
        t = array(data, 'time_us', (301,))
        close(t, np.linspace(0, 1, 301), 'Use the documented time grid.')
        p0, p1, p2 = [array(data, key, (301,)) for key in ['p0', 'p1', 'p2']]
        close(p0 + p1 + p2, 1, 'The three level populations must sum to one.')
        require(min(p0.min(), p1.min(), p2.min()) >= -1e-8, 'Populations cannot be negative.')
        # Direct spectral propagation is independent of the learner ODE solve.
        h = np.array([[0, np.pi / 2, 0], [np.pi / 2, 0, np.pi / np.sqrt(2)],
                      [0, np.pi / np.sqrt(2), -8 * np.pi]])
        vals, vecs = np.linalg.eigh(h)
        state = vecs @ (np.exp(-1j * vals[:, None] * t) * vecs[0, :].conj()[:, None])
        for got, expected in zip([p0, p1, p2], abs(state) ** 2):
            close(got, expected, 'Check rotating-frame drift, sqrt(n) coupling, and solver accuracy.')
    elif name == 'convergence':
        t = array(data, 'time_us', (401,))
        close(t, np.linspace(0, 4, 401), 'Use the documented time grid.')
        reference = np.sin(np.pi * t / 2) ** 2
        loose, tight = array(data, 'loose_p1', (401,)), array(data, 'tight_p1', (401,))
        error_loose, error_tight = np.max(abs(loose - reference)), np.max(abs(tight - reference))
        close(scalar(data, 'loose_max_error'), error_loose, 'Compute loose error against the analytic reference.', atol=1e-12)
        close(scalar(data, 'tight_max_error'), error_tight, 'Compute tight error against the analytic reference.', atol=1e-12)
        require(error_loose < 1e-3 and error_tight < 1e-7, 'The numerical errors exceed the specified tolerances.')
        require(error_tight <= error_loose + 1e-12, 'Tightening solver tolerance should improve this fixed example.')
    elif name == 'assignment':
        bits = array(data, 'bits', (64, 6))
        expected_bits = np.array(list(itertools.product([0, 1], repeat=6)))
        close(bits, expected_bits, 'Enumerate bitstrings in MSB-first tensor order.')
        assignments = expected_bits.reshape(64, 2, 3)
        row = ((assignments.sum(axis=2) - 1) ** 2).sum(axis=1)
        duplicates = (assignments[:, 0] * assignments[:, 1]).sum(axis=1)
        expected_feasible = (row == 0) & (duplicates == 0)
        feasible = array(data, 'feasible', (64,))
        require(feasible.dtype == bool, 'feasible: return a boolean array, not numeric labels.')
        close(feasible, expected_feasible, 'Require exactly one sector per UAV and no duplicates.')
        travel = (assignments * np.array([[1, 4, 6], [3, 1, 5]])).sum(axis=(1, 2))
        energy = travel + 8 * (row + duplicates)
        close(array(data, 'energies', (64,)), energy, 'The penalty energy table is incorrect.')
        close(scalar(data, 'exact_optimum'), 2, 'The exact feasible cost is two.')
        zero_probs = array(data, 'zero_angle_probabilities', (64,))
        close(zero_probs, np.ones(64) / 64, 'Zero angles must give a uniform distribution.')
        hcost = qt.Qobj(np.diag(energy), dims=[[2] * 6, [2] * 6])
        hmix = sum(qt.tensor([qt.sigmax() if k == i else qt.qeye(2) for k in range(6)]) for i in range(6))
        initial = qt.tensor([(zero + one).unit()] * 6)
        state = (-0.23j * hmix).expm() * (-0.12j * hcost).expm() * initial
        close(array(data, 'probabilities', (64,)), abs(state.full().ravel()) ** 2,
              'Check cost sign, mixer factor, layer order, and angle ordering.')
    else:
        raise ValueError(f'Unknown lab: {name}')
