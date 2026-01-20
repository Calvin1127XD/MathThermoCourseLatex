# Codex CLI Quick Reference

## Initialize Agents

First time only:
```bash
cd ~/Desktop/MathThermoCourseLatex
codex /init
```

This creates the AGENTS.md file that Codex will use.

## Simple Commands

### Process one lecture:
```bash
codex "Process LectureNotes/ThermoS26-01.pdf following codex-workflows/create.md"
```

### Process multiple lectures:
```bash
codex "Process ThermoS26-01.pdf, ThermoS26-02.pdf, ThermoS26-03.pdf from LectureNotes/ following codex-workflows/create.md"
```

### Update existing lecture:
```bash
codex "Process LectureNotes/ThermoS26-01.pdf following codex-workflows/update.md"
```

### Interactive mode:
```bash
codex
> Follow codex-workflows/create.md for ThermoS26-01
```

## Auto-approve Mode

Skip approval prompts:
```bash
codex --auto-approve "Process LectureNotes/ThermoS26-01.pdf following codex-workflows/create.md"
```

## Check Status

```bash
codex /status
```

## List MCP Tools

```bash
codex /mcp
```

## Change Model

```bash
codex /model gpt-5.2-codex xhigh   # Most accurate (slower)
codex /model gpt-5.2-codex high    # Balanced
codex /model gpt-5.2-codex medium  # Faster (less accurate)
```

## Example Session

```bash
$ codex
> /model gpt-5.2-codex xhigh
> Follow codex-workflows/create.md to process LectureNotes/ThermoS26-01.pdf
[Codex executes all 4 steps automatically]
> /review  # Check what was done
> /quit
```

## Tips

1. **Use workflow files** - They contain all detailed instructions
2. **Review first run** - Check output quality before batch processing
3. **Use xhigh model** - Better for complex mathematical notation
4. **Check MCP tools** - Ensure filesystem access is configured
5. **Approve carefully** - Review what Codex plans to do before approving

## File Structure

```
~/Desktop/MathThermoCourseLatex/
├── AGENTS.md                    # Agent definitions (Codex reads this)
├── codex-workflows/
│   ├── create.md               # Full transcription workflow
│   ├── update.md               # Delta update workflow
│   └── README.md               # This file
├── LectureNotes/               # Source PDFs here
├── output/                     # Generated LaTeX here
└── LatexNotes/                 # Main document and macros
```

## One-Line Command Summary

```bash
# New lecture (most common):
codex "Process LectureNotes/ThermoS26-XX.pdf following codex-workflows/create.md"

# Update lecture:
codex "Process LectureNotes/ThermoS26-XX.pdf following codex-workflows/update.md"
```

Replace `ThermoS26-XX` with your actual filename.
