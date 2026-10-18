# Lesson 04. Density matrices and Lindblad noise

## Why density matrices are needed

A ket describes a pure state. A mixture has the form rho = sum(p_k*|psi_k><psi_k|). rho must be Hermitian, have trace 1, and have nonnegative eigenvalues within numerical error. The purity Tr(rho^2) is 1 for a pure state and 1/2 for a maximally mixed single-qubit state.

The Lindblad equation contains the term -i[H,rho] and a dissipator for each collapse operator L: L*rho*L.dag() - (L.dag()*L*rho + rho*L.dag()*L)/2. This model assumes an environment compatible with a Markovian description; it does not cover all forms of environmental memory.

## Practical work

```console
python -m qubit_course.cli noise --output runs/lesson04
```

The code uses T1 = 8 and Tphi = 12 microseconds. Collapse operators are defined explicitly in models.py. T2 follows 1/T2 = 1/(2*T1)+1/Tphi, giving approximately 6.857 microseconds. Starting from |1>, the population decays as exp(-t/T1). Starting from |+>, the X expectation decays as exp(-t/T2).

These two runs use different initial states with the same noise mechanism. Together they check the direction of relaxation, the dephasing coefficient, and the coherence time. A very slightly negative minimum_eigenvalue can arise from solver tolerances; a substantially negative value needs investigation.

## Exercises

1. Create rho = I/2 and check its trace and purity.
2. Increase Tphi substantially and observe T2 approaching 2*T1.
3. On an experimental branch, deliberately replace LOWER with ONE*ZERO.dag(). Observe why the model now excites the qubit instead of relaxing toward |0>.

You are finished when you can interpret T1, Tphi, and T2 and distinguish average open-system evolution from a conditional measurement trajectory. This course does not implement stochastic measurement feedback.

Source: [Master equation](https://qutip.readthedocs.io/en/stable/guide/dynamics/dynamics-master.html).
