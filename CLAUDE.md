# AIDD Review Paper Project

## Project Overview
Writing a critical review paper targeting Nature sub-journal (Nature Reviews Drug Discovery / Nature Machine Intelligence).
- **Topic**: "Why AIDD pipelines fail in practice: the automation gap between benchmarks and bedside"
- **Core thesis**: AI drug discovery automation is a major trend, but current approaches suffer fundamental gaps between computational predictions and real-world clinical outcomes.
- **See**: `review_workflow.md` for full phased plan, `raw.md` for original ideas.

## Language & Writing
- Draft in **English** for the manuscript; internal notes/communication in **中文** is fine.
- Nature-level academic English: active voice, concise, no filler.
- Every claim must have a citation. Use numbered references `[1]`, `[2]` style.
- Balanced tone: critical but constructive. We expose gaps AND propose solutions.
- Target length: 5,000–8,000 words + 4–6 figures.

## Key Workflow Commands
- Build PDF from draft: `pandoc draft_v1.md -o draft_v1.pdf --citeproc --bibliography=references.bib`
- Generate figures: `python figures/gen_*.py`
- Spell/grammar check: use Claude's built-in capabilities

## Directory Structure
```
raw.md                  # Original raw ideas
review_workflow.md      # Phased workflow plan
outline.md              # Detailed section outline
existing_reviews.md     # Landscape of existing reviews
papers/                 # Downloaded key PDFs
notes/                  # Per-paper annotation notes
references.bib          # Bibliography (BibTeX)
figures_data/           # Raw data for figures
figures/                # Generated figures + scripts
draft_v1.md             # First complete draft
draft_v2.md             # Revised draft
cover_letter.md         # Submission cover letter
```

## Working Principles
- IMPORTANT: When searching literature, always use multiple sources (Google Scholar, PubMed, arXiv, bioRxiv). Launch parallel agents for different subtopics.
- IMPORTANT: When drafting, read the current outline.md first to maintain structural coherence.
- When citing papers, always include: authors, title, journal, year, DOI.
- Prefer quantitative data over qualitative claims (e.g., "Phase II success rate is 28%" not "most drugs fail").
- Distinguish clearly between: computational validation, in vitro, in vivo, and clinical outcomes.
- Never fabricate citations or statistics. If data is unavailable, say so explicitly.

## Context: Why This Review Matters
The first author has clinical experience (hospital director, clinical trial center director) — this review uniquely bridges computational AIDD with real clinical pain points that pure CS researchers miss. Key differentiators:
1. Cascading failure analysis across pipeline stages
2. The CS-biochemistry knowledge gap (SOTA ≠ clinical utility)
3. Honest assessment of AI agent capabilities in drug discovery
4. Domain-specific pitfalls (pH, enzymatic hydrolysis, ADMET) that computational papers ignore
