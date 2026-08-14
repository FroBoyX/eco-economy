# Ironwood Masonry — Current-Era Foundation

Rebuilt from Eco 14 Core using entry skill efficiency and current Ironwood consumer input prices.

## Raw inputs used

| Item | Town Buys | Town Sells |
|---|---:|---:|
| Ordinary Rock | **0.15** | **0.17** |
| Sand | **0.10** | **0.11** |
| Limestone | **0.15** | **0.17** |

Limestone is tracked separately from generic Rock because it feeds Crushed Limestone, Quicklime, Glass, Cement and later industry. It currently carries the same extraction value as ordinary Rock; Ironwood is not imposing an extra scarcity premium without evidence of actual shortage.

## Mortar — Masonry 1

Core: 1 Sand + 25 calories → 3 Mortar.

At Masonry 1:

- 0.8 Sand × 0.11 = 0.088
- 20 calories = 0.020
- total craft cost = 0.108
- cost ≈ **0.036 per Mortar**

**Mortar: 0.04 Town Buy / 0.05 Town Sell.**

## Mortared Stone — Masonry 1

Core: 1 Mortar + 4 Rock + 15 calories → 1 Mortared Stone.

At Masonry 1:

- 0.8 Mortar × 0.05 = 0.040
- 3.2 Rock × 0.17 = 0.544
- 12 calories = 0.012
- cost ≈ **0.596**

**Mortared Stone: 0.63 Town Buy / 0.66 Town Sell.**

## Crushed Limestone — Mining 1 dependency

Core Arrastra recipe: 12 static Limestone + 50 calories → 3 Crushed Limestone.

At Mining 1:

- 12 Limestone × 0.17 = 2.04
- 40 calories = 0.040
- cost/output ≈ **0.693**

**Crushed Limestone: 0.73 Town Buy / 0.77 Town Sell.**

## Quicklime — Masonry 1, Blast Furnace

Core: 1 Crushed Limestone + 50 calories → 1 Quicklime.

At Masonry 1, including 50 W Blast Furnace fuel:

- 0.8 Crushed Limestone × 0.77 = 0.616
- 40 calories = 0.040
- fuel ≈ 0.030
- cost ≈ **0.686**

**Quicklime: 0.72 Town Buy / 0.76 Town Sell.**

Quicklime is a later industrial Masonry output because the recipe requires a Blast Furnace.

## Mill Stone and Whetstone

| Item | Entry cost | Town Buys | Town Sells |
|---|---:|---:|---:|
| Whetstone | ~0.432 | **0.46** | **0.49** |
| Mill Stone | ~0.776 | **0.82** | **0.87** |

## Workstations and utility goods

| Item | Town Buys | Town Sells | Notes |
|---|---:|---:|---|
| Stone Brazier | **2.17** | **2.28** | Rock-based; unchanged by Sand correction. |
| Grindstone | **11.96** | **12.56** | Hewn Log, Board and Rock based. |
| **Kiln** | **6.27** | **6.58** | Recalculated from 8 effective Mortar + 8 effective Mortared Stone + 288 calories at Masonry 1. |
| Mill | **13.06** | **13.72** | Rock, Wood and static Mill Stone; unchanged. |

## Current Exchange-ready Masonry table

| Item | Town Buys | Town Sells |
|---|---:|---:|
| Rock | **0.15** | **0.17** |
| Sand | **0.10** | **0.11** |
| Limestone | **0.15** | **0.17** |
| Mortar | **0.04** | **0.05** |
| Mortared Stone | **0.63** | **0.66** |
| Crushed Limestone | **0.73** | **0.77** |
| Quicklime | **0.72** | **0.76** |
| Whetstone | **0.46** | **0.49** |
| Mill Stone | **0.82** | **0.87** |
| Kiln | **6.27** | **6.58** |

Brick is owned by Pottery and Glass by Glassworking; both are now priced from these corrected anchors.
