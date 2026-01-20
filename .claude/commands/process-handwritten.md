---
allowed-tools: Read, Write, Bash, Edit
argument-hint: [create|update] [filename1 filename2 ...]
description: Process handwritten PDFs to LaTeX. Use 'create' for new transcription or 'update' for delta changes.
---

# Handwritten PDF to LaTeX Processor

## Usage

**Create mode** (transcribe from scratch):
```
/project:process-handwritten create lecture-01.pdf lecture-02.pdf
```

**Update mode** (delta update for typo corrections):
```
/project:process-handwritten update lecture-01.pdf
```

---

## Mode: CREATE

Process: $ARGUMENTS

When mode is **create**:

### Input assumptions:
- All PDF files are located in `LectureNotes/` folder
- Only filename needed (e.g., `lecture-01.pdf` not full path)
- Can process multiple files in sequence

### Step 1: OCR Extraction (for each file)
Delegate to the **ocr-extractor** subagent:
- Extract all text from `LectureNotes/{filename}`
- Preserve document structure and formatting
- Mark uncertain text and identify figures/math expressions
- Save extracted text to `output/{basename}-extracted.txt`

### Step 2: LaTeX Conversion
Delegate to the **latex-converter** subagent:
- Convert extracted text to proper LaTeX format
- Format all mathematical notation correctly
- Create document structure with sections and environments
- Use the template structure from `LatexNotes/MathThermoNotes.tex`
- Use macros from `LatexNotes/Macros/thermoHead.tex` and `thermoSymbols.tex`
- Save to `output/{basename}.tex`

### Step 3: TikZ Diagram Generation
Delegate to the **tikz-generator** subagent:
- Identify all figures marked during OCR
- Convert each figure to standalone TikZ code
- Save diagrams to `output/figures/{basename}-fig-{number}.tex`
- Compile standalone TikZ to PDF
- Update main .tex file with proper \includegraphics references

### Step 4: Compilation and Proofreading
Delegate to the **latex-proofreader** subagent:
- Compile the LaTeX document with latexmk -pdf
- Fix any compilation errors
- Verify mathematical accuracy
- Check against source PDF for quality
- Ensure all figures render correctly

### Step 5: Import into Main Document
For each successfully compiled file:
- Add `\include{../output/{basename}}` to `LatexNotes/MathThermoNotes.tex` in the mainmatter section
- Place includes in order (lecture-01, lecture-02, etc.)
- Ensure proper formatting with comments indicating lecture numbers
- Compile main document to verify integration

### Step 6: Git Commit
After successful compilation of all files:
```bash
git add output/
git add LectureNotes/
git commit -m "docs: transcribe handwritten notes [list filenames]"
```

---

## Mode: UPDATE

Process: $ARGUMENTS

When mode is **update**:

### Input assumptions:
- Source PDF is in `LectureNotes/{filename}`
- Existing LaTeX is in `output/{basename}.tex`
- This is a typo fix or minor correction, not a full rewrite

### Step 1: Compare and Extract Changes
- Load existing LaTeX from `output/{basename}.tex`
- Extract text from updated PDF in `LectureNotes/{filename}`
- Delegate to **ocr-extractor** to extract new version
- Identify differences between old and new versions

### Step 2: Delta Conversion
Delegate to the **latex-converter** subagent:
- Compare extracted text with existing LaTeX
- Identify only the changed sections
- Update LaTeX for those specific sections
- Preserve existing formatting and structure
- Fix typos or corrections while maintaining style

### Step 3: Verify Figures
- Check if any figures changed
- If figures changed, delegate to **tikz-generator** for those specific figures
- Otherwise, keep existing TikZ diagrams
- No need to re-import (already in main document)

### Step 4: Incremental Proofreading
Delegate to the **latex-proofreader** subagent:
- Compile updated LaTeX document
- Verify only changed sections
- Ensure no new errors introduced
- Quick quality check

### Step 5: Git Commit
After successful compilation:
```bash
git add output/{basename}.tex
git add LectureNotes/{filename}
git commit -m "docs: update {filename} with corrections"
```

---

## Error Handling

- If OCR quality is poor, request clarification on uncertain sections
- If LaTeX compilation fails, iterate with proofreader to fix issues
- If figures are complex, create simplified versions first
- For update mode, if changes are too extensive, suggest using create mode instead
- Always verify final PDF matches source content

---

## Examples

**Create single file:**
```
/project:process-handwritten create lecture-01.pdf
```

**Create multiple files:**
```
/project:process-handwritten create lecture-01.pdf lecture-02.pdf lecture-03.pdf
```

**Update existing file:**
```
/project:process-handwritten update lecture-01.pdf
```
