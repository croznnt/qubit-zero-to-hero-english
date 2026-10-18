# Lesson 07. Pulse optimization with bounds

## Define the complete problem

The goal is to implement an X gate over the entire qubit space, not merely transfer |0> to |1>. The duration is fixed at T = 1 microsecond, divided into six segments. Each segment has two amplitudes, ux and uy, bounded from -2*pi to 2*pi radians per microsecond. The Hamiltonian in each segment is (delta*Z + ux*X + uy*Y)/2.

Calculate each segment's unitary using a matrix exponential. The total product in time order is U_last*...*U_first. The loss is 1 minus the squared normalized trace overlap with the X gate. The reference pulse ux = pi, uy = 0 already gives an ideal X gate up to global phase in the absence of noise and detuning.

```console
python -m qubit_course.cli control --seed 42 --output runs/lesson07
```

The program initializes near the reference pulse with small perturbations, then uses SciPy L-BFGS-B. This therefore teaches optimization structure and verification; it is not a demonstration of outperforming a baseline that is already optimal at the nominal setting.

## Read the results

1. training_infidelity evaluates exactly the ensemble used in optimization, which in this lesson contains only the nominal point.
2. validation_mean_overlap and validation_min_overlap use a detuning and calibration grid distinct from the training point.
3. optimizer_success and optimizer_message describe the stopping condition; they do not prove global optimality.
4. slot_split_operator_error compares the same pulse after splitting each constant segment in half. This checks product ordering and composition, rather than establishing convergence for a different continuous model.

## Exercises

1. Replace the target gate with a pi/2 rotation about Y and construct the corresponding analytical baseline.
2. Reduce the maximum amplitude and identify when the current duration no longer supports the simple baseline.
3. Add a smoothness penalty, then report infidelity, smoothness, and fluence separately. Do not combine them into a single claim about fidelity.

You are finished when you can distinguish state transfer from gate synthesis and check bounds, product ordering, and the baseline. This optimizer does not implement GRAPE gradients; compare advanced methods in the [research bridge](../docs/RESEARCH_BRIDGE.md).
