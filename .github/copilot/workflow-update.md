# UPDATE MODE WORKFLOW

Process delta changes for a corrected PDF.

## STEP 1: COMPARE CHANGES

**Action:**
- Open `LectureNotes/{FILENAME}.pdf` (updated version)
- Read existing `output/{FILENAME}.tex`
- Extract text from new PDF
- Identify differences between old and new

---

## STEP 2: DELTA UPDATE

Read and follow: `.github/copilot/agents/latex-converter.md`

**Action:**
- Update ONLY changed sections in `output/{FILENAME}.tex`
- Preserve existing formatting and structure
- Fix typos or corrections while maintaining style

---

## STEP 3: VERIFY FIGURES

**Action:**
- Check if any figures changed in new PDF
- If yes, regenerate those specific TikZ figures
- Otherwise, keep existing figures

---

## STEP 4: QUICK PROOFREAD

Read and follow: `.github/copilot/agents/latex-proofreader.md`

**Action:**
- Compile `output/{FILENAME}.tex` with `latexmk -pdf`
- Verify only changed sections
- Ensure no new errors introduced

---

Replace `{FILENAME}` with the actual filename (without .pdf extension).

Execute all steps without asking for confirmation.
