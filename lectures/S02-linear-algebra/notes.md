# S02 instructor notes

Prerequisite: S01 complex arithmetic. Suggested delivery: two sessions of approximately 60 minutes, with the first ending after slide 14. Slides 1 through 28 are core.

## 1. Vectors, matrices and operators

This follows S01 complex numbers and phase. Allow two sessions of about 60 minutes, or one extended session with a break after slide 14. The 28 core slides cover linear algebra needed for qubit simulation. Four appendices supply notation, a proof, practice answers and run commands. Define each new symbol before using it. QuTiP stays the simulation framework. Formulas are compiled from LaTeX and embedded as rendered images; formulas.tex and Markdown retain the editable equation source.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 2. Column vectors and components

Connect each component to S01 scalar complex numbers. C denotes the complex numbers, and the superscript 2 by 1 describes the shape. Order matters: exchanging entries generally changes the vector. A ket notation such as |psi> names a vector in an abstract Hilbert space; its displayed components depend on the chosen basis. In NumPy a one-dimensional array has shape (2,), so use an explicit column shape when comparing with QuTiP full(), whose ket shape is (2,1).

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 3. Matrix shapes and multiplication

Read m as the number of matrix rows and n as columns. Show a 2 by 2 matrix acting on a two-component column. Each output is a sum over the shared index j. This is a linear map: A(cu+dv)=cAu+dAv for complex scalars c and d. Matrix multiplication is not entrywise multiplication. In NumPy use @ for the linear-algebra product. In QuTiP, multiplication between Qobj instances uses *. This difference is revisited in the code walkthrough.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 4. Example 1 · Normalizing a vector

Worked example 1. Use |i|²=1 from S01. A raw vector is not automatically a normalized state. Dividing by sqrt(2) leaves relative phase and component ratios intact while setting total squared magnitude to one. This example anticipates the formal inner-product norm in slide 7. Ask learners to check the two squared magnitudes separately. A zero vector has norm zero, so division is undefined. QuTiP .unit() and a NumPy division by the norm are numerical counterparts for a nonzero vector.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 5. Transpose, conjugate and adjoint

The superscript T means transpose. Here A* means entrywise complex conjugation and dagger means conjugate transpose. This convention must be stated because some texts use a star for the adjoint. In NumPy use A.conj().T; A.T alone is insufficient for complex data. In QuTiP use A.dag(). The adjoint reverses multiplication order. A column becomes a row, enabling a scalar inner product. In Dirac notation the adjoint of a ket is a bra.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 6. The complex inner product

State the physicists’ convention: the first argument is conjugate linear and the second is linear. Conjugation is essential to get a nonnegative self-inner-product. Orthogonal means u†v=0. Zero vectors are orthogonal algebraically but do not represent normalized quantum states. In NumPy, np.vdot(u,v) conjugates the first flattened argument; use it for vector inputs here. Do not call np.dot a complex inner product without explicitly conjugating its first argument.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 7. Norm and overlap bound

The second formula is Cauchy–Schwarz. It ensures |u†v|²<=1 for normalized vectors and supports probability interpretations. Norm zero occurs only for the zero vector. A normalized overlap is an amplitude; its squared magnitude can become a measurement probability in the appropriate rank-one projection setting. The norm defined here is the vector 2-norm. Later validation uses the Frobenius norm for matrices, which should be named separately.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 8. Example 2 · A complex orthogonality check

Worked example 2. Write u†=(1,−i)/sqrt(2) explicitly before multiplying. The two terms cancel. Without conjugation u transpose times v equals i, which falsely reports nonorthogonality. This is a concrete reason for the dagger. Ask students to compute v†u as a second check. It is the conjugate of zero and is still zero. examples.py checks this independent hand calculation and the unit norms.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 9. Outer products are operators

Emphasize multiplication shapes. The same vectors in reversed order produce different objects: u†v is 1 by 1 while uv† is n by n. A rank-one outer product need not be Hermitian unless the two vectors coincide up to suitable factors. For unit u, P=uu† maps w to u(u†w), extracting the coefficient in the direction u. This linear operator is a projector. np.outer(u,u.conj()) is the explicit NumPy form for one-dimensional inputs.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 10. Example 3 · A rank-one projector

Worked example 3. Use the u and v from slide 8. Expand the outer product entry by entry, including i times −i =1. Show P²= u(u†u)u†=uu† because u is normalized. Show Pv=u(u†v)=0 using the prior calculation. The diagonal entries sum to one. A normalized pure-state density matrix also has the form uu†; S08 develops that interpretation. Here the focus is shape, Hermiticity and idempotence.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 11. Hermitian operators

The examples Z and Y are Pauli operators. Hermitian does not mean every entry is real: the imaginary off-diagonal entries of Y demonstrate this. For a finite complex Hermitian matrix the spectral theorem supplies a complete orthonormal eigenbasis with real eigenvalues. Quantum observables use Hermitian operators in this finite-dimensional course. Avoid introducing infinite-dimensional domain issues here. Validate with A.conj().T or Qobj.dag(), not with transpose alone.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 12. Why Hermitian expectations are real

