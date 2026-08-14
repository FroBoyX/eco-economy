# Ironwood Mining — Current Metal Chain

Rebuilt from the supplied Eco 14 Core using raw anchors plus the approved depth-sensitive commercial margins.

Raw ore remains Depth 0. Ore crushing is a shallow specialty conversion; concentrates are a deeper Mining output because they consume processed ore and create Tailings disposal liability.

## Raw anchors

| Resource | Town Buys | Town Sells |
|---|---:|---:|
| Sandstone | **0.10** | **0.11** |
| Granite | **0.10** | **0.11** |
| Limestone | **0.15** | **0.17** |
| Iron Ore | **0.20** | **0.22** |
| Copper Ore | **0.30** | **0.33** |
| Gold Ore | **0.30** | **0.35** |

## Abundant crushed-rock byproducts

Crushed Sandstone, Crushed Granite and Crushed Mixed Rock remain **0.05 Town Buy / 0.06 Town Sell**. They are abundant ore-processing byproducts and generic `CrushedRock`/`Silica` inputs; hypothetical dedicated crushing cost does not control their value.

## Crushed Limestone — Mining 1

Dedicated Limestone crushing is different because exact downstream recipes consume it.

Core:

- 12 Limestone, static
- 50 calories
- → 3 Crushed Limestone

At Mining 1 using the public 0.17 Limestone input:

- 12 × 0.17 + 40 calories = 2.080
- cash cost/output ≈ 0.693

With a shallow processing margin:

**Crushed Limestone: 0.76 Town Buy / 0.80 Town Sell.**

This supersedes the prior 0.64/0.67 cost-baseline value.

## Ore → crushed ore — Arrastra, Mining 1

Raw ore quantities are static; Mining skill reduces labor but not the 12-ore input. Incidental Crushed Sandstone/Granite is credited at 0.05 Town Buy.

| Output | Exchange-sourced cost/output | Town Buys | Town Sells |
|---|---:|---:|---:|
| Crushed Iron Ore | ~1.315 | **1.45** | **1.52** |
| Crushed Copper Ore | ~1.983 | **2.18** | **2.29** |
| Crushed Gold Ore | ~2.103 | **2.31** | **2.43** |

Gold crushing is now modestly above Copper because the existing Ironwood Gold Ore public Sell is 0.35 rather than 0.33.

## Crushed ore → concentrate — Rocker Box, Mining 1

Tailings remain at printed garbage quantity and cost **0.35 per unit to dispose**.

Entry-effective Core recipes:

- Iron: 4.0 Crushed Iron + 40 calories + 1.5 Tailings;
- Copper: 5.6 Crushed Copper + 40 calories + 2.25 Tailings;
- Gold: 8.0 Crushed Gold + 40 calories + 3 Tailings.

Concentrates receive a Depth-2 margin because a miner can buy crushed ore from another producer and must finance the Tailings liability.

| Output | Exchange-sourced cash cost | Town Buys | Town Sells |
|---|---:|---:|---:|
| Iron Concentrate | ~6.645 | **7.64** | **8.02** |
| Copper Concentrate | ~13.652 | **15.70** | **16.48** |
| Gold Concentrate | ~20.530 | **23.61** | **24.79** |

## Exchange-ready Mining table

| Item | Town Buys | Town Sells |
|---|---:|---:|
| Sandstone | **0.10** | **0.11** |
| Granite | **0.10** | **0.11** |
| Limestone | **0.15** | **0.17** |
| Crushed Sandstone | **0.05** | **0.06** |
| Crushed Granite | **0.05** | **0.06** |
| Crushed Mixed Rock | **0.05** | **0.06** |
| Crushed Limestone | **0.76** | **0.80** |
| Iron Ore | **0.20** | **0.22** |
| Copper Ore | **0.30** | **0.33** |
| Gold Ore | **0.30** | **0.35** |
| Crushed Iron Ore | **1.45** | **1.52** |
| Crushed Copper Ore | **2.18** | **2.29** |
| Crushed Gold Ore | **2.31** | **2.43** |
| Iron Concentrate | **7.64** | **8.02** |
| Copper Concentrate | **15.70** | **16.48** |
| Gold Concentrate | **23.61** | **24.79** |

This is the first industrial chain fully converted from the old 5%-over-cost baseline to the approved commercial model. The raw anchors did not move; the additional value appears as specialization and cash exposure accumulate.
