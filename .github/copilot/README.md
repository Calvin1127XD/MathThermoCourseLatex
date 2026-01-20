# Using This Workflow with GitHub Copilot

Since you have GitHub Copilot through GitHub Education, you can use these agents in VS Code.

## What You Have vs What You Need

❌ **ChatGPT Pro** - Web only, no VS Code integration without API keys
✅ **GitHub Copilot** - Full VS Code integration with agent support!

## Setup in VS Code

### 1. Enable GitHub Copilot (Already Done)
Your GitHub Education gives you Copilot access.

### 2. How to Use the Agents

#### Option A: Direct Chat (Simplest)

Open Copilot Chat (`Cmd+Shift+I` or `Ctrl+Shift+I`) and reference agent files:

```
@workspace Process handwritten PDF from LectureNotes/ThermoS26-01.pdf following .github/copilot/instructions.md in CREATE mode.

Use these agents step by step:
1. ocr-extractor: .github/copilot/agents/ocr-extractor.md
2. latex-converter: .github/copilot/agents/latex-converter.md  
3. tikz-generator: .github/copilot/agents/tikz-generator.md
4. latex-proofreader: .github/copilot/agents/latex-proofreader.md
```

#### Option B: Use Copilot Edits

1. Select files in Explorer
2. Open Copilot Edits (`Cmd+Shift+I`)
3. Paste the same prompt

#### Option C: Custom Task (Automation)

Create `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Process Handwritten PDF (CREATE)",
      "type": "shell",
      "command": "code",
      "args": [
        "--command",
        "workbench.action.chat.open",
        "--args",
        "Process ${input:pdfFile} from LectureNotes/ following .github/copilot/instructions.md in CREATE mode"
      ]
    }
  ],
  "inputs": [
    {
      "id": "pdfFile",
      "type": "promptString",
      "description": "PDF filename"
    }
  ]
}
```

Then: `Cmd+Shift+P` → "Tasks: Run Task" → "Process Handwritten PDF"

## Key Differences from Claude Code

| Feature | Claude Code | GitHub Copilot |
|---------|-------------|----------------|
| Agent files | `.claude/agents/*.md` | `.github/copilot/agents/*.md` |
| Instructions | `CLAUDE.md` | `.github/copilot/instructions.md` |
| Slash commands | `/project:command` | Chat prompts |
| MCP servers | Native support | Native support |
| Invocation | Automatic | Manual via chat |

## Usage Example

### Full Transcription Workflow:

```
Open Copilot Chat and paste:

Process LectureNotes/ThermoS26-01.pdf in CREATE mode:

Step 1: Use ocr-extractor agent (.github/copilot/agents/ocr-extractor.md)
- Extract ALL text with LaTeX math
- Save to output/ThermoS26-01-extracted.txt

Step 2: Use latex-converter agent (.github/copilot/agents/latex-converter.md)
- Convert to LaTeX preserving ALL content
- Use macros from LatexNotes/Macros/
- Save to output/ThermoS26-01.tex

Step 3: Use tikz-generator agent (.github/copilot/agents/tikz-generator.md)
- Create TikZ for all figures
- Save to output/figures/

Step 4: Use latex-proofreader agent (.github/copilot/agents/latex-proofreader.md)
- Compile and verify
- Add to LatexNotes/MathThermoNotes.tex
- REJECT if incomplete

Follow .github/copilot/instructions.md for all rules.
```

## Tips

1. **Reference agent files explicitly** - Copilot will read and follow them
2. **Use @workspace** to give full context
3. **Break into steps** if needed - ask for one agent at a time
4. **Verify each step** before proceeding

## No API Keys Needed!

Your GitHub Copilot subscription (via Education) is all you need. No OpenAI API keys, no extra costs.

## Limitations vs Claude Code

- **Manual invocation** - You paste prompts instead of slash commands
- **No saved workflows** - Each time you type the full instruction
- **Solution**: Save common prompts in `.github/copilot/prompts.md` and copy-paste

This is functionally equivalent to Claude Code's agent system, just with a different interface!
