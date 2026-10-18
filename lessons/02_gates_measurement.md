# Lesson 02. Quantum gates and measurement

## From matrices to operations

An ideal closed-system gate is a unitary matrix U satisfying U.dag()*U = I. X exchanges |0> and |1>. The Hadamard gate H = (X+Z)/sqrt(2) creates a superposition when applied to |0>. A rotation about X by angle theta is exp(-i*theta*X/2).

```console
python -m qubit_course.cli gates --output runs/lesson02
```

hadamard_p1 should be close to 0.5; double_hadamard_p0 and x_pi_p1 should be close to 1. A pi rotation about X may produce a state differing from X|0> by a global phase, so compare squared overlaps rather than requiring elementwise equality of the vectors.

## Measurement conditioned on an outcome

For a projector P, the probability is p = <psi|P|psi>. If that outcome is observed, the new state is P|psi>/sqrt(p), provided p is positive. Sampling in basics only simulates Z measurements on many independently prepared copies. It does not simulate repeated measurements of the same qubit or automatically update the state after each shot.

```python
import qutip as qt
psi = (qt.basis(2, 0) + qt.basis(2, 1)).unit()
p0 = qt.basis(2, 0).proj()
probability = qt.expect(p0, psi)
post_measurement = (p0 * psi) / probability**0.5
print(qt.expect(p0, post_measurement))
```

The standard deviation of a binary measurement fraction is sqrt(p*(1-p)/N). Increasing the shot count by a factor of four reduces the standard deviation by only about a factor of two.

## Exercises

1. Check X*X, H*H, and U.dag()*U using the norm of their difference from I.
2. Calculate the X and Z expectations for |+>. Change the relative sign to create |->, then compare.
3. Sample 100, 1000, and 10000 shots using the same rule and record the deviation from 0.5. Do not require the deviation to decrease monotonically in each random trial.

You are finished when you can explain the difference between the state before measurement, an outcome probability, a shot outcome, and the conditional state after measurement.

Source: [QuTiP operator conventions](https://qutip.readthedocs.io/en/stable/guide/guide-basics.html).
