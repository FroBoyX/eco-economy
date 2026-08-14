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

- Clay: **0.05 Town Buy / 0.06 Town Sell**;
- Clay Mold: **0.03 Town Buy / 0.04 Town Sell**;
- Slag: **0.05 Town Buy / 0.08 Town Sell**;
- Ceramic Scrap disposal: **0.15/unit**;
- Tailings disposal is already included upstream in concentrate prices;
- Bloomery fuel is included as a small operating cost using conservative Charcoal pricing.

### Clay Mold check

Core Gathering 1 recipe: 1 Clay + 50 calories → 4 Clay Molds.

At Gathering 1:

- 0.8 Clay × 0.06 retail = 0.048;
- 40 calories = 0.040;
- total craft cost ≈ 0.088;
- cost per mold ≈ **0.022**.

Practical Exchange rounding gives **0.03 Town Buy / 0.04 Town Sell**.

Clay has moved upward from its day-one near-waste value because Pottery, Brick, Cement and other uses now create recurring demand. The effect on metal bars remains very small.

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

This keeps a shallow entry margin while relying on Gold's poor Core conversion ratio—not an oversized raw Gold Ore premium—to create scarcity.

## Why Gold Concentrate can cost more than a Gold Bar

The item units are not one-to-one.

At the first Gold-smelting skill level:

- 1.3 Gold Concentrate → 3 Gold Bars;
- therefore 1 Gold Concentrate → about **2.31 Gold Bars**.

At 18.00 retail, one Gold Concentrate carries about **7.80 credits of concentrate cost per eventual bar**. Smelting adds molds, labor, fuel, waste handling, and a shallow producer margin to reach the 8.70 Gold Bar retail price.

## Validated bar table

| Item | Town Buys | Town Sells |
|---|---:|---:|
| **Iron Bar** | **1.55** | **1.65** |
| **Copper Bar** | **3.40** | **3.60** |
| **Gold Bar** | **8.35** | **8.70** |

## Why Gold is still meaningfully expensive

The complete first-unlock chain consumes roughly:

- 6.4 Iron Ore per Iron Bar;
- 8.96 Copper Ore per Copper Bar;
- **20.8 Gold Ore per Gold Bar**.

Gold therefore remains much more expensive than Iron and Copper even when Gold Ore itself is priced close to Copper Ore.

## Progression

Later Blast Furnace production, higher skill, modules, talents, and Recycling should reduce effective costs and raise producer margins while these fixed bar prices remain stable unless Ironwood deliberately passes technological deflation downstream.
