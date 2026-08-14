# Ironwood Logging Prices

Ground-up Logging table derived from the current Ironwood raw anchors and Eco 14 Core recipes.

## Method

- Raw `Wood` consumer cost: **0.45**.
- Labor: **0.001 credit per calorie**.
- Conservative production cost assumes required inputs are purchased at their current Exchange **sell** price.
- Exchange **buy** is the producer floor and is chosen near 8–15% above that conservative base cost when practical.
- Exchange **sell** is the consumer price and carries a shallow additional spread.
- The printed Core recipe quantities are used as the conservative baseline. Any actual skill/resource-efficiency reduction increases producer margin without increasing the fixed sale price.
- Primitive/unskilled fallback recipes do not set professional prices.
- When later infrastructure provides a more efficient recipe for the same output, the output price remains fixed and the efficiency gain becomes professional profit.

## Core processed commodities

| Output | Earliest pricing recipe | Base inputs at consumer price | Labor | Base cost / output | Exchange buys | Exchange sells | Base markup vs cost |
|---|---|---:|---:|---:|---:|---:|---:|
| **Dowel** | Logging 1, Carpentry Table: 2 Wood → 16 | 0.90 | 0.04 | 0.0588 | **0.07** | **0.08** | 19.1%* |
| **Board** | Logging 1, Carpentry Table: 1 Wood → 1 | 0.45 | 0.025 | 0.475 | **0.53** | **0.60** | 11.6% |
| **Hewn Log** | Logging 1, Carpentry Table: 2 Dowels + 2 Wood → 1 | 1.06 | 0.02 | 1.08 | **1.20** | **1.35** | 11.1% |
| **Charcoal** | Logging 3, Kiln: 7 Wood → 2 | 3.15 | 0.025 | 1.5875 | **1.75** | **1.95** | 10.2% |

\* Dowel is above the target percentage only because a clean two-decimal value is more useful than micro-pricing a sixteenth of a recipe output. Absolute profit remains tiny.

### Progression checks

**Boards at the Sawmill:** Core later allows 2 Wood + 20 calories → 3 Boards. At the same fixed 0.53 producer price, the raw recipe cost falls to about 0.307 per Board before any further skill efficiency. The later Blacksmith-built Sawmill therefore creates a large but earned infrastructure/progression margin instead of causing us to lower the Board price.

**Peat Charcoal:** Logging 4 allows 1 Peat + 50 calories → 4 Charcoal. The Peat anchor is therefore set to 5.55 buy / 6.25 sell. At a 6.25 consumer Peat cost, Charcoal costs about 1.575 each and still earns only ~11% at the fixed 1.75 producer price. Cheap Peat would otherwise create extreme arbitrage.

**Dense Charcoal:** Logging 5 uses Hewn Logs for the same Charcoal output. It does not receive a separate Charcoal price. Its viability must come from the level-5 player's actual resource efficiency or contextual advantages; one common output cannot carry several incompatible prices.

## Logging products priced now

These rows have all material dependencies priced in the current ledger.

| Product | Core requirement | Conservative cost | Exchange buys | Exchange sells | Notes |
|---|---:|---:|---:|---:|---|
| Dowel | Logging 1 | 0.0588 ea | **0.07** | **0.08** | 16 per craft. |
| Board | Logging 1 | 0.475 | **0.53** | **0.60** | Early Carpentry Table route sets price; Sawmill increases later margin. |
| Hewn Log | Logging 1 | 1.08 | **1.20** | **1.35** | Uses 2 Dowels + 2 Wood + 20 cal. |
| Charcoal | Logging 3 | 1.5875 | **1.75** | **1.95** | Common price across wood/peat/dense recipes. |
| Dendrology Research Paper Basic | Logging 1 | 9.03 | **9.95** | **11.15** | Calculated production floor; research policy may later replace the public-market treatment. |
| Wooden Keel | Logging 2 | 3.66 | **4.05** | **4.55** | 8 Wood + 60 cal. |
| Wooden Oar | Logging 2 | 5.46 | **6.05** | **6.80** | 4 Hewn Logs + 60 cal. |
| Logging Basic Upgrade | Logging 2 | 12.80 | **14.10** | **15.80** | 10 Dowels + 20 Wood + 3000 cal. |
| Small Wood Cart | Logging 1 | 22.55 | **24.80** | **27.80** | 10 Hewn Logs + 15 Boards + 50 cal. |
| Butchery Table | Logging 1 | 25.80 | **28.40** | **31.80** | 10 Hewn Logs + 20 Boards + 300 cal. |
| Fiber Scutching Station | Logging 2 | 25.80 | **28.40** | **31.80** | 10 Hewn Logs + 20 Boards + 300 cal. |
| Fletching Table | Logging 2 | 25.68 | **28.25** | **31.65** | 10 Hewn Logs + 20 Boards + 180 cal. |
| Hewn Bench | Logging 2 | 27.96 | **30.75** | **34.45** | 18 Hewn Logs + 6 Boards + 60 cal. |
| Hewn Chair | Logging 1 | 24.90 | **27.40** | **30.70** | 12 Plant Fibers + 12 Hewn Logs + 12 Boards + 60 cal. |
| Hewn Door | Logging 1 | 2.76 | **3.05** | **3.42** | 2 Hewn Logs + 60 cal. |
| Hewn Dresser | Logging 3 | 27.96 | **30.75** | **34.45** | Same core material burden as Hewn Bench. |
| Hewn Nightstand | Logging 4 | 23.76 | **26.15** | **29.30** | 14 Hewn Logs + 8 Boards + 60 cal. |
| Hewn Table | Logging 2 | 23.91 | **26.30** | **29.50** | 15 Hewn Logs + 6 Boards + 60 cal. |
| Small Shipyard | Logging 1 | 18.66 | **20.55** | **23.00** | 10 Hewn Logs + 8 Boards + 360 cal. |
| Tiki Torch | Logging 1 | 2.61 | **2.90** | **3.25** | 5 Wood + 360 cal. |
| Wainwright Table | Logging 1 | 26.43 | **29.10** | **32.60** | 15 Hewn Logs + 10 Boards + 180 cal. |

## Logging rows intentionally not priced yet

These are current Core products, but their external dependencies are not yet rebuilt. They should receive a price only when those dependencies become canonical:

- Wooden Mold — needs Nails;
- Blacksmith Table — needs Iron Bars;
- Farmers Table — needs a deliberate Dirt valuation/policy;
- Huge Banner Sign / Huge Wooden Banner Sign — need Cotton Fabric and Linen Yarn;
- Paint Mixer — needs Iron Bars;
- Pottery Table — needs Wooden Wheel;
- Registrar — needs the rebuilt ore/metal chain policy;
- Carpentry / Basic Engineering / Shipwright skill books — depend on the research economy;
- Particle Boards — depend on Wood Pulp/Paper Milling but retain the common Board output price once available.

Do not fill these from old tables. Price them when their actual dependencies are rebuilt.
