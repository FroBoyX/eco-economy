# Ironwood Carpentry — Current-Era Table

Derived directly from the supplied Eco 14 Core using current Ironwood producer values, minimum unlock skill, and the corrected static-vs-skill-modified ingredient rules.

Derived producer costs use upstream producer/Town Buy values rather than recursively stacking Exchange resale spreads. Unless a deliberate policy premium applies, priced finished goods use roughly a 5% entry producer margin and the normal Ironwood Exchange spread.

## Current key inputs

- Board: **0.26 Town Buy / 0.27 Town Sell**
- Nail: **0.09 / 0.10**
- Hewn Log: **0.87 / 0.91**
- Lumber: **1.60 / 1.68**
- Iron Bar: **1.70 / 1.79**
- Iron Plate: **1.48 / 1.55**
- Iron Gear: **1.49 / 1.56**
- Glass: **1.45 / 1.52**
- Flaxseed Oil: **1.20 / 1.26** working current-era value
- labor: **0.001 credit/calorie**

## Lumber — Carpentry 1, Sawmill

Core recipe:

- 10 WoodBoard-tag inputs, skill-modified
- 2 Nails, skill-modified
- 0.5 Flaxseed Oil, skill-modified
- 60 calories
- output 2 Lumber

At Carpentry 1 (0.80):

- 8 Boards × 0.26 = 2.080
- 1.6 Nails × 0.09 = 0.144
- 0.4 Flaxseed Oil × 1.20 = 0.480
- 48 calories = 0.048
- total craft cost = **2.752**
- modeled cost/Lumber = **1.376**

Lumber receives Ironwood's modest Tier-3 bulk-construction/logistics uplift.

**Lumber: 1.60 Town Buy / 1.68 Town Sell.**

## Tier-3 structural comparison

| Material | Modeled floor | Town Buys | Town Sells |
|---|---:|---:|---:|
| Brick | ~0.53 | **1.20** | **1.25** |
| Glass | ~1.15 | **1.45** | **1.52** |
| Lumber | ~1.38 | **1.60** | **1.68** |

Mortared Stone remains the cheaper Tier-2 baseline at **0.38 / 0.40**.

## Exchange-ready Carpentry outputs

These recipes have all material dependencies currently priced.

