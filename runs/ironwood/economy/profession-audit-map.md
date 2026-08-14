# Ironwood Eco 14 Profession Audit Map

Source: supplied Eco 14 Core (`Eco14-Core(3).zip`).

This is the master completeness checklist for Ironwood. It is based on all **44 current Core Skill classes**, not on remembered profession names.

The run is currently **entering the Steam era**. For live pricing, Tier 1–3 specialties are the active economy. Higher-tier specialties are tracked as future transition layers and do not set current prices.

## Status meanings

- **canonical-current** — current Core audited and ordinary current Exchange outputs are priced or explicitly scoped.
- **future-transition** — later specialty/technology; may have planning notes but does not set the live run price.
- **policy/special** — not appropriate for an unlimited ordinary commodity order.

## Farmer

| Specialty | Tier | Status |
|---|---:|---|
| Gathering | 1 | **canonical-current** |
| Farming | 2 | **canonical-current** |
| Milling | 2 | **canonical-current** |
| Fertilizers | 3 | **canonical-current** |

## Hunter

| Specialty | Tier | Status |
|---|---:|---|
| Hunting | 1 | **canonical-current** |
| Butchery | 2 | **canonical-current** |

## Chef

| Specialty | Tier | Status |
|---|---:|---|
| Campfire Cooking | 2 | **canonical-current** |
| Baking | 3 | **canonical-current** |
| Cooking | 3 | **canonical-current** |
| Advanced Baking | 4 | **future-transition** |
| Advanced Cooking | 4 | **future-transition** |
| Cutting Edge Cooking | 5 | **future-transition** |

Research/skill-book outputs remain under the separate research economy rather than ordinary food pricing.

## Carpenter

| Specialty | Tier | Status |
|---|---:|---|
| Logging | 1 | **canonical-current** |
| Carpentry | 2 | **canonical-current** |
| Shipwright | 2 | **canonical-current** |
| Paper Milling | 3 | **canonical-current** |
| Composites | 5 | **future-transition** |

## Tailor

| Specialty | Tier | Status |
|---|---:|---|
| Tailoring | 2 | **canonical-current** |

Current Linen/Cotton/Wool/Cellulose goods are priced. Nylon/Plastic/chemical/Steel rows are future and intentionally excluded from live pricing.

## Mason

| Specialty | Tier | Status |
|---|---:|---|
| Mining | 1 | **canonical-current** |
| Masonry | 2 | **canonical-current** |
| Glassworking | 3 | **canonical-current** |
| Pottery | 3 | **canonical-current** |
| Advanced Masonry | 5 | **future-transition** |

Important correction: **Cement is current Masonry 4**, not Advanced Masonry. Current Cement and Asphalt Concrete are live; Reinforced Concrete remains future because its present route requires Fiberglass.

## Smith

| Specialty | Tier | Status |
|---|---:|---|
| Smelting | 2 | **canonical-current** |
| Blacksmith | 3 | **canonical-current** |
| Advanced Smelting | 4 | **future-transition** |

Steel has been inspected for future planning but does not set current Steam-entry prices.

## Engineer

| Specialty | Tier | Status |
|---|---:|---|
| Basic Engineering | 2 | **canonical-current** |
| Mechanics | 3 | **canonical-current** |
| Electronics | 4 | **future-transition** |
| Industry | 5 | **future-transition** |

Current Mechanics is priced through Steam Truck, Steam Tractor, Crane, Cement Kiln and the current supporting workstation chain.

## Scientist

| Specialty | Tier | Status |
|---|---:|---|
| Painting | 3 | **canonical-current** |
| Recycling | 3 | **canonical-current / activation-sensitive** |
| Oil Drilling | 4 | **future-transition** |

Recycling is current, but only exact recovery streams become positive when their recovery lane is actually operating. The negative disposal schedule remains authoritative for unopened/mixed streams.

## Survivalist

| Specialty | Tier | Status |
|---|---:|---|
| Self Improvement | 1 | **policy/special** |

Self Improvement is not an ordinary commodity profession; upgrades/research are handled separately.

## Current canonical milestones

### Raw / agricultural foundation

- raw food: **1 credit / 1,000 calories** baseline;
- Flax Seed **0.04 / 0.05**;
- Flax Fiber **0.29 / 0.30**;
- Cotton Lint **0.39 / 0.41**;
- Leather Hide **0.60 / 0.63**;
- Tallow **0.20 / 0.21**;
- current animal-fat Lubricant **0.14 / 0.15**;
- current Huckleberry-era Sugar **1.16 / 1.22**;
- Flaxseed Oil **0.66 / 0.69**.

### Construction / metal foundation

- Brick **1.20 / 1.25**;
- Glass **1.57 / 1.65**;
- Lumber **1.62 / 1.70**;
- Iron Bar **2.54 / 2.67**;
- Copper Bar **5.14 / 5.40**;
- Gold Bar **12.51 / 13.14**;
- Cement **0.94 / 0.99**;
- Asphalt Concrete **0.78 / 0.82**.

### Steam capital milestones

- Steam Engine **275.75 / 285.75**;
- Portable Steam Engine **439.48 / 449.48**;
- Assembly Line **682.23 / 692.23**;
- Steam Truck **955.62 / 965.62**;
- Steam Tractor **955.62 / 965.62**;
- Crane **1,034.32 / 1,044.32**;
- Wooden Transport Ship **778.08 / 788.08**;
- Medium Fishing Trawler **900.52 / 910.52**.

These large terminal payouts are deliberate capital-formation events rather than recursively compounded margins at the raw-material level.

## Current dependency spine

The active current economy is now source-audited through:

**Gathering/Farming/Hunting -> Butchery/Milling/Tailoring/Fertilizers -> Logging/Mining -> Smelting/Blacksmith/Masonry/Pottery/Glassworking/Paper Milling/Painting/Shipwright -> Basic Engineering/Mechanics -> terminal Steam vehicles/vessels.**

The ordinary food spine is current through **Campfire Cooking, Baking and Cooking**.

## Explicit current exclusions

The current Exchange does **not** use future efficiency to reprice live goods. Explicit future layers include:

- automatic/industrial textile efficiency and Nylon;
- Advanced Smelting / Steel economy;
- Electronics;
- Oil Drilling / petroleum / Plastic / Epoxy;
- Advanced Masonry and Reinforced Concrete;
- Composites;
- Industry;
- advanced/cutting-edge food specialties.

Those will eventually form a separate transition scale. For this run, present technology sets present prices.

## Remaining consolidation work

Recipe discovery for the active Steam-era specialty set is complete enough for public output generation. Remaining work is administrative/presentation:

1. synchronize the central price ledger to the current profession files;
2. normalize tag-product names/variants in public tables;
3. keep civic one-offs and unopened Recycling streams out of unlimited Buy orders;
4. produce the actual Ironwood Exchange tables by profession.