The adjoint of a scalar is its conjugate. Reverse product order and use the fact that the adjoint of v† is v. Hermiticity then makes a equal to a*. Normalization is not needed for the algebraic reality claim, but it is needed for the stated expectation interpretation without dividing by v†v. An expectation is an average, and does not have to equal an eigenvalue. Tiny computed imaginary residues may result from roundoff; inspect their size before discarding them.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 13. Unitary operators preserve inner products

The square-matrix assumption is important for the inverse statement. For a square matrix, U†U=I implies UU†=I as well. Substituting u=v gives norm preservation. Unitary evolution therefore preserves normalization of closed-system states. Rectangular matrices can satisfy U†U=I without being invertible on the larger space; those are isometries and are outside this slide’s definition. Later gate matrices are unitary.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 14. Hermitian and unitary are different tests

Use examples instead of conflating the two properties. Z is both, which can mislead beginners if it is the only example shown. The real scalar multiple 2Z remains Hermitian but stretches every vector norm by two. The phase-diagonal U is unitary for every real theta; it is Hermitian only when sin(theta)=0. There is no general implication from one property to the other. Ask learners to explain each conclusion using the defining product or adjoint rather than appearance.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 15. Eigenvalues and eigenvectors

The eigenvector must be nonzero or every lambda would satisfy the equation trivially. For a finite square matrix, a nonzero solution exists when A−lambda I is singular. For a general matrix eigenvalues may be complex and a full basis of eigenvectors may not exist. Hermitian matrices avoid that defect. An eigenvector is defined up to nonzero scalar scaling, and a normalized eigenvector still has arbitrary unit global phase. Compare eigenvectors with this freedom in mind.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 16. Hermitian eigensolvers and degeneracy

eigh exploits the Hermitian problem and returns real eigenvalues within numerical precision. The eigenvectors are columns, not rows. Confirm the residual A@Q−Q@diag(values) and Q†Q−I. Degeneracy means the basis within a repeated-eigenvalue subspace is not unique. Even nondegenerate eigenvectors can differ by a unit phase. Do not grade eigenvectors by exact component equality. A matrix accidentally made non-Hermitian should not be passed blindly to eigh; check A≈A† first.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 17. Spectral decomposition

Expand Q Lambda Q† by columns to obtain the sum. Completeness of the orthonormal basis gives the identity resolution. For a degenerate eigenvalue one may combine its rank-one terms into a projector onto the whole eigenspace; the combined projector is independent of the chosen basis. The Hermitian assumption provides a unitary Q. A general diagonalizable matrix instead has a potentially nonunitary inverse, and a defective matrix does not admit this eigenvector expansion.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 18. Example 4 · The spectrum of Pauli X

Worked example 4. Direct multiplication swaps the vector entries. For the plus vector this changes nothing. For the minus vector the swapped result is its negative. Form Pplus and Pminus from their outer products and subtract to recover X. Add them to recover I. This example becomes an independent spectral reference for the exponential in slide 22. No numerical eigensolver is needed to derive these particular eigenvectors.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 19. Functions of a Hermitian matrix

For a polynomial, A^k=Q Lambda^k Q† follows because adjacent Q†Q factors cancel. The exponential follows by its convergent series. More general functions can be defined on the finite spectrum when their scalar values are defined. Do not treat branch-dependent functions such as logarithms as automatically unambiguous. Distinguish the matrix function from elementwise NumPy ufuncs. In this lesson f(A)=exp(A) is the target.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 20. The matrix exponential series

The matrix exponential is defined even when A has no eigenbasis. A^0 is the identity with the same square dimension. A^2 means A@A, not entrywise squaring. Factorials rapidly damp high-order terms for a fixed finite matrix, but naively truncating the series is not the preferred general numerical algorithm. SciPy expm uses dedicated matrix algorithms. np.exp(A) applies scalar exponentials entry by entry and is not a replacement. The next slides derive a special exact formula from powers of X.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 21. Pauli powers separate even and odd terms

Use a as a real scalar in this derivation. Start with e^(−iaX)=sum(−ia)^n X^n/n!. For n=2k the factor (−i)^(2k)=(-1)^k and X^(2k)=I. For n=2k+1 it is −i(-1)^k times X. This yields the two displayed scalar series. Both converge absolutely, allowing even and odd regrouping. For k=0 the even power is X^0=I. Compare the scalar pattern with the Euler derivation in S01.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 22. A closed form for an X rotation

Set a=theta/2 in the previous slide. At theta=0 sine vanishes and cosine is one. At theta=pi the identity term vanishes and −iX sends basis zero to −i times basis one. Multiplying by a common phase does not change measurement probabilities. The spectral derivation gives exp(−i theta/2)Pplus+exp(+i theta/2)Pminus, providing an independent reference. examples.py compares that reference and the trigonometric formula with scipy.linalg.expm and QuTiP .expm().

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 23. Time evolution and the units of the exponent

