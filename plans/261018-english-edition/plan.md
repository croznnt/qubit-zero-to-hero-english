---
title: Independent English course edition
status: in-progress
priority: P1
effort: medium
branch: main
tags: [translation, education, qutip]
created: 2026-10-18
---

# English edition plan

The user requested an English edition in a new repository uploaded to GitHub, following the preceding request to publish the course. Create `croznnt/qubit-zero-to-hero-english` as a public repository with English learner-facing content. Preserve the original local Vietnamese edition.

## Acceptance criteria

1. Translate all twelve lessons, ten exercise guides and index, and supporting course documentation into English without reducing educational coverage.
2. Preserve all Python source, physics models, example artifacts, tests, dependency requirements, and existing CLI contracts.
3. Replace self-references and clone commands with the new repository name; resolve all local links.
4. Clearly distinguish preserved historical simulation evidence from fresh verification of this edition.
5. Run the full physics and lab regression suite, all reference checks, and review the English documentation before publication.
6. Do not install or copy the session-only CK kit or any persistent skill configuration.
7. Provide complete Windows PowerShell and Ubuntu Bash workflows, including prerequisites, isolated environments, exercises, tests and troubleshooting; extend CI to both operating systems.
8. Commit the reviewed edition, create the new GitHub repository, push main, and verify repository identity and publication status.

## Execution

Independent agents own lesson translation, exercise translation, and six supporting documents. The primary agent owns README, validation, provenance, package checks, and publication. The implementation is an additive documentation edition; scientific source code must remain byte-identical to the original.

| Phase | Status |
| :--- | :--- |
| Copy tracked source without Git history or machine configuration | completed |
| Translate and review English learner-facing documentation | completed |
| Verify source equivalence, tests, CLI and local links | completed |
| Add explicit Windows/Ubuntu instructions and CI matrix | completed |
| Publish and verify new GitHub repository | pending |

## Scope update on October 19, 2026

The user requested Windows and Ubuntu execution instructions. Two full platform guides and matching quick starts are included. The workflow change is intentional and excluded from source-equivalence assertions; scientific code remains unchanged. Original translation review covers the prior snapshot; platform additions are verified separately through documentation checks and the new CI matrix.
