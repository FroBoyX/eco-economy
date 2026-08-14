# Ironwood Fertilizers — Current-Era Table

Rebuilt from the supplied Eco 14 Core using current agriculture, garbage, Mining and Butchery values.

Fertilizers is the first profession where the pre-Recycling disposal economy begins to flip selected waste outputs into useful positive commodities. **Waste inputs do not all become positive automatically**; only actual useful outputs do.

## New shallow anchors / recovery values

| Item | Town Buys | Town Sells | Note |
|---|---:|---:|---|
| Dirt | **0.02** | **0.03** | abundant excavated raw material |
| Sulfur | **0.10** | **0.11** | excavated raw strategic mineral |
| Crushed Sulfur | **0.50** | **0.53** | current Mining 2 route controls value |
| Compost | **0.05** | **0.06** | now useful fertilizer input; Food Scrap/Bio Residue remain negative intake streams |

The existing waste schedule remains in force: Food Scrap and Bio Residue are still **-0.05 public intake**. Recycling/composting can profit both from accepting waste and from selling a usable Compost output.

## Fertilizer Filler

Core has several routes that satisfy the generic `FertilizerFiller` tag. At current prices, **Composite Filler** is the cheapest legitimate route:

- 1 Dirt
- 15 `NaturalFiber`
- 15 calories
- Fertilizers 3

Kelp is valid `NaturalFiber` at 0.04 public Sell.

At level 3:

- 0.7 Dirt × 0.03 = 0.021
- 10.5 Natural Fiber × 0.04 = 0.420
- 10.5 calories = 0.011
- cash cost ≈ **0.452**

**Fertilizer Filler / Composite Filler: 0.51 Town Buy / 0.54 Town Sell.**

Alternative Fiber/Pulp fillers remain useful resource-substitution routes but do not set the central market price.

## Current fertilizer outputs

| Item | Fertilizers | Cash cost | Town Buys | Town Sells |
|---|---:|---:|---:|---:|
| Soil Decontaminant | 1 | 0.106 ea | **0.12** | **0.13** |
| Blood Meal Fertilizer | 1 | 1.404 | **1.61** | **1.69** |
| Hide Ash Fertilizer | 1 | 1.956 | **2.25** | **2.36** |
| Pelt Fertilizer | 2 | 1.474 | **1.69** | **1.77** |
| Camas Ash Fertilizer | 2 | 2.636 | **3.03** | **3.18** |
| Phosphate Fertilizer | 3 | 1.691 | **1.94** | **2.04** |
| Berry Extract Fertilizer | 3 | 4.463 | **5.13** | **5.39** |
| Compost Fertilizer | 5 | 0.369 | **0.42** | **0.44** |
| Heavy Mineral Decontaminant | 4 | 1.391 ea | **1.60** | **1.68** |
| Black Powder | 3 | 0.374 ea | **0.43** | **0.45** |

## Useful equipment / capital

### Soil Sampler — Fertilizers 1

Core: 2 Wood + 2 `WoodBoard` + 50 calories.

At level 1 cash cost is **1.208**.

**Soil Sampler: 1.43 / 1.50.**

### Wood / Rustic Window Planter — Fertilizers 1

Core: 5 Wood + 360 calories.

At level 1 cash cost = **2.088**.

**Wood Window Planter: 2.40 / 2.52.**

**Rustic Window Planter: 2.40 / 2.52.**

### Fertilizers Upgrade — level 2

Core:

- 10 Hide Ash Fertilizer, static
- 6,000 calories

At level 2:

- 10 × 2.36 = 23.60
- 4,500 calories = 4.50
- cash cost = **28.10**

**Fertilizers Upgrade: 36.53 / 38.36.**

## Crushed Sulfur sanity check

Current Mining 2 route: 20 static Sulfur + 70 calories -> 5 Crushed Sulfur.

At public Sulfur 0.11 and Mining 2:

- 20 × 0.11 = 2.20
- 52.5 calories = 0.053
- cost/output ≈ 0.451

With shallow Mining margin:

**Crushed Sulfur: 0.50 / 0.53.**

This is cheaper than the earlier low-efficiency sulfur-crushing routes and is appropriate once Mining 2 is normal.

## Still blocked Fertilizers outputs

- Chemical Decontaminant — Iron Oxide;
- Plastic Window Planter — Plastic;
- Agriculture Research Paper Advanced — research chain;
- later filler routes may reprice when Wood Pulp/Recycling inputs become abundant.

The ordinary fertilizer economy is now usable without waiting for Oil Drilling or modern Recycling.
