# Ironwood Carpentry — Lumber Foundation

Derived from Eco 14 Core using current Ironwood producer values and entry-skill efficiency.

## Current inputs

- Board: **0.26 Town Buy / 0.27 Town Sell**
- Nail: **0.09 / 0.10**
- Flax Seed: **0.10 / 0.11** working current-era procurement anchor
- labor: **0.001 credit/calorie**

Derived production costs use upstream producer/Town Buy values rather than recursively stacking Exchange resale spreads.

## Flaxseed Oil — Milling 3

Core Mill recipe:

- 16 Flax Seeds
- 25 calories
- output 1 Flaxseed Oil

Milling 3 uses the 0.70 resource/labor multiplier:

- 11.2 Flax Seeds × 0.10 producer value = 1.120
- 17.5 calories = 0.0175
- entry production cost ≈ **1.138**

With a shallow producer margin:

**Flaxseed Oil: 1.20 Town Buy / 1.26 Town Sell.**

This is a working price pending the full Farming/Tailoring audit. Lumber is not highly sensitive to moderate changes in Oil because each finished Lumber consumes only 0.2 Oil at Carpentry 1.

## Lumber — Carpentry 1, Sawmill

Core recipe:

- 10 WoodBoard-tag inputs
- 2 Nails
- 0.5 Flaxseed Oil
- 60 calories
- output 2 Lumber

At Carpentry 1 (0.80 multiplier):

- 8 Boards
- 1.6 Nails
- 0.4 Flaxseed Oil
- 48 calories
- output 2 Lumber

Using upstream producer values:

- Boards: 8 × 0.26 = 2.080
- Nails: 1.6 × 0.09 = 0.144
- Flaxseed Oil: 0.4 × 1.20 = 0.480
- labor: 0.048
- total craft cost = **2.752**
- cost per Lumber = **1.376**

With a shallow producer margin and normal Ironwood Exchange spread:

**Lumber: 1.45 Town Buy / 1.52 Town Sell.**

The previous working value around 3 credits is superseded. It cannot be supported by the current Eco 14 recipe unless Flaxseed Oil is priced at an implausibly high level.

## Building-material comparison

| Material | Block Tier | Town Buys | Town Sells |
|---|---:|---:|---:|
| Mortared Stone | 2 | **0.38** | **0.40** |
| Brick | 3 | **0.56** | **0.59** |
| Glass | 3 | **1.21** | **1.27** |
| Lumber | 3 | **1.45** | **1.52** |

This is a much more coherent perceived progression. Lumber remains the most expensive of the current Tier-3 building materials because it combines processed Boards, metal fasteners, and milled oil, but it is only about 20% above Glass rather than more than twice Glass.

Do not raise Brick or Glass merely to preserve the old 3-credit Lumber price.
