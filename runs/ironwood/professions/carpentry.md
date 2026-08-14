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

This is a working price pending the full Farming/Tailoring audit.

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
- modeled cost per Lumber = **1.376**

Lumber is a Tier-3 bulk construction material. The modeled recipe floor already captures much more of its real burden than Brick because Boards, metal fasteners and milled oil are priced inputs, but Ironwood still gives it a modest construction/logistics premium.

**Lumber: 1.60 Town Buy / 1.68 Town Sell.**

The prior 3-credit working price remains superseded. The 1.60/1.68 value keeps Lumber at the top of the current Tier-3 structural band without making it perceptually detached from Brick and Glass.

## Tier-3 structural comparison

| Material | Modeled floor | Town Buys | Town Sells |
|---|---:|---:|---:|
| Brick | ~0.53 | **1.20** | **1.25** |
| Glass | ~1.15 | **1.45** | **1.52** |
| Lumber | ~1.38 | **1.60** | **1.68** |

Mortared Stone remains a cheaper Tier-2 baseline at approximately **0.38 / 0.40**.

The Tier-3 prices are deliberately not identical. Brick receives the largest uplift because its shovel/haul burden is poorly represented by recipe calories; Glass and Lumber already internalize more of their real effort through expensive processed inputs.
