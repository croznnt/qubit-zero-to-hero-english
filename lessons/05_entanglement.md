# Lesson 05. Tensor products and entanglement

## Combine two qubits

qt.tensor(a,b) creates a system with a at the left site and b at the right site. Its space has four basis states: |00>, |01>, |10>, and |11>. An operator acting on the left site is tensor(X,I), not X alone.

```console
python -m qubit_course.cli entanglement --output runs/lesson05
```

The Bell state is (|00>+|11>)/sqrt(2). Tracing out either qubit gives I/2, with purity 0.5 and von Neumann entropy 1 bit. This is entanglement entropy because the full system is in a pure state; subsystem entropy alone cannot establish entanglement for an arbitrary mixed state of the full system.

## Compare with classical correlations

The mixture 0.5*|00><00| + 0.5*|11><11| gives the same Z-measurement statistics as the Bell state. However, the expectation of X tensor X is 0 for this mixture and 1 for the Bell state. Results from a single measurement basis are insufficient to determine coherence.

```python
import qutip as qt
z, o = qt.basis(2, 0), qt.basis(2, 1)
bell = (qt.tensor(z, z) + qt.tensor(o, o)).unit()
print(bell.ptrace(0))
print(qt.expect(qt.tensor(qt.sigmax(), qt.sigmax()), bell))
```

## Exercises

1. Calculate the expectation of Z tensor Z for both the Bell state and the classical mixture.
2. Change the relative sign between |00> and |11>, and predict the expectation of X tensor X.
3. Check that tensor(X,I)|00> gives |10>, and record the bit-order convention before working on QAOA.

You are finished when you can distinguish subsystem mixedness from full-system mixedness and confirm tensor ordering with a concrete example.

Source: [Tensor products and partial traces](https://qutip.readthedocs.io/en/stable/guide/guide-tensor.html).
