# Ironwood Basic Engineering — Current Early Infrastructure

Rebuilt from the supplied Eco 14 Core using current Ironwood Logging, Masonry, Mining, Carpentry and metal-chain prices.

Derived producer costs use Town Buy/producer values. The Exchange retail spread is applied afterward rather than compounded through every dependency.

## Reusable Mining byproduct

Crushed Mixed Rock, Crushed Sandstone and Crushed Granite are abundant `CrushedRock` byproduct streams.

**Common CrushedRock reuse value: 0.05 Town Buy / 0.06 Town Sell.**

Crushed Limestone remains separate because exact-item recipes consume it.

## Exchange-ready Basic Engineering table

| Item | Basic Engineering | Entry cost | Town Buys | Town Sells | Notes |
|---|---:|---:|---:|---:|---|
| Wooden Gear | 1 | 2.816 | **2.96** | **3.11** | 4 Hewn Logs, skill-modified. |
| Wooden Wheel | 1 | 2.816 | **2.96** | **3.11** | Same material burden as Wooden Gear. |
| Arrastra | 1 | 6.840 | **7.18** | **7.54** | Includes static Mill Stone. |
| Rocker Box | 1 | 4.080 | **4.28** | **4.49** | Boards + Wood. |
| Stone Road | 1 | 0.224 | **0.24** | **0.25** | Cheap public-use sink for CrushedRock byproduct. |
| Stone Road Tool | 1 | 4.240 | **4.45** | **4.67** | Wood + common Rock. |
| **Basic Engineering Upgrade** | 2 | **20.010** | **21.01** | **22.06** | Six Wooden Gears are static; 2,250 effective labor calories. |
| Stop Sign | 2 | 10.245 | **10.76** | **11.30** | 8 Iron Bars, skill-modified. |
| Street Sign | 2 | 10.245 | **10.76** | **11.30** | Same recipe burden as Stop Sign. |
| **Iron Wheel** | 3 | **7.210** | **7.57** | **7.95** | 6 Iron Bars at Basic Engineering 3. |

## Key calculations

### Basic Engineering Upgrade — level 2

Core:

- 6 Wooden Gears, **static**
- 3000 calories, skill-modified

At Basic Engineering 2:

- 6 × 2.96 = 17.760
- 2250 calories = 2.250
- total = **20.010**

**21.01 Town Buy / 22.06 Town Sell.**

### Stop Sign / Street Sign — level 2

Core: 8 Iron Bars + 60 calories.

At level 2:

- 6 Iron Bars × 1.70 = 10.200
- 45 calories = 0.045
- cost = **10.245**

**10.76 / 11.30** each.

### Iron Wheel — level 3

Core: 6 Iron Bars + 100 calories.

At level 3:

- 4.2 Iron Bars × 1.70 = 7.140
- 70 calories = 0.070
- cost = **7.210**

**7.57 / 7.95.**

## Deferred Basic Engineering rows

These are source-confirmed recipes but still depend on unpriced chains:

- Waterwheel — Wooden Hull Planks + Lubricant;
- Windmill — Linen Fabric + Lubricant;
- Wood Cart — Lubricant;
- Wood Shop Cart — Cotton Fabric, Wood Cart, Store, Lubricant;
- Wooden Elevator — Hemp Mooring Rope + Lubricant;
- Hand Plow — Lubricant;
- Iron Road Tool — Leather Hide;
- Wooden Liquid Tank — Iron Pipe;
- Powered Cart — Fabric, Cast Iron Stove, Lubricant;
- Carbon Filter — Linen Fabric + Charcoal Powder;
- Mechanical Water Pump — Iron Pipe;
- Asphalt Concrete — Cement;
- Engineering research outputs — research-economy inputs.
