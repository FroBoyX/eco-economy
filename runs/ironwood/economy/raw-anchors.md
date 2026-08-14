# Ironwood Raw Commodity Anchors

These are the currently validated raw anchors for the Ironwood Eco 14 run.

Raw anchors are design inputs. Processed goods must be checked through their complete Core production chain before the anchor is accepted.

## Public Exchange convention

- **Town Buys** = what Ironwood pays a player supplying the resource.
- **Town Sells** = what Ironwood charges a player consuming the resource.
- downstream profitability is tested using Town Sell prices for purchased inputs;
- prices are evaluated at the recipe's minimum required skill level;
- `staticIngredient` recipe inputs are not reduced by skill efficiency;
- the Exchange spread is deliberately shallow so repeated processing stages do not inflate deep production chains excessively.

## Validated metal-chain anchors

| Resource | Town Buys | Town Sells | Status | Reason |
|---|---:|---:|---|---|
| Sandstone | **0.15** | **0.17** | validated | Arrastra byproduct/reference rock for Iron Ore processing. |
| Granite | **0.15** | **0.17** | validated | Arrastra byproduct/reference rock for Copper and Gold processing. |
| Clay | **0.15** | **0.17** | working | Used for Clay Molds. Its effect on bar cost is small; revisit with Gathering/Masonry. |
| **Iron Ore** | **0.20** | **0.22** | validated | Full ore → crushed → concentrate → Bloomery chain supports the intended ~1.65 Iron Bar retail price. |
| **Copper Ore** | **0.30** | **0.35** | validated | Higher scarcity/extraction anchor plus the less favorable Copper concentration ratio supports ~3.85 Copper Bar retail. |
| **Gold Ore** | **0.50** | **0.60** | validated | Scarcity anchor plus the much poorer Gold concentration/smelting ratio supports ~16 Gold Bar retail. |

These ore anchors are not being retained because they appeared in an older table. They were re-adopted because the Eco 14 Core chain validates them against the current shallow-margin objective.

## Why the ore anchors differ

The three metals do not need identical raw-resource values.

Iron is deliberately inexpensive because it becomes the foundational industrial metal.

Copper receives a larger extraction/scarcity premium and also requires more Crushed Copper Ore per concentrate than Iron.

Gold receives the largest raw-resource premium and then compounds that scarcity through the least favorable concentration and Bloomery output ratio.

This places meaningful value in both extraction and specialist processing instead of forcing all scarcity premium into the final Smelter.

## Current metal-chain checks

The validated chain currently uses:

- Mining 1 Arrastra ore crushing;
- Mining 1 Rocker Box concentration;
- Smelting 1 Bloomery for Iron and Copper;
- Smelting 4 Bloomery for Gold;
- 1 credit per 1,000 calories;
- current Tailings disposal cost of **0.35 per unit**;
- current Ceramic Scrap disposal cost of **0.15 per unit**;
- a small Slag byproduct credit;
- Bloomery fuel consumption as a real but minor operating cost.

The current prices are valid only while those assumptions remain current. If Recycling turns Tailings or Ceramic Scrap into positive-value feedstock, recalculate the chain directly.

## Other raw anchors

Other commodities are intentionally omitted from this validation file until their own profession chain is rebuilt. Ironwood-specific prices for Logging, agriculture, food, Masonry, and later industry should not be inferred from the metal chain.
