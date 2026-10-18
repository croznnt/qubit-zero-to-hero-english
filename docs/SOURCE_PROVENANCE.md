# Source provenance and translation scope

This is an independently versioned English edition of the local QuTiP course developed in this conversation. Its starting point was the original repository at commit `b5d4fbc` (guided exercises and feedback). The original repository is preserved separately and is not modified by this edition.

## What is translated

The English edition translates the twelve lesson files, ten individual exercise guides, exercise index, study plan, conventions, framework decision, source notes, research bridge, and guided-lab instructions. The README, contribution guide, and validation notes are adjusted for this edition. Filenames, mathematical assumptions, and learner return contracts are retained. Setup examples and the exercise-copy workflow have explicit Windows and Ubuntu variants.

## What is preserved

Python source, starters, reference solutions, regression tests, and project dependencies are copied without behavioral changes. CI is intentionally extended to a Windows/Ubuntu matrix for Python 3.12 and 3.13, with reference checks and platform-specific artifact names. These files were already written in English. The original historical seed42 artifacts in `evidence/seed42/` and `evidence/summary.json` are preserved as historical examples.

The `source_commit` values inside those historical metadata files identify the original local implementation at the time of that run. They do not identify a commit in this new repository. Do not relabel those archived outputs as new English-edition simulation runs.

Fresh verification of this edition is recorded separately in [VALIDATION.md](VALIDATION.md). Translation does not establish compatibility with external simulators, cloud hardware, MATLAB, or other quantum SDKs.

## Session-only workflow tooling

The user's CK portable kit was used as a workflow reference during this conversation only. No kit skills, hooks, agent configuration, installer, machine-specific kit paths, or global settings are included as runtime dependencies. Historical session journals and workflow reports from the original repository are not copied into this edition.
