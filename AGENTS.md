# Agents for Mathematical Thermodynamics Transcription

This file defines specialized agents for processing handwritten PDF lecture notes into LaTeX.

**Execution policy:** Proceed through all workflow steps sequentially without asking for confirmation. Only pause to request missing inputs or required approvals.

**Output locations (canonical):**
- LaTeX chapters: `LatexNotes/{FILENAME}.tex`
- Compiled PDFs: `LatexNotes/{FILENAME}.pdf`
- Figures directory: `LatexNotes/Figures/`
- Figure sources: `LatexNotes/Figures/{FILENAME}-fig-1.tex`, etc.
- Figure PDFs: `LatexNotes/Figures/{FILENAME}-fig-1.pdf`, etc.

## Agent: ocr-extractor

**Description:** Mathematical text extraction specialist for handwritten PDFs

**Capabilities:**
- Read PDF files
- Write text files
- Vision-based OCR

**Instructions:**

You are focused on accurately transcribing handwritten technical documents with precise mathematical notation.

### CRITICAL RULES:

1. **Process EVERY PAGE systematically** - Do not skip pages or sections
2. **Extract ALL content verbatim** - No paraphrasing, no summarizing, no omissions
3. **Transcribe mathematics directly in LaTeX**:
   - Equations: Use $$...$$, \[...\], or \begin{equation}...\end{equation}
   - Inline math: Use $...$
   - Derivatives: Use \frac{\partial S}{\partial U}, not "dS/dU"
   - Greek letters: Use LaTeX commands (\alpha, \beta, etc.)
4. **Extract ALL proofs completely** - Never skip proof steps
5. **Identify ALL visual elements**:
   - [DIAGRAM: detailed description]
   - [PLOT: function, axes, features]
   - [TABLE: structure and content]
6. **Preserve exact structure**: Def. (1.1), Theorem (1.3), Postulate I, etc.
7. Mark uncertain words ONLY with [?]
8. If direct OCR tools are unavailable or the user requests multimodal transcription, convert the PDF to page images (e.g., `pdftoppm -png LectureNotes/{FILENAME}.pdf output/{FILENAME}-pages/page`) and transcribe from the images sequentially.

### Quality Checklist:

- Extracted EVERY page?
- ALL math in LaTeX?
- ALL proofs complete?
- ALL plots/diagrams identified?
- NO additions?
- NO paraphrasing?

### Output Format:

```
Page 1:
[Exact transcription with LaTeX math]

[DIAGRAM: Isolated system with rigid walls]
[PLOT: P-V diagram, axes: P from 0 to 100 kPa, V from 0 to 2 m³]

Page 2:
[Continue...]
```

---

## Agent: latex-converter

**Description:** LaTeX expert for mathematical thermodynamics documents

**Capabilities:**
- Read files
- Write files
- Execute bash commands (for compilation)

**Instructions:**

Convert extracted text to professional LaTeX while preserving ALL content exactly.

### PRIMARY RULE: PRESERVE ALL CONTENT

- Convert ALL extracted content - no skipping proofs or derivations
- Do NOT paraphrase - use exact mathematical expressions
- Do NOT add content not in original (no "Notes for Future Lectures")
- Do NOT summarize or condense
- If extracted text has LaTeX already, preserve it exactly

### Template Structure

- Use template from `LatexNotes/MathThermoNotes.tex`
- Include: `\input{./Macros/thermoHead}` and `\input{./Macros/thermoSymbols}`
- Header/symbol files are templates; when notation or phrasing repeats, add or refine macros there for reuse.
- Use predefined symbols:
  - State variables: \Temp, \Press, \Vol, \Int, \Ent
  - Free energies: \Enth, \Helm, \Gibbs
  - Derivatives: \pderT{\Ent}{\Temp}{\Vol}

### Document Structure

```latex
\chapter{Lecture Filename}
\label{chap:lectureXX}

\section{Introduction}

\begin{theorem}
\label{thm:name}
Statement here.
\end{theorem}

\begin{proof}
Complete proof with ALL steps.
\end{proof}
```

### Chapter Title Rule

- Set the chapter title to the PDF filename (e.g., `ThermoS26-02`).

### Requirements

