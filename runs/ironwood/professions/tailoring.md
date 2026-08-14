# Ironwood Tailoring — Textile Foundation

Current foundation rebuilt from the supplied Eco 14 Core after canonicalizing Gathering, Farming and Butchery inputs.

This file currently locks the textile intermediates needed by other professions. The full 112-row Tailoring output table (clothing, furniture, rugs, curtains, backpacks, etc.) remains for the final output pass.

## Canonical upstream inputs

- Flax Fiber: **0.29 Town Buy / 0.30 Town Sell**
- Cotton Lint: **0.39 / 0.41**
- Shorn Wool: **0.45 / 0.47**
- labor: **0.001 credit/calorie**

Tailoring 1 uses the 0.80 recipe/labor multiplier.

## Linen Yarn — Tailoring 1

Core Tailoring Table recipe:

- 1 Flax Fiber
- 30 calories
- → 2 Linen Yarn

At Tailoring 1:

- 0.8 Flax Fiber × 0.30 = 0.240
- 24 calories = 0.024
- cost/yarn = 0.132

With a shallow specialist margin:

**Linen Yarn: 0.15 Town Buy / 0.16 Town Sell.**

## Linen Fabric — Tailoring 1, Loom

Core:

- 4 Linen Yarn
- 100 calories
- → 1 Linen Fabric

At Tailoring 1:

- 3.2 Yarn × 0.16 = 0.512
- 80 calories = 0.080
- Exchange-sourced cash cost = 0.592

Linen Fabric is now a multi-step textile output rather than a raw conversion.

**Linen Fabric: 0.68 Town Buy / 0.71 Town Sell.**

The later Automatic Loom route makes 2 Linen Fabric from the same printed 4 Yarn with 80 calories. When Automatic Loom production becomes the normal economy-wide method, Linen Fabric may undergo structural repricing; until then the manual Loom establishes the market floor.

## Cotton Thread — Tailoring 1

Core:

- 1 Cotton Lint
- 30 calories
- → 2 Cotton Thread

At Tailoring 1:

- cash cost/thread ≈ 0.176

**Cotton Thread: 0.20 / 0.21.**

## Cotton Fabric — Tailoring 1, Loom

Core:

- 4 Cotton Thread
- 100 calories
- → 1 Cotton Fabric

At Tailoring 1:

- Exchange-sourced cash cost ≈ 0.752

**Cotton Fabric: 0.86 / 0.90.**

## Wool Yarn — early Tailoring Table route

Current Core contains two wool-yarn routes. The early Tailoring Table recipe (`Spin Wool Yarn`) uses:

- 3 Shorn Wool
- 60 calories
- → 1 Wool Yarn

At Tailoring 1:

- 2.4 Wool × 0.47 = 1.128
- 48 calories = 0.048
- cash cost ≈ 1.176

**Early Wool Yarn: 1.32 / 1.39.**

A later Advanced Tailoring Table recipe uses only 2 printed Shorn Wool. That is a later technology-efficiency transition and should increase producer profit or eventually reprice Wool Yarn if it becomes the economy-wide norm.

## Wool Fabric — early Loom chain

Core:

- 4 Wool Yarn
- 100 calories
- → 1 Wool Fabric

Using the early Wool Yarn route:

**Wool Fabric: 5.21 Town Buy / 5.47 Town Sell.**

This is intentionally much more expensive than Linen/Cotton because the early wool chain consumes a large quantity of hunted animal output. The Automatic Loom later halves fabric output cost per batch and may create a major structural wool-textile repricing.

## Foundation table

| Item | Town Buys | Town Sells |
|---|---:|---:|
| Flax Fiber | **0.29** | **0.30** |
| Linen Yarn | **0.15** | **0.16** |
| Linen Fabric | **0.68** | **0.71** |
| Cotton Lint | **0.39** | **0.41** |
| Cotton Thread | **0.20** | **0.21** |
| Cotton Fabric | **0.86** | **0.90** |
| Shorn Wool | **0.45** | **0.47** |
| Wool Yarn (early) | **1.32** | **1.39** |
| Wool Fabric (early) | **5.21** | **5.47** |

These values now unblock Linen/Fabric dependencies in Carpentry, Basic Engineering, Hunting and Mechanics without relying on legacy Tailoring assumptions.
