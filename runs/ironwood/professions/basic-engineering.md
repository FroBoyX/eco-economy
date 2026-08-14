# Ironwood Basic Engineering — Early Infrastructure

Rebuilt from Eco 14 Core using the current Ironwood Logging, Masonry, Mining and metal-chain prices.

Derived producer costs use Town Buy/producer values. The Exchange retail spread is applied afterward rather than compounded through every dependency.

## Reusable Mining byproduct

Crushed Mixed Rock, Crushed Sandstone and Crushed Granite are abundant `CrushedRock` byproduct streams.

**Common CrushedRock reuse value: 0.05 Town Buy / 0.06 Town Sell.**

Crushed Limestone remains separate because exact-item recipes consume it.

## Wooden Gear / Wooden Wheel — Basic Engineering 1

Core: 4 Hewn Logs + 40 calories → 1.

At Basic Engineering 1:

- 3.2 Hewn Logs × 0.87 = 2.784
- 32 calories = 0.032
- entry cost ≈ **2.816**

**Wooden Gear: 2.96 Town Buy / 3.11 Town Sell.**

**Wooden Wheel: 2.96 Town Buy / 3.11 Town Sell.**

## Arrastra — Basic Engineering 1

Entry-effective inputs:

- 4 Wood × 0.40 = 1.600
- 24 Rock × 0.10 = 2.400
- 8 Boards × 0.26 = 2.080
- 1 static Mill Stone × 0.52 = 0.520
- 240 calories = 0.240
- entry cost ≈ **6.840**

**Arrastra: 7.18 Town Buy / 7.54 Town Sell.**

## Rocker Box — Basic Engineering 1

Entry-effective inputs:

- 8 Boards × 0.26 = 2.080
- 4.8 Wood × 0.40 = 1.920
- 80 calories = 0.080
- entry cost = **4.080**

**Rocker Box: 4.28 Town Buy / 4.49 Town Sell.**

## Stone Road — Basic Engineering 1

Core:

- 3 Mortar
- 2 `CrushedRock`
- 60 calories

At Basic Engineering 1:

- 2.4 Mortar × 0.04 = 0.096
- 1.6 CrushedRock × 0.05 = 0.080
- 48 calories = 0.048
- entry cost ≈ **0.224**

**Stone Road: 0.24 Town Buy / 0.25 Town Sell.**

This is intentionally cheap because the road recipe is a public-use sink for abundant crushed-rock byproduct.

## Stone Road Tool — Basic Engineering 1

Entry-effective inputs:

- 6.4 Wood × 0.40 = 2.560
- 16 Rock × 0.10 = 1.600
- 80 calories = 0.080
- entry cost = **4.240**

**Stone Road Tool: 4.45 Town Buy / 4.67 Town Sell.**

## Exchange-ready Basic Engineering table

| Item | Town Buys | Town Sells |
|---|---:|---:|
| Common CrushedRock | **0.05** | **0.06** |
| Wooden Gear | **2.96** | **3.11** |
| Wooden Wheel | **2.96** | **3.11** |
| Arrastra | **7.18** | **7.54** |
| Rocker Box | **4.28** | **4.49** |
| Stone Road | **0.24** | **0.25** |
| Stone Road Tool | **4.45** | **4.67** |

Later Engineering products will be added as their dependencies become canonical.