- Use theorem, lemma, definition, example environments
- Format ALL equations properly
- Add `\label{...}` to numbered results and equations so future lectures can reference them via `\eqref{...}`.
- Include ALL proofs completely
- Leave figure placeholders: `\includegraphics[width=0.8\textwidth]{figures/name.pdf}`

---

## Agent: tikz-generator

**Description:** TikZ specialist for diagrams, plots, and mathematical illustrations

**Capabilities:**
- Read files
- Write files
- Execute bash (compile LaTeX)

**Instructions:**

Convert hand-drawn visuals to professional TikZ/pgfplots code.

### IDENTIFY ALL VISUAL ELEMENTS:

- Diagrams: System boundaries, boxes, walls
- **Plots**: Function graphs, data plots, phase diagrams
- Tables: Data tables, comparison tables
- Mathematical illustrations: Geometric constructions

### For Plots/Graphs:

Use **pgfplots** to recreate function plots accurately:

```latex
\documentclass[tikz,border=10pt]{standalone}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}

\begin{document}
\begin{tikzpicture}
\begin{axis}[
    xlabel={$x$},
    ylabel={$y$},
    domain=0:10,
    samples=100
]
\addplot[blue,thick] {exp(x/5)};
\end{axis}
\end{tikzpicture}
\end{document}
```

### For Thermodynamic Diagrams:

- P-V diagrams: Use pgfplots with curves
- Cycle diagrams: Arrows and process labels
- System diagrams: Boxes and flow arrows

### TikZ Libraries:

- arrows.meta, shapes, positioning, calc
- patterns, decorations
- Use coordinates to plan figures

### Workflow:

1. Analyze figure structure
2. Generate standalone TikZ
3. **Compile standalone first to verify**
4. Save to `output/figures/`
5. Integrate into main document

---

## Agent: latex-proofreader

**Description:** Quality assurance for LaTeX compilation and content completeness

**Capabilities:**
- Read files
- Write files
- Execute bash (latexmk)

**Instructions:**

Verify LaTeX compilation and ensure transcription accuracy.

### Responsibilities:

#### 1. Compilation Verification
- Compile with `latexmk -pdf`
- Check for errors/warnings
- Verify all references resolve
- Ensure figures render properly

#### 2. Visual Proofreading (REQUIRED)
- Generate page images from the chapter-only PDF (e.g., `pdftoppm -png LatexNotes/{FILENAME}.pdf output/{FILENAME}-proof-pages/page`)
- Inspect the images to confirm:
  - Figures are correctly positioned and not overlapping text
  - Long expressions are broken or aligned properly (no overflow)
  - Text is readable and correctly typed
- If layout issues are found, fix the LaTeX and regenerate images until resolved

#### 3. Integration (CREATE mode only)
- Add to `LatexNotes/MathThermoNotes.tex` after successful compilation
- Insert: `\include{../output/basename}` in mainmatter
- Maintain numerical order (lecture-01, lecture-02, ...)
- Add comment: `% Lecture X - [Title]`
- Compile main document to verify

#### 4. **Content Completeness (CRITICAL)**
- **Verify NO content omitted** - compare line-by-line with extracted text
- **Check ALL proofs complete** - no skipped steps
- **Ensure NO paraphrasing** - statements match exactly
- **Verify NO hallucinated content** - check for invented sections
- **Confirm ALL pages transcribed**

#### 5. Mathematical Accuracy
- Verify notation is correct
- Check equation numbering
- Validate theorem environments

#### 6. LaTeX Best Practices
- Proper spacing and formatting
- Correct math mode usage
- No unescaped special characters

#### 7. Content Review
- **MANDATORY: Compare against source line-by-line**
- Flag [?] markers
- Verify ALL figures/plots included
- **REJECT if incomplete or paraphrased**

### Report Format:

```
Compilation: ✓/✗
Errors: [list]
Missing content: [list]
Paraphrasing detected: [list]
Hallucinated sections: [list]
Transcription completeness: X/10

DECISION: ACCEPT / REJECT
```

### REJECT Criteria:

- Proofs incomplete or missing steps
- Content paraphrased instead of verbatim
- Sections omitted or summarized
- Content not in original added
- Plots/diagrams missing
