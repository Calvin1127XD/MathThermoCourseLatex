# Codex Workflow: Process Handwritten PDF to LaTeX

## Quick Commands

### Process a new lecture (CREATE mode):
```bash
codex "Process LectureNotes/ThermoS26-01.pdf using the workflow in codex-workflows/create.md"
```

### Update existing lecture (UPDATE mode):
```bash
codex "Process LectureNotes/ThermoS26-01.pdf using the workflow in codex-workflows/update.md"
```

### Process multiple lectures:
```bash
codex "Process LectureNotes/ThermoS26-01.pdf, ThermoS26-02.pdf, ThermoS26-03.pdf using the workflow in codex-workflows/create.md"
```

## Interactive Mode

You can also use Codex interactively:

```bash
codex
```

Then inside Codex CLI:
```
> Follow codex-workflows/create.md to process LectureNotes/ThermoS26-01.pdf
```

## What Gets Created

After running the CREATE workflow:
- `output/ThermoS26-01-extracted.txt` - OCR extracted text
- `output/ThermoS26-01.tex` - LaTeX chapter file
- `output/figures/ThermoS26-01-fig-*.tex` - TikZ diagrams
- `output/ThermoS26-01.pdf` - Compiled PDF
- Updated `LatexNotes/MathThermoNotes.tex` - Main document with new chapter included

## Agent Information

Agents are defined in `AGENTS.md`:
- **ocr-extractor** - Extracts text from handwritten PDFs
- **latex-converter** - Converts to LaTeX with thermodynamics macros
- **tikz-generator** - Creates TikZ diagrams and plots
- **latex-proofreader** - Verifies compilation and content completeness

## Troubleshooting

If Codex asks for approval, you can:
1. Use `/approvals` to see what needs approval
2. Type `/y` or `/yes` to approve and continue
3. Or use `codex --auto-approve` flag to skip approvals

## Model Selection

Default model is `gpt-5.2-codex xhigh`. To change:
```bash
codex /model gpt-5.2-codex medium  # Faster but less capable
codex /model gpt-5.2-codex xhigh   # Slower but more accurate
```
