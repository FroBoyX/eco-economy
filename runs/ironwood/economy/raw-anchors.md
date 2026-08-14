# Ironwood Raw Commodity Anchors

These are the currently validated raw anchors for the Ironwood Eco 14 run.

Raw anchors are design inputs. Processed goods must be checked through their complete Core production chain before the anchor is accepted.

## Public Exchange convention

- **Town Buys** = what Ironwood pays a player supplying the resource.
- **Town Sells** = what Ironwood charges a player consuming the resource.
- derived producer costs use the underlying producer/Town Buy value of intermediate inputs rather than recursively stacking the Exchange retail spread;
- prices are evaluated at the recipe's minimum required skill level;
- `staticIngredient` recipe inputs are not reduced by skill efficiency;
- Exchange spreads are applied after the producer value is established.

## Current raw hierarchy

| Resource | Town Buys | Town Sells | Reason |
|---|---:|---:|---|
| Wood | **0.40** | **0.45** | Foundational timber anchor. |
| **Sand** | **0.10** | **0.11** | Abundant shovel-gathered earth material. |
| **Clay** | **0.10** | **0.11** | Abundant earth material with growing Pottery/Brick/Cement demand. |
| **Ordinary Rock** | **0.10** | **0.11** | Common mined stone; peer of Sand and Clay in the current economy. |
| **Sandstone** | **0.10** | **0.11** | Common rock; also produces Silica-tagged crushed byproduct. |
| **Granite** | **0.10** | **0.11** | Common rock; also produces Silica-tagged crushed byproduct. |
| **Limestone** | **0.15** | **0.17** | Strategic rock feeding Quicklime, Glass, Cement and later industry. |
| **Iron Ore** | **0.20** | **0.22** | Foundational industrial ore. |
| **Copper Ore** | **0.30** | **0.33** | Moderate scarcity premium. |
| **Gold Ore** | **0.30** | **0.35** | Poor Core ore-to-bar conversion already supplies most Gold scarcity. |

## Common earth tier

Sand, Clay, ordinary Rock, Sandstone and Granite are all abundant enough that Ironwood values them at the same **0.10 buy / 0.11 sell** tier.

This avoids arbitrary premiums simply because one material is mined rather than shoveled. Their downstream products separate naturally through recipe quantities, specialization, labor and workstation requirements.

## Limestone premium

Limestone stays above the common rock tier at **0.15 / 0.17**.

The premium is deliberate because Limestone has strategically distinct demand:

- exact-input Crushed Limestone;
- Quicklime;
- Glass;
- Cement;
- fertilizer and later industrial pathways.

A 0.12 anchor would barely distinguish it after downstream rounding. A 0.15 anchor creates a meaningful but still modest premium without treating Limestone like an ore.

## Crushed-rock byproduct rule

Core confirms Crushed Sandstone and Crushed Granite are tagged `CrushedRock` and `Silica`, but no recipe requires either exact stone by name. They are also produced automatically while crushing Iron, Copper and Gold Ore.

They therefore should **not** be valued from the expensive dedicated crushing recipe when abundant ore-processing byproduct supply exists. Ironwood treats these common crushed stones as low-value reusable byproducts, alongside Crushed Mixed Rock.

Crushed Limestone is different: several recipes explicitly require `CrushedLimestoneItem`, so its dedicated production chain remains economically relevant.

## Clay Mold check

Gathering 1: 1 Clay + 50 calories → 4 Clay Molds.

At Gathering 1 and producer-value pricing:

- 0.8 Clay × 0.10 = 0.080
- 40 calories = 0.040
- total = 0.120
- cost/mold = **0.030**

Practical Exchange price remains **0.04 buy / 0.05 sell**.

## Mortar check

Masonry 1: 1 Sand + 25 calories → 3 Mortar.

At Masonry 1:

- 0.8 Sand × 0.10 = 0.080
- 20 calories = 0.020
- total = 0.100
- cost/Mortar ≈ **0.033**

Practical Exchange price remains **0.04 buy / 0.05 sell**.

## Gold conversion warning

At first legitimate production, the complete Core chain effectively consumes approximately:

- **6.4 Iron Ore per Iron Bar**
- **8.96 Copper Ore per Copper Bar**
- **20.8 Gold Ore per Gold Bar**

Gold already carries a very large recipe scarcity penalty, so Ironwood does not also assign a large raw Gold Ore premium.
