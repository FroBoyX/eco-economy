# Ironwood Smelting — Metal Bars

This file contains the currently validated Smelting portion of the Ironwood metal economy.

It uses the corrected Mining chain from `mining.md` and Eco 14 Core. Other Smelting products are intentionally omitted until recalculated from these bar values.

## Entry-skill rule

Smelting uses the same multiplicative resource strategy:

- level 1: 0.80
- level 2: 0.75
- level 3: 0.70
- level 4: 0.65
- level 5: 0.60
- level 6: 0.55
- level 7: 0.50

The Bloomery recipes for Iron and Copper require Smelting 1. Gold requires Smelting 4.

Their concentrate and Clay Mold ingredients are skill-modified, so entry quantities are not the printed quantities.

## Cross-profession input: Clay Mold

Core Gathering 1 recipe:

- 1 Clay, skill-modified;
- 50 calories, skill-modified;
- 4 Clay Molds.

At Gathering 1 with Clay retail 0.17:

- effective Clay: 0.8;
- effective labor: 40 calories;
- cost per four molds: about 0.176;
- cost per mold: about 0.044.

**Clay Mold: 0.05 Town Buy / 0.06 Town Sell.**

## Environmental costs

Current pre-recycling treatment:

- Tailings disposal: **0.35/unit** — already included in concentrate prices;
- Ceramic Scrap disposal: **0.15/unit**;
- Slag: **0.05 Town Buy / 0.08 Town Sell** as a low-value useful byproduct.

Bloomery recipes create 1.5 Ceramic Scrap per craft.

Slag output is skill-modified. At Smelting 1, a printed 2 Slag becomes 1.6; at Smelting 4 it becomes 1.3.

## Bloomery fuel

The Bloomery consumes 10 W of heat power from `Burnable Fuel`.

For a conservative entry-cost check, this calculation uses Charcoal at 1.95 retail rather than relying on the cheapest possible fuel arbitrage.

Fuel remains a small part of bar cost:

- Iron Bloomery craft: roughly 0.23 credit;
- Copper Bloomery craft: roughly 0.28 credit;
- Gold Bloomery craft: roughly 0.23 credit.

A cheaper valid fuel would increase Smelting margin slightly without requiring a price change.

## Iron Bar

Core Bloomery recipe, Smelting 1:

Printed:

- 2 Iron Concentrate;
- 2 Clay Molds;
- 60 calories;
- 6 Iron Bars;
- 2 Slag;
- 1.5 Ceramic Scrap;
- 5 craft minutes.

Entry-effective at Smelting 1:

- **1.6 Iron Concentrate**;
- **1.6 Clay Molds**;
- **48 calories**;
- **6 Iron Bars**;
- **1.6 Slag**;
- **1.5 Ceramic Scrap**;
- about **4 minutes** of Bloomery operation.

Using Iron Concentrate retail 5.35:

- concentrate: 8.56;
- molds: 0.096;
- labor: 0.048;
- Ceramic Scrap disposal: 0.225;
- conservative Charcoal fuel: ~0.234;
- Slag credit: -0.080.

Total craft cost: about **9.083**.

Cost per Iron Bar: about **1.514**.

**Iron Bar: 1.55 Town Buy / 1.65 Town Sell.**

Entry Bloomery margin at the Town Buy price is about **2.4%**. That is deliberately shallow.

## Copper Bar

Core Bloomery recipe, Smelting 1:

Entry-effective:

- **1.6 Copper Concentrate**;
- **1.6 Clay Molds**;
- **48 calories**;
- **6 Copper Bars**;
- **1.6 Slag**;
- **1.5 Ceramic Scrap**;
- about **4.8 minutes** of Bloomery operation.

Using Copper Concentrate retail 12.90:

Total craft cost is about **21.210**.

Cost per Copper Bar: about **3.535**.

**Copper Bar: 3.65 Town Buy / 3.85 Town Sell.**

Entry Bloomery margin at the Town Buy price is about **3.3%**.

## Gold Bar

Gold is different because the Bloomery recipe requires **Smelting 4**.

Core printed recipe:

- 2 Gold Concentrate;
- 2 Clay Molds;
- 60 calories;
- 3 Gold Bars;
- 2 Slag;
- 1.5 Ceramic Scrap;
- 6 craft minutes.

At Smelting 4, the multiplier is 0.65:

- **1.3 Gold Concentrate**;
- **1.3 Clay Molds**;
- **39 calories**;
- **3 Gold Bars**;
- **1.3 Slag**;
- **1.5 Ceramic Scrap**;
- about **3.9 minutes** of Bloomery operation.

Using Gold Concentrate retail 32.90:

Total craft cost is about **43.275**.

Cost per Gold Bar: about **14.425**.

**Gold Bar: 15.10 Town Buy / 16.00 Town Sell.**

Entry Bloomery margin at the Town Buy price is about **4.7%**.

## Validated bar table

| Item | Town Buys | Town Sells | Entry Bloomery cost/unit |
|---|---:|---:|---:|
| **Iron Bar** | **1.55** | **1.65** | ~1.514 |
| **Copper Bar** | **3.65** | **3.85** | ~3.535 |
| **Gold Bar** | **15.10** | **16.00** | ~14.425 |

## Blast Furnace progression check

The later Blast Furnace recipes use fewer concentrates, less Ceramic Scrap, and much less craft time.

Using the same fixed bar prices and conservative Charcoal fuel, approximate entry costs at the relevant skill level are:

| Bar | Blast Furnace cost/unit | Town Buy | Approx. producer margin |
|---|---:|---:|---:|
| Iron | ~1.13 | 1.55 | ~38% |
| Copper | ~2.64 | 3.65 | ~38% |
| Gold | ~10.79 | 15.10 | ~40% |

This is intentional technological progression.

The bar price does **not** fall merely because the producer acquires better infrastructure. The improved machine creates the producer's larger margin.

## Recycling transition

When Tailings, Ceramic Scrap, or Slag gain stronger recovery value, do not preserve the old disposal assumption. Recalculate the chain.

The default expectation is that recycling technology should reduce effective Mining/Smelting cost and improve margins unless Ironwood deliberately lowers prices to pass some technological deflation downstream.
