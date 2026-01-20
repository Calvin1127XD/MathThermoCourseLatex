# EXECUTE THIS FULL WORKFLOW AUTONOMOUSLY

You are processing a handwritten PDF lecture note to LaTeX. Follow these steps IN ORDER without asking for confirmation.

## STEP 1: OCR EXTRACTION

Read and follow: `.github/copilot/agents/ocr-extractor.md`

**Action:**
- Open `LectureNotes/{FILENAME}.pdf`
- Extract ALL text with LaTeX math notation
- Extract ALL proofs completely
- Identify ALL diagrams and plots
- Create `output/{FILENAME}-extracted.txt`

**DO NOT SKIP THIS. Execute now.**

---

## STEP 2: LATEX CONVERSION

Read and follow: `.github/copilot/agents/latex-converter.md`

**Action:**
- Read `output/{FILENAME}-extracted.txt`
- Convert to LaTeX using macros from `LatexNotes/Macros/thermoHead.tex` and `thermoSymbols.tex`
- Preserve ALL content verbatim (NO paraphrasing, NO omissions, NO additions)
- Create `output/{FILENAME}.tex`

**Execute this step immediately after step 1.**

---

## STEP 3: TIKZ GENERATION

Read and follow: `.github/copilot/agents/tikz-generator.md`

**Action:**
- Identify all [DIAGRAM] and [PLOT] markers in extracted text
- Generate standalone TikZ code for each
- Use pgfplots for function plots
- Save to `output/figures/{FILENAME}-fig-*.tex`
- Compile standalone files to verify

**Execute this step immediately.**

---

## STEP 4: PROOFREADING & INTEGRATION

Read and follow: `.github/copilot/agents/latex-proofreader.md`

**Action:**
- Compile `output/{FILENAME}.tex` with `latexmk -pdf`
- Fix any compilation errors
- Verify content completeness (compare with extracted text)
- Add `\include{../output/{FILENAME}}` to `LatexNotes/MathThermoNotes.tex` in mainmatter section
- Add comment: `% Lecture X - [Title]`
- Compile main document to verify integration

**Execute this step and complete the workflow.**

---

## CRITICAL RULES (from .github/copilot/instructions.md)

1. **NO PARAPHRASING** - Transcribe verbatim
2. **NO OMISSIONS** - Include ALL content, ALL proofs
3. **NO ADDITIONS** - Don't invent "Notes for Future Lectures" or summaries
4. **LaTeX math immediately** - Don't use ASCII notation
5. **ALL plots identified** - Use pgfplots to recreate them

---

## DO ALL STEPS WITHOUT ASKING FOR CONFIRMATION

Replace `{FILENAME}` with the actual filename (without .pdf extension).

Execute the complete pipeline from OCR to final integration.
