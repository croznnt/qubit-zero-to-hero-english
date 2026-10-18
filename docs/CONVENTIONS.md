# Model and result conventions

1. Time is measured in microseconds and angular frequency in radians per microsecond. Set hbar to 1. For a frequency in MHz (cycles per microsecond), multiply by 2*pi before using it in a Hamiltonian.
2. ZERO is basis(2, 0), and ONE is basis(2, 1). Pauli Z has expectation value +1 on ZERO. The lowering operator is defined explicitly as LOWER = |0><1|, without relying on spin-up or spin-down names.
3. The single-qubit Hamiltonian is H = (delta*Z + ux*X + uy*Y)/2. With ux = pi and duration 1, ZERO evolves into ONE up to a global phase.
4. State transfer uses the probability <target|rho|target>. For a ket, this is the squared magnitude of the overlap. Do not compare it directly with an unsquared fidelity returned by another API.
5. gate_overlap uses |Tr(U_target.dag()*U)|^2/d^2 for two full unitaries. In this unitary setting, the corresponding average gate fidelity is (d*gate_overlap+1)/(d+1). Do not apply this formula mechanically to a projection with leakage or to a noisy channel.
6. The collapse operators are sqrt(1/T1)*|0><1| and sqrt(1/(2*Tphi))*Z. Consequently, 1/T2 = 1/(2*T1) + 1/Tphi. T1 and Tphi must be positive.
7. Tensor site 0 is on the left and corresponds to the most significant bit when mapping a statevector to integer indices. Convert this convention explicitly when integrating another library.
8. QAOA minimizes penalty energy. Each layer applies exp(-i*gamma*Hcost), followed by exp(-i*beta*sum(X)). The parameter array is [gamma1,beta1,gamma2,beta2]. Do not assume external QAOA pipelines use the same convention.
9. The leakage model has three levels in a rotating frame, with H = -alpha*|2><2| + omega*(a+a.dag())/2 and positive alpha. This is a teaching model, not a calibrated device model.
10. Populations and probabilities are dimensionless. UAV assignment costs use abstract cost units; do not interpret them automatically as meters, seconds, or joules.

The arrays.npz output stores numerical arrays only. Load it with numpy.load(path, allow_pickle=False). Metadata records package versions and the source commit when running from a Git checkout. If the checkout has uncommitted changes, include the diff in your research report before interpreting the results.
