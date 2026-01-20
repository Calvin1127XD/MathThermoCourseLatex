---
allowed-tools: Read, Write, Bash, Edit
argument-hint: [create|update] [FILENAME1 FILENAME2 ...]
description: Process handwritten PDFs to LaTeX. Use create for full transcription or update for delta changes.
---

# Handwritten PDF to LaTeX Processor

## Usage

**Create mode** (transcribe from scratch):
```
/project:process-handwritten create ThermoS26-01 ThermoS26-02
```

**Update mode** (delta update for corrections):
```
/project:process-handwritten update ThermoS26-01
```

---

## Mode: CREATE

Process: $ARGUMENTS

When mode is **create**:

### Input assumptions
- All PDF files are located in `LectureNotes/`
- Only base filename is needed (e.g., `ThermoS26-01` not full path)
- Can process multiple files in sequence

### Step 1: OCR Extraction (for each file)
Delegate to the **ocr-extractor** subagent:
- Extract all text from `LectureNotes/{FILENAME}.pdf`
- Preserve document structure and formatting
- Mark uncertain text and identify figures/math expressions
- Save extracted text to `output/{FILENAME}-extracted.txt`

### Step 2: LaTeX Conversion
Delegate to the **latex-converter** subagent:
- Convert extracted text to proper LaTeX format
- Format all mathematical notation correctly
- Create document structure with sections and environments
- Use the template structure from `LatexNotes/MathThermoNotes.tex`
- Use macros from `LatexNotes/Macros/thermoHead.tex` and `thermoSymbols.tex`
- Save to `LatexNotes/{FILENAME}.tex`

### Step 3: TikZ Diagram Generation
Delegate to the **tikz-generator** subagent:
- Identify all figures marked during OCR
- Convert each figure to standalone TikZ code
- Save diagrams to `output/figures/{FILENAME}-fig-{number}.tex`
- Compile standalone TikZ to PDF
- Update `LatexNotes/{FILENAME}.tex` with proper \includegraphics references

### Step 4: Compilation and Proofreading
Delegate to the **latex-proofreader** subagent:
- Compile the LaTeX document with `latexmk -pdf`
- Fix any compilation errors
- Verify mathematical accuracy
- Compare line-by-line with `output/{FILENAME}-extracted.txt`
- Ensure all figures render correctly

### Step 5: Import into Main Document
After successful compilation:
- Add `\input{./{FILENAME}}` to `LatexNotes/MathThermoNotes.tex` in mainmatter
- Place includes in order (lecture-01, lecture-02, ...)
- Add comment: `% Lecture X - [Title from PDF]`
- Compile main document to verify integration

---

## Mode: UPDATE

Process: $ARGUMENTS

When mode is **update**:

### Input assumptions
- Updated PDF is in `LectureNotes/{FILENAME}.pdf`
- Existing LaTeX is in `LatexNotes/{FILENAME}.tex`
- Existing extracted text is in `output/{FILENAME}-extracted.txt`
- This is a typo fix or minor correction, not a full rewrite

### Step 1: Compare Changes
- Read existing `LatexNotes/{FILENAME}.tex`
- Read existing `output/{FILENAME}-extracted.txt`
- Extract text from updated PDF
- Identify specific differences (typos, corrections, additions)
- Create `output/{FILENAME}-changes.txt`
- Save new OCR to `output/{FILENAME}-extracted-new.txt`

### Step 2: Delta Update
Delegate to the **latex-converter** subagent:
- Update ONLY changed sections in `LatexNotes/{FILENAME}.tex`
- Preserve existing formatting and structure
- Do NOT rewrite sections that haven't changed

### Step 3: Verify Figures
Delegate to the **tikz-generator** subagent:
- Compare figure descriptions in old vs new extracted text
- Regenerate only figures that changed
- Keep existing figures that haven't changed

### Step 4: Quick Proofread
Delegate to the **latex-proofreader** subagent:
- Compile updated LaTeX document
- Verify only changed sections updated correctly
- Ensure no new errors introduced
- Quick comparison with new PDF

---

## Error Handling

- If OCR quality is poor, request clarification on uncertain sections
- If LaTeX compilation fails, iterate with proofreader to fix issues
- If figures are complex, create simplified versions first
- For update mode, if changes are too extensive, suggest using create mode instead
- Always verify final PDF matches source content
