# UPDATE MODE: Delta Update Workflow

This workflow processes corrections/typos in an existing PDF.

**Filename:** {FILENAME} (e.g., ThermoS26-01)

---

## STEP 1: COMPARE CHANGES

**Task:**
Compare new PDF with existing LaTeX:
- Open `LectureNotes/{FILENAME}.pdf` (updated version)
- Read existing `output/{FILENAME}.tex`
- Read existing `output/{FILENAME}-extracted.txt`
- Extract text from new PDF
- Identify specific differences (typos, corrections, additions)
- Create list of changes

**Output:** 
- Create `output/{FILENAME}-changes.txt` listing all differences
- Create `output/{FILENAME}-extracted-new.txt` from new PDF

---

## STEP 2: DELTA UPDATE

**Agent:** latex-converter (defined in AGENTS.md)

**Task:**
Update ONLY changed sections in existing LaTeX:
- Read change list from Step 1
- Update specific sections in `output/{FILENAME}.tex`
- Preserve existing formatting and structure
- Fix typos or corrections while maintaining style
- Do NOT rewrite sections that haven't changed

**Output:** Updated `output/{FILENAME}.tex`

---

## STEP 3: VERIFY FIGURES

**Agent:** tikz-generator (defined in AGENTS.md)

**Task:**
Check if figures changed:
- Compare figure descriptions in old vs new extracted text
- If any figures changed, regenerate those specific TikZ files
- Keep existing figures that haven't changed

**Output:** Updated figure files if needed

---

## STEP 4: QUICK PROOFREAD

**Agent:** latex-proofreader (defined in AGENTS.md)

**Task:**
Verify updates:
- Compile `output/{FILENAME}.tex` with `latexmk -pdf`
- Verify only changed sections updated correctly
- Ensure no new errors introduced
- Quick comparison with new PDF

**Output:** 
- Compiled `output/{FILENAME}.pdf`
- Confirmation of successful update

---

**Workflow complete.**
