# Ironwood Mining — Metal Chain

This file contains the currently validated Mining portion of the Ironwood metal economy.

It is derived from Eco 14 Core and the Ironwood raw anchors. Derived producer costs use Town Buy/producer values for upstream materials so the Exchange retail spread is not recursively compounded through the chain.

## Skill rule

Mining's multiplicative resource strategy is:

- level 0: 1.00
- level 1: 0.80
- level 2: 0.75
- level 3: 0.70
- level 4: 0.65
- level 5: 0.60
- level 6: 0.55
- level 7: 0.50

Arrastra metal-crushing recipes use 12 raw ore as a `staticIngredient`, so ore quantity is not reduced by Mining skill.

Rocker Box concentrate recipes are skill-modified, so at Mining 1 their crushed-ore inputs use the 0.80 multiplier.

## Raw anchors

| Resource | Town Buys | Town Sells |
|---|---:|---:|
| Sandstone | **0.10** | **0.11** |
| Granite | **0.10** | **0.11** |
| Limestone | **0.15** | **0.17** |
| Iron Ore | **0.20** | **0.22** |
| Copper Ore | **0.30** | **0.33** |
| Gold Ore | **0.30** | **0.35** |

## Common crushed-rock byproducts

Core facts:

- Crushed Sandstone and Crushed Granite are tagged `CrushedRock` and `Silica`.
- No recipe requires `CrushedSandstoneItem` or `CrushedGraniteItem` specifically.
- Iron Ore crushing automatically outputs Crushed Sandstone.
- Copper and Gold Ore crushing automatically output Crushed Granite.
- Generic `CrushedRock` has several useful sinks, including Stone Roads and concrete.

Because these stones are abundant ore-processing byproducts, dedicated crushing cost does **not** establish their market value.

**Crushed Sandstone / Crushed Granite / Crushed Mixed Rock: 0.05 Town Buy / 0.06 Town Sell.**

This preserves a small reuse value while recognizing that the supply is largely incidental waste material.

Crushed Limestone is different because exact-item recipes consume it. Its current price is **0.64 / 0.67** from the dedicated Limestone chain.

## Ore → crushed ore — Arrastra, Mining 1

Producer cost credits the incidental rock byproduct at its actual 0.05 Town Buy value.

| Output | Entry calculation | Cost/output | Town Buys | Town Sells |
|---|---|---:|---:|---:|
| Crushed Iron Ore | 12×0.20 + 40 cal − 0.05 byproduct → 2 | ~1.195 | **1.25** | **1.31** |
| Crushed Copper Ore | 12×0.30 + 56 cal − 0.05 byproduct → 2 | ~1.803 | **1.89** | **1.98** |
| Crushed Gold Ore | 12×0.30 + 56 cal − 0.05 byproduct → 2 | ~1.803 | **1.89** | **1.98** |

Ironwood intentionally does not give Gold Ore a large raw premium; Gold's later conversion ratio creates the scarcity.

## Crushed ore → concentrate — Rocker Box, Mining 1

Tailings remain at their printed garbage quantities and currently carry a **0.35/unit disposal cost**.

| Output | Entry-effective recipe | Entry cost | Town Buys | Town Sells |
|---|---|---:|---:|---:|
| Iron Concentrate | 4.0 Crushed Iron + 40 cal + 1.5 Tailings | ~5.565 | **5.84** | **6.13** |
| Copper Concentrate | 5.6 Crushed Copper + 40 cal + 2.25 Tailings | ~11.412 | **11.98** | **12.58** |
| Gold Concentrate | 8.0 Crushed Gold + 40 cal + 3 Tailings | ~16.210 | **17.02** | **17.87** |

## Gold concentrate unit warning

At Smelting 4, the Bloomery recipe uses **1.3 effective Gold Concentrate to make 3 Gold Bars**.

One concentrate therefore represents about **2.31 finished bars** at first Gold-smelting unlock. A concentrate item can numerically cost more than one Gold Bar without creating a value inversion.

## Exchange-ready Mining metal table

| Item | Town Buys | Town Sells |
|---|---:|---:|
| Sandstone | **0.10** | **0.11** |
| Granite | **0.10** | **0.11** |
| Limestone | **0.15** | **0.17** |
| Crushed Sandstone | **0.05** | **0.06** |
| Crushed Granite | **0.05** | **0.06** |
| Crushed Limestone | **0.64** | **0.67** |
| Iron Ore | **0.20** | **0.22** |
| Copper Ore | **0.30** | **0.33** |
| Gold Ore | **0.30** | **0.35** |
| Crushed Iron Ore | **1.25** | **1.31** |
| Crushed Copper Ore | **1.89** | **1.98** |
| Crushed Gold Ore | **1.89** | **1.98** |
| Iron Concentrate | **5.84** | **6.13** |
| Copper Concentrate | **11.98** | **12.58** |
| Gold Concentrate | **17.02** | **17.87** |

Later machinery, skill, modules and Recycling improve producer margins without automatically raising these prices.
