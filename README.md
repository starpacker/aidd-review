# aidd-review

> **Working title:** *“The Automation Gap: Why AI-Driven Drug Discovery
> Pipelines Fail Between Benchmarks and Bedside.”*
>
> An in-progress critical review paper targeting **Nature Reviews Drug
> Discovery / Nature Machine Intelligence**.

This repository holds the manuscript, outline, citation database,
figure-generation scripts, and supporting research notes for the review.

---

## Core thesis

AI has solved the **Chemistry Problem** of drug discovery — designing
drug-like molecules with good ADMET — and the data show it: AI-native
biotechs achieve Phase I success rates of 80–90% versus a 52% historical
baseline. But AI has **not** solved the **Biology Problem** — predicting
whether modulating a target will reverse disease in a human patient. As
of writing, **no AI-designed drug has achieved full FDA approval**, and
Phase II efficacy rates for AI-discovered drugs remain comparable to
industry norms.

The review systematically dissects four distinct biological failure
modes that current computational models are structurally unable to
anticipate (target-hypothesis insufficiency, therapeutic-index
miscalculation, surrogate-endpoint invalidity, undisclosed biological
complexity), grounded in case studies of high-profile AI drug failures
(BEN-2293, EXS-21546, REC-994, DSP-1181), and proposes a three-layer
integration framework (organ-on-a-chip data, clinician-in-the-loop
processes, causal inference algorithms) as a path forward.

## Why this review matters

The first author has clinical experience (hospital director, clinical
trial center director). This review uniquely bridges computational AIDD
with the real clinical pain points that pure-CS researchers tend to
miss — particularly the cascading-failure analysis across pipeline
stages and domain-specific pitfalls (pH, enzymatic hydrolysis, ADMET)
that computational papers ignore.

## Repository layout

```
aidd-review/
├── raw.md                ← original raw ideas brain-dump
├── review_workflow.md    ← phased workflow plan
├── outline.md            ← detailed section-by-section outline (current target ≈ 6,000 words + 6 figures + 1 table)
├── draft_v1.md           ← first complete draft of the manuscript
├── existing_reviews.md   ← landscape survey of existing AIDD reviews + differentiation notes
├── gemini_deep_research.md ← research notes from a deep-research session
├── notes/                ← per-paper annotation notes
├── references.bib        ← bibliography (BibTeX)
├── figures/              ← generated figures + their generation scripts
├── figures_data/         ← raw data feeding the figure scripts
├── experiments/          ← supporting analyses (e.g., 36-molecule gold-standard evaluation)
├── to_do.md              ← rolling task list
└── CLAUDE.md             ← project / writing-style instructions for Claude
```

## Workflow

```bash
# Build PDF from the current draft
pandoc draft_v1.md -o draft_v1.pdf --citeproc --bibliography=references.bib

# Generate / refresh figures
python figures/gen_*.py
```

## Writing rules

- Manuscript is drafted in **English** (Nature-level academic style:
  active voice, concise, no filler). Internal notes may be in 中文.
- **Every claim has a citation.** Numbered references `[1]`, `[2]` style.
- **Quantitative over qualitative** — e.g., *"Phase II success rate is
  28.9%"*, not *"most drugs fail"*.
- **Critical but constructive.** Expose gaps AND propose solutions.
- Distinguish carefully between computational validation, in vitro,
  in vivo, and clinical outcomes.
- **Never fabricate citations or statistics.** If a number isn't
  available, say so explicitly.

See [`CLAUDE.md`](./CLAUDE.md) and [`review_workflow.md`](./review_workflow.md)
for the full project instructions and the phased plan.

## Status

Draft v1 complete — currently in revision toward v2. See [`to_do.md`](./to_do.md)
for the live punch list.
