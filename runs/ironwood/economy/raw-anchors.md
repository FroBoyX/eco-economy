# Ironwood Raw Commodity Anchors

These are the currently validated raw anchors for the Ironwood Eco 14 run.

Raw anchors are design inputs. Processed goods must be checked through their complete Core production chain before the anchor is accepted.

## Public Exchange convention

- **Town Buys** = what Ironwood pays a player supplying the resource.
- **Town Sells** = what Ironwood charges a player consuming the resource.
- downstream profitability is tested using Town Sell prices for purchased inputs;
- prices are evaluated at the recipe's minimum required skill level;
- `staticIngredient` recipe inputs are not reduced by skill efficiency;
- Exchange spreads on industrial inputs should stay narrow enough that repeated processing stages do not create artificial inflation.

## Current validated raw anchors

| Resource | Town Buys | Town Sells | Status | Reason |
|---|---:|---:|---|---|
| Sandstone | **0.15** | **0.17** | validated | Arrastra byproduct/reference rock for Iron Ore processing. |
| Granite | **0.15** | **0.17** | validated | Arrastra byproduct/reference rock for Copper and Gold processing. |
| **Sand** | **0.10** | **0.11** | validated current-era | Abundant shovel-gathered construction feedstock. Mortar and Glass create recurring demand without requiring Rock-level pricing. |
| **Clay** | **0.10** | **0.11** | validated current-era | Transitioned from day-one spoil to recurring feedstock for Clay Molds, Pottery, Brick, Cement and later industry. Still treated as abundant rather than scarce. |
| **Iron Ore** | **0.20** | **0.22** | validated | Foundational industrial ore. |
| **Copper Ore** | **0.30** | **0.33** | validated | Moderate scarcity premium; narrowed Exchange spread avoids compounding through the metal chain. |
| **Gold Ore** | **0.30** | **0.35** | validated | Gold's Core conversion is already much worse than Iron/Copper, so the recipe itself supplies the scarcity premium. |

## Sand and Clay as current-era commodities

Sand and Clay are abundant resources, but abundance does not mean zero value once the economy has persistent uses for them.

Ironwood therefore uses **0.10 buy / 0.11 sell** for both in the current era.

This is deliberately below ordinary Rock and far below processed building materials. It gives Gatherers a reason to move these materials into the Exchange while leaving most downstream value creation to Masonry, Pottery, Glassworking and later industry.

### Clay Mold check

Core Gathering 1: 1 Clay + 50 calories → 4 Clay Molds.

At Gathering 1:

- effective Clay: 0.8 × 0.11 = 0.088;
- effective labor: 40 calories = 0.040;
- total craft cost ≈ 0.128;
- cost per mold ≈ **0.032**.

Practical Exchange price: **0.04 buy / 0.05 sell per Clay Mold**.

### Mortar check

Core Masonry 1: 1 Sand + 25 calories → 3 Mortar.

At Masonry 1:

- effective Sand: 0.8 × 0.11 = 0.088;
- effective labor: 20 calories = 0.020;
- total craft cost = 0.108;
- cost per Mortar = **0.036**.

Practical Exchange price: **0.04 buy / 0.05 sell per Mortar**.

### Pottery sanity check

Core Pottery 1 Wet Brick uses 12 Clay + 3 Sand + 1 Wooden Mold + 100 calories → 4 Wet Bricks.

At Pottery 1, Clay + Sand + labor contribute about **0.35 credit per Wet Brick before allocating the reusable Wooden Mold**. That is enough raw-material value to reward supply without overwhelming the later Pottery work, mold cost, firing, fuel and waste handling.

## Why Gold Ore is not given a large raw premium

At first legitimate production, the complete Core chain effectively consumes approximately:

- **6.4 Iron Ore per Iron Bar**;
- **8.96 Copper Ore per Copper Bar**;
- **20.8 Gold Ore per Gold Bar**.

Gold therefore already requires about **3.25×** as much raw ore per finished bar as Iron and **2.32×** as much as Copper before any raw-resource premium is assigned.

Giving Gold Ore an additional large price premium double-counts scarcity and drives advanced downstream goods disproportionately high. Ironwood therefore keeps Gold Ore near Copper Ore and lets the poor Gold conversion ratio create most of Gold's final value.

## Gold unit warning

One Gold Concentrate item is not equivalent to one Gold Bar.

At the entry Bloomery Gold recipe (Smelting 4), **1.3 effective Gold Concentrate produces 3 Gold Bars**. Therefore one Gold Concentrate represents about **2.31 bar-equivalents** before Smelting labor, fuel, mold, waste handling, and margin.

A Gold Concentrate price numerically above a Gold Bar price is therefore mechanically normal. The relevant comparison is concentrate price per bar-equivalent.

## Current metal-chain assumptions

- Mining 1 Arrastra ore crushing;
- Mining 1 Rocker Box concentration;
- Smelting 1 Bloomery for Iron and Copper;
- Smelting 4 Bloomery for Gold;
- 1 credit per 1,000 calories;
- Tailings disposal at **0.35/unit** (working pre-Recycling);
- Ceramic Scrap disposal at **0.15/unit** (working pre-Recycling);
- small Slag byproduct credit;
- Bloomery fuel included as an operating cost.

If Recycling changes the value of Tailings, Ceramic Scrap, or Slag, recalculate the chain directly.
