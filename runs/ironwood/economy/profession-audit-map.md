# Ironwood Eco 14 Profession Audit Map

Source basis: supplied Eco 14 Core recovery work and the current Ironwood profession files.

This is the master completeness/status checklist for Ironwood. It tracks the current **44 Core Skill classes** by live-run treatment rather than preserving old price snapshots that can drift from the profession ledgers.

The run is currently **entering the Steam era**. Tier 1–3 specialties are the active economy. Higher-tier specialties are tracked as transition layers and do not set current prices until Ironwood deliberately moves eras.

## Status meanings

- **canonical-current** — current specialty audited and ordinary current outputs are priced or explicitly scoped;
- **operational-current** — canonical-current and now actually operating in the live run;
- **future-transition** — later specialty/technology; may have planning notes but does not set live prices;
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
| Baking | 3 | **operational-current** |
| Cooking | 3 | **operational-current** |
| Advanced Baking | 4 | **future-transition** |
| Advanced Cooking | 4 | **future-transition** |
| Cutting Edge Cooking | 5 | **future-transition** |

Baking and Cooking ordinary-output discovery is complete by distinct market output. Alternate recipes that make the same final item are grouped rather than duplicated. Specialty modules/upgrades are limited capital rather than unlimited food imports.

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

Current Linen/Cotton/Wool/Cellulose goods are priced. Nylon/Plastic/chemical/Steel routes remain later-transition work unless the live run changes.

## Mason

| Specialty | Tier | Status |
|---|---:|---|
| Mining | 1 | **canonical-current** |
| Masonry | 2 | **canonical-current** |
| Glassworking | 3 | **canonical-current** |
| Pottery | 3 | **canonical-current** |
| Advanced Masonry | 5 | **future-transition** |

Cement is current Masonry, not Advanced Masonry. Later Reinforced Concrete remains dependent on later material routes.

## Smith

| Specialty | Tier | Status |
|---|---:|---|
| Smelting | 2 | **canonical-current** |
| Blacksmith | 3 | **canonical-current** |
| Advanced Smelting | 4 | **future-transition** |

Later Steel routes may be inspected for transition planning without back-propagating into the current Steam-entry market.

## Engineer

| Specialty | Tier | Status |
|---|---:|---|
| Basic Engineering | 2 | **canonical-current** |
| Mechanics | 3 | **canonical-current** |
| Electronics | 4 | **future-transition** |
| Industry | 5 | **future-transition** |

## Scientist

| Specialty | Tier | Status |
|---|---:|---|
| Painting | 3 | **canonical-current** |
| Recycling | 3 | **operational-current** |
| Oil Drilling | 4 | **future-transition** |

Current exact sorted Recycling lanes are active for Food Scrap, Bio Residue, Wood Scrap, Glass Scrap, Iron Scrap, Copper Scrap and Gold Scrap. Their positive values are managed/capped procurement tied to recovery capacity. Mixed and future-tech waste streams remain disposal-priced.

## Survivalist

| Specialty | Tier | Status |
|---|---:|---|
| Self Improvement | 1 | **policy/special** |

Self Improvement is not an ordinary commodity profession; upgrades/research remain separately managed.

## Current dependency spine

The active current economy is audited through:

**Gathering/Farming/Hunting -> Butchery/Milling/Tailoring/Fertilizers -> Logging/Mining -> Smelting/Blacksmith/Masonry/Pottery/Glassworking/Paper Milling/Painting/Shipwright -> Basic Engineering/Mechanics -> Steam vehicles/vessels.**

The current ordinary food spine is live through **Campfire Cooking -> Baking/Cooking**.

Recycling now overlays the current economy with exact sorted recovery paths into **Compost, Cellulose Fiber, Glass, Iron Bars, Copper Bars and Gold Bars** without making mixed waste generically valuable.

## Explicit current exclusions

Current pricing does not use future efficiency to reprice live goods. Explicit transition layers include:

- automatic/industrial textile efficiency and Nylon;
- later Advanced Smelting / Steel normalization;
- Electronics;
- Oil Drilling / petroleum / Plastic / Epoxy;
- Advanced Masonry and later composite concrete routes;
- Composites;
- Industry;
- Advanced/Cutting Edge food specialties;
- later Recycling recovery requiring those technologies.

## Remaining consolidation work

Active recipe discovery is substantially complete. Remaining work is primarily:

1. synchronize older stale sections of the central Exchange publication against current profession files as discrepancies surface;
2. normalize grouped/tag-product names and variants;
3. keep civic one-offs, research, Recycling feedstocks and other bounded lanes out of unlimited ordinary Buy orders;
4. recalculate only when live-run conditions or a real economy-wide technology transition changes the structural route.
