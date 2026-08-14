# Ironwood Basic Engineering — Current Infrastructure Table

Rebuilt from the supplied Eco 14 Core after canonicalizing Lubricant, Leather, Linen/Cotton textiles, Shipwright materials, Iron/Copper Pipe and the commercially viable metal/wood chains.

Basic Engineering now spans simple components, ordinary tools, infrastructure workstations and vehicle-scale capital. Margin therefore increases with economic depth.

## Current key inputs

- Hewn Log: **0.93 / 0.98**
- Board: **0.27 / 0.28**
- Iron Bar: **2.54 / 2.67**
- Iron Plate: **2.45 / 2.57**
- Copper Plate: **4.89 / 5.13**
- Iron Pipe: **2.41 / 2.53**
- Leather Hide: **0.60 / 0.63**
- Lumber: **1.62 / 1.70**
- Linen Fabric: **0.68 / 0.71**
- Cotton Fabric: **0.86 / 0.90**
- Lubricant: **0.28 / 0.29**
- Wooden Hull Planks: **1.10 / 1.16**
- Hemp Mooring Rope: **1.05 / 1.10**
- Charcoal Powder: **0.22 / 0.23** working canonical Milling value

## Exchange-ready Basic Engineering outputs

| Item | Basic Eng. | Exchange cash cost | Town Buys | Town Sells | Class |
|---|---:|---:|---:|---:|---|
| Wooden Gear | 1 | 3.168 | **3.55** | **3.73** | simple component |
| Wooden Wheel | 1 | 3.168 | **3.55** | **3.73** | simple component |
| Arrastra | 1 | 7.570 | **9.84** | **10.33** | capital workstation |
| Rocker Box | 1 | 4.480 | **5.82** | **6.11** | capital workstation |
| Stone Road | 1 | ~0.264 | **0.30** | **0.32** | special public/byproduct sink |
| Stone Road Tool | 1 | 4.720 | **5.57** | **5.85** | durable finished tool |
| **Waterwheel** | 1 | 16.336 | **21.24** | **22.30** | capital power infrastructure |
| **Windmill** | 1 | 19.648 | **25.54** | **26.82** | capital power infrastructure |
| **Wood Cart** | 1 | 12.798 | **16.64** | **17.47** | early vehicle/capital good |
| **Mechanical Water Pump** | 1 | 33.328 | **43.33** | **45.50** | capital machine |
| **Carbon Filter** | 1 | 5.648 ea | **6.66** | **6.99** | multi-step component |
| Basic Engineering Upgrade | 2 | 24.630 | **32.02** | **33.62** | capital/upgrade |
| Stop Sign | 2 | 16.065 | **18.47** | **19.39** | ordinary finished |
| Street Sign | 2 | 16.065 | **18.47** | **19.39** | ordinary finished |
| **Hand Plow** | 2 | 32.520 | **42.28** | **44.39** | vehicle/tool capital |
| Iron Wheel | 3 | 11.284 | **12.64** | **13.27** | industrial component |
| **Iron Road Tool** | 3 | 59.154 | **73.94** | **77.64** | deep durable tool |
| **Wooden Liquid Tank** | 4 | 52.728 | **68.55** | **71.98** | capital infrastructure |
| **Wooden Elevator** | 1 | 80.100 | **112.14** | **117.75** | deep infrastructure/late-capital windfall |

## Key new dependencies and calculations

### Waterwheel — Basic Engineering 1

Core:

- 8 Wooden Hull Planks
- 4 Lubricant
- 10 Hewn Logs
- 180 calories

At level 1:

- 6.4 Hull Planks × 1.16 = 7.424
- 3.2 Lubricant × 0.29 = 0.928
- 8 Hewn Logs × 0.98 = 7.840
- 144 calories = 0.144
- cash cost = **16.336**

**21.24 / 22.30.**

### Windmill — Basic Engineering 1

Core:

- 12 Linen Fabric
- 4 Lubricant
- 15 Hewn Logs
- 180 calories

At level 1:

- 9.6 Linen Fabric × 0.71 = 6.816
- 3.2 Lubricant × 0.29 = 0.928
- 12 Hewn Logs × 0.98 = 11.760
- 144 calories = 0.144
- cash cost = **19.648**

**25.54 / 26.82.**

### Wood Cart — Basic Engineering 1

Core:

- 4 Hewn Logs, skill-modified
- 8 Boards, skill-modified
- 2 Wooden Wheels, **static**
- 1 Lubricant, **static**
- 150 calories

At level 1:

- 3.2 Hewn Logs × 0.98 = 3.136
- 6.4 Boards × 0.28 = 1.792
- 2 Wheels × 3.73 = 7.460
- Lubricant = 0.290
- 120 calories = 0.120
- cash cost = **12.798**

**16.64 / 17.47.**

### Wooden Elevator — Basic Engineering 1

Core:

- 16 Iron Bars
- 6 Wooden Gears
- 4 Hemp Mooring Rope
- 30 Hewn Logs
- 2 Lubricant, static
- 500 calories

At level 1:

- 12.8 Iron Bars × 2.67 = 34.176
- 4.8 Wooden Gears × 3.73 = 17.904
- 3.2 Hemp Rope × 1.10 = 3.520
- 24 Hewn Logs × 0.98 = 23.520
- 2 static Lubricant × 0.29 = 0.580
- 400 calories = 0.400
- total cash cost = **80.100**

This is exactly the sort of deep, low-volume infrastructure good that should create a noticeable currency event for the specialist.

**Wooden Elevator: 112.14 Town Buy / 117.75 Town Sell** using a ~40% late-capital uplift.

### Iron Road Tool — Basic Engineering 3

Core:

- 20 Iron Bars
- 6 Leather Hide
- 16 Lumber
- 125 calories

At level 3 (0.70):

- 14 Iron Bars × 2.67 = 37.380
- 4.2 Leather × 0.63 = 2.646
- 11.2 Lumber × 1.70 = 19.040
- 87.5 calories = 0.088
- cash cost ≈ **59.154**

As a deep durable tool:

**73.94 / 77.64.**

## Stone Road note

Stone Road now costs roughly 0.264 in public inputs at Basic Engineering 1, so the commodity price is raised slightly to **0.30 / 0.32**. The existing government road-placement payment should be reviewed separately because its purpose is infrastructure labor/subsidy rather than ordinary commodity margin.

## Still deferred

- Wood Shop Cart — `Store` dependency still needs its Carpentry price;
- Powered Cart — Cast Iron Stove and generic Fabric lane need final source audit;
- research outputs — research-economy policy;
- Asphalt Concrete — Cement/Advanced Masonry;
- advanced electrical/industrial Engineering — later professions.
