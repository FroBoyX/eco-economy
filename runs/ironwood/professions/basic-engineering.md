# Ironwood Basic Engineering — Current Infrastructure Table

Rebuilt from the supplied Eco 14 Core after canonicalizing Lubricant, Leather, textiles, Shipwright materials, Pipes, Store and the commercially viable metal/wood chains.

## Current key inputs

- Hewn Log **0.93 / 0.98**
- Board **0.27 / 0.28**
- Iron Bar **2.54 / 2.67**
- Iron Plate **2.45 / 2.57**
- Copper Plate **4.89 / 5.13**
- Iron Pipe **2.41 / 2.53**
- Leather Hide **0.60 / 0.63**
- Lumber **1.62 / 1.70**
- Linen Fabric **0.68 / 0.71**
- Cotton Fabric **0.86 / 0.90**
- Lubricant **0.28 / 0.29**
- Wooden Hull Planks **1.10 / 1.16**
- Hemp Mooring Rope **1.05 / 1.10**
- Charcoal Powder **0.22 / 0.23**
- Store **7.41 / 7.78**
- Cast Iron Stove **36.85 / 38.69**

## Exchange-ready Basic Engineering outputs

| Item | Level | Cash cost | Town Buys | Town Sells | Class |
|---|---:|---:|---:|---:|---|
| Wooden Gear | 1 | 3.168 | **3.55** | **3.73** | simple component |
| Wooden Wheel | 1 | 3.168 | **3.55** | **3.73** | simple component |
| Arrastra | 1 | 7.570 | **9.84** | **10.33** | capital workstation |
| Rocker Box | 1 | 4.480 | **5.82** | **6.11** | capital workstation |
| Stone Road | 1 | ~0.264 | **0.30** | **0.32** | public/byproduct sink |
| Stone Road Tool | 1 | 4.720 | **5.57** | **5.85** | durable tool |
| Waterwheel | 1 | 16.336 | **21.24** | **22.30** | power infrastructure |
| Windmill | 1 | 19.648 | **25.54** | **26.82** | power infrastructure |
| Wood Cart | 1 | 12.798 | **16.64** | **17.47** | early vehicle |
| **Wood Shop Cart** | 1 | 45.530 | **63.74** | **66.93** | late/deep shop vehicle |
| Mechanical Water Pump | 1 | 33.328 | **43.33** | **45.50** | capital machine |
| Carbon Filter | 1 | 5.648 ea | **6.66** | **6.99** | multi-step component |
| Wooden Elevator | 1 | 80.100 | **112.14** | **117.75** | late infrastructure |
| Basic Engineering Upgrade | 2 | 24.630 | **32.02** | **33.62** | capital/upgrade |
| Stop Sign | 2 | 16.065 | **18.47** | **19.39** | ordinary finished |
| Street Sign | 2 | 16.065 | **18.47** | **19.39** | ordinary finished |
| Hand Plow | 2 | 32.520 | **42.28** | **44.39** | vehicle/tool capital |
| Iron Wheel | 3 | 11.284 | **12.64** | **13.27** | industrial component |
| Iron Road Tool | 3 | 59.154 | **73.94** | **77.64** | deep durable tool |
| Wooden Liquid Tank | 4 | 52.728 | **68.55** | **71.98** | capital infrastructure |
| **Powered Cart** | 5 | 92.760 | **129.86** | **136.35** | late vehicle/capital good |

## Newly completed shop/vehicle loop

### Wood Shop Cart — Basic Engineering 1

Core:

- 12 Cotton Fabric
- 8 Lumber
- 1 Wood Cart, static
- 1 Store, static
- 2 Lubricant, static
- 225 calories

At level 1:

- 9.6 Cotton Fabric × 0.90 = 8.640
- 6.4 Lumber × 1.70 = 10.880
- Wood Cart = 17.47
- Store = 7.78
- 2 Lubricant = 0.58
- 180 calories = 0.180
- cash cost = **45.530**

This is both a vehicle and mobile retail-capital object, so it receives the ~40% late-capital treatment:

**Wood Shop Cart: 63.74 / 66.93.**

### Powered Cart — Basic Engineering 5

Core:

- 30 Boards
- 20 generic `Fabric`
- 1 Cast Iron Stove, static
- 3 Iron Wheels, static
- 2 Lubricant, static
- 200 calories

At level 5 (0.60), using Linen Fabric as the cheapest current public `Fabric` input:

- 18 Boards × 0.28 = 5.040
- 12 Fabric × 0.71 = 8.520
- Cast Iron Stove = 38.69
- 3 Iron Wheels × 13.27 = 39.810
- 2 Lubricant = 0.580
- 120 calories = 0.120
- cash cost = **92.760**

**Powered Cart: 129.86 / 136.35.**

## Important capital examples

- Waterwheel: **21.24 / 22.30**
- Windmill: **25.54 / 26.82**
- Wood Cart: **16.64 / 17.47**
- Wooden Elevator: **112.14 / 117.75**
- Powered Cart: **129.86 / 136.35**

The deeper goods create larger absolute currency injections because they tie up more player-shop inventory and upstream production value.

## Still deferred

- Asphalt Concrete — Cement/Advanced Masonry;
- research outputs — research-economy policy;
- advanced electrical/industrial Engineering — later profession families.
