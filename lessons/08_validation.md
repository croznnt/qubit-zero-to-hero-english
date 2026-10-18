# Lesson 08. Robustness, leakage, and convergence checks

## Ensemble control

Device parameters do not always match their nominal values. This example uses detuning and an amplitude-calibration error factor. Training uses detuning in {-0.4,0,0.4} and calibration in {-0.08,0,0.08}. The validation grid uses other values, recorded explicitly in arrays.npz.

```console
python -m qubit_course.cli robustness --seed 42 --output runs/lesson08-robust
python -m qubit_course.cli leakage --output runs/lesson08-leakage
python -m qubit_course.cli convergence --output runs/lesson08-convergence
```

Compare validation_mean_overlap and validation_min_overlap with the baseline in the same metrics file. Do not assume ensemble optimization improves every point, and do not select the most favorable seed to represent the method. A validation grid separate from training is still a finite design and does not cover every possible device error.

## Leakage

The three-level model has ladder couplings proportional to sqrt(n). Applying a pi pulse from the two-level model can produce population in |2>. final_leakage and maximum_leakage are different quantities; low final leakage does not mean the system stayed inside the computational space throughout the evolution.

The current code illustrates three levels only and does not establish convergence with respect to the cutoff. Oscillator research requires at least one larger cutoff, consistent Hamiltonian conventions, and comparisons of both observables and trajectories before drawing conclusions.

## Numerical convergence

convergence compares sesolve results at two tolerance settings with the Rabi formula. Increasing the number of plotting points does not tighten the internal integration steps. For piecewise-constant pulses, the matrix exponential propagates that model exactly up to numerical error; changing the segment count may also change the control space.

## Exercises

1. Run robustness with five seeds, recording failures as well as the total number of objective evaluations.
2. Extend the leakage model to four and five levels using H0 = -alpha*n*(n-1)/2, and check that it matches the three-level model on their shared subspace.
3. Evaluate an optimized pulse under Lindblad noise using mesolve. Choose a channel metric or a set of test states; do not apply unitary trace overlap to density-matrix results.

You are finished when you can report numerical error, model uncertainty, and changes to the objective function as three separate issues.
