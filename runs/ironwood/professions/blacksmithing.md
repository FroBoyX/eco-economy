# Ironwood Blacksmithing — Current Industrial Table

Rebuilt from Eco 14 Core after the Mining/Smelting commercial-margin correction and the Hunting/Butchery audit.

Blacksmithing spans several economic depths:

- plates and Nails are shallow industrial components;
- Cooking Utensils and Saw Blades are ordinary multi-step goods/components;
- Iron hand tools are durable finished goods;
- the Sawmill is a low-volume capital workstation.

Commercial margin therefore increases with cash exposure rather than applying one markup to the entire profession.

## Current inputs

- Iron Bar: **2.54 Town Buy / 2.67 Town Sell**
- Copper Bar: **5.14 / 5.40**
- Leather Hide: **0.60 / 0.63**
- Board: **0.27 / 0.28**
- Wood: **0.40 / 0.45**
- labor: **0.001 credit/calorie**

## Shallow industrial components

### Iron Plate — Blacksmith 1

Core: 1 Iron Bar + 60 calories → 1 Iron Plate.

At Blacksmith 1:

- 0.8 Iron Bar × 2.67 = 2.136
- 48 calories = 0.048
- Exchange cash cost = **2.184**

With a ~12% shallow-processing margin:

**Iron Plate: 2.45 Town Buy / 2.57 Town Sell.**

### Copper Plate — Blacksmith 1

- 0.8 Copper Bar × 5.40 = 4.320
- 48 calories = 0.048
- cash cost = **4.368**

**Copper Plate: 4.89 Town Buy / 5.13 Town Sell.**

### Nails — Blacksmith 1

Core: 1 Iron Bar + 50 calories → 16 Nails.

At Blacksmith 1:

- 0.8 Iron Bar × 2.67 = 2.136
- 40 calories = 0.040
- cash cost/Nail = **0.136**

**Nail: 0.15 Town Buy / 0.16 Town Sell.**

## Ordinary Blacksmith outputs

### Cooking Utensils — Blacksmith 1

Core: 2 Iron Bars + 50 calories → 1.

At Blacksmith 1:

- 1.6 Iron Bars × 2.67 = 4.272
- 40 calories = 0.040
- cash cost = **4.312**

**Cooking Utensils: 4.96 Town Buy / 5.21 Town Sell.**

### Iron Saw Blade — Blacksmith 2

Core: 6 Iron Bars + 60 calories → 1.

At Blacksmith 2 (0.75):

- 4.5 Iron Bars × 2.67 = 12.015
- 45 calories = 0.045
- cash cost = **12.060**

**Iron Saw Blade: 13.87 Town Buy / 14.56 Town Sell.**

## Iron hand tools — Blacksmith 1

Current Core gives the same production recipe to:

- Iron Axe;
- Iron Pickaxe;
- Iron Shovel;
- Iron Hoe;
- Iron Sickle;
- Iron Machete;
- Iron Hammer.

Printed recipe for each:

- 12 Iron Bars;
- 8 Leather Hide;
- 12 `WoodBoard`;
- 250 calories;
- crafted at the Grindstone.

At Blacksmith 1:

- 9.6 Iron Bars × 2.67 = 25.632
- 6.4 Leather Hide × 0.63 = 4.032
- 9.6 Boards × 0.28 = 2.688
- 200 calories = 0.200
- Exchange-sourced cash cost = **32.552**

Durable hand tools receive an ~18% ordinary-finished-goods margin:

**Iron tools: 38.41 Town Buy / 40.33 Town Sell each.**

This gives the Blacksmith roughly **5.86 credits of entry-level wholesale surplus per tool** even if every input is purchased from the Exchange. Higher Blacksmith skill and direct supplier relationships expand that profit further.

## Sawmill — Blacksmith 2

Core:

- 4 Iron Bars, skill-modified;
- 16 Wood, skill-modified;
- 1 Iron Saw Blade, **static**;
- 600 calories, skill-modified.

At Blacksmith 2:

- 3 Iron Bars × 2.67 = 8.010
- 12 Wood × 0.45 = 5.400
- 1 static Iron Saw Blade × 14.56 = 14.560
- 450 calories = 0.450
- Exchange cash cost = **28.420**

As a low-volume capital workstation, Sawmill receives the 30% capital-good target:

**Sawmill: 36.95 Town Buy / 38.80 Town Sell.**

Entry-level wholesale surplus is approximately **8.53 credits per Sawmill**.

## Exchange-ready Blacksmith foundation

| Item | Town Buys | Town Sells |
|---|---:|---:|
| Nail | **0.15** | **0.16** |
| Iron Plate | **2.45** | **2.57** |
| Copper Plate | **4.89** | **5.13** |
| Cooking Utensils | **4.96** | **5.21** |
| Iron Saw Blade | **13.87** | **14.56** |
| Iron Axe | **38.41** | **40.33** |
| Iron Pickaxe | **38.41** | **40.33** |
| Iron Shovel | **38.41** | **40.33** |
| Iron Hoe | **38.41** | **40.33** |
| Iron Sickle | **38.41** | **40.33** |
| Iron Machete | **38.41** | **40.33** |
| Iron Hammer | **38.41** | **40.33** |
| Sawmill | **36.95** | **38.80** |

## Deferred Blacksmith rows

- Sharpening Steel and Steel tools require the Advanced Smelting/Steel chain;
- civic capital goods such as Bank, Mint and Currency Exchange need their complete cross-profession inputs and may receive separate civic procurement treatment;
- lighting/candle outputs use the newly canonical Tallow/Cotton values and will be included in the full profession-output pass;
- remaining decorative metal goods will be priced after their dependency classes are verified.