| Item | Carpentry | Modeled entry cost | Town Buys | Town Sells | Notes |
|---|---:|---:|---:|---:|---|
| Distribution Station | 1 | 9.120 | **9.58** | **10.06** | 10 Hewn Logs + 10 Boards, both skill-modified. |
| Icebox | 1 | 9.504 | **9.98** | **10.48** | 10 Hewn Logs + 12 Boards. |
| Machinist Table | 1 | 36.624 | **38.46** | **40.38** | 12 Iron Plates + 2 Wooden Gears + 12 Lumber + 10 Boards. |
| Small Hanging Wood Sign | 1 | 4.820 | **5.06** | **5.31** | Same price as standing version. |
| Small Standing Wood Sign | 1 | 4.820 | **5.06** | **5.31** | Same recipe burden as hanging version. |
| Window Shutters Center | 1 | 5.408 | **5.68** | **5.96** | 4 Lumber, skill-modified. |
| Wood Plaque | 1 | 9.104 | **9.56** | **10.04** | 10 Hewn Logs + 10 Boards. |
| Lumber Chair | 2 | 7.785 | **8.17** | **8.58** | 8 Nails + 6 Lumber, skill-modified. |
| Wooden Dumpster | 2 | 9.600 | **10.08** | **10.58** | 20 Dowels + 2 Iron Bars + 30 Boards. |
| Wooden Latrine | 2 | 7.208 | **7.57** | **7.95** | 5 Hewn Logs + 20 Boards. |
| Coffee Table | 3 | 18.676 | **19.61** | **20.59** | Same material burden as Lumber Hallway Table. |
| Large Hanging Wood Sign | 3 | 6.188 | **6.50** | **6.83** | Same price as standing version. |
| Large Standing Wood Sign | 3 | 6.188 | **6.50** | **6.83** | Same price as hanging version. |
| Lumber Bench | 3 | 10.038 | **10.54** | **11.07** | 2 Nails + 8 Lumber + 5 Boards. |
| Lumber Hallway Table | 3 | 18.676 | **19.61** | **20.59** | 14 Lumber + 16 Boards. |
| Square Lumber Pot | 3 | 4.511 | **4.74** | **4.98** | 4 Lumber. |
| Long Basic Wood Shelf | 4 | 1.560 | **1.64** | **1.72** | Same price as floating version. |
| Long Floating Wood Shelf | 4 | 1.560 | **1.64** | **1.72** | 8 Nails + 6 Boards. |
| Long Lumber Shelf | 4 | 6.786 | **7.13** | **7.49** | 8 Nails + 6 Lumber. |
| Lumber Stockpile | 4 | 17.680 | **18.56** | **19.49** | Skill-modified 15 Lumber + 10 Boards. |
| Short Basic Wood Shelf | 4 | 0.819 | **0.86** | **0.90** | Same price as floating/double variants. |
| Short Floating Wood Shelf | 4 | 0.819 | **0.86** | **0.90** | 4 Nails + 3 Boards. |
| Wood Double Shelf | 4 | 0.819 | **0.86** | **0.90** | 4 Nails + 3 Boards. |
| Wooden Frame Wide | 4 | 1.235 | **1.30** | **1.37** | 2 Hewn Logs. |
| Wooden Rudder | 4 | 6.123 | **6.43** | **6.75** | 2 Iron Gears + 4 Lumber. |
| Elevator Call Post | 5 | 8.688 | **9.12** | **9.58** | 8 Lumber + 6 Boards. |
| **Large Lumber Door** | 5 | **39.836** | **41.83** | **43.92** | **20 Lumber + 30 Boards are static; no resource-efficiency reduction.** |
| **Large Lumber Stockpile** | 5 | **22.260** | **23.37** | **24.54** | 20 Lumber + 15 Boards are skill-modified at Carpentry 5. |
| Lumber Door | 5 | 4.276 | **4.49** | **4.71** | 2 Lumber + 4 Boards are static. |
| Lumber Dresser | 5 | 7.548 | **7.93** | **8.33** | 8 Nails + 6 Lumber + 8 Boards. |
| Ornate Wooden Frame Wide | 5 | 2.016 | **2.12** | **2.23** | 2 Lumber. |
| Shelf Cabinet | 5 | 9.840 | **10.33** | **10.85** | 14 Hewn Logs + 16 Boards. |
| Small Hanging Lumber Sign | 5 | 4.812 | **5.05** | **5.30** | Same price as standing version. |
| Small Standing Lumber Sign | 5 | 4.812 | **5.05** | **5.30** | 6 Boards + 4 Lumber. |
| Store Sign | 5 | 3.720 | **3.91** | **4.11** | 4 Hewn Logs + 10 Boards. |
| Wooden Sliding Door | 5 | 14.928 | **15.67** | **16.45** | 8 Lumber + 8 Boards are static. |
| Large Hanging Lumber Sign | 6 | 8.536 | **8.96** | **9.41** | Same price as standing version. |
| Large Standing Lumber Sign | 6 | 8.536 | **8.96** | **9.41** | 8 Lumber + 10 Boards, skill-modified. |
| **Large Windowed Lumber Door** | 6 | **36.582** | **38.41** | **40.33** | 5 Glass + 15 Lumber + 20 Boards are all static. |
| Lumber Table | 6 | 16.269 | **17.08** | **17.93** | 8 Nails + 18 Lumber. |

## Why the Large Lumber Door costs more than the stockpile

This is source-confirmed rather than a pricing artifact.

The **Large Lumber Door** recipe marks both 20 Lumber and 30 Boards as static ingredients. Carpentry skill does not reduce them.

The **Large Lumber Stockpile** uses 20 Lumber and 15 Boards as Carpentry-skill ingredients. At Carpentry 5, they are reduced to 60% of printed quantities.

The earlier 90-credit door and 55-credit stockpile were too high, but the direction of the difference was mechanically real. At current prices the relationship is roughly **43.92 retail door vs 24.54 retail stockpile**.

## Deferred Carpentry rows

Do not fill these from old tables until their dependencies are canonical:

- Tailoring Table, Wooden Straw Bed — Plant Fiber;
- Loom — Linen Yarn;
- Court Chair — Cotton Fabric;
- Storage Silo — Iron Pipe;
- Bookshelf / Heated Display Cabinet / Refrigerated Display Cabinet — Paper;
- Real Estate Desk — Linen Fabric;
- Towel Rack — Cotton Fabric;
- Kitchen — Steel Bar and Fabric;
- Wooden Fabric Bed — Fabric;
- wooden electric lamps — Copper Wiring/Fabric/Light Bulb;
- Carpentry Basic Upgrade — research-economy input;
- advanced Carpentry/Composites outputs — later technology chains.
