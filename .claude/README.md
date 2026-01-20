# Multi-Agent Document Workflow Setup

This directory contains the complete configuration for Claude Code's multi-agent system to process handwritten PDFs into LaTeX documents.

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

3. **Install MCP dependencies**:
   ```bash
   # Ensure Node.js is installed for filesystem MCP
   # Ensure uv/uvx is installed for git MCP
   brew install uv  # macOS
   ```

4. **Add a handwritten PDF**:
   ```bash
   cp ~/path/to/handwritten-notes.pdf source-documents/
   ```

5. **Run the workflow** in Claude Code:
   ```
   claude
   > /project:process-handwritten source-documents/handwritten-notes.pdf
   ```

## What Was Created

### Directory Structure
```
.claude/
├── agents/                      # Specialized subagents
│   ├── ocr-extractor.md        # Fast OCR extraction (Haiku)
│   ├── latex-converter.md      # LaTeX formatting (Sonnet)
│   ├── tikz-generator.md       # Diagram generation (Sonnet)
│   └── latex-proofreader.md    # Quality assurance (Sonnet)
├── commands/
│   └── process-handwritten.md  # Main workflow orchestration
└── settings.json               # Claude Code settings

source-documents/               # Input: Place PDFs here
output/                        # Output: Generated LaTeX files
└── figures/                   # Generated TikZ diagrams

.mcp.json                      # MCP server configuration
CLAUDE.md                      # Project context and conventions
```

### Key Features

**4 Specialized Subagents:**
- **ocr-extractor**: Extracts text from handwritten PDFs with vision OCR
- **latex-converter**: Converts to LaTeX with proper math notation
- **tikz-generator**: Creates TikZ code from hand-drawn diagrams
- **latex-proofreader**: Verifies compilation and accuracy

**Custom Workflow Command:**
- `/project:process-handwritten [pdf-path]` - Complete automation from PDF to git commit

**MCP Servers:**
- Filesystem server: Secure file operations
- Git server: Automated version control

## Usage Examples

### Process a single handwritten document
```bash
claude
> /project:process-handwritten source-documents/lecture-notes.pdf
```

### Use individual subagents
```bash
# Extract text only
> @ocr-extractor Extract text from source-documents/notes.pdf

# Convert existing text to LaTeX
> @latex-converter Convert extracted-text.txt to LaTeX format

# Generate a specific diagram
> @tikz-generator Create a TikZ diagram for the P-V cycle in notes.pdf

# Proofread existing LaTeX
> @latex-proofreader Check output/lecture-notes.tex for errors
```

### Edit project memory
```bash
> /memory  # Opens CLAUDE.md for editing
```

## Configuration Details

### .mcp.json
Configures two MCP servers:
1. **Filesystem**: Access to source-documents/, output/, and existing notes
2. **Git**: Repository automation for the project

### CLAUDE.md
Persistent context including:
- Project structure and workflow
- LaTeX conventions and thermodynamics notation
- Troubleshooting guidance
- Quick reference commands

### Subagent Specifications

Each agent has:
- **Model selection**: Haiku for fast OCR, Sonnet for complex tasks
- **Tool restrictions**: Limited to Read, Write, Bash as needed
- **Specialized prompts**: Domain expertise for each step

## Prerequisites

Before using the workflow, ensure you have:

1. **LaTeX distribution** (for compilation):
   ```bash
   # macOS
   brew install --cask mactex-no-gui
   
   # Or full MacTeX
   brew install --cask mactex
   ```

2. **latexmk** (included with MacTeX):
   ```bash
   which latexmk  # Should return a path
   ```

3. **Git** (for version control):
   ```bash
   git --version  # Should be installed on macOS
   ```

4. **Python uv** (for git MCP):
   ```bash
   brew install uv
   ```

5. **Node.js** (for filesystem MCP):
   ```bash
   brew install node
   ```

## Testing the Setup

1. **Test MCP servers**:
   ```bash
   claude
   > /mcp list
   # Should show filesystem and git servers
   ```

2. **Test with a sample PDF**:
   - Create a simple handwritten note
   - Save as PDF in source-documents/
   - Run the workflow
   - Check output/ for generated .tex file

3. **Verify LaTeX compilation**:
   ```bash
   cd output
   latexmk -pdf test-file.tex
   ```

## Troubleshooting

### MCP Servers Not Loading
- Check Node.js installation: `node --version`
- Check uv installation: `uv --version`
- Verify paths in [.mcp.json](.mcp.json) are absolute

### OCR Quality Issues
- Ensure handwriting is clear and high-contrast
- Scan at 300+ DPI for best results
- Review and manually correct uncertain text marked with [?]

### LaTeX Compilation Errors
- Run `@latex-proofreader` on the output file
- Check for missing packages in LaTeX installation
- Verify all math delimiters are properly matched

### Git Commit Fails
- Ensure git is initialized: `git init` (if needed)
- Configure git user: `git config user.name "Your Name"`
- Check git MCP server is running: `/mcp list`

## Next Steps

1. **Customize conventions**: Edit [CLAUDE.md](CLAUDE.md) for your specific notation preferences
2. **Add shortcuts**: Create additional commands in `.claude/commands/` for common tasks
3. **Extend subagents**: Modify agent prompts in `.claude/agents/` for specialized behavior
4. **Batch processing**: Create shell scripts to process multiple PDFs

## Resources

- Claude Code docs: [claude.ai/docs](https://claude.ai/docs)
- MCP specification: [modelcontextprotocol.io](https://modelcontextprotocol.io)
- LaTeX documentation: [ctan.org](https://ctan.org)
- TikZ examples: [texample.net](https://texample.net)
