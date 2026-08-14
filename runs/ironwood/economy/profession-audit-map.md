# Ironwood Eco 14 Profession Audit Map

Source: supplied Eco 14 Core (`Eco14-Core(3).zip`).

This is the master checklist for the Ironwood economy. A profession is not considered covered merely because one downstream item has been priced. Every specialty family below must eventually have either a canonical price table or an explicit reason that it is outside Exchange scope.

## Status meanings

- **canonical-audited** — current Eco 14 source has been inspected and a canonical Ironwood profession file exists.
- **foundation-rebuild** — current source is being rebuilt now because it controls major unresolved inputs.
- **legacy-only** — prior session work exists, but it has not yet been revalidated into the current canonical source/price model.
- **untouched** — not yet audited for the current Ironwood model.

## Farmer

| Specialty | Tier | Approx. source recipes | Status |
|---|---:|---:|---|
| Gathering | 1 | 8 | **foundation-rebuild** |
| Farming | 2 | 37 | **foundation-rebuild** |
| Milling | 2 | 57 | **foundation-rebuild** |
| Fertilizers | 3 | 20 | untouched |

## Hunter

| Specialty | Tier | Approx. source recipes | Status |
|---|---:|---:|---|
| Hunting | 1 | 38 | **foundation-rebuild** |
| Butchery | 2 | 18 | **foundation-rebuild** |

## Chef

| Specialty | Tier | Approx. source recipes | Status |
|---|---:|---:|---|
| Campfire Cooking | 2 | 47 | legacy-only |
| Baking | 3 | 24 | legacy-only |
| Cooking | 3 | 30 | legacy-only |
| Advanced Baking | 4 | 11 | untouched |
| Advanced Cooking | 4 | 27 | untouched |
| Cutting Edge Cooking | 5 | 3 | untouched |

## Carpenter

| Specialty | Tier | Approx. source recipes | Status |
|---|---:|---:|---|
| Logging | 1 | 36 | **canonical-audited** |
| Carpentry | 2 | 62 | **canonical-audited** |
| Shipwright | 2 | 23 | untouched |
| Paper Milling | 3 | 10 | untouched |
| Composites | 5 | 11 | untouched |

## Mason

| Specialty | Tier | Approx. source recipes | Status |
|---|---:|---:|---|
| Mining | 1 | 55 | **canonical-audited** |
| Masonry | 2 | 44 | **canonical-audited** |
| Glassworking | 3 | 17 | **canonical-audited** |
| Pottery | 3 | 23 | **canonical-audited** |
| Advanced Masonry | 5 | 21 | untouched |

## Smith

| Specialty | Tier | Approx. source recipes | Status |
|---|---:|---:|---|
| Smelting | 2 | 19 | **canonical-audited** |
| Blacksmith | 3 | 63 | **canonical-audited** |
| Advanced Smelting | 4 | 26 | untouched |

## Engineer

| Specialty | Tier | Approx. source recipes | Status |
|---|---:|---:|---|
| Basic Engineering | 2 | 25 | **canonical-audited** |
| Mechanics | 3 | 68 | **canonical-audited** |
| Electronics | 4 | 33 | untouched |
| Industry | 5 | 37 | untouched |

## Scientist

| Specialty | Tier | Approx. source recipes | Status |
|---|---:|---:|---|
| Painting | 3 | 10 | untouched |
| Recycling | 3 | 19 | legacy-only / separate garbage-policy work |
| Oil Drilling | 4 | 18 | untouched |

## Survivalist

| Specialty | Tier | Approx. source recipes | Status |
|---|---:|---:|---|
| Self Improvement | 1 | 5 | outside normal commodity pricing except upgrade objects |

## Immediate dependency order

The next canonicalization order is intentionally upstream-first:

1. Gathering raw plant/fiber outputs;
2. Farming crops and seeds;
3. Hunting carcasses/fish and simple hunting processing;
4. Butchery meat, hides, wool, tallow and **early Grease/Lubricant**;
5. Milling flours, cereal germ, oils, sugar and Flaxseed Oil;
6. Tailoring textile intermediates (Flax Fiber → Linen Yarn/Fabric; Cotton Lint → Cotton Thread/Fabric; Wool);
7. re-propagate Leather/Fabric/Lubricant into Blacksmith, Carpentry, Basic Engineering and Mechanics;
8. Smelting Pipe outputs;
9. resume remaining Engineering/Mechanics;
10. then food professions and later technology families.

## Critical source discoveries

- Farming 1 can craft **6 Flax Seeds from 2 Flax Stems** before skill reduction. Flax Seed is therefore a farm-derived input, not an arbitrary raw anchor once Farming exists.
- Gathering 2 converts **3 Flax Stems → 1 Flax Fiber + 0.25 Plant Fiber** and **4 Cotton Bolls → 1 Cotton Lint + 0.25 Plant Fiber**.
- Tailoring 1 converts **1 Flax Fiber → 2 Linen Yarn** and **4 Linen Yarn → 1 Linen Fabric** at the manual Loom route.
- Butchery 1 provides an early non-petroleum Lubricant route: **2 Tallow → 4 Lubricant** (`Grease`). Petroleum Lubricant remains a later Oil Drilling route.
- Campfire processing is an early Tallow source: medium carcasses can produce Charred Meat plus Tallow; Bison produces two Tallow. Later Campfire/Baking routes can render Scrap Meat into Tallow as well.

This checklist supersedes any prior implicit assumption that the economy was complete because the industrial professions had been audited.
