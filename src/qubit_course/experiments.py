"""Small reproducible experiments, with raw arrays and independent references."""
import numpy as np
import qutip as qt
from scipy.optimize import minimize

from .models import (ZERO, ONE, PLUS, P1, rotation, collapse_operators,
                     density_checks, gate_overlap, pulse_unitary,
                     assignment_problem, qaoa_state)


def basics(seed):
    rng = np.random.default_rng(seed)
    theta, phi = np.pi / 3, np.pi / 4
    psi = np.cos(theta / 2) * ZERO + np.exp(1j * phi) * np.sin(theta / 2) * ONE
    bloch = np.array([qt.expect(op, psi) for op in [qt.sigmax(), qt.sigmay(), qt.sigmaz()]], float)
    p1 = float(qt.expect(P1, psi))
    shots = rng.binomial(1, p1, size=2000)
    return {'probability_one': p1, 'measured_fraction_one': float(shots.mean()),
            'shots': len(shots), 'bloch_norm': float(np.linalg.norm(bloch))}, {
                'bloch': bloch, 'shots': shots, 'amplitudes': psi.full()}


def gates(seed):
    h = (qt.sigmax() + qt.sigmaz()) / np.sqrt(2)
    psi = h * ZERO
    recovered = h * psi
    x_after_pi = rotation('x', np.pi) * ZERO
    return {'hadamard_p1': float(qt.expect(P1, psi)),
            'double_hadamard_p0': float(qt.expect(ZERO.proj(), recovered)),
            'x_pi_p1': float(qt.expect(P1, x_after_pi))}, {'hadamard': h.full()}


def rabi(seed, tight=True):
    t = np.linspace(0, 4, 401)
    omega = np.pi
    options = {'atol': 1e-10 if tight else 1e-6, 'rtol': 1e-10 if tight else 1e-6}
    result = qt.sesolve(omega / 2 * qt.sigmax(), ZERO, t, e_ops=[P1], options=options)
    p1 = np.real(result.expect[0])
    reference = np.sin(omega * t / 2) ** 2
    return {'max_analytic_error': float(np.max(abs(p1 - reference))),
            'omega_rad_per_us': omega, 'duration_us': float(t[-1])}, {
                'time_us': t, 'p1': p1, 'analytic': reference}


def noise(seed):
    t1, tphi = 8., 12.
    t2 = 1 / (1 / (2 * t1) + 1 / tphi)
    t = np.linspace(0, 24, 241)
    cops = collapse_operators(t1, tphi)
    options = {'atol': 1e-10, 'rtol': 1e-10, 'store_states': True}
    relax = qt.mesolve(0 * qt.sigmaz(), ONE.proj(), t, c_ops=cops, e_ops=[P1], options=options)
    dephase = qt.mesolve(0 * qt.sigmaz(), PLUS.proj(), t, c_ops=cops, e_ops=[qt.sigmax()], options=options)
    p1, sx = np.real(relax.expect[0]), np.real(dephase.expect[0])
    checks = [density_checks(rho) for rho in relax.states + dephase.states]
    return {'t1_us': t1, 'tphi_us': tphi, 't2_us': t2,
            'max_relaxation_error': float(np.max(abs(p1 - np.exp(-t / t1)))),
            'max_coherence_error': float(np.max(abs(sx - np.exp(-t / t2)))),
            'max_trace_error': max(c['trace_error'] for c in checks),
            'minimum_eigenvalue': min(c['minimum_eigenvalue'] for c in checks)}, {
                'time_us': t, 'p1': p1, 'sx': sx, 'relax_reference': np.exp(-t / t1),
                'coherence_reference': np.exp(-t / t2)}


def entanglement(seed):
    bell = (qt.tensor(ZERO, ZERO) + qt.tensor(ONE, ONE)).unit()
    rho_a = bell.ptrace(0)
    classical = 0.5 * qt.tensor(ZERO, ZERO).proj() + 0.5 * qt.tensor(ONE, ONE).proj()
    return {'reduced_purity': float((rho_a * rho_a).tr().real),
            'entanglement_entropy_bits': float(qt.entropy_vn(rho_a, base=2)),
            'bell_xx': float(qt.expect(qt.tensor(qt.sigmax(), qt.sigmax()), bell)),
            'classical_xx': float(qt.expect(qt.tensor(qt.sigmax(), qt.sigmax()), classical))}, {
                'bell_density': bell.proj().full(), 'reduced_density': rho_a.full(),
                'classical_density': classical.full()}


