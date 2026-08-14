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
| **Clay** | **0.05** | **0.06** | validated current-era | Clay began as near-waste, but Clay Molds, Pottery, Brick, Cement and later industrial recipes now create recurring demand. It remains cheaper than Sand/Rock because it is abundant. |
| **Iron Ore** | **0.20** | **0.22** | validated | Foundational industrial ore. |
| **Copper Ore** | **0.30** | **0.33** | validated | Moderate scarcity premium; narrowed Exchange spread avoids compounding through the metal chain. |
| **Gold Ore** | **0.30** | **0.35** | validated | Gold's Core conversion is already much worse than Iron/Copper, so the recipe itself supplies the scarcity premium. |

## Why Clay moved upward from day-one waste pricing

Clay was initially almost a spoil material. That was appropriate before there was meaningful demand.

It is now a recurring input across several profession chains. Eco 14 Core includes Clay in:

- Gathering 1 Clay Molds;
- Pottery 1 Wet Bricks and Shale Brick processing;
- Pottery Ceramic Molds and ceramic goods;
- Masonry 4 Cement;
- later Electronics and environmental-remediation recipes.

That technological transition justifies paying more for Clay without pretending it is scarce.

The current **0.05 buy / 0.06 sell** anchor deliberately keeps Clay below Sand and ordinary Rock while giving Gatherers a reason to collect and deliver it.

### Clay Mold check

Core Gathering 1: 1 Clay + 50 calories → 4 Clay Molds.

At Gathering 1:

- effective Clay: 0.8 × 0.06 = 0.048;
- effective labor: 40 calories = 0.040;
- total craft cost ≈ 0.088;
- cost per mold ≈ **0.022**.

A practical Exchange price is therefore about **0.03 buy / 0.04 sell per Clay Mold**.

### Pottery sanity check

Core Pottery 1 Wet Brick uses 12 Clay + 3 Sand + 1 Wooden Mold + 100 calories → 4 Wet Bricks.

At Pottery 1 and Sand at the intended 0.11 consumer anchor, Clay + Sand + labor contribute about **0.23 credit per Wet Brick before allocating the reusable Wooden Mold**.

That keeps the raw Clay contribution meaningful without allowing the raw material to dominate Brick value. Pottery skill, molds, firing, fuel, waste and later processing still create most of the finished-product value.

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
