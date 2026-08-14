# Ironwood Mining Prices

Ground-up Mining table derived from Ironwood raw anchors and Eco 14 Core.

## Pricing baseline

The earliest intended Mining infrastructure sets the entry price when it exists:

- **Arrastra** for early crushing;
- **Rocker Box** for early concentrating;
- later Stamp Mill, Jaw Crusher, Screening Machine, Froth Flotation and sensor sorting recipes keep the same output price and create progression margin.

Inputs are costed at their current Exchange **sell** price. Labor is 0.001 credit/calorie. Useful byproducts receive their current Exchange **buy** value as a credit.

## Crushed rock family

| Output | Entry Core recipe | Base cost / output | Exchange buys | Exchange sells |
|---|---|---:|---:|---:|
| Crushed Sandstone | 12 Sandstone + 30 cal → 3 | 0.690 | **0.76** | **0.85** |
| Crushed Shale | 12 Shale + 30 cal → 3 | 0.690 | **0.76** | **0.85** |
| Crushed Granite | 12 Granite + 70 cal → 3 | 0.703 | **0.78** | **0.88** |
| Crushed Limestone | 12 Limestone + 50 cal → 3 | 0.937 | **1.03** | **1.16** |
| Crushed Basalt | Stamp Mill: 20 Basalt + 150 cal → 5 | 0.710 | **0.78** | **0.88** |
| Crushed Gneiss | Stamp Mill: 20 Gneiss + 120 cal → 5 | 0.704 | **0.78** | **0.88** |
| Crushed Mixed Rock | Byproduct/reference value | — | **0.70** | **0.80** |

Crushed Mixed Rock is deliberately slightly cheaper than clean single-rock crushed products. It is commonly a byproduct and later Recycling output rather than a premium dedicated material.

## Ore processing

The entry ore crushers produce a useful rock byproduct. That byproduct is credited at its Exchange buy value rather than treated as free waste.

| Output | Entry Core recipe | Byproduct credit | Base cost / output | Exchange buys | Exchange sells |
|---|---|---:|---:|---:|---:|
| **Crushed Iron Ore** | 12 Iron Ore + 50 cal → 2 | 1 Crushed Sandstone @ 0.76 | 0.845 | **0.93** | **1.04** |
| **Crushed Copper Ore** | 12 Copper Ore + 70 cal → 2 | 1 Crushed Granite @ 0.78 | 1.145 | **1.26** | **1.41** |
| **Crushed Gold Ore** | 12 Gold Ore + 70 cal → 2 | 1 Crushed Granite @ 0.78 | 1.325 | **1.46** | **1.64** |
| **Crushed Coal** | 12 Coal + 50 cal → 2 | 1 Crushed Mixed Rock @ 0.70 | 1.055 | **1.17** | **1.31** |
| **Crushed Sulfur** | 12 Sulfur + 70 cal → 2 | 1 Crushed Mixed Rock @ 0.70 | 1.065 | **1.18** | **1.32** |

## Concentrates

| Output | Entry Core recipe | Conservative cost | Exchange buys | Exchange sells |
|---|---|---:|---:|---:|
| **Iron Concentrate** | 5 Crushed Iron + 50 cal → 1 | 5.25 | **5.80** | **6.50** |
| **Copper Concentrate** | 7 Crushed Copper + 50 cal → 1 | 9.92 | **10.90** | **12.20** |
| **Gold Concentrate** | 10 Crushed Gold + 50 cal → 1 | 16.45 | **18.10** | **20.30** |

Later concentration recipes produce more output from similar inputs. They do not lower the fixed concentrate price; that improved yield is the Mining progression profit.

## Other Mining outputs priced now

| Product | Core basis | Conservative cost | Exchange buys | Exchange sells | Notes |
|---|---|---:|---:|---:|---|
| Garden Gravel | 4 Rock + 50 cal → 2 | 0.365 | **0.40** | **0.45** | Uses generic Rock. |
| Geology Research Paper Basic | 30 Rock + 30 cal → 1 | 5.13 | **5.65** | **6.35** | Production floor; research policy may later override public treatment. |
| Mining Basic Upgrade | 30 Crushed Iron + 10 Crushed Rock + 6000 cal | 45.20 | **49.75** | **55.75** | Uses Crushed Mixed Rock as the cheapest valid CrushedRock reference. |
| Mining Advanced Upgrade | 30 Crushed Copper + 10 Crushed Rock + 6000 cal | 56.30 | **61.95** | **69.40** | Same methodology. |
| Mining Modern Upgrade | 30 Crushed Gold + 10 Crushed Rock + 9000 cal | 66.20 | **72.80** | **81.55** | Same methodology. |

## Recipes that do not set a new price

- later crushed-rock recipes at Stamp Mill/Jaw Crusher;
- later ore crushing recipes;
- later iron/copper/gold concentration recipes;
- Sand Concentrate recipes: natural high-quality Sand is already available at 0.15/0.17; converting valuable Silica-tag crushed rock back into Sand is a contextual fallback and does not raise the Sand commodity price;
- Crushed Mortared Stone: same Crushed Mixed Rock output;
- dry/wet tailings reprocessing later feeds the same Crushed Mixed Rock price through Recycling.

## Dependencies not yet priced

- Crushed Slag — wait for the Smelting/slag value;
- Dynamite and Mining Charge — wait for black powder, paper, plastics, electronics and related chains;
- Smelting/Masonry skill books — wait for the research economy.
