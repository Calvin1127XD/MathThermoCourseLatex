# Math & Thermodynamics Course LaTeX Project

This project uses a multi-agent workflow to convert handwritten lecture notes into LaTeX.

## Project Structure

```
MathThermoCourseLatex/
├── LectureNotes/         # Input PDFs (ThermoS26-XX.pdf)
├── LatexNotes/           # LaTeX chapters + main document
├── output/               # OCR output and figures
│   └── figures/          # TikZ diagram sources + PDFs
├── AGENTS.md             # Agent specifications
└── codex-workflows/      # create/update workflow definitions
```

## Workflow

### Create Mode (transcribe from scratch)
1. Add PDF to `LectureNotes/` (e.g., `LectureNotes/ThermoS26-03.pdf`).
2. Run: `/project:process-handwritten create ThermoS26-03`.
3. OCR output goes to `output/ThermoS26-03-extracted.txt`.
4. Chapter LaTeX goes to `LatexNotes/ThermoS26-03.tex`.
5. Figures go to `output/figures/ThermoS26-03-fig-*.tex` and `.pdf`.
6. Chapter PDF is built in `LatexNotes/ThermoS26-03.pdf`.
7. Chapter is included in `LatexNotes/MathThermoNotes.tex`.

### Update Mode (typos/corrections only)
1. Replace the PDF in `LectureNotes/`.
2. Run: `/project:process-handwritten update ThermoS26-03`.
3. Changes are limited to modified sections in `LatexNotes/ThermoS26-03.tex`.
4. Updated OCR and change list are saved in `output/`.

## Specialized Subagents

- **ocr-extractor**: Extracts text and math from handwritten PDFs.
- **latex-converter**: Converts extracted text to LaTeX chapters.
- **tikz-generator**: Builds TikZ/pgfplots figures.
- **latex-proofreader**: Compiles and verifies transcription quality.

## LaTeX Conventions

- Use the main template in `LatexNotes/MathThermoNotes.tex`.
- Include macros: `LatexNotes/Macros/thermoHead.tex` and `thermoSymbols.tex`.
- Use theorem/lemma/definition/example environments.
- Label all numbered equations and results.
- Keep notation consistent with the handwritten notes.

## Compilation

Chapter-only:
```bash
cd LatexNotes
latexmk -pdf ThermoS26-03.tex
```

Main document:
```bash
cd LatexNotes
latexmk -pdf MathThermoNotes.tex
```

## Quick Commands

- `/project:process-handwritten create ThermoS26-XX`
- `/project:process-handwritten update ThermoS26-XX`
- `/memory` (edit this file)
