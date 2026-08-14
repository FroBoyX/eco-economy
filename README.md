# Eco Economy

Canonical design repository for reusable planned-economy, civic, and recycling systems in **Eco 14**.

This repository exists so pricing methods, profession relationships, government design, environmental controls, recycling policy, and reusable tooling can support **multiple Eco servers and runs** without living only in conversation history.

A specific server or playthrough may apply, override, or specialize the reusable framework. Those run-specific decisions belong under `runs/` and must not silently redefine the generic Eco model.

## Core Objective

Build a coherent reusable framework in which:

- every profession has meaningful economic participation;
- prices are intentionally set rather than left to uncontrolled market drift;
- early-profession profit margins are shallow but positive;
- profession profitability grows primarily because skilled players become more efficient, not because canonical prices rise with their skill;
- raw-material anchors keep downstream prices understandable;
- research and progression remain economically reachable without trivializing advancement;
- government policy reduces pollution and resource waste without stopping productive play;
- recycling is a first-class profession and economic loop;
- government can evolve coherently from **Town → Country → Federation**;
- public policy keeps progress steady while preserving useful work for all professions.

## Framework vs. Run State

The root of this repository describes the **general Eco 14 model**.

Run-specific identity and policy belong under:

`runs/<run-name>/`

Examples of run-specific state include:

- settlement and nation names;
- color palettes and visual identity;
- exact market prices selected for that server;
- current population and profession mix;
- local laws and districts;
- treasury policy;
- current shortages or surpluses;
- progression stage;
- temporary interventions;
- server-specific political history.

A run may be informed by the reusable framework without becoming the framework itself.

**Ironwood is the current run, not the identity of the Eco Economy project.**

## Economic Doctrine

### Stable prices, increasing efficiency

The preferred mechanism is:

> **Keep canonical prices stable while production cost falls as the worker becomes more efficient.**

A novice should generally be able to sell a useful product for a small profit. As specialization level, modules, tables, labor organization, and other efficiencies improve, the same nominal sale price should produce a healthier margin.

Skill progression therefore rewards the producer without requiring continuous price inflation.

### Anchored planned economy

Core raw materials and foundational goods receive explicit anchor values. Downstream prices are derived from:

1. canonical input prices;
2. expected recipe consumption;
3. labor and processing burden;
4. waste or byproduct value;
5. desired shallow entry-level profit;
6. progression and strategic importance.

A government may operate credit shops, import/export shops, subsidies, purchase programs, or public-works payments to stabilize these prices when player supply is insufficient.

### Participation before maximum efficiency

The system should prefer economic chains that give multiple professions useful work over chains that allow one profession or public shop to bypass the rest of the economy.

Efficiency improvements are desirable when they come from progression, specialization, infrastructure, organization, recycling, or technology—not from eliminating another profession's reason to participate.

## Government Doctrine

The civic framework is designed as a hierarchy:

1. **Town** — local roads, land use, harvesting rules, waste handling, local subsidies, public works, and municipal exchange policy.
2. **Country** — broader resource, pollution, infrastructure, currency, research, and inter-settlement policy.
3. **Federation** — shared standards and coordination between constituent governments while preserving useful local authority.

Law design must be grounded in what **Eco 14 actually supports** through its civic objects, clauses, conditions, actions, districts, demographics, accounts, taxes, titles, elections, and related systems. Policy wording should never be treated as mechanically enforceable unless the game can actually express and execute it.

The government framework has three co-equal goals:

- **minimize pollution and destructive extraction;**
- **maximize meaningful participation by all professions;**
- **keep technological and economic progression moving at a steady pace.**

## Recycling Doctrine

Recycling is not merely waste cleanup. It is intended to become a participatory economic loop.

Early in progression, garbage may have a **negative import value**: the public system pays people to surrender waste because disposal is itself a service.

As recycling technology becomes available:

- collection remains economically worthwhile;
- recyclers are paid for sorting and processing work;
- recoverable materials gain derived value;
- recovered outputs feed back into other professions as usable inputs;
- pollution and landfill pressure are reduced;
- virgin-resource professions remain useful rather than being completely displaced.

The target loop is:

**production → consumption → waste → paid collection → recycling → recovered inputs → production**

Recycling prices should therefore be evaluated against both environmental benefit and their effect on the wider profession network.

## Repository Authority

The repository is the canonical state store for this project.

Chat sessions are working sessions. When a decision is locked, corrected, or superseded, the repository should be updated so future work does not depend on remembering the full conversation history.

Old material is evidence, not something to preserve. Current framework files should contain only the current reusable model. Current run files should contain only the current state of that run.

## Structure

- `economy/` — reusable pricing doctrine, calculation methods, and cross-profession economics.
- `professions/` — reusable profession economic and participation models.
- `government/` — reusable Town, Country, Federation, law, public-works, and enforcement models.
- `recycling/` — reusable garbage, waste-stream, recycling-progression, and recovered-material models.
- `research/` — reusable research and progression economics.
- `style/` — reusable rendering conventions and presentation tooling.
- `tools/` — deterministic calculators and renderers.
- `decisions/` — important project-level design decisions and corrections.
- `data/` — reusable machine-readable data when introduced.
- `runs/` — server/playthrough-specific state and overrides.
  - `runs/ironwood/` — current Ironwood run.

## Current Status

Repository bootstrap is in progress. Existing Eco 14 work will be recovered into either the reusable framework or the appropriate run profile. A historical Ironwood decision should not be promoted into the generic Eco framework merely because it happened first.
