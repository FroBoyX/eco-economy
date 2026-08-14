# Ironwood Mining — Metal Chain

This file contains the currently validated Mining portion of the Ironwood metal economy.

It is derived from Eco 14 Core and the Ironwood raw anchors. Other Mining outputs are intentionally omitted until audited with the same corrected skill-efficiency model.

## Core mechanic that controls the math

Mining's multiplicative resource strategy is:

- level 0: 1.00
- level 1: 0.80
- level 2: 0.75
- level 3: 0.70
- level 4: 0.65
- level 5: 0.60
- level 6: 0.55
- level 7: 0.50

The Arrastra metal-crushing recipes declare the 12 raw ore as `staticIngredient`, so the ore quantity is not reduced by Mining skill.

The Rocker Box concentrate recipes are skill-modified, so at Mining 1 their crushed-ore inputs use the 0.80 multiplier.

## Assumptions

- labor value: 0.001 credit/calorie;
- entry recipes evaluated at Mining 1;
- Tailings disposal charge: 0.35/unit;
- useful rock byproducts receive Town Buy credit;
- industrial producer margin is only a few percent at entry;
- intermediate Exchange spreads are kept narrow.

## Raw anchors

| Ore | Town Buys | Town Sells |
|---|---:|---:|
| Iron Ore | **0.20** | **0.22** |
| Copper Ore | **0.30** | **0.33** |
| Gold Ore | **0.50** | **0.55** |

## Supporting crushed rock

| Product | Entry cost | Town Buys | Town Sells |
|---|---:|---:|---:|
| Crushed Sandstone | ~0.688 | **0.73** | **0.76** |
| Crushed Granite | ~0.699 | **0.74** | **0.77** |

## Ore → crushed ore

Arrastra ore quantity remains static at 12.

| Output | Entry calculation | Cost/output | Town Buys | Town Sells |
|---|---|---:|---:|---:|
| Crushed Iron Ore | 12×0.22 + 40 cal - 0.73 sandstone credit → 2 | ~0.975 | **1.02** | **1.06** |
| Crushed Copper Ore | 12×0.33 + 56 cal - 0.74 granite credit → 2 | ~1.638 | **1.72** | **1.79** |
| Crushed Gold Ore | 12×0.55 + 56 cal - 0.74 granite credit → 2 | ~2.958 | **3.11** | **3.23** |

## Crushed ore → concentrate

At Mining 1, effective crushed-ore quantities are 80% of the printed Rocker Box inputs. Tailings remain at their printed garbage quantities.

| Output | Entry-effective recipe | Entry cost | Town Buys | Town Sells |
|---|---|---:|---:|---:|
| Iron Concentrate | 4.0 Crushed Iron + 40 cal + 1.5 Tailings | ~4.81 | **5.00** | **5.20** |
| Copper Concentrate | 5.6 Crushed Copper + 40 cal + 2.25 Tailings | ~10.85 | **11.30** | **11.75** |
| Gold Concentrate | 8.0 Crushed Gold + 40 cal + 3 Tailings | ~26.93 | **28.00** | **29.00** |

## Gold concentrate is not one-bar-equivalent

At Smelting 4, the Bloomery Gold recipe uses **1.3 effective Gold Concentrate to make 3 Gold Bars**.

Therefore:

`29.00 / (3 / 1.3) ≈ 12.57 credits per bar-equivalent`

The concentrate's nominal item price being higher than the Gold Bar item price is not a value inversion. It is a unit-size issue: one concentrate item contains enough material for more than two bars at the skill level where Gold can first be smelted.

## Validated Mining metal table

| Item | Town Buys | Town Sells |
|---|---:|---:|
| Iron Ore | **0.20** | **0.22** |
| Copper Ore | **0.30** | **0.33** |
| Gold Ore | **0.50** | **0.55** |
| Crushed Iron Ore | **1.02** | **1.06** |
| Crushed Copper Ore | **1.72** | **1.79** |
| Crushed Gold Ore | **3.11** | **3.23** |
| Iron Concentrate | **5.00** | **5.20** |
| Copper Concentrate | **11.30** | **11.75** |
| Gold Concentrate | **28.00** | **29.00** |

Later Mining skills, machinery, modules, talents, and Recycling should improve producer margins without automatically changing these prices.
