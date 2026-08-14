# Ironwood Smelting — Metal Bars

This file contains the currently validated Smelting portion of the Ironwood metal economy.

It uses the corrected Mining chain from `mining.md` and Eco 14 Core. Derived producer costs use Town Buy/producer values for intermediate inputs so the public Exchange spread is not recursively compounded through every stage.

## Entry-skill rule

Smelting resource multipliers are:

- level 1: 0.80
- level 2: 0.75
- level 3: 0.70
- level 4: 0.65
- level 5: 0.60
- level 6: 0.55
- level 7: 0.50

Iron and Copper Bloomery recipes require Smelting 1. Gold requires Smelting 4.

## Supporting inputs and environmental costs

- Clay: **0.10 Town Buy / 0.11 Town Sell**
- Clay Mold: **0.04 / 0.05**
- Slag: **0.05 / 0.08** working byproduct value
- Ceramic Scrap disposal: **0.15/unit**
- Tailings disposal is already included upstream in concentrate values
- Charcoal producer value: **1.17**, 20,000 J fuel value
- Bloomery fuel consumption: **10 W**

## Iron Bar — Bloomery, Smelting 1

Effective recipe:

- 1.6 Iron Concentrate
- 1.6 Clay Molds
- 48 calories
- 6 Iron Bars
- 1.6 Slag
- 1.5 Ceramic Scrap
- about 4 effective craft minutes

Producer-value cost:

- 1.6 × 5.84 Iron Concentrate = 9.344
- 1.6 × 0.04 Clay Mold = 0.064
- labor = 0.048
- Ceramic Scrap disposal = 0.225
- Bloomery fuel ≈ 0.140
- Slag credit = −0.080
- total ≈ 9.741
- cost/bar ≈ **1.624**

**Iron Bar: 1.70 Town Buy / 1.79 Town Sell.**

## Copper Bar — Bloomery, Smelting 1

Effective recipe:

- 1.6 Copper Concentrate
- 1.6 Clay Molds
- 48 calories
- 6 Copper Bars
- 1.6 Slag
- 1.5 Ceramic Scrap
- about 4.8 effective craft minutes

Producer-value cost:

- 1.6 × 11.98 Copper Concentrate = 19.168
- molds = 0.064
- labor = 0.048
- Ceramic Scrap disposal = 0.225
- fuel ≈ 0.168
- Slag credit = −0.080
- total ≈ 19.593
- cost/bar ≈ **3.266**

**Copper Bar: 3.43 Town Buy / 3.60 Town Sell.**

## Gold Bar — Bloomery, Smelting 4

Gold unlocks at Smelting 4, so skill-modified resources use the 0.65 multiplier.

Effective recipe:

- 1.3 Gold Concentrate
- 1.3 Clay Molds
- 39 calories
- 3 Gold Bars
- 1.3 Slag
- 1.5 Ceramic Scrap
- about 3.9 effective craft minutes

Producer-value cost:

- 1.3 × 17.02 Gold Concentrate = 22.126
- molds = 0.052
- labor = 0.039
- Ceramic Scrap disposal = 0.225
- fuel ≈ 0.137
- Slag credit = −0.065
- total ≈ 22.514
- cost/bar ≈ **7.505**

**Gold Bar: 7.88 Town Buy / 8.27 Town Sell.**

Gold remains substantially more expensive than Copper because the complete first-unlock chain requires about 20.8 Gold Ore per finished bar versus 8.96 Copper Ore and 6.4 Iron Ore.

## Exchange-ready bar table

| Item | Town Buys | Town Sells | Entry cost/unit |
|---|---:|---:|---:|
| Iron Bar | **1.70** | **1.79** | ~1.624 |
| Copper Bar | **3.43** | **3.60** | ~3.266 |
| Gold Bar | **7.88** | **8.27** | ~7.505 |

## Why these shifted

The previous chain gave Crushed Sandstone/Granite a large byproduct credit based on their hypothetical dedicated crushing cost. Core shows they are generic `CrushedRock`/`Silica` byproducts with no exact-item consumer, so Ironwood now values them as low-value reuse material instead.

At the same time, the corrected pricing model no longer compounds the Exchange retail spread through every industrial stage. Those two corrections largely offset one another: Copper remains at **3.60 retail**, Iron rises modestly, and Gold falls slightly.

## Progression

Later Blast Furnace production, higher skill, modules, talents and Recycling should reduce effective costs and raise producer margins. Civilization-wide technology transitions may later pass part of those gains downstream through deliberate repricing.
