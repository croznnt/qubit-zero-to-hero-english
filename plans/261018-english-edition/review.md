# Independent English-edition review

Review date: October 18, 2026. Result: PASS for local translation and regression verification. Publication and remote CI are outside this review.

## Checks performed

1. Compared SHA-256 hashes for 74 preserved files against the original local course: Python source, tests, exercise starters and reference solutions, CI configuration, dependency metadata and lock file, archived seed42 evidence, and LICENSE. All matched. This count includes LICENSE; the primary source-equivalence manifest records 73 source/configuration/evidence files without it.
2. Independently ran the full test suite using the original isolated Python environment, with PYTHONPATH explicitly set to this English edition's src directory and a separate writable pytest temporary directory. Result: 157 passed in 5.13 seconds. The original checkout and its installed dependencies were not modified.
3. Independently ran python -m qubit_course.labs check all --solution against the English edition. All ten reference solutions reported PASSED.
4. Audited 35 Markdown files across the README, contribution guide, docs, lessons, exercises, and current plan. Checked 92 relative links; none pointed to missing files. No stale original guided-lab report paths remained.
5. Confirmed the README clone command and working-directory name target croznnt/qubit-zero-to-hero-english. Research links intentionally continue to point to the original research catalogs.
6. Scanned all learner-facing Markdown for characteristic Vietnamese words and diacritics; no Vietnamese prose remained. Reviewed the translated lesson and exercise structure. Independently compared fenced code blocks in all twelve lessons with the original: none changed.
7. Reviewed scientific conventions: time and angular-frequency units, explicit lowering operator, T1/T2 relation, squared overlaps and unitary fidelity boundaries, tensor/bit ordering, QAOA minimization and layer order, and the teaching-only three-level leakage model remain intact.
8. Checked provenance and validation text. Fresh English-edition checks are distinguished from preserved original-course outputs. Historical metadata and original source_commit values remain unchanged. No external adapter, hardware, MATLAB, or UAV-simulator validation is claimed. Session-only CK workflow tooling is not included as a dependency or persistent skill installation.

## Limits

This review did not publish the repository, execute remote GitHub Actions, provision a clean environment, validate external websites, or run external simulators or quantum hardware. The complete numerical experiments were not rerun by this reviewer; their archived evidence was checked for byte identity. Local tests and ten reference checks do not prove correctness for every possible model parameter or research extension.

No blocking findings remain for the reviewed local English edition.
