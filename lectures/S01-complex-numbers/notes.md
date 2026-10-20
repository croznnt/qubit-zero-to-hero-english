# S01 instructor notes

Suggested duration: 75 to 90 minutes. Slides 1 through 20 form the core. Slides 21 through 24 are optional reference material. Prerequisite: S00 and real-number arithmetic.

## 1. Complex numbers and phase

This is the second lecture deck after S00. Assume only real-number arithmetic and the ability to run a Python file. Aim for 75 to 90 minutes, including two code walkthroughs and the exercises. Explain that qubit amplitudes can be complex, while measurement probabilities are real and nonnegative. Today develops the scalar arithmetic needed before vectors and matrices in S02. QuTiP remains the simulation framework throughout the course. Scientific plots in this deck come from the supplied numerical plotting script.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 2. The imaginary unit

Begin with x² = 1, which has real solutions ±1. For x² = −1 there is no real solution. Define a new unit i by i² = −1. This is an algebraic definition, not an approximate numerical value. The symbol j in Python serves the same purpose. It is written 1j rather than an undefined variable j. Ask learners to predict i³ = −i and i⁴ = 1. Do not introduce square-root product rules for negative real arguments.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 3. Cartesian form and arithmetic

Explain each symbol before manipulating it. Both a and b are real coordinates. In particular, Im(3+4i)=4, not 4i. Derive multiplication by distributing all four products: ac + iad + ibc + i²bd, then use i²=−1. Quick example: (1+i)(1−i)=1−i+i−i²=2. Addition combines real and imaginary components separately. Complex multiplication will later give a geometric rotation and scale.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 4. The complex plane

Use the plot to map algebra onto geometry. The point 3+4i is three units along the real axis and four along the imaginary axis. Its distance from the origin is five. The angle is measured counterclockwise from the positive real axis. The plot uses equal axis scales so distances and angles are not distorted. Ask learners to locate −3+4i, then compare distance and angle with 3+4i. This figure is a deterministic scientific plot, not a generated illustration.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 5. Complex conjugation

Read z* as z conjugate. Some texts use an overbar instead of a star. Geometrically it reflects the point across the real axis. A real number is its own conjugate. In Python use np.conjugate(z) or z.conjugate(). Do not confuse conjugation with negation: −z = −a−ib whereas z* = a−ib. Ask learners for the conjugate of −2−3i and require −2+3i.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 6. Squared magnitude, line by line

Here z*z means z-conjugate times z, not z squared. Read the star aloud before expanding. Show that the two cross terms cancel because a and b are ordinary real scalars. Define the magnitude |z| = sqrt(a²+b²), taking the nonnegative square root. For z=0, both magnitude and squared magnitude are zero. This identity is the reason complex amplitudes can generate valid nonnegative probabilities. Normalization of a complete state is also needed, as the next slide explains.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 7. Amplitude and probability

Introduce alpha and beta as two complex amplitudes associated with computational-basis outcomes zero and one. Avoid assuming learners know ket notation yet. For a normalized pure qubit state, the Born probabilities in that basis are the squared magnitudes, and they sum to one. A standalone complex number with magnitude larger than one cannot serve as an amplitude in such a state without rescaling. Later S03 defines states and S04 develops measurement more fully. The sum rule prevents students from treating every squared magnitude as an automatically valid probability.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 8. A complex square is different

Work the numerator explicitly: (1+i)² = 1+2i+i² = 2i. Dividing by four gives i/2. Conjugate multiplication gives (1−i)(1+i)/4 = 2/4 = 1/2. This is a worked contrast supporting the later example rather than a new formula group. In Python compare z**2 with abs(z)**2. If this is one component of a normalized two-outcome state, the other component must contribute the remaining probability 1/2. Ask learners which result could be a probability and why.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 9. Polar coordinates and radians

