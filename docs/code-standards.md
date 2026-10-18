# Code standards

The project uses a Python src package with QuTiP as its only quantum framework. Python modules use snake_case; learner-facing exercise directories reuse the existing experiment identifiers.

1. Keep physical conventions in docs/CONVENTIONS.md and preserve existing models, experiments, and CLI contracts.
2. Use NumPy, SciPy, Matplotlib and the standard library for supporting work. Do not add another quantum SDK for an exercise.
3. Prefer explicit computational-basis lowering operators and documented tensor ordering.
4. New physics requires an analytic reference, exhaustive enumeration, or an independently constructed check.
5. Exercise starters must not silently return complete reference answers. Use explicit NotImplementedError for unfinished work.
6. Feedback must report actual failures. Do not count missing or nonfinite values as success.
7. Keep scientific source code separate from presentation and learner feedback. Reuse existing helpers where they teach the intended concept without hiding the entire exercise.
8. Runtime imports must not write files, install dependencies, or alter configuration. Running a learner submission executes that Python file, as documented by the exercise CLI.
