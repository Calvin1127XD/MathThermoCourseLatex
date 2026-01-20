---
applyTo: "**"
---

# Mathematical Thermodynamics Course Project

This project transcribes handwritten lecture notes to LaTeX.

## Project Structure

- `LectureNotes/` - Source handwritten PDFs
- `output/` - Generated LaTeX and figures
- `LatexNotes/` - Main document and macros

## Workflow: Handwritten PDF → LaTeX

### CREATE Mode (full transcription):

Process: `ThermoS26-01.pdf` (or multiple files)

**Steps:**
1. **OCR Extraction** (agent: ocr-extractor)
   - Extract ALL text verbatim with LaTeX math
   - Identify ALL proofs, plots, diagrams
   - Save to `output/filename-extracted.txt`

2. **LaTeX Conversion** (agent: latex-converter)
   - Convert to LaTeX preserving ALL content
   - Use macros from `LatexNotes/Macros/`
   - NO paraphrasing, NO additions
   - Save to `output/filename.tex`

3. **TikZ Generation** (agent: tikz-generator)
   - Create TikZ for ALL diagrams and plots
   - Use pgfplots for function graphs
   - Save to `output/figures/`

4. **Proofreading** (agent: latex-proofreader)
   - Compile and verify
   - Compare line-by-line with source
   - REJECT if incomplete or paraphrased
   - Add to main document

5. **Git Commit**
   - Commit all changes

### UPDATE Mode (delta changes):

For typo fixes in existing PDFs:
1. Compare with existing LaTeX
2. Update only changed sections
3. Preserve formatting
4. Quick proofread

## LaTeX Conventions

### Template
- Main: `LatexNotes/MathThermoNotes.tex`
- Headers: `LatexNotes/Macros/thermoHead.tex`
- Symbols: `LatexNotes/Macros/thermoSymbols.tex`

### Thermodynamic Symbols
- `\Temp`, `\Press`, `\Vol` - Temperature, Pressure, Volume
- `\Int`, `\Ent` - Internal energy, Entropy
- `\Enth`, `\Helm`, `\Gibbs` - Enthalpy, Helmholtz, Gibbs
- `\pderT{X}{Y}{Z}` - Partial derivative with subscript

### Structure
- Use `\chapter` for lectures
- Use theorem, lemma, definition environments
- All proofs must be complete

## Critical Rules

1. **NO PARAPHRASING** - Transcribe verbatim
2. **NO OMISSIONS** - Include ALL content
3. **NO ADDITIONS** - Don't invent sections
4. **LaTeX math immediately** - Don't use ASCII
5. **ALL proofs complete** - Every step included
6. **ALL plots identified** - Use pgfplots

## Commands

```bash
# Compile LaTeX
cd output && latexmk -pdf filename.tex

# Compile main document
cd LatexNotes && pdflatex MathThermoNotes.tex
```
