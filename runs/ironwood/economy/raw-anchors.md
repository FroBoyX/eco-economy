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

## Validated metal-chain anchors

| Resource | Town Buys | Town Sells | Status | Reason |
|---|---:|---:|---|---|
| Sandstone | **0.15** | **0.17** | validated | Arrastra byproduct/reference rock for Iron Ore processing. |
| Granite | **0.15** | **0.17** | validated | Arrastra byproduct/reference rock for Copper and Gold processing. |
| **Clay** | **0.02** | **0.03** | validated | Abundant shovel-extracted feedstock. Core Gathering 1 turns 1 Clay into 4 Clay Molds, so pricing Clay like premium construction stone was unjustified. |
| **Iron Ore** | **0.20** | **0.22** | validated | Foundational industrial ore. |
| **Copper Ore** | **0.30** | **0.33** | validated | Moderate scarcity premium; narrowed Exchange spread avoids compounding through the metal chain. |
| **Gold Ore** | **0.30** | **0.35** | validated | Gold's Core conversion is already much worse than Iron/Copper, so the recipe itself supplies the scarcity premium. |

## Why Clay stays cheap

Clay is abundant raw material, and its main early metal-chain role is as feedstock for Clay Molds.

Eco 14 Core: Gathering 1 uses 1 skill-modified Clay + 50 skill-modified calories to produce 4 Clay Molds. At Gathering 1, that means 0.8 Clay and 40 calories per craft.

With Clay at 0.03 retail, the material-plus-labor cost is only about 0.064 for four molds, or 0.016 per mold. The practical Exchange price therefore rounds to about **0.02 buy / 0.03 sell per Clay Mold**.

Clay should not be normalized to Rock or Sand merely because all are raw construction materials.

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

A Gold Concentrate price numerically above a Gold Bar price is mechanically normal. The relevant comparison is concentrate price per bar-equivalent.

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
