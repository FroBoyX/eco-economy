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

| Resource | Town Buys | Town Sells | Reason |
|---|---:|---:|---|
| Wood | **0.40** | **0.45** | Foundational timber anchor. |
| Ordinary Rock | **0.15** | **0.17** | Common mined construction stone. |
| Sandstone | **0.15** | **0.17** | Ordinary rock plus Iron Arrastra reference/byproduct role. |
| Granite | **0.15** | **0.17** | Ordinary rock plus Copper/Gold Arrastra reference/byproduct role. |
| **Limestone** | **0.15** | **0.17** | Tracked separately because it feeds Quicklime, Glass, Cement and later industry; no extra scarcity premium unless actual supply warrants one. |
| **Sand** | **0.10** | **0.11** | Abundant shovel-gathered construction feedstock. |
| **Clay** | **0.10** | **0.11** | Transitioned from day-one spoil to recurring Pottery/Brick/Cement feedstock. |
| **Iron Ore** | **0.20** | **0.22** | Foundational industrial ore. |
| **Copper Ore** | **0.30** | **0.33** | Moderate scarcity premium. |
| **Gold Ore** | **0.30** | **0.35** | Poor Core ore-to-bar conversion already supplies most Gold scarcity. |

## Sand and Clay

Sand and Clay are abundant resources, but abundance does not mean zero value once the economy has persistent uses for them.

Ironwood therefore uses **0.10 buy / 0.11 sell** for both in the current era. They remain cheaper than mined Rock while giving Gatherers a reason to move them into the Exchange.

### Clay Mold check

Gathering 1: 1 Clay + 50 calories → 4 Clay Molds.

At Gathering 1:

- 0.8 Clay × 0.11 = 0.088
- 40 calories = 0.040
- total = 0.128
- cost/mold = **0.032**

Practical Exchange price: **0.04 buy / 0.05 sell**.

### Mortar check

Masonry 1: 1 Sand + 25 calories → 3 Mortar.

At Masonry 1:

- 0.8 Sand × 0.11 = 0.088
- 20 calories = 0.020
- total = 0.108
- cost/Mortar = **0.036**

Practical Exchange price: **0.04 buy / 0.05 sell**.

## Limestone

Limestone is separately tracked because demand is strategically different from generic Rock, not because extraction is currently more expensive.

Mining 1 Arrastra crushing uses **12 static Limestone + 40 effective calories → 3 Crushed Limestone**, giving an entry cost around **0.693 per Crushed Limestone** at the 0.17 Limestone retail anchor.

That produces a natural processed premium of **0.73 buy / 0.77 sell** without needing to inflate the raw Limestone price.

## Gold conversion warning

At first legitimate production, the complete Core chain effectively consumes approximately:

- **6.4 Iron Ore per Iron Bar**
- **8.96 Copper Ore per Copper Bar**
- **20.8 Gold Ore per Gold Bar**

Gold already carries a very large recipe scarcity penalty, so Ironwood does not also assign a large raw Gold Ore premium.

One Gold Concentrate also represents about **2.31 Gold Bars** at the first Gold-smelting level, so a concentrate item can numerically cost more than one bar without creating a value inversion.
