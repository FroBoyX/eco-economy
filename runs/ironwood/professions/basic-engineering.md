# Ironwood Basic Engineering — Early Infrastructure

Rebuilt from Eco 14 Core using current Ironwood Logging, Masonry, Mining and metal-chain prices.

A critical pricing rule here is that **Crushed Mixed Rock is an abundant Mining byproduct/waste stream**, not a premium dedicated-crushing product. Recipes accepting the generic `CrushedRock` tag should use the cheapest practical valid input when that byproduct is available.

## Reusable Mining byproduct

### Crushed Mixed Rock

Eco 14 Core describes Crushed Mixed Rock as a mixture usable in recipes or simply as landfill. It is produced as a byproduct while crushing Coal and Sulfur and later appears as a Recycling output from reprocessed Tailings.

It therefore receives a low reuse value rather than a dedicated production-cost price:

**Crushed Mixed Rock: 0.05 Town Buy / 0.06 Town Sell.**

This creates an economic sink for a bulky byproduct without pretending it has the same value as clean crushed stone.

## Utility components

### Wooden Gear / Wooden Wheel — Basic Engineering 1

Core: 4 Hewn Logs + 40 calories → 1.

At Basic Engineering 1 (0.80 multiplier):

- 3.2 Hewn Logs;
- 32 calories;
- entry cost ≈ **2.94**.

**Wooden Gear: 3.10 Town Buy / 3.26 Town Sell.**

**Wooden Wheel: 3.10 Town Buy / 3.26 Town Sell.**

## Mining infrastructure

### Arrastra — Basic Engineering 1

Entry-effective inputs:

- 4 Wood;
- 24 Rock;
- 8 Boards;
- 1 Mill Stone, static;
- 240 calories.

Entry cost ≈ **9.15**.

**Arrastra: 9.60 Town Buy / 10.08 Town Sell.**

### Rocker Box — Basic Engineering 1

Entry-effective inputs:

- 8 Boards;
- 4.8 Wood;
- 80 calories.

Entry cost ≈ **4.40**.

**Rocker Box: 4.62 Town Buy / 4.85 Town Sell.**

## Stone Road — Basic Engineering 1

Core:

- 3 Mortar;
- 2 `CrushedRock`;
- 60 calories;
- 1 Stone Road.

At Basic Engineering 1:

- 2.4 Mortar;
- 1.6 CrushedRock;
- 48 calories.

Because Crushed Mixed Rock satisfies `CrushedRock` and is the practical low-value byproduct stream, use its **0.06 retail value**, not the dedicated production cost of clean Crushed Sandstone/Granite.

Using Mortar retail 0.07:

`2.4 × 0.07 + 1.6 × 0.06 + 0.048 ≈ 0.312`

**Stone Road: 0.33 Town Buy / 0.35 Town Sell.**

This essentially validates the old Ironwood 0.35 retail Stone Road price from first principles. The earlier 1.59 rebuild was wrong because it priced a waste/byproduct tag input as premium clean crushed rock.

## Stone Road Tool — Basic Engineering 1

Entry-effective inputs:

- 6.4 Wood;
- 16 Rock;
- 80 calories.

Entry cost ≈ **5.68**.

**Stone Road Tool: 5.97 Town Buy / 6.27 Town Sell.**

## Current Exchange-ready Basic Engineering table

| Item | Town Buys | Town Sells |
|---|---:|---:|
| Crushed Mixed Rock | **0.05** | **0.06** |
| Wooden Gear | **3.10** | **3.26** |
| Wooden Wheel | **3.10** | **3.26** |
| Arrastra | **9.60** | **10.08** |
| Rocker Box | **4.62** | **4.85** |
| Stone Road | **0.33** | **0.35** |
| Stone Road Tool | **5.97** | **6.27** |

Later Engineering products will be added as their dependencies become canonical.
