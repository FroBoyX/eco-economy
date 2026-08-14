# Ironwood Butchery — Meat, Hides, Tallow and Early Lubricant

Derived from the supplied Eco 14 Core using current Hunting anchors and the depth-sensitive commercial policy.

The Campfire Cooking audit exposed an important cross-profession arbitrage: Campfire Cooking 1 can render Scrap Meat into Tallow cheaply. Tallow and Lubricant are therefore corrected here before final Engineering outputs are locked.

## Core material outputs

| Item | Town Buys | Town Sells | Role |
|---|---:|---:|---|
| Raw Meat | **0.25** | **0.27** | 250-calorie raw food anchor |
| Scrap Meat | **0.09** | **0.10** | low-grade meat / fat-rendering input |
| Leather Hide | **0.60** | **0.63** | strategic tool/equipment input |
| Fur Pelt | **0.45** | **0.47** | clothing/tanning input |
| Shorn Wool | **0.45** | **0.47** | Tailoring input |
| **Tallow** | **0.20** | **0.21** | 200-calorie fat/fuel/industrial input |
| **Lubricant** | **0.14** | **0.15** | early Butchery Grease route |

## Why Tallow is 0.20, not 0.50

Core Campfire Cooking 1 `Render Fat`:

- 10 Scrap Meat
- 20 calories
- → 5 Tallow

At Campfire Cooking 1 (0.80):

- 8 Scrap Meat × 0.10 = 0.800
- 16 calories = 0.016
- cash cost/craft = 0.816
- cash cost/Tallow = **0.163**

At the old 0.50 Town Buy, a player could buy Scrap Meat from Ironwood, render it, and sell the Tallow back for a huge risk-free government arbitrage.

Tallow itself contains **200 calories**, so the locked food-energy anchor gives a natural floor of 0.20.

**Tallow: 0.20 Town Buy / 0.21 Town Sell.**

That still leaves Render Fat a useful Campfire-cook margin without creating a money printer.

## Grease — Lubricant — Butchery 1

Core:

- 2 Tallow
- 180 calories
- → 4 Lubricant

At Butchery 1:

- 1.6 Tallow × 0.21 = 0.336
- 144 calories = 0.144
- cash cost/craft = 0.480
- cash cost/Lubricant = **0.120**

With a shallow processing margin:

**Lubricant: 0.14 Town Buy / 0.15 Town Sell.**

This supersedes the provisional 0.28/0.29 value. Petroleum Lubricant remains a later Oil Drilling technology route and can trigger a structural repricing only if it materially undercuts this already-cheap animal-fat route.

## Carcass processing sanity checks

At Butchery 1:

- Medium Leather carcass cash cost at 1.58 public carcass price ≈ 1.304; 5 Raw Meat + 1 Leather Hide return **1.85 Town Buy value**.
- Medium Wooly carcass cash cost ≈ 1.512; 5 Raw Meat + 1 Leather + 2 Wool return **2.75**.
- Bison at Butchery 2 has cash cost ≈ 2.813; 10 Raw Meat + 2 Leather + 3 Wool return **5.05**.

Hunter and Butcher both retain meaningful margins without inflating the raw carcass anchors.

## Tanning Leather — Butchery 5

Core: 2 Fur Pelts + 25 calories → 1 Leather Hide + 1 Tallow.

At Butchery 5:

- Exchange cash cost ≈ 0.579
- Town Buy outputs = 0.60 + 0.20 = **0.80**

The route remains profitable and converts excess Fur into two useful outputs.

## Prepared meat outputs

| Item | Butchery | Calories | Town Buys | Town Sells | Control |
|---|---:|---:|---:|---:|---|
| Raw Sausage | 2 | 500 | **0.50** | **0.53** | calorie floor |
| Raw Roast | 3 | 600 | **0.60** | **0.63** | calorie floor |
| Raw Bacon | 3 | 200 | **0.35** | **0.37** | recipe cost |
| Prepared Meat | 4 | 600 | **0.60** | **0.63** | calorie floor |
| Prime Cut | 6 | 600 | **1.76** | **1.85** | deep recipe cost |

The corrected Tallow/Lubricant values must be propagated through Basic Engineering and Mechanics before the public ledger is finalized.
