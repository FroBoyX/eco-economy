# Ironwood Butchery — Meat, Hides, Tallow and Early Lubricant

Derived from the supplied Eco 14 Core using current Hunting anchors and the depth-sensitive commercial policy.

Butchery is the bridge between raw Hunting outputs and several major downstream sectors: food, Tailoring, Blacksmith tools, Engineering and Mechanics.

## Core material outputs

Ironwood working values:

| Item | Town Buys | Town Sells | Role |
|---|---:|---:|---|
| Raw Meat | **0.25** | **0.27** | 250-calorie raw food anchor |
| Scrap Meat | **0.09** | **0.10** | low-grade meat / fat-rendering input |
| Leather Hide | **0.60** | **0.63** | strategic tool, clothing and equipment input |
| Fur Pelt | **0.45** | **0.47** | clothing/tanning input |
| Shorn Wool | **0.45** | **0.47** | Tailoring input |
| Tallow | **0.50** | **0.53** | food/fuel/lighting and early Lubricant feedstock |

Tallow is deliberately above its 200-calorie food floor because its industrial and lighting uses create strategic demand.

## Carcass processing sanity checks

At Butchery 1 (0.80 recipe multiplier):

### Medium Leather carcass

Core: 1 MediumLeatherCarcass → 5 Raw Meat + 1 Leather Hide, 50 calories.

With a 1.58 Exchange carcass cost:

- entry cash cost ≈ 1.304;
- Town Buy output value = 5 × 0.25 + 0.60 = **1.85**.

That leaves a useful Butcher margin while the hunter can still sell the unprocessed carcass directly for 1.50.

### Medium Wooly carcass

Core: 1 MediumWoolyCarcass → 5 Raw Meat + 1 Leather Hide + 2 Shorn Wool.

- entry cash cost at the 1.84 public carcass price ≈ 1.512;
- Town Buy output value = **2.75**.

The extra wool makes wooly animals meaningfully valuable to the processing economy.

### Bison — Butchery 2

Core: 1 Bison Carcass → 10 Raw Meat + 2 Leather Hide + 3 Shorn Wool, 70 calories.

At Butchery 2 (0.75):

- entry cash cost using the 3.68 public carcass price ≈ 2.813;
- Town Buy output value = 2.50 + 1.20 + 1.35 = **5.05**.

Bison therefore gives both hunter and butcher a real windfall without requiring an arbitrary deep-manufacturing multiplier on the carcass itself.

## Scrap Meat — Butchery 1

Core:

- 1 Raw Meat
- 15 calories
- → 3 Scrap Meat

At Butchery 1, Exchange-sourced cash cost is about 0.228/craft or 0.076 per Scrap Meat.

**Scrap Meat: 0.09 / 0.10.**

## Grease — early Lubricant — Butchery 1

This is a major dependency correction.

Core:

- 2 Tallow
- 180 calories
- → 4 Lubricant

At Butchery 1:

- 1.6 Tallow × 0.53 Exchange Sell = 0.848
- 144 calories = 0.144
- cash cost/craft = 0.992
- cash cost/Lubricant = 0.248

With a shallow specialist margin:

**Lubricant: 0.28 Town Buy / 0.29 Town Sell.**

This is the canonical **early-era Lubricant route** for Ironwood. The later Oil Drilling recipe (Petroleum → Lubricant + Sulfur) is an economy-wide technology transition and may justify a later structural repricing.

## Tanning Leather — Butchery 5

Core:

- 2 Fur Pelts
- 25 calories
- → 1 Leather Hide + 1 Tallow

At Butchery 5 (0.60):

- Exchange-sourced cost ≈ 1.2 × 0.47 + 15 calories = 0.579;
- Town Buy outputs = 0.60 + 0.50 = **1.10**.

This high-level conversion is intentionally profitable and turns excess Fur into two useful industrial outputs.

## Prepared meat outputs

Food outputs must satisfy both recipe economics and the locked calorie floor.

| Item | Butchery | Calories | Town Buys | Town Sells | Pricing control |
|---|---:|---:|---:|---:|---|
| Raw Sausage | 2 | 500 | **0.50** | **0.53** | calorie floor exceeds recipe floor |
| Raw Roast | 3 | 600 | **0.60** | **0.63** | calorie floor; also creates 2 Scrap Meat |
| Raw Bacon | 3 | 200 | **0.35** | **0.37** | recipe cost exceeds calorie floor; creates 3 Scrap Meat |
| Prepared Meat | 4 | 600 | **0.60** | **0.63** | calorie floor; creates 4 Scrap Meat |
| Prime Cut | 6 | 600 | **1.76** | **1.85** | deep/high-input premium cut; recipe cash cost dominates calories |

Prime Cut is a good example of why calories cannot be the sole pricing rule: at Butchery 6 it still consumes 5.5 effective Raw Meat at entry efficiency, so pricing it at 0.60 would destroy the butcher's input value.

## Downstream dependencies now resolved

This audit unlocks canonical pricing work for:

- all Iron tools requiring Leather Hide;
- Tailoring Wool and leather clothing lanes;
- early Lubricant-dependent Basic Engineering;
- Gearbox/Steam Engine/Power Hammer and other Mechanics routes using Lubricant;
- Campfire/Baking fat-rendering comparisons;
- several Hunting bows and equipment items.
