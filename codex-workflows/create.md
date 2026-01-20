# CREATE MODE: Full Transcription Workflow

This workflow processes a handwritten PDF lecture note into LaTeX from scratch.

**Filename:** {FILENAME} (e.g., ThermoS26-01)

---

## STEP 1: OCR EXTRACTION

**Agent:** ocr-extractor (defined in AGENTS.md)

**Task:**
Extract ALL text from `LectureNotes/{FILENAME}.pdf` with these requirements:
- Transcribe ALL mathematics in LaTeX notation immediately
- Extract ALL proofs completely with every step
- Identify ALL visual elements: [DIAGRAM: ...], [PLOT: ...], [TABLE: ...]
- Preserve exact structure (Def., Theorem, Postulate numbers)
- Mark uncertain text with [?] only
- NO paraphrasing, NO omissions, NO additions

**Output:** Create `output/{FILENAME}-extracted.txt`

**Execute this step completely before proceeding.**

---

## STEP 2: LATEX CONVERSION

**Agent:** latex-converter (defined in AGENTS.md)

**Task:**
Convert `output/{FILENAME}-extracted.txt` to LaTeX:
- Use template structure from `LatexNotes/MathThermoNotes.tex`
- At the beginning of each .tex file, put this piece of code so that it can be compiled both as a separated .tex document or be included my the main .tex file.
  \newif\ifthermosubfile
  \ifdefined\THERMONOTESMAIN
    \thermosubfilefalse
  \else
    \thermosubfiletrue
  \fi

  \providecommand{\THERMOEND}{} % safe in both modes

  \ifthermosubfile
    \documentclass[11pt]{book}
    \input{./Macros/thermoHead}
    \input{./Macros/thermoSymbols}
    \graphicspath{{./Figures/}}
    \begin{document}
    \renewcommand{\THERMOEND}{\end{document}}
  \fi

  And at the very end, add this line:

  \THERMOEND
  
- Include macros: `\input{../LatexNotes/Macros/thermoHead}` and `thermoSymbols`
- Use predefined symbols: \Temp, \Press, \Vol, \Int, \Ent, \Enth, \Helm, \Gibbs
- Set chapter title to the PDF filename (e.g., `\chapter{ThermoS26-02}`)
- Preserve ALL content verbatim (NO paraphrasing, NO omissions, NO additions)
- Include ALL proofs with every step
- Create proper theorem, lemma, definition environments
- Leave figure placeholders for TikZ diagrams

**Output:** Create `LatexNotes/{FILENAME}.tex`

**Execute this step completely before proceeding.**

---

## STEP 3: TIKZ GENERATION

**Agent:** tikz-generator (defined in AGENTS.md)

**Task:**
Generate TikZ code for ALL visual elements in extracted text:
- Search for [DIAGRAM], [PLOT], [TABLE] markers
- Create standalone TikZ files for each
- Use pgfplots for function plots and graphs
- Use standard TikZ for system diagrams
- Compile each standalone file to verify
- Save to `output/figures/{FILENAME}-fig-1.tex`, `{FILENAME}-fig-2.tex`, etc.

**Output:** 
- Create all figure files in `LatexNotes/Figures/`
- Update `LatexNotes/{FILENAME}.tex` with correct `\includegraphics` references pointing to `../output/figures/{FILENAME}-fig-*`

**Execute this step completely before proceeding.**

---

## STEP 4: PROOFREADING & INTEGRATION

**Agent:** latex-proofreader (defined in AGENTS.md)

**Task:**
Verify compilation and integrate into main document:

1. **Compile:** Run `cd LatexNotes && latexmk -pdf {FILENAME}.tex`
2. **Fix errors:** If compilation fails, fix errors and recompile
3. **Visual proofreading (REQUIRED):**
   - Generate page images from the chapter-only PDF:
     `pdftoppm -png LatexNotes/{FILENAME}.pdf output/{FILENAME}-proof-pages/page`
   - Inspect images for layout issues:
     - Figures are correctly positioned and do not overlap text
     - Long expressions are broken/aligned properly (no overflow)
     - Text is readable and correctly typed
   - Fix LaTeX and regenerate images until resolved
4. **Verify completeness:** 
   - Compare `LatexNotes/{FILENAME}.tex` line-by-line with `output/{FILENAME}-extracted.txt`
   - Check ALL proofs are complete
   - Verify NO paraphrasing occurred
   - Confirm NO hallucinated content added (like "Notes for Future Lectures")
   - Ensure ALL pages transcribed
5. **Integration:** Add to `LatexNotes/MathThermoNotes.tex`:
   ```latex
   \mainmatter
       % Lecture XX - [Title from PDF]
       \input{./{FILENAME}}
   ```
6. **Final verification:** Compile main document to verify integration

**Output:** 
- Compiled `LatexNotes/{FILENAME}.pdf`
- Updated `LatexNotes/MathThermoNotes.tex`

**Report:**
```
Compilation: ✓/✗
Missing content: [list or "None"]
Paraphrasing: [list or "None"]
Hallucinated additions: [list or "None"]
Transcription completeness: X/10
DECISION: ACCEPT/REJECT
```

If REJECT, return to appropriate step and fix issues.

---

## CRITICAL RULES (from AGENTS.md)

1. **NO PARAPHRASING** - Transcribe verbatim
2. **NO OMISSIONS** - Include ALL content, ALL proofs
3. **NO ADDITIONS** - Don't invent sections
4. **LaTeX math immediately** - Don't use ASCII
5. **ALL plots identified** - Use pgfplots

---

## COMPLETION

After all steps complete successfully:
- Extracted text saved
- LaTeX chapter created
- All figures generated
- Document compiled
- Integrated into main document

**Workflow complete.**
