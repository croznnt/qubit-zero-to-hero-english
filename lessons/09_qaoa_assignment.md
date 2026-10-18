# Lesson 09. QAOA for a small UAV assignment problem

## Scope

This lesson connects the course to the [UAV and SAR repository](https://github.com/croznnt/uav-swarm-sar-resources). It does not simulate flight or searching for people. Two UAVs receive distinct sectors from three available sectors. Each UAV must receive exactly one sector, and each sector may receive at most one UAV.

The cost matrix is [[1,4,6],[3,1,5]]. The variables x[u,s] are binary. Six variables correspond to six qubits, in bit order [x00,x01,x02,x10,x11,x12], with the first bit on the left. Exhaustive enumeration finds six feasible assignments. The optimum is 100010 with cost 2.

## Energy function

```text
E(x) = sum(u,s) cost[u,s] * x[u,s]
       + 8 * sum(u) (sum(s) x[u,s] - 1)^2
       + 8 * sum(s) x[0,s] * x[1,s]
```

The first penalty penalizes missing or extra assignments; the second penalizes assigning both UAVs to the same sector. Tests confirm that the energy minimum is feasible for this specific instance. Do not generalize the coefficient 8 to other costs or problem sizes without a proof or another check.

## The circuit as operators

Initialize all six qubits in |+>. Each layer applies exp(-i*gamma*diag(E)), followed by exp(-i*beta*sum(X)). Minimize the expectation of E using Powell with three random initializations and depth 2. All quantum states and operators remain in QuTiP.

```console
python -m qubit_course.cli assignment --seed 42 --output runs/lesson09
```

feasible_probability is the total probability of the six feasible bitstrings. expected_penalized_energy differs from best_sampled_feasible_cost. A distribution containing an optimal solution in its support does not guarantee that 2000 actual shots will sample it. The code reports both exact statevector probabilities and sampling results.

## Exercises

1. Change the costs, enumerate all solutions again, and confirm that the penalty remains appropriate.
2. Compare p = 1 and p = 2 across multiple seeds with the same evaluation budget. Do not compare iteration counts alone when evaluation counts differ.
3. Add a search-probability reward to the cost, keeping units and tradeoffs explicit. Export the assignment to a UAV simulator as a separate project, checking coordinates and sector IDs.

You are finished when you can decode bitstrings correctly, compare results with the exact optimum, and explain why this result does not demonstrate quantum advantage. To connect the two QAOA libraries previously studied, see the [research bridge](../docs/RESEARCH_BRIDGE.md).
