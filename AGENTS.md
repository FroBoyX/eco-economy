# Agent Instructions

This repository is the canonical working state for the Eco 14 planned-economy project.

## Core authority rule

Do not preserve obsolete assumptions, legacy structures, or prior-file behavior merely because they already exist.

Old files, old chat outputs, prior tables, prior laws, and earlier economic assumptions are evidence only. They are not automatically authoritative.

When new analysis establishes that an older assumption, structure, price, legal mechanism, profession model, or recycling flow is wrong, incomplete, superseded, or no longer useful, replace it directly.

## No preservation or scaffolding

Do not create compatibility layers, migration scaffolding, deprecated aliases, transitional wrappers, parallel old/new systems, or other preservation mechanisms unless the Product Owner explicitly requests them.

Do not retain obsolete files "for reference" inside the active canonical structure if doing so creates ambiguity about which model is current.

Do not preserve bad abstractions, anti-patterns, temporary compromises, or stale calculations simply to reduce churn.

The repository should represent the best current understanding of the intended Eco 14 system, not the historical sequence of how that understanding was reached.

Git history is sufficient for recovering prior states when needed.

## Rewrite policy

When a canonical model changes:

- update or replace the affected canonical files;
- remove superseded assumptions from active documentation;
- recalculate downstream prices or rules that depend on the changed value;
- identify any remaining unresolved dependencies explicitly;
- prefer one clear current model over multiple competing versions.

Do not write "temporary" bridge logic into documentation unless the temporary state is itself a deliberate current design decision.

## Recovery policy

When recovering information from old chats or earlier files:

- recover decisions and evidence, not formatting or structure by default;
- revalidate recovered assumptions against the current project goals;
- do not promote uncertain legacy numbers into canonical status without support;
- if a prior value is no longer defensible, replace it rather than preserving it for continuity;
- mark genuinely unresolved questions as unresolved rather than inventing continuity.

## Project goals

All work should serve the current Eco 14 design goals:

1. Maintain a coherent planned economy with set prices across all professions.
2. Keep initial professional profit margins shallow, with profit increasing primarily through player efficiency and specialization rather than arbitrary price inflation.
3. Build a coherent legal system across Town, Country, and Federation layers.
4. Minimize pollution while preserving useful economic activity and steady technological progression.
5. Maximize meaningful participation across professions rather than allowing a small number of professions to dominate the economy.
6. Treat Recycling as a first-class profession and economic loop that converts waste liabilities into paid work and recovered production inputs.
7. Prefer direct, current, internally coherent design over preserving historical assumptions.

## Decision standard

The correct question is not "How do we preserve what was here before?"

The correct question is "What should the canonical Eco 14 economy and government be now, given the best available evidence and the Product Owner's current direction?"
