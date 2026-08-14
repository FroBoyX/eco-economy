# Ironwood Mining — Metal Chain

This file contains the currently validated Mining portion of the Ironwood metal economy.

It is derived from Eco 14 Core and the Ironwood raw anchors. Other Mining outputs are intentionally omitted until audited with the corrected skill-efficiency model.

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

However, Eco recipes may deliberately declare an ingredient as `staticIngredient`.

The Arrastra metal-crushing recipes use:

`new IngredientElement(<Ore>, 12, true)`

So the **12 raw ore is static and does not receive Mining's resource reduction**.

The Rocker Box concentrate recipes use `typeof(MiningSkill)`, so their crushed-ore input **does** receive the Mining multiplier. At Mining 1, that input is 80% of the printed amount.

This distinction is mandatory for pricing.

## Assumptions

- labor value: 0.001 credit/calorie;
- entry recipes evaluated at Mining 1;
- Tailings disposal charge: 0.35/unit;
- useful rock byproducts receive Town Buy credit;
- target producer margin on industrial intermediates: roughly 5–6%;
- intermediate Exchange spread: roughly 4%, rounded to practical values.

## Supporting crushed rock

| Product | Core entry recipe | Entry cost | Town Buys | Town Sells |
|---|---|---:|---:|---:|
| Crushed Sandstone | 12 Sandstone static + 24 effective cal → 3 | ~0.688 | **0.73** | **0.76** |
| Crushed Granite | 12 Granite static + 56 effective cal → 3 | ~0.699 | **0.74** | **0.77** |

These values supply the byproduct credit for ore crushing.

## Ore → crushed ore

### Iron

Core at Arrastra, Mining 1:

- 12 Iron Ore — **static**;
- 40 effective calories;
- outputs 2 Crushed Iron Ore;
- outputs 1 Crushed Sandstone byproduct.

Using Iron Ore retail 0.22 and Crushed Sandstone Town Buy 0.73:

`(12 × 0.22 + 0.04 - 0.73) / 2 ≈ 0.975 per Crushed Iron Ore`

**Price: 1.03 Town Buy / 1.08 Town Sell.**

### Copper

Core at Arrastra, Mining 1:

- 12 Copper Ore — **static**;
- 56 effective calories;
- outputs 2 Crushed Copper Ore;
- outputs 1 Crushed Granite byproduct.

Using Copper Ore retail 0.35 and Crushed Granite Town Buy 0.74:

`(12 × 0.35 + 0.056 - 0.74) / 2 ≈ 1.758`

**Price: 1.86 Town Buy / 1.94 Town Sell.**

### Gold

Core at Arrastra, Mining 1:

- 12 Gold Ore — **static**;
- 56 effective calories;
- outputs 2 Crushed Gold Ore;
- outputs 1 Crushed Granite byproduct.

Using Gold Ore retail 0.60 and Crushed Granite Town Buy 0.74:

`(12 × 0.60 + 0.056 - 0.74) / 2 ≈ 3.258`

**Price: 3.45 Town Buy / 3.60 Town Sell.**

## Crushed ore → concentrate

These Rocker Box inputs are skill-modified. At Mining 1 the printed input is multiplied by 0.80.

Tailings are a real disposal cost and remain at their printed garbage quantity.

### Iron Concentrate

Core printed recipe:

- 5 Crushed Iron Ore;
- 50 calories;
- 1 Iron Concentrate;
- 1.5 Tailings.

Mining 1 effective input:

- **4.0 Crushed Iron Ore**;
- **40 calories**;
- **1.5 Tailings**.

Cost:

`4 × 1.08 + 0.04 + (1.5 × 0.35) = 4.885`

**Price: 5.15 Town Buy / 5.35 Town Sell.**

### Copper Concentrate

Core printed recipe:

- 7 Crushed Copper Ore;
- 50 calories;
- 1 Copper Concentrate;
- 2.25 Tailings.

Mining 1 effective input:

- **5.6 Crushed Copper Ore**;
- **40 calories**;
- **2.25 Tailings**.

Cost:

`5.6 × 1.94 + 0.04 + (2.25 × 0.35) ≈ 11.692`

**Price: 12.40 Town Buy / 12.90 Town Sell.**

### Gold Concentrate

Core printed recipe:

- 10 Crushed Gold Ore;
- 50 calories;
- 1 Gold Concentrate;
- 3 Tailings.

Mining 1 effective input:

- **8.0 Crushed Gold Ore**;
- **40 calories**;
- **3 Tailings**.

Cost:

`8 × 3.60 + 0.04 + (3 × 0.35) = 29.89`

**Price: 31.60 Town Buy / 32.90 Town Sell.**

## Validated Mining metal table

| Item | Town Buys | Town Sells |
|---|---:|---:|
| Iron Ore | **0.20** | **0.22** |
| Copper Ore | **0.30** | **0.35** |
| Gold Ore | **0.50** | **0.60** |
| Crushed Iron Ore | **1.03** | **1.08** |
| Crushed Copper Ore | **1.86** | **1.94** |
| Crushed Gold Ore | **3.45** | **3.60** |
| Iron Concentrate | **5.15** | **5.35** |
| Copper Concentrate | **12.40** | **12.90** |
| Gold Concentrate | **31.60** | **32.90** |

## Progression behavior

Later Mining recipes, better machines, higher skill levels, modules, and talents should not automatically reduce these fixed prices.

They reduce the miner's cost and therefore increase profit. That is intentional.

If Tailings later become positive-value Recycling feedstock, the concentrate stage should become more profitable or be deliberately repriced as part of that technology transition.
