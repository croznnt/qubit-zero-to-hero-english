# Independent platform additions review

Result: PASS (static review; remote platform execution remains unverified).

Reviewed README OS quickstarts, docs/WINDOWS.md, docs/UBUNTU.md, lessons/00_setup.md, exercises/README.md, .github/workflows/verify.yml, and docs/SOURCE_PROVENANCE.md.

1. Windows PowerShell commands consistently use the environment interpreter, valid paths, and an optional activation step. The base-pip fallback correctly distinguishes its prerequisites.
2. Ubuntu commands install venv prerequisites, use Bash syntax and the Linux interpreter, avoid system pip installation, and explicitly exclude Ubuntu 22.04's default Python 3.10.
3. Both platform guides document expected UNFINISHED starter behavior with exit code 1, trusted-code execution, separate reference-solution checks, tests, complete experiments, and overwrite protection.
4. CI matrix syntax expresses four jobs: Windows and Ubuntu 24.04, each with Python 3.12 and 3.13. Commands are shell-portable. Artifact names include both OS and Python, preventing collisions across matrix jobs. Reference reports and simulation outputs use separate paths.
5. Compared all Python files in source, tests, and exercises byte-for-byte with the original: unchanged. pyproject.toml and requirements-lock.txt also remain identical. Setup documentation and CI are intentional platform additions described in provenance.
6. Historical outputs are identified as original-run evidence rather than new English-edition measurements. Configuring CI is not claimed as a successful remote run.

No blocking correctness issues found. This review inspected commands and source; it did not install dependencies or execute Windows, Ubuntu, or GitHub Actions jobs. Full remote matrix verification is still needed after publication.
