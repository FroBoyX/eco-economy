# Ironwood Blacksmithing — Industrial Intermediates

Rebuilt from Eco 14 Core using the corrected Ironwood metal and wood prices.

This file currently locks Blacksmith products whose dependencies are fully priced. Iron tools remain deferred until Leather Hide is rebuilt through Hunting/Tailoring.

## Inputs

- Iron Bar retail: **1.65**
- Copper Bar retail: **3.60**
- Wood retail: **0.45**

## Core intermediates

### Iron Plate — Blacksmith 1

Core: 1 Iron Bar + 60 calories → 1 Iron Plate.

At Blacksmith 1:

- 0.8 Iron Bar;
- 48 calories;
- entry cost ≈ **1.368**.

**Iron Plate: 1.44 Town Buy / 1.52 Town Sell.**

### Copper Plate — Blacksmith 1

At Blacksmith 1:

- 0.8 Copper Bar;
- 48 calories;
- entry cost ≈ **2.928**.

**Copper Plate: 3.08 Town Buy / 3.24 Town Sell.**

### Nails — Blacksmith 1

Core: 1 Iron Bar + 50 calories → 16 Nails.

At Blacksmith 1, cost ≈ **0.085 per Nail**.

**Nail: 0.09 Town Buy / 0.10 Town Sell.**

### Cooking Utensils — Blacksmith 1

Core: 2 Iron Bars + 50 calories → 1.

Entry cost ≈ **2.68**.

**Cooking Utensils: 2.82 Town Buy / 2.97 Town Sell.**

### Iron Saw Blade — Blacksmith 2

Core: 6 Iron Bars + 60 calories → 1.

At Blacksmith 2 (0.75 multiplier), entry cost ≈ **7.47**.

**Iron Saw Blade: 7.85 Town Buy / 8.25 Town Sell.**

## Sawmill — Blacksmith 2

Core:

- 4 Iron Bars, skill-modified;
- 16 Wood, skill-modified;
- 1 Iron Saw Blade, static;
- 600 calories, skill-modified.

At Blacksmith 2:

- 3 Iron Bars;
- 12 Wood;
- 1 Iron Saw Blade;
- 450 calories.

Using current consumer input prices, entry cost ≈ **19.05**.

**Sawmill: 20.00 Town Buy / 21.00 Town Sell.**

This infrastructure is what supports the current-era Board price of 0.26 / 0.27.

## Current Exchange-ready Blacksmith table

| Item | Town Buys | Town Sells |
|---|---:|---:|
| Nail | **0.09** | **0.10** |
| Iron Plate | **1.44** | **1.52** |
| Copper Plate | **3.08** | **3.24** |
| Cooking Utensils | **2.82** | **2.97** |
| Iron Saw Blade | **7.85** | **8.25** |
| Sawmill | **20.00** | **21.00** |

## Deferred Blacksmith rows

- Iron Axe/Hammer/Hoe/Machete/Pickaxe/Rock Drill/Shovel/Sickle — require Leather Hide;
- Bank, Mint and Currency Exchange — require later building materials and are civic/capital goods whose Exchange markup should be individually reviewed;
- Steel tools and Steel products — require the advanced Smelting/Steel chain;
- lamps/candles — require Tallow/Cotton dependencies.