The exponent must be dimensionless. In physical units H is an energy and H/hbar is an angular-frequency operator. The course sets hbar=1 numerically, so Hamiltonian coefficients carry angular-frequency units. Omega is in radians per microsecond and time is in microseconds. Real time and Hermitian H imply a unitary U, since the generator is anti-Hermitian. This equation prepares S07 dynamics; it does not claim that open-system noise is unitary. A time-dependent noncommuting Hamiltonian needs time ordering rather than simply inserting H(t)t.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 24. Matrix order matters

Define the commutator by the displayed difference. Multiply XZ and ZX explicitly to confirm the sign: XZ=[[0,−1],[1,0]] and ZX=[[0,1],[−1,0]], so the commutator is −2iY with the Y convention shown earlier. Commutation is a sufficient condition for the exponential splitting rule; special noncommuting cases may coincide, so do not state it as a universal if-and-only-if. Products of unitary factors remain unitary but need not equal the exponential of their summed generators. This distinction matters for pulse composition and simulation approximations.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 25. Code walkthrough 1 · NumPy and SciPy

This is code walkthrough 1. Run examples.py and stop at the spectral exponential comparison. Explain np.diag builds a diagonal matrix from the scalar exponentials of the eigenvalues. eigh places eigenvectors in columns, matching Q Lambda Q†. np.exp is correct on the one-dimensional eigenvalue array but not on the entries of the full X matrix as a matrix-function substitute. Use dtype=complex to preserve imaginary components. A tolerance test compares matrices up to floating-point errors.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 26. Code walkthrough 2 · QuTiP

Code walkthrough 2 continues the same Python process or examples.py. QuTiP Qobj multiplication uses *, unlike NumPy’s elementwise * between arrays. .expm() gives the matrix exponential, .dag() gives the adjoint and .full() gives a two-dimensional NumPy array. The probability for outcome one is sin²(theta/2), obtained by acting with the closed-form rotation on basis zero. This QuTiP implementation stays compatible with the course’s later Hamiltonian and noise simulations. The standalone examples.py includes all imports and definitions.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 27. Independent numerical checks

Define the Frobenius norm as the square root of the sum of squared magnitudes of all matrix entries. It differs from the vector 2-norm used in r_k. An incorrect rotation angle still produces a unitary, so structural checks alone do not establish semantic correctness. For this two-dimensional double-precision example, examples.py uses errors below 1e−12 for deterministic references. That is an example-specific threshold, not a universal accuracy promise for large systems or optimizers. Print residuals and investigate scale and solver settings when adapting the code.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 28. Practice and exit checkpoint

Allow ten minutes for written work, then use the standalone starter.py task to implement a projector and an X rotation without using expm in the rotation implementation. Answers: v†=(1,−i), norm sqrt(2); u=v/sqrt(2). The projector is one half times [[1,−i],[i,1]]. exp(−iaZ)=diag(exp(−ia),exp(ia))=cos(a)I−i sin(a)Z. An incorrect angle can retain exact unitarity, so an analytic or independent reference is needed. Appendix 31 summarizes these answers. Next S03 uses this mathematics for qubit states and Bloch coordinates.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 29. Appendix · Notation and dimensions

Review notation without adding a new mathematical topic. The dimension n refers to the size of the chosen basis. The scalar inner product is customarily treated as a complex number even if a strict array implementation represents it with a 1 by 1 shape. All components are in the same fixed orthonormal basis in this lecture. Indexing in the displayed sums is mathematical 1 through n; code arrays start at zero. A ket is an abstract vector; the shown column is its representation.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 30. Proof of eigenvector orthogonality

Multiply A qk=lambda_k qk on the left by qj†. For the other expression, use qj†A=(Aqj)† because A is Hermitian, then real lambda_j gives lambda_j qj†. Subtract. When lambda_k differs from lambda_j the scalar factor is nonzero, forcing orthogonality. If eigenvalues coincide the equation gives no orthogonality constraint, but Gram–Schmidt can choose an orthonormal basis within that eigenspace. This proof relies on Hermiticity and real eigenvalues, not on arbitrary matrix eigenvectors.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 31. Appendix · Practice answers

Return to each practice question. For the projector use the orthogonal vector from slide 8 to check Pv=0 as well. The diagonal exponential follows either from the power series on a diagonal matrix or its two eigenvalues ±1. The formula requires real a for unitarity, though the matrix-function identity itself also extends to complex a. The exit-check answer about angle validation is conceptual: several different rotations satisfy U†U=I. Use a hand-derived special-angle action or a full analytic reference.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.

## 32. Running on Windows and Ubuntu

Use the same virtual environment created in S00. The Python exercises need only course dependencies already installed. No LaTeX installation is required to run them or view the exported slides. The untouched starter raises NotImplementedError intentionally. Complete its two functions and rerun. The reference solution prints S02 exercises: PASSED. The examples print numerical errors and S02 examples: PASSED. The standalone exercises are not entries in qubit_course.labs. Rebuilding formula images additionally requires a TeX distribution and Poppler; see the lecture README.

Course: lessons/00b_python_math.md; lessons/01_states.md; lessons/03_dynamics.md; src/qubit_course/models.py. Definitions and exact calculations are developed in these notes. Numerical counterparts: examples.py in this lecture.