Relate a=r cos(phi) and b=r sin(phi) to ordinary right-triangle trigonometry, then extend to all quadrants. NumPy trigonometric functions use radians. Explain why atan(b/a) can fail: a may be zero and the ratio loses quadrant information. np.arctan2(b,a) handles these cases for nonzero points. Phase is defined modulo 2π. Numerical conventions can return a placeholder angle for zero, but that does not make its mathematical phase defined.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 10. Unit magnitude and phase

Trace the unit-circle plot counterclockwise. The coordinates of the point at angle phi are (cos(phi),sin(phi)). All points on this circle have squared magnitude one. At pi/2, the point is i, whose square is −1. Reinforce that phase changes can leave a single complex number’s magnitude unchanged. The plotted circle has equal axis scales and uses radians. Ask learners for the point at −pi/2, which is −i.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 11. Euler’s identity and polar form

This is Euler’s formula, with the famous identity at phi=pi as a special case. Explain e as the natural exponential base, approximately 2.71828. On screen e^(i phi) is plain-text exponential notation and means e raised to the power i times phi. Do not multiply e by i phi. State the formula here and reserve the optional power-series derivation for appendix 23. Show |e^(i phi)|²=1 using the Pythagorean trigonometric identity. Python uses np.exp(1j*phi).

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 12. Multiplication adds phase

Use the ordinary exponential product rule for these commuting scalar numbers. The magnitudes r1 and r2 are nonnegative. Phases add modulo 2pi. Conjugating cos(phi)+i sin(phi) changes the sign of sine, which equals evaluation at negative phi. Do not generalize the scalar exponential product rule to arbitrary matrices in S02. For the example, 2i has radius two and phase pi/2; −i has radius one and phase −pi/2. Their product is positive real two.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 13. Example 1 · Cartesian to polar

Worked example 1. Ask learners to compute the magnitude first without a calculator. Then use atan2(4,3) for phase. To check the result, evaluate 5*cos(phi) and 5*sin(phi), recovering approximately 3 and 4. The shown decimal phase is rounded; do not expect exact reconstruction from that rounded value. Distinguish a mathematical equality with the full angle from an approximate equality using six decimal digits. Let learners convert the same point back from polar to Cartesian.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 14. Example 2 · A probability contribution

Worked example 2. Ask learners to supply the conjugate and identify the denominator: multiplying two factors of 1/2 gives 1/4. The magnitude is sqrt(1/2), approximately 0.70710678, whereas squared magnitude is exactly one half in exact arithmetic. Choose beta=1/sqrt(2) as one possible second amplitude. Many other beta phases work because only its magnitude is fixed by normalization. Use this to prepare the distinction between global and relative phase in appendix 22.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 15. Example 3 · Phase rotation

Worked example 3. Derive i+i² = i−1 before dividing by two. The original alpha has phase pi/4 and the rotated alpha has phase 3pi/4. Both have radius 1/sqrt(2). If every amplitude of a state receives the same factor, this is global phase and cannot change any measurement probability. If only one amplitude receives it, it changes relative phase: the current basis populations stay the same, but another basis can reveal the difference. State this scope carefully to avoid the mistaken claim that phase never affects observable results.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 16. Phase can affect an interference result

This is a preview, not a matrix prerequisite. Consider normalized amplitudes 1/sqrt(2) and e^(i phi)/sqrt(2) for the two basis states. Measuring in the equal-superposition plus/minus basis gives plus amplitude (1+e^(i phi))/2. The 1/2 scale is essential; |1+e^(i phi)|² alone can reach four. Derive the numerator using conjugation: (1+e^(−i phi))(1+e^(i phi)) = 2+2 cos(phi). Divide by four. The graph plots this analytic probability, not experimental shots. In the original zero/one basis both probabilities stay one half. This demonstrates a relative-phase effect. S03 and S04 explain the basis change formally.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 17. Code walkthrough 1 · NumPy arithmetic

Run examples.py, then inspect the first section. Explain import, assignment, attribute access, function calls and assertion as needed. 4j is a Python imaginary literal; do not leave a multiplication symbol out of a variable expression such as 1j*phi. z.real and z.imag are the real coordinate values. abs(z) is the magnitude and abs(z)**2 is the squared magnitude. The ^ operator is bitwise XOR rather than exponentiation. np.angle returns the principal phase. Floating-point comparisons use np.isclose with appropriate tolerances, not exact equality for computed trigonometric expressions.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 18. Code walkthrough 2 · QuTiP correspondence

