# Ironwood Smelting — Metal Bars

This file contains the currently validated Smelting portion of the Ironwood metal economy.

It uses the corrected Mining chain from `mining.md` and Eco 14 Core. Other Smelting products are intentionally omitted until recalculated from these bar values.

## Entry-skill rule

Smelting resource multipliers are:

- level 1: 0.80
- level 2: 0.75
- level 3: 0.70
- level 4: 0.65
- level 5: 0.60
- level 6: 0.55
- level 7: 0.50

Iron and Copper Bloomery recipes require Smelting 1. Gold requires Smelting 4.

## Supporting inputs and environmental costs

- Clay Mold: **0.05 Town Buy / 0.06 Town Sell**;
- Slag: **0.05 Town Buy / 0.08 Town Sell**;
- Ceramic Scrap disposal: **0.15/unit**;
- Tailings disposal is already included upstream in concentrate prices;
- Bloomery fuel is included as a small operating cost using conservative Charcoal pricing.

## Iron Bar

Smelting 1 effective Bloomery recipe:

- 1.6 Iron Concentrate;
- 1.6 Clay Molds;
- 48 calories;
- 6 Iron Bars;
- 1.6 Slag;
- 1.5 Ceramic Scrap;
- Bloomery fuel.

Using Iron Concentrate retail **5.20**, entry cost is about **1.47 per bar**.

**Iron Bar: 1.55 Town Buy / 1.65 Town Sell.**

## Copper Bar

Smelting 1 effective Bloomery recipe:

- 1.6 Copper Concentrate;
- 1.6 Clay Molds;
- 48 calories;
- 6 Copper Bars;
- 1.6 Slag;
- 1.5 Ceramic Scrap;
- Bloomery fuel.

Using Copper Concentrate retail **11.75**, entry cost is about **3.23 per bar**.

**Copper Bar: 3.40 Town Buy / 3.60 Town Sell.**

This is slightly below the earlier 3.85 retail value because the corrected model removes an unnecessarily wide raw Copper Ore Exchange spread.

## Gold Bar

Gold unlocks at Smelting 4, so the Bloomery uses the 0.65 resource multiplier.

Entry-effective recipe:

- **1.3 Gold Concentrate**;
- **1.3 Clay Molds**;
- **39 calories**;
- **3 Gold Bars**;
- **1.3 Slag**;
- **1.5 Ceramic Scrap**;
- Bloomery fuel.

Using Gold Concentrate retail **29.00**, total craft cost is about **38.2**, or roughly **12.74 per Gold Bar**.

**Gold Bar: 13.40 Town Buy / 14.00 Town Sell.**

## Why Gold Concentrate can cost more than a Gold Bar

The item units are not one-to-one.

At the first Gold-smelting skill level:

- 1.3 Gold Concentrate → 3 Gold Bars;
- therefore 1 Gold Concentrate → about **2.31 Gold Bars**.

At 29.00 retail, one Gold Concentrate carries about **12.57 credits of concentrate cost per eventual bar**. Smelting then adds molds, labor, fuel, waste handling, and a shallow producer margin to reach the 14.00 Gold Bar retail price.

So the nominal comparison `29 concentrate vs 14 bar` is misleading; the economically relevant comparison is **29 concentrate vs ~32.3 credits of finished bars produced from one concentrate-equivalent**.

## Validated bar table

| Item | Town Buys | Town Sells | Entry cost/unit |
|---|---:|---:|---:|
| **Iron Bar** | **1.55** | **1.65** | ~1.47 |
| **Copper Bar** | **3.40** | **3.60** | ~3.23 |
| **Gold Bar** | **13.40** | **14.00** | ~12.74 |

## Downstream reason not to overprice Gold

Gold Bars feed Electronics, Mechanics, advanced Masonry, banking/currency infrastructure, Country/Federation foundations, and later high-volume products such as the Laser. Core includes recipes consuming dozens of Gold Bars at once.

The Gold ore-to-bar conversion already creates strong scarcity. An additional large Exchange spread would magnify every later technology and government structure unnecessarily.

## Progression

Later Blast Furnace production, higher skill, modules, talents, and Recycling should reduce effective costs and raise producer margins while these fixed bar prices remain stable unless Ironwood deliberately passes technological deflation downstream.
