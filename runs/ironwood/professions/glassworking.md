# Ironwood Glassworking — Glass Foundation

Derived from Eco 14 Core using current Ironwood anchors and entry-skill efficiency.

## Limestone policy

Limestone is tracked separately from generic Rock because it is a strategic feedstock for Crushed Limestone, Quicklime, Glass, Cement and later industry.

For the current Ironwood era, raw Limestone uses the same base extraction value as ordinary Rock:

**Limestone: 0.15 Town Buy / 0.17 Town Sell.**

This keeps the resource separately visible without inventing a scarcity premium before actual supply justifies one.

## Crushed Limestone — Mining 1, Arrastra

Core recipe:

- 12 Limestone, static
- 50 calories
- output 3 Crushed Limestone

At Mining 1:

- Limestone remains 12 because the ingredient is static
- labor falls to 40 calories
- cost = (12 × 0.17 + 0.040) / 3 ≈ **0.693**

**Crushed Limestone: 0.73 Town Buy / 0.77 Town Sell.**

The Stamp Mill and Jaw Crusher later improve throughput/time, but do not automatically raise the fixed commodity price.

## Basic Glass — Glassworking 1, Glassworks

Core recipe:

- 4 Sand, skill-modified
- 1 Crushed Limestone, static
- 30 calories
- output 1 Glass
- base craft time 1.2 minutes

Glassworks consumes Burnable Fuel at 50 W. Charcoal is valued at 1.23 retail with 20,000 J fuel value.

At Glassworking 1:

- 3.2 Sand × 0.11 = 0.352
- 1 Crushed Limestone × 0.77 = 0.770
- 24 calories = 0.024
- effective craft time 0.96 minutes
- fuel ≈ 0.177
- total entry cost ≈ **1.323**

**Glass: 1.39 Town Buy / 1.46 Town Sell.**

## Quicklime — Masonry 1, Blast Furnace

Core recipe:

- 1 Crushed Limestone, skill-modified
- 50 calories
- output 1 Quicklime
- base craft time 0.2 minutes

Blast Furnace consumes Burnable Fuel at 50 W.

At Masonry 1:

- 0.8 Crushed Limestone × 0.77 = 0.616
- 40 calories = 0.040
- effective craft time 0.16 minutes
- fuel ≈ 0.030
- entry cost ≈ **0.686**

**Quicklime: 0.72 Town Buy / 0.76 Town Sell.**

Quicklime is a later industrial input because this recipe requires access to a Blast Furnace.

## Quicklime Glass — Glassworking 4

Core recipe:

- 3 Sand
- 2 Quicklime
- 45 calories
- output 1 Glass
- base craft time 1 minute

At Glassworking 4 (65%):

- 1.95 Sand × 0.11 = 0.215
- 1.3 Quicklime × 0.76 = 0.988
- 29.25 calories ≈ 0.029
- effective craft time 0.65 minutes
- fuel ≈ 0.120
- total ≈ **1.352**

This is close to the Glassworking-1 route rather than dramatically cheaper. The fixed Glass price therefore remains **1.39 / 1.46**; later personal efficiency becomes producer margin.

## Glassworks — Pottery 1

Core recipe:

- 8 Iron Bars
- 16 Bricks
- 20 WoodBoard
- 150 calories

At Pottery 1:

- 6.4 Iron Bars × 1.65 = 10.56
- 12.8 Bricks × 0.67 = 8.576
- 16 Boards × 0.27 = 4.32
- 120 calories = 0.120
- total entry cost ≈ **23.58**

**Glassworks: 24.75 Town Buy / 26.00 Town Sell.**

## Exchange-ready glass chain

| Item | Town Buys | Town Sells |
|---|---:|---:|
| Limestone | **0.15** | **0.17** |
| Crushed Limestone | **0.73** | **0.77** |
| Quicklime | **0.72** | **0.76** |
| Glass | **1.39** | **1.46** |
| Glassworks | **24.75** | **26.00** |

The near-parity of the two Glass recipes is a useful sanity check on the Limestone and Quicklime values.