def control(seed, robust=False):
    rng = np.random.default_rng(seed)
    nslots, bound = 6, 2 * np.pi
    initial = np.column_stack([np.full(nslots, np.pi), np.zeros(nslots)])
    initial += rng.normal(0, 0.08, initial.shape)
    training = [(d, e) for d in [-0.4, 0., 0.4] for e in [-0.08, 0., 0.08]] if robust else [(0., 0.)]
    target = qt.sigmax()

    def loss(values):
        pulse = values.reshape(nslots, 2)
        return np.mean([1 - gate_overlap(pulse_unitary(pulse, detuning=d, calibration=e), target) for d, e in training])

    result = minimize(loss, initial.ravel(), method='L-BFGS-B', bounds=[(-bound, bound)] * initial.size,
                      options={'maxiter': 100, 'ftol': 1e-11})
    pulse = result.x.reshape(nslots, 2)
    # Midpoint uncertainty grid, disjoint from the training pairs.
    validation = np.array([(d, e) for d in [-0.5, -0.2, 0.2, 0.5] for e in [-0.1, -0.04, 0.04, 0.1]])
    scores = np.array([gate_overlap(pulse_unitary(pulse, detuning=d, calibration=e), target) for d, e in validation])
    baseline = np.column_stack([np.full(nslots, np.pi), np.zeros(nslots)])
    base_scores = np.array([gate_overlap(pulse_unitary(baseline, detuning=d, calibration=e), target) for d, e in validation])
    # Splitting constant slots in half is an independent composition check.
    fine = pulse_unitary(np.repeat(pulse, 2, axis=0))
    return {'robust_training': robust, 'training_infidelity': float(loss(result.x)),
            'validation_mean_overlap': float(scores.mean()), 'validation_min_overlap': float(scores.min()),
            'baseline_validation_mean_overlap': float(base_scores.mean()),
            'baseline_validation_min_overlap': float(base_scores.min()),
            'slot_split_operator_error': float((fine - pulse_unitary(pulse)).norm()),
            'optimizer_success': bool(result.success), 'optimizer_message': str(result.message),
            'objective_evaluations': int(result.nfev), 'amplitude_bound_rad_per_us': bound,
            'duration_us': 1.0}, {'pulse_xy': pulse, 'training_grid': np.array(training),
                                 'validation_grid': validation, 'validation_overlap': scores,
                                 'baseline_validation_overlap': base_scores}


def leakage(seed):
    t = np.linspace(0, 1, 301)
    a = qt.destroy(3)
    two = qt.basis(3, 2).proj()
    alpha, omega = 8 * np.pi, np.pi
    h = -alpha * two + omega / 2 * (a + a.dag())
    result = qt.sesolve(h, qt.basis(3, 0), t,
                       e_ops=[qt.basis(3, 1).proj(), two], options={'atol': 1e-10, 'rtol': 1e-10})
    return {'final_target_population': float(result.expect[0][-1]),
            'final_leakage': float(result.expect[1][-1]),
            'maximum_leakage': float(np.max(result.expect[1])),
            'anharmonicity_rad_per_us': alpha,
            'two_level_ideal_target_population': 1.0}, {
                'time_us': t, 'p1': result.expect[0], 'p2': result.expect[1]}


def convergence(seed):
    loose, la = rabi(seed, tight=False)
    tight, ta = rabi(seed, tight=True)
    return {'loose_max_error': loose['max_analytic_error'],
            'tight_max_error': tight['max_analytic_error'],
            'max_difference': float(np.max(abs(la['p1'] - ta['p1'])))}, {
                'time_us': ta['time_us'], 'loose_p1': la['p1'], 'tight_p1': ta['p1'], 'analytic': ta['analytic']}


def assignment(seed):
    bits, energies, feasible, travel = assignment_problem()
    rng = np.random.default_rng(seed)
    def objective(angles):
        state = qaoa_state(angles, energies)
        return float(np.dot(abs(state.full().ravel()) ** 2, energies))
    runs = [minimize(objective, rng.uniform(0, np.pi, 4), method='Powell',
                     options={'maxiter': 45, 'ftol': 1e-7}) for _ in range(3)]
    best = min(runs, key=lambda result: result.fun)
    probabilities = abs(qaoa_state(best.x, energies).full().ravel()) ** 2
    exact_index = int(np.argmin(np.where(feasible, travel, np.inf)))
    best_feasible_index = int(np.argmax(np.where(feasible, probabilities, -1)))
    sampled = rng.choice(len(bits), 2000, p=probabilities / probabilities.sum())
    valid = sampled[feasible[sampled]]
    return {'num_qubits': 6, 'depth': 2, 'angle_order': 'gamma1,beta1,gamma2,beta2',
            'expected_penalized_energy': float(best.fun),
            'feasible_probability': float(probabilities[feasible].sum()),
            'exact_optimal_cost': float(travel[exact_index]),
            'exact_optimal_bits': ''.join(map(str, bits[exact_index])),
            'most_probable_feasible_bits': ''.join(map(str, bits[best_feasible_index])),
            'most_probable_feasible_cost': float(travel[best_feasible_index]),
            'sampled_feasible_fraction': float(len(valid) / len(sampled)),
            'best_sampled_feasible_cost': float(travel[valid].min()) if len(valid) else None,
            'optimizer_success': bool(best.success), 'optimizer_message': str(best.message),
            'total_objective_evaluations': sum(int(r.nfev) for r in runs)}, {
                'bits': bits, 'penalized_energy': energies, 'feasible': feasible,
                'travel_cost': travel, 'probabilities': probabilities, 'angles': best.x,
                'sampled_indices': sampled}


EXPERIMENTS = {'basics': basics, 'gates': gates, 'rabi': rabi, 'noise': noise,
               'entanglement': entanglement, 'control': control,
               'robustness': lambda seed: control(seed, robust=True),
               'leakage': leakage, 'convergence': convergence, 'assignment': assignment}
