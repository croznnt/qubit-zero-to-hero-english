# Lesson 03. Hamiltonians and Rabi oscillations

## The model

Set hbar = 1. The Schrödinger equation is d|psi>/dt = -i*H|psi>. For constant H, U(t) = exp(-i*H*t). The Hamiltonian H = Omega*X/2 and initial state |0> give P1(t) = sin(Omega*t/2)^2.

```console
python -m qubit_course.cli rabi --output runs/lesson03
```

The program chooses Omega = pi radians per microsecond and a time interval from 0 to 4 microseconds. At t = 1, P1 is close to 1; at t = 2, it is close to 0. The plot shows both sesolve results and the analytical formula. max_analytic_error should be smaller than 1e-7 with the current test configuration.

## Implement the evolution yourself

```python
import numpy as np
import qutip as qt
h = np.pi / 2 * qt.sigmax()
psi = (-1j * h * 1.0).expm() * qt.basis(2, 0)
print(qt.expect(qt.basis(2, 1).proj(), psi))
```

Comparing expm with a solver is a useful independent check for a small, constant Hamiltonian. For a time-dependent Hamiltonian, do not replace the full evolution with exp(-i*H(t_final)*T).

## Exercises

1. Change Omega to 2*pi and predict the state-inversion time.
2. Add delta*Z/2. Investigate why detuning reduces the inversion probability at the original pulse duration.
3. Run convergence and read the errors at two tolerance settings. The list of output times is not the adaptive solver's internal integration grid.

```console
python -m qubit_course.cli convergence --output runs/lesson03-check
```

You are finished when you can explain the factor of 1/2, distinguish Hz from radians per unit time, and verify a solver against an analytical limit.

Source: [Closed- and open-system evolution in QuTiP](https://qutip.readthedocs.io/en/stable/guide/dynamics/dynamics-master.html).
