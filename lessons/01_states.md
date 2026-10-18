# Lesson 01. Complex numbers, vectors, and your first qubit

## The idea

A pure qubit state is a complex vector with two amplitudes. Write |psi> = a|0> + b|1>, with |a|^2 + |b|^2 = 1. An amplitude is not a probability: the probability of measuring 1 is |b|^2. Python writes the imaginary unit i as 1j.

```python
import numpy as np
import qutip as qt
zero = qt.basis(2, 0)
one = qt.basis(2, 1)
psi = (zero + 1j * one).unit()
print(psi.full())
print(psi.dag() * psi)
print(qt.expect(one.proj(), psi))
```

dag is the conjugate transpose, proj creates |psi><psi|, and unit normalizes a vector. a.dag()*b is an inner product, not elementwise multiplication. The core operations are in [models.py](../src/qubit_course/models.py).

## Parameterization and the Bloch sphere

For theta from 0 to pi and phi from 0 to 2*pi, choose a = cos(theta/2), b = exp(i*phi)*sin(theta/2). The three Bloch coordinates are the expectation values of X, Y, and Z. For a pure single-qubit state, the Bloch vector has length 1 within numerical error.

```console
python -m qubit_course.cli basics --seed 42 --output runs/lesson01
```

The program uses theta = pi/3 and phi = pi/4. probability_one should be close to 0.25, and bloch_norm close to 1. Measured_fraction_one fluctuates because it comes from 2000 samples. Changing the seed changes sampling only, not the theoretical state.

## Exercises

1. Predict the results for theta equal to 0, pi/2, and pi before changing the code.
2. Multiply psi by exp(0.7j). Check that the probabilities stay unchanged. This is a global phase.
3. Keep theta = pi/2 and vary phi. Measure Z, then X; explain why one measurement basis may fail to distinguish two states.

You are finished when you can distinguish amplitudes, probabilities, relative phase, and global phase, and check normalization.

Source: [Quantum objects in QuTiP](https://qutip.readthedocs.io/en/stable/guide/guide-basics.html).
