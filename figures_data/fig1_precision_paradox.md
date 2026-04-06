# Figure 1: The Precision Paradox — AI vs. Traditional Clinical Success Rates

## Data Table

| Phase | Traditional (BIO 2021) | AI-Native (Jayatunga 2024) | Δ | Interpretation |
|-------|----------------------|---------------------------|---|----------------|
| Phase I → Phase II | 52.0% | 80-90% (21/24) | +28-38 pp | AI clearly superior (ADMET/safety optimization) |
| Phase II → Phase III | 28.9% | ~40% (small N) | +~11 pp | Comparable; AI advantage may be target selection bias |
| Phase III → NDA | 57.8% | Insufficient data | — | Cannot compare |
| Overall LOA (I→Approval) | 7.9% | TBD | — | Cannot compare |

## Notes
- AI Phase I: 21/24 = 87.5% (midpoint of 80-90% range)
- AI Phase II: ~40% is from limited sample. N not explicitly stated by Jayatunga
- Traditional data: n=12,728 transitions, 9,704 programs, 2011-2020
- Key visual: Phase I bars show dramatic divergence; Phase II bars converge

## Visualization Spec
- Type: Grouped bar chart (2 bars per phase: Traditional vs AI)
- X-axis: Phase I, Phase II, Phase III
- Y-axis: Success rate (%)
- Colors: Traditional = gray; AI = blue
- Phase III AI bar: hatched or dotted to indicate "insufficient data"
- Annotation: Arrow pointing to Phase II convergence with label "The Precision Paradox"

## Citations
- BIO/QLS 2021 report
- Jayatunga et al., Drug Discovery Today, 2024
