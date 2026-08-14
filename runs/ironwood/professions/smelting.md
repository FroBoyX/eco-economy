# Ironwood Smelting — Metal Bars

This file contains the currently validated Smelting portion of the Ironwood metal economy.

It uses the corrected Mining chain from `mining.md` and Eco 14 Core. Other Smelting products are intentionally omitted until recalculated from these bar values.

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

- Clay: **0.10 Town Buy / 0.11 Town Sell**;
- Clay Mold: **0.04 Town Buy / 0.05 Town Sell**;
- Slag: **0.05 Town Buy / 0.08 Town Sell**;
- Ceramic Scrap disposal: **0.15/unit**;
- Tailings disposal is already included upstream in concentrate prices;
- Bloomery fuel is included as a small operating cost using conservative Charcoal pricing.

### Clay Mold check

Core Gathering 1 recipe: 1 Clay + 50 calories → 4 Clay Molds.

At Gathering 1:

- 0.8 Clay × 0.11 retail = 0.088;
- 40 calories = 0.040;
- total craft cost ≈ 0.128;
- cost per mold ≈ **0.032**.

Practical Exchange rounding gives **0.04 Town Buy / 0.05 Town Sell**.

The current-era Clay value is higher than the original day-one spoil price because Clay now has recurring uses in molds, Pottery, Brick, Cement and later industry. The effect on metal bars remains too small to change their rounded prices.

## Iron Bar

Smelting 1 effective Bloomery recipe:

- 1.6 Iron Concentrate;
- 1.6 Clay Molds;
- 48 calories;
- 6 Iron Bars;
- 1.6 Slag;
- 1.5 Ceramic Scrap;
- Bloomery fuel.

Using Iron Concentrate retail **5.20**, entry cost remains about **1.47 per bar**.

**Iron Bar: 1.55 Town Buy / 1.65 Town Sell.**

## Copper Bar

Smelting 1 effective Bloomery recipe:

- 1.6 Copper Concentrate;
- 1.6 Clay Molds;
- 48 calories;
- 6 Copper Bars;
- 1.6 Slag;
- 1.5 Ceramic Scrap;
- Bloomery fuel.

Using Copper Concentrate retail **11.75**, entry cost remains about **3.23 per bar**.

**Copper Bar: 3.40 Town Buy / 3.60 Town Sell.**

## Gold Bar

Gold unlocks at Smelting 4, so the Bloomery uses the 0.65 resource multiplier.

Entry-effective recipe:

- **1.3 Gold Concentrate**;
- **1.3 Clay Molds**;
- **39 calories**;
- **3 Gold Bars**;
- **1.3 Slag**;
- **1.5 Ceramic Scrap**;
- Bloomery fuel.

Using Gold Concentrate retail **18.00**, total craft cost remains just under **8 credits per Gold Bar**.

**Gold Bar: 8.35 Town Buy / 8.70 Town Sell.**

## Validated bar table

| Item | Town Buys | Town Sells |
|---|---:|---:|
| **Iron Bar** | **1.55** | **1.65** |
| **Copper Bar** | **3.40** | **3.60** |
| **Gold Bar** | **8.35** | **8.70** |

## Progression

Later Blast Furnace production, higher skill, modules, talents, and Recycling should reduce effective costs and raise producer margins while these fixed bar prices remain stable unless Ironwood deliberately passes technological deflation downstream.
