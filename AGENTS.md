# Agent Instructions

This repository is the canonical working state for the reusable Eco 14 planned-economy project and its individual server/run profiles.

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

## Framework vs. run boundary

The root project is a **reusable Eco 14 framework**, not a record of one server.

Generic work belongs in the root domain directories when it is intended to apply across servers or is a reusable method, model, tool, or design principle.

Server/playthrough-specific state belongs under:

`runs/<run-name>/`

Run-specific state includes, but is not limited to:

- town, country, federation, shop, or institution names;
- visual identity and colors;
- exact prices selected for that run;
- current profession roster and population constraints;
- laws currently enacted on that server;
- local districts, treasury choices, and subsidies;
- current shortages, surpluses, resource conditions, and progression stage;
- temporary interventions or server-specific political history.

Do not allow the first or current run to become the assumed universal Eco model.

**Ironwood is a run profile. Ironwood-specific assumptions must not pollute the reusable Eco framework.**

Likewise, generic theory should not overwrite a deliberate run-specific decision unless the Product Owner chooses to change that run.

## Rewrite policy

When a canonical model changes:

- update or replace the affected canonical files;
- remove superseded assumptions from active documentation;
- recalculate downstream prices or rules that depend on the changed value;
- identify any remaining unresolved dependencies explicitly;
- prefer one clear current model over multiple competing versions.

When a run-specific decision changes, update that run directly rather than adding compatibility text for the prior state.

Do not write "temporary" bridge logic into documentation unless the temporary state is itself a deliberate current design decision.

## Recovery policy

When recovering information from old chats or earlier files:

- recover decisions and evidence, not formatting or structure by default;
- first classify each recovered item as **generic framework** or **run-specific state**;
- revalidate recovered assumptions against current project goals;
- do not promote uncertain legacy numbers into canonical status without support;
- do not promote an Ironwood-specific choice into the reusable framework merely because it is the only historical example;
- if a prior value is no longer defensible, replace it rather than preserving it for continuity;
- mark genuinely unresolved questions as unresolved rather than inventing continuity.

## Eco Core reference workflow

Before asking the Product Owner to upload an Eco Core archive, inspect `reference/eco14/` for already-ingested mechanical facts.

The adopted Core snapshot is identified by `reference/eco14/source.json`. Normalized facts derived from that snapshot are preferred for routine economy and policy analysis because they remain available across chat sessions through GitHub.

When the required mechanic has already been ingested, use the repository reference and do **not** request the ZIP again.

When a required mechanic has not yet been ingested and direct Core inspection is necessary:

1. use the supplied Core archive as mechanical evidence;
2. extract the smallest coherent reusable mechanical dataset needed;
3. record the original Core source path and adopted source hash;
4. commit the normalized facts under `reference/eco14/` so the same upload is not required next time;
5. keep raw Core source code out of the public repository unless the Product Owner explicitly approves it and redistribution is known to be appropriate.

Do not confuse extracted mechanical facts with economic policy. Core answers what Eco mechanically does; the project decides what prices, laws, incentives, and server policy should be.

## Project goals

All work should serve the current Eco 14 design goals:

1. Maintain a coherent planned-economy framework with set prices across all professions.
2. Keep initial professional profit margins shallow, with profit increasing primarily through player efficiency and specialization rather than arbitrary price inflation.
3. Build a coherent legal system across Town, Country, and Federation layers.
4. Minimize pollution while preserving useful economic activity and steady technological progression.
5. Maximize meaningful participation across professions rather than allowing a small number of professions to dominate the economy.
6. Treat Recycling as a first-class profession and economic loop that converts waste liabilities into paid work and recovered production inputs.
7. Make the framework reusable across multiple Eco servers and runs.
8. Keep server identity, local policy, and run-specific economic state isolated under the appropriate run profile.
9. Prefer direct, current, internally coherent design over preserving historical assumptions.

## Decision standard

For generic work, the correct question is:

> "What should the reusable Eco 14 economy, government, recycling, and progression model be now?"

For run work, the correct question is:

> "What should this server's current implementation be, given the reusable model, its actual conditions, and the Product Owner's direction?"

The wrong question in either case is:

> "How do we preserve what was here before?"
