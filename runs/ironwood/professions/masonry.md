# Ironwood Masonry — Current-Era Foundation

Rebuilt from Eco 14 Core using entry skill efficiency and the current Ironwood raw hierarchy.

Derived producer costs use Town Buy/producer values for intermediate inputs. The Exchange retail spread is applied afterward rather than compounded through every recipe stage.

## Raw inputs

| Item | Town Buys | Town Sells |
|---|---:|---:|
| Ordinary Rock | **0.10** | **0.11** |
| Sand | **0.10** | **0.11** |
| Limestone | **0.15** | **0.17** |

Limestone remains the strategic exception to the common 0.10 earth/rock tier.

## Mortar — Masonry 1

Core: 1 Sand + 25 calories → 3 Mortar.

At Masonry 1:

- 0.8 Sand × 0.10 = 0.080
- 20 calories = 0.020
- total craft cost = 0.100
- cost ≈ **0.033 per Mortar**

**Mortar: 0.04 Town Buy / 0.05 Town Sell.**

## Mortared Stone — Masonry 1

Core: 1 Mortar + 4 Rock + 15 calories → 1 Mortared Stone.

At Masonry 1:

- 0.8 Mortar × 0.04 = 0.032
- 3.2 Rock × 0.10 = 0.320
- 12 calories = 0.012
- cost ≈ **0.364**

**Mortared Stone: 0.38 Town Buy / 0.40 Town Sell.**

## Crushed Limestone — Mining 1 dependency

Core Arrastra recipe: 12 static Limestone + 50 calories → 3 Crushed Limestone.

At Mining 1:

- 12 Limestone × 0.15 = 1.800
- 40 calories = 0.040
- cost/output ≈ **0.613**

**Crushed Limestone: 0.64 Town Buy / 0.67 Town Sell.**

Unlike Crushed Sandstone/Granite, Crushed Limestone has exact downstream consumers and is not priced as generic waste rock.

## Quicklime — Masonry 1, Blast Furnace

Core: 1 Crushed Limestone + 50 calories → 1 Quicklime.

At Masonry 1, using producer-value inputs and 50 W Blast Furnace fuel:

- 0.8 Crushed Limestone × 0.64 = 0.512
- 40 calories = 0.040
- fuel ≈ 0.028
- cost ≈ **0.580**

**Quicklime: 0.61 Town Buy / 0.64 Town Sell.**

## Other core Masonry goods

| Item | Entry cost | Town Buys | Town Sells |
|---|---:|---:|---:|
| Whetstone | ~0.264 | **0.28** | **0.29** |
| Mill Stone | ~0.496 | **0.52** | **0.55** |
| Stone Brazier | ~1.220 | **1.28** | **1.34** |
| Grindstone | ~8.904 | **9.35** | **9.82** |
| Kiln | ~3.648 | **3.83** | **4.02** |
| Mill | ~9.608 | **10.09** | **10.59** |

### Source checks

- Whetstone: 3 skill-modified Rock + 30 calories.
- Mill Stone: 5 skill-modified Rock + 120 calories.
- Stone Brazier: 15 skill-modified Rock + 25 calories.
- Grindstone: 5 Hewn Logs + 10 Boards + 40 Rock + 180 calories, all skill-modified.
- Kiln: 10 Mortar + 10 Mortared Stone + 360 calories, all skill-modified.
- Mill: 30 Rock + 20 Wood skill-modified, plus 1 static Mill Stone and 360 calories.

## Exchange-ready Masonry table

| Item | Town Buys | Town Sells |
|---|---:|---:|
| Rock | **0.10** | **0.11** |
| Sand | **0.10** | **0.11** |
| Limestone | **0.15** | **0.17** |
| Mortar | **0.04** | **0.05** |
| Mortared Stone | **0.38** | **0.40** |
| Crushed Limestone | **0.64** | **0.67** |
| Quicklime | **0.61** | **0.64** |
| Whetstone | **0.28** | **0.29** |
| Mill Stone | **0.52** | **0.55** |
| Stone Brazier | **1.28** | **1.34** |
| Grindstone | **9.35** | **9.82** |
| Kiln | **3.83** | **4.02** |
| Mill | **10.09** | **10.59** |

Brick is owned by Pottery and Glass by Glassworking; both are priced from this corrected foundation.
