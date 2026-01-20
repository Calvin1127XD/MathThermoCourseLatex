# Math & Thermodynamics Course LaTeX Project

This project uses Claude Code's multi-agent system to convert handwritten notes to LaTeX.

## Project Structure

```
MathThermoCourseLatex/
├── source-documents/     # Place handwritten PDFs here
├── output/              # Generated LaTeX files
│   └── figures/         # TikZ diagrams
├── LatexNotes/          # Existing LaTeX notes
└── LectureNotes/        # Existing lecture materials
```

## Workflow

### Processing Handwritten Documents

**Source PDFs should be in `LectureNotes/` folder**

#### Create Mode (transcribe from scratch):
1. **Add source PDF**: Place handwritten notes in `LectureNotes/`
2. **Run workflow**: `/project:process-handwritten create lecture-01.pdf lecture-02.pdf`
3. **Review output**: Check `output/lecture-01.tex` and compile to PDF
4. **Auto-import**: New chapters are automatically added to `LatexNotes/MathThermoNotes.tex`
5. **Compile main**: The main document includes all lectures in order
6. **Commit**: Changes are automatically committed to git

#### Update Mode (fix typos/corrections):
1. **Teacher updates PDF**: Replace PDF in `LectureNotes/` with corrected version
2. **Run delta update**: `/project:process-handwritten update lecture-01.pdf`
3. **Review changes**: Only modified sections are updated
4. **Commit**: Delta changes are automatically committed to git

### Specialized Subagents

The Main template**: `LatexNotes/MathThermoNotes.tex` (book class, 11pt)
- **Header macros**: `LatexNotes/Macros/thermoHead.tex`
- **Symbol macros**: `LatexNotes/Macros/thermoSymbols.tex`
- **Document class**: book (11pt) for main notes, article for individual chapters
- **Required packages**: amsmath, amsthm, amssymb, graphicx, tikz, pgfplots
- **Math environments**: Use equation, align, gather for display math
- **Theorems**: Use predefined theorem, lemma, definition, examplefigures (Sonnet)
- **latex-proofreader**: Verifies compilation and accuracy (Sonnet)

## LaTeX Conventions

### Document Style
- **Document class**: article (12pt)
- **Required packages**: amsmath, amsthm, amssymb, graphicx, tikz
- **Math environments**: Use equation, align, gather for display math
- **Theorems**: Define theorem, lemma, definition environments

### Mathematical Notation
- Use consistent notation throughout documents
- Inline math: \( ... \) or $ ... $
- Display math: \[ ... \] or equation/align environments
- Vectors: \mathbf{v} or \vec{v}
- Matrices: use bmatrix or pmatrix

### Thermodynamics Specific
- State variables: Use uppercase (P, V, T, S, U, H, G, A)
- Processes: Use subscripts (1→2, iso, rev)
- Partial derivatives: \left(\frac{\partial X}{\partial Y}\right)_Z
- Heat/Work: Q, W with appropriate signs

### Figure Guidelines
- All diagrams as standalone TikZ when possible
- P-V diagrams: Label axes, processes, and states clearly
- System diagrams: Use boxes for boundaries, arrows for flows
- Save standalone TikZ in `output/figures/`
- Include in documents with \includegraphics[width=0.8\textwidth]{figures/name.pdf}

## LaTeX Compilation

Use latexmk for compilation:
```bash
cd output
latexmk -pdf filename.tex
```

Clean auxiliary files:
```bash
latexmk -c
```

## Git Workflow

- Commits are automated through the workflow command
- Commit format: "docs: convert handwritten notes from [filename]"
- Review changes before pushing: `git log`, `git diff`
- Create branches for major revisions

## Troubleshooting

### OCR Issues
- If text quality is poor, rescan at higher resolution
- Mark uncertain text with [?] for manual review
- Complex mathematical notation may need manual correction

### LaTeX Compilation Errors
- Check for missing packages in preamble
- Verify all math mode delimiters are matched
- Ensure special characters are escaped (%, &, _, etc.)
- Run proofreader subagent to identify issues

### TikZ Diagrams
- Test standalone compilation first
- Use appropriate TikZ libraries for your diagram type
- Keep diagrams simple and well-commented
- Scale diagrams to fit page width (0.6-0.8\textwidth)
create [file1 file2 ...]` - Transcribe PDFs from LectureNotes/
- `/project:process-handwritten update [file]` - Delta update for corrected PDF
## Quick Commands

- `/project:process-handwritten [path]` - Full PDF to LaTeX pipeline
- `/memory` - Edit this CLAUDE.md file
- `/mcp` - Manage MCP servers

## Resources

- LaTeX packages: CTAN (ctan.org)
- TikZ examples: TeXample.net
- Math symbols: Detexify (detexify.kirelabs.org)
