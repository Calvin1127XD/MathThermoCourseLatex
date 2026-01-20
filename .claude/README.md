# Multi-Agent Transcription Workflow Setup

This directory contains the configuration for Claude Code's multi-agent system to process handwritten PDFs into LaTeX documents for the Mathematical Thermodynamics notes.

## Quick Start

1. **Install Claude Code** (if not already installed):
   ```bash
   curl -fsSL https://claude.ai/install.sh | bash
   ```

2. **Authenticate**:
   ```bash
   claude
   # Then type: /login
   ```

3. **Add a handwritten PDF**:
   ```bash
   cp ~/path/to/handwritten-notes.pdf LectureNotes/ThermoS26-XX.pdf
   ```

4. **Run the workflow** in Claude Code:
   ```
   claude
   > /project:process-handwritten create ThermoS26-XX
   ```

## Directory Structure

```
.claude/
├── agents/                      # Specialized subagents
│   ├── ocr-extractor.md        # OCR extraction
│   ├── latex-converter.md      # LaTeX conversion
│   ├── tikz-generator.md       # Diagram generation
│   └── latex-proofreader.md    # QA and compilation
├── commands/
│   └── process-handwritten.md  # Workflow orchestration
└── settings.json               # Claude Code settings

LectureNotes/                   # Input PDFs
LatexNotes/                     # LaTeX chapters and main document
output/                         # OCR output and generated figures
└── figures/                    # TikZ figures (PDF/TeX)
```

## Usage Examples

**Create a single lecture**:
```
/project:process-handwritten create ThermoS26-01
```

**Create multiple lectures**:
```
/project:process-handwritten create ThermoS26-01 ThermoS26-02
```

**Update an existing lecture**:
```
/project:process-handwritten update ThermoS26-01
```

## Notes

- The workflow mirrors `codex-workflows/create.md` and `codex-workflows/update.md`.
- Agent specifications mirror `AGENTS.md`.
- Output locations follow the canonical paths in `AGENTS.md`.
