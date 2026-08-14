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
| Clay | **0.15** | **0.17** | working | Used for Clay Molds. Revisit with Gathering/Masonry. |
| **Iron Ore** | **0.20** | **0.22** | validated | Foundational industrial ore. |
| **Copper Ore** | **0.30** | **0.33** | validated | Moderate scarcity premium; narrowed Exchange spread avoids compounding through the metal chain. |
| **Gold Ore** | **0.50** | **0.55** | validated | Gold already has a much worse ore-to-bar conversion than Iron/Copper, so it does not need an additional 20% Exchange toll. |

## Why the raw spreads are narrow

The earlier 0.30 → 0.35 Copper and 0.50 → 0.60 Gold spreads created a large government toll before Mining added any value. That toll then propagated through Crushed Ore, Concentrate, Bars, and every downstream profession.

The current metal anchors retain the extraction values while narrowing the consumption side:

- Iron: 0.20 → 0.22;
- Copper: 0.30 → 0.33;
- Gold: 0.50 → 0.55.

The scarcity difference is primarily created by the ore anchor itself and by the Eco production ratios, not by an increasingly large Exchange markup.

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
