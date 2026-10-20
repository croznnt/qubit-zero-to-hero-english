# S00: Your first qubit simulation

An English introductory lecture with 12 core slides and 2 reference slides. Allow approximately 60 minutes, with extra installation time as needed.

1. [PowerPoint with speaker notes](deck.pptx)
2. [PDF slides](deck.pdf), rendered for consistent viewing; use the Markdown for selectable commands
3. [Slide content and copyable commands](content.md)
4. [Instructor notes and checkpoint answers](notes.md)

Topics include the course map, native Windows PowerShell and Ubuntu Bash setup, interpreter verification, repository structure, reproducible outputs, the first `basics` experiment, and troubleshooting. Mathematical derivations begin in S01.

The seed 42 reference run produced probability `0.24999999999999994`, measured fraction `0.262`, 2000 shots and Bloch norm `1.0`. These are simulated measurements. Wall time is not a numerical acceptance criterion.

Use [the Windows guide](../../docs/WINDOWS.md) or [the Ubuntu guide](../../docs/UBUNTU.md) for full installation instructions. Run commands from the checkout root, not from this lecture directory. The untouched learner starter intentionally reports `UNFINISHED` until implemented.

## Authoring

`build.mjs` exports the English content, instructor notes and an editable slide builder for an Artifact Session presentation canvas (1280 × 720). Run `writeSources()` to regenerate the Markdown and `build(presentation)` on an empty canvas to create the slides. The Python course does not require this JavaScript authoring tool. Text and commands remain editable in PowerPoint. The cover uses a generated abstract illustration in `assets/cover.png`; it is not a physical apparatus or scientific plot.