Run the second section of examples.py. QuTiP basis(2,0) and basis(2,1) create the two computational-basis kets. Their coefficients are the amplitudes just studied. proj() makes the zero-state projector; expect computes its expectation in psi, which is the probability for outcome zero. This is a bridge to later notation rather than a demand to memorize projectors today. Verify psi.norm() is one in the source example. Then change the phase of a while keeping its magnitude and observe the same p0. Explain that the same Qobj machinery will support later dynamics, so no framework switch is needed.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 19. Practice · Calculate before running code

Allow eight minutes. Written problem 1: conjugate −3−4i, squared magnitude 25, quadrant II. Its principal phase is atan2(4,−3)≈2.214297436 rad. Problem 2: alpha squared = −i/2 whereas squared magnitude =1/2. Problem 3: real part 1 and imaginary part sqrt(3). The coding task asks for a probability function, a Cartesian reconstruction function and a phase rotation function. Run the starter to see its explicit unfinished error, implement each function and run its checks. The reference solution is separate and need not be copied. Appendix 21 contains worked answers.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 20. Exit check and the next lesson

Use these as three concept questions rather than a slide to read aloud. Expected answers: cross terms cancel and i² supplies a positive b²; the phase factor has unit magnitude; coherent amplitudes add before squared magnitude is taken, so cross terms depend on relative phase. A complete exit response also states the measurement basis: computational-basis populations may stay unchanged while plus-basis outcomes change. Learners should be able to compute all three worked examples and run examples.py and their finished starter. Revisit normalization if anyone treats |3+4i|²=25 as a probability.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 21. Appendix · Worked practice answers

Use this after learners attempt the questions. In the first example, both components of −3+4i are not negated by conjugation: the real part remains negative three. In the second example, expand (1−i)²=−2i. In the third, use cos(pi/3)=1/2 and sin(pi/3)=sqrt(3)/2. Ask learners to state which result is Cartesian and which is polar. The angle quoted for quadrant II is about 126.87 degrees. Differences of integer multiples of 2pi represent the same nonzero complex number.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 22. Appendix · Global and relative phase

The ordered pair here lists coefficients in a fixed basis; S02 supplies vector notation. For any outcome amplitude c, a common phase gives |e^(i chi)c|²=|c|². The same holds after any linear basis change, which is why global phase is unobservable for an isolated state. Applying a phase to only beta generally changes the state physically through its relative phase. Computational-basis probabilities remain |alpha|² and |beta|², but the plus-basis interference example can change. If one component is zero, this particular relative-phase parameter has no observable effect. Avoid saying all phases are unobservable.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 23. Appendix · Why Euler’s formula works

Optional calculus background. State the absolutely convergent power series definitions for exponential, cosine and sine. Substitute i phi into the exponential series and group even and odd powers. Even powers i^(2k)=(-1)^k generate cosine. Odd powers i^(2k+1)=i(-1)^k generate i times sine. Absolute convergence permits this grouping for every finite real phi. For learners without series, retain Euler’s formula as a working identity and return to the unit-circle geometry. The factorial n! multiplies integers from one to n, with 0!=1.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).

## 24. Appendix · Running the supplied files

The S00 environment already installs NumPy and QuTiP. Run these commands from the repository root. No new packages or activation are required when using the explicit interpreter path. examples.py prints values and finishes with S01 examples: PASSED. The untouched starter intentionally raises NotImplementedError. After implementing its functions, it prints S01 exercises: PASSED. Run solution.py separately for the reference. These lecture exercises are standalone and are not registered in qubit_course.labs. To regenerate scientific figures only, run plot_figures.py with the same environment. The code uses no platform-specific Python features.

Course sources: lessons/00b_python_math.md; lessons/01_states.md; src/qubit_course/experiments.py (basics).