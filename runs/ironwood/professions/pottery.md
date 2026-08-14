# Ironwood Pottery — Brick Foundation

Derived from Eco 14 Core using current Ironwood anchors and entry-skill efficiency.

Derived producer costs use Town Buy/producer values for inputs. The Exchange retail spread is applied after the producer price is established.

## Current inputs

- Sand: **0.10 Town Buy / 0.11 Town Sell**
- Clay: **0.10 / 0.11**
- Board: **0.26 / 0.27**
- Nail: **0.09 / 0.10**
- Mortar: **0.04 / 0.05**
- Charcoal: **1.17 / 1.23**, 20,000 J fuel value
- labor: **0.001 credit/calorie**
- Kiln fuel consumption: **50 W**

Pottery 1 uses 80% of skill-modified ingredients, labor and craft time.

## Wooden Mold — Logging 3

Core recipe:

- 2 Nails
- 8 WoodBoard
- 120 calories
- output 4 Wooden Molds

At Logging 3 (70%):

- 1.4 Nails × 0.09 = 0.126
- 5.6 Boards × 0.26 = 1.456
- 84 calories = 0.084
- total = **1.666**
- cost/mold ≈ **0.417**

**Wooden Mold: 0.44 Town Buy / 0.46 Town Sell.**

Wooden Molds are consumed fractionally by the Wet Brick recipe; they are not a free permanent tool.

## Wet Brick — Pottery 1

Core recipe:

- 3 Sand
- 12 Clay
- 1 Wooden Mold
- 100 calories
- 0.1 Wood Scrap garbage
- output 4 Wet Bricks

At Pottery 1:

- 2.4 Sand × 0.10 = 0.240
- 9.6 Clay × 0.10 = 0.960
- 0.8 Wooden Mold × 0.44 = 0.352
- 80 calories = 0.080
- Wood Scrap disposal allowance ≈ 0.008/craft
- total craft cost ≈ **1.640**
- cost/Wet Brick ≈ **0.410**

**Wet Brick: 0.43 Town Buy / 0.45 Town Sell.**

Wet Brick remains a process/intermediate value. The finished Brick receives an Ironwood bulk-construction valuation premium; do not infer finished Brick price only from the Wet Brick public price.

## Brick — Pottery 1, Kiln

Core recipe:

- 1 Wet Brick
- 4 Mortar
- 15 calories
- output 1 Brick
- base craft time 0.32 minutes

At Pottery 1, the mechanically modeled entry floor is:

- 0.8 Wet Brick × 0.43 = 0.344
- 3.2 Mortar × 0.04 = 0.128
- 12 calories = 0.012
- effective craft time = 0.256 minutes
- 50 W Kiln fuel ≈ 0.045
- modeled entry floor ≈ **0.529**

The modeled floor understates the practical burden of Brick supply. Brick is a bulk Tier-3 construction block assembled from large quantities of hand-shoveled Sand and Clay, then moved through molds, intermediate Wet Bricks, Mortar, Kiln throughput, storage, and repeated hauling. Those burdens are only weakly represented by recipe calories.

Ironwood therefore applies a deliberate **bulk construction valuation premium** rather than pricing Brick as an ordinary low-friction intermediate.

**Brick: 1.20 Town Buy / 1.25 Town Sell.**

This is a policy value, not a claim that the recipe consumes 1.20 credits of modeled ingredients. It rewards the real logistics burden while keeping Brick below Glass and Lumber in the Tier-3 structural band.

A materially higher value such as 1.50–2.00 should be used only if actual supply remains weak, because at the current recipe floor it would create an extremely large guaranteed Exchange margin for producers.

## Construction comparison

| Material | Tier | Town Buys | Town Sells |
|---|---:|---:|---:|
| Mortared Stone | 2 | **0.38** | **0.40** |
| Brick | 3 | **1.20** | **1.25** |
| Glass | 3 | **1.45** | **1.52** |
| Lumber | 3 | **1.60** | **1.68** |

This creates a clear Tier-3 structural band rather than letting Brick appear to be only marginally more valuable than Tier-2 Mortared Stone.

## Exchange-ready Pottery foundation

| Item | Town Buys | Town Sells |
|---|---:|---:|
| Wooden Mold | **0.44** | **0.46** |
| Wet Brick | **0.43** | **0.45** |
| **Brick** | **1.20** | **1.25** |

Ceramics, pottery furniture and advanced Pottery remain to be audited from this corrected foundation.
