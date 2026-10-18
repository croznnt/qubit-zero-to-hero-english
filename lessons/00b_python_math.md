# Preparation lesson. Essential Python and mathematics

Read this after the installation lesson if you have not written Python before or are unfamiliar with vectors. Create a scratch.py file in the project folder, enter the examples, and run python scratch.py. This file is for experiments; it does not need to become part of the package.

## Variables, functions, and loops

```python
import numpy as np

shots = 1000
probability = 0.25

def expected_count(n, p):
    return n * p

for n in [100, 1000, 10000]:
    print(n, expected_count(n, probability))
```

import loads a library. The = symbol assigns a value; == tests equality. def declares a function. Indented lines belong to the function or loop body. return returns a result. print only displays a value; it cannot replace return when you need the result for further calculations.

## Complex numbers and amplitudes

```python
amplitude = (1 + 1j) / np.sqrt(2)
print(abs(amplitude))
print(abs(amplitude)**2)
print(np.conjugate(amplitude) * amplitude)
```

A complex number has real and imaginary parts. ** means exponentiation, not ^. The squared magnitude of an amplitude gives a probability, which is different from squaring the complex number itself. Complex conjugation changes the sign of the imaginary part.

## Vectors, matrices, and shape

```python
vector = np.array([1, 0], dtype=complex)
x = np.array([[0, 1], [1, 0]], dtype=complex)
print(vector.shape)
print(x.shape)
print(x @ vector)
print(x * x)
print(x @ x)
```

In NumPy, @ means matrix multiplication, whereas * multiplies elements individually. In QuTiP, however, * between two Qobj objects means operator multiplication. Read the data types as well as the operator symbols. full() converts a Qobj to a NumPy array and preserves the two-dimensional shape of a ket.

## Trigonometric functions and probability

```python
theta = np.pi / 3
a = np.cos(theta / 2)
b = np.sin(theta / 2)
assert np.isclose(abs(a)**2 + abs(b)**2, 1.0)
print(abs(b)**2)
```

sin and cos take angles in radians. pi radians equals 180 degrees. Use isclose or an appropriate tolerance when comparing floating-point numbers, because a computer stores finite approximations.

## Exercises and completion criteria

1. Write your own function that returns a probability from a complex amplitude.
2. Use a loop to calculate probabilities for theta equal to 0, pi/2, and pi.
3. Check that the vector [1,1] is not normalized, then divide it by its norm.
4. Deliberately misspell a variable name and read the traceback from the final error message back to its location in scratch.py. Fix the underlying cause rather than suppressing the error.

You are finished when you can run a Python file yourself, distinguish matrix multiplication from elementwise multiplication, understand shape, and calculate a vector norm. Then continue to lesson 01.

References: [Python tutorial](https://docs.python.org/3/tutorial/), [NumPy absolute beginners](https://numpy.org/doc/stable/user/absolute_beginners.html).
