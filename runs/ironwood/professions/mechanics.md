# Ironwood Mechanics — Current Industrial Table

Rebuilt directly from the supplied Eco 14 Core using current Ironwood producer values and minimum unlock skill.

Derived producer costs use upstream Town Buy/producer values. The Exchange retail spread is applied after the producer value is established.

## Current key inputs

- Iron Bar: **1.70 Town Buy / 1.79 Town Sell**
- Copper Bar: **3.43 / 3.60**
- Gold Bar: **7.88 / 8.27**
- Iron Plate: **1.48 / 1.55**
- Copper Plate: **2.93 / 3.08**
- Iron Wheel: **7.57 / 7.95**
- Iron Saw Blade: **8.08 / 8.48**
- Lumber: **1.60 / 1.68**
- Board: **0.26 / 0.27**
- Wooden Gear: **2.96 / 3.11**
- labor: **0.001 credit/calorie**

## Exchange-ready Mechanics table

| Item | Mechanics | Entry cost | Town Buys | Town Sells | Notes |
|---|---:|---:|---:|---:|---|
| Screws | 1 | 0.345 ea | **0.36** | **0.38** | 1 Iron Bar → 4, skill-modified. |
| Iron Gear | 1 | 1.420 | **1.49** | **1.56** | 1 Iron Bar + labor. |
| **Copper Wiring** | 1 | 0.919 ea | **0.96** | **1.01** | 4 Copper Bars → 12. |
| **Iron Axle** | 1 | 2.780 | **2.92** | **3.07** | 2 Iron Bars. |
| **Boiler** | 1 | 30.160 | **31.67** | **33.25** | Iron Plate + Screws + Copper Plate. |
| **Screw Press** | 1 | 19.184 | **20.14** | **21.15** | Iron Plate + Wooden Gears. |
| **Lathe** | 1 | 38.552 | **40.48** | **42.50** | 4 Iron Wheels + 12 Iron Plates. |
| **Heat Sink** | 2 | 21.945 | **23.04** | **24.19** | Copper Plate + Copper Wiring. |
| **Mechanics Advanced Upgrade** | 2 | 41.930 | **44.03** | **46.23** | Six Copper Wiring + one Boiler are static. |
| **Recycler** | 2 | 5.280 | **5.54** | **5.82** | 4 Iron Bars, skill-modified. |
| Stamp Mill | 2 | 21.915 | **23.01** | **24.16** | Iron Bars + Screws + Iron Gears + Boards. |
| **Steam Tractor Plow** | 2 | 13.830 | **14.52** | **15.25** | Iron Plate + Screws. |
| **Steam Tractor Scoop** | 2 | 13.830 | **14.52** | **15.25** | Same burden as Plow. |
| **Steam Tractor Tree Cutter** | 2 | 33.670 | **35.35** | **37.12** | Static Iron Saw Blade plus plate/screws/gears. |
| **Steam Truck Flatbed** | 2 | 22.215 | **23.33** | **24.50** | Lumber is the dominant input. |
| **Steam Truck Garbage Collector** | 2 | 10.275 | **10.79** | **11.33** | Iron Plate + Screws. |
| **Screening Machine** | 3 | 62.020 | **65.12** | **68.38** | 40 Iron Bars + Screws + Iron Gears at Mechanics 3. |
| **Gold Wiring** | 4 | 2.580 ea | **2.71** | **2.85** | 2 Gold Bars → 4. |
| **Metal Keel** | 4 | 8.918 | **9.36** | **9.83** | 8 Iron Bars. |

## Key calculations

### Copper Wiring — Mechanics 1

Core Screw Press recipe:

- 4 Copper Bars
- 60 calories
- output 12 Copper Wiring

At Mechanics 1:

- 3.2 Copper Bars × 3.43 = 10.976
- 48 calories = 0.048
- total = 11.024 / 12 = **0.919 per wire**

**0.96 Town Buy / 1.01 Town Sell.**

### Boiler — Mechanics 1

At entry efficiency:

- 12 Iron Plates × 1.48 = 17.760
- 8 Screws × 0.36 = 2.880
- 3.2 Copper Plates × 2.93 = 9.376
- 144 calories = 0.144
- total = **30.160**

**31.67 / 33.25.**

### Lathe — Mechanics 1

At entry efficiency:

- 3.2 Iron Wheels × 7.57 = 24.224
- 9.6 Iron Plates × 1.48 = 14.208
- 120 calories = 0.120
- total = **38.552**

**40.48 / 42.50.**

### Stamp Mill — Mechanics 2

At Mechanics 2:

- 3.75 Iron Bars × 1.70 = 6.375
- 10.5 Screws × 0.36 = 3.780
- 6 Iron Gears × 1.49 = 8.940
- 10.5 Boards × 0.26 = 2.730
- 90 calories = 0.090
- total = **21.915**

**23.01 / 24.16.**

### Steam Truck Flatbed — Mechanics 2

At Mechanics 2:

- 1.5 Iron Plates × 1.48 = 2.220
- 4.5 Screws × 0.36 = 1.620
- 11.25 Lumber × 1.60 = 18.000
- 375 calories = 0.375
- total = **22.215**

**23.33 / 24.50.**

This is a good downstream check on the Lumber rebalance: Lumber matters strongly, but the part does not inherit the old 3-credit Lumber inflation.

## Deferred Mechanics rows

Do not fill these from old tables until the missing dependencies are canonical:

- Gearbox, Steam Engine, Power Hammer — Lubricant;
- Mechanical/vehicle chains using Iron Pipe or Copper Pipe;
- Assembly Line and Portable Steam Engine — Pipe + Boiler/Piston chain;
- Steam Tractor / Steam Truck — Leather Hide, Lubricant, Light Bulb and engine chain;
- Blast Furnace — Iron Hull Sheet + Iron Pipe;
- Laboratory / Camera Film / research machines — Paper and research economy;
- Electric Machinist Table and modern machines — Steel and circuits;
- Desalinator / Water Filter — Copper Pipe and Gearbox/Piston;
- recycling sorters — Fabric, Lubricant, Reinforced Concrete;
- Transmission Pole / advanced electrical equipment — Basic Circuit;
- Steel and industrial liquid equipment — Steel chain.
