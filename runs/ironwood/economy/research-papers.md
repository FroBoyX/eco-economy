# Ironwood Research Papers — Basic through Modern

Source: supplied Eco 14 Core (`Eco14-Core(3).zip`) plus the current Ironwood schema-18 Steam-entry price ledger.

This is a **separate research projection lane**. Modern-support materials are priced only far enough to calculate research-paper economics; they do **not** become current Steam-era Exchange price setters.

## Naming and producer map

Eco uses two related naming systems here, and they should not be conflated:

- the **Research Paper family** is the actual item name (`Agriculture`, `Culinary`, `Dendrology`, `Engineering`, `Gathering`, `Geology`, `Metallurgy`);
- the **producing specialty** is the skill that crafts that tier of paper.

This matters especially for Engineering: **Basic Engineering is the specialty that produces `Engineering Research Paper Advanced`**. The supplied vanilla Core does not define an `Engineering Research Paper Basic` item.

| Core paper family | Basic producer | Advanced producer | Modern producer |
|---|---|---|---|
| Agriculture | Farming | Fertilizers | Oil Drilling |
| Culinary | Campfire Cooking | Cooking / alternate Baking route | Advanced Cooking |
| Dendrology | Logging | Carpentry / alternate Shipwright route | Paper Milling |
| Engineering | — | **Basic Engineering** | Mechanics |
| Gathering | Gathering | Tailoring | — |
| Geology | Mining | Masonry | Pottery / alternate Glassworking route |
| Metallurgy | Smelting | Blacksmith | Advanced Smelting |

The Core display names use **`Agriculture Research Paper ...`** and **`Dendrology Research Paper ...`** exactly. Ironwood may use friendlier labels in signage, but the ledger should preserve the source item names.

## Pricing rule

Research papers use the same integrated-specialty accounting as the rest of Ironwood:

- same-specialty crafted components enter at **Projected Cost**;
- cross-specialty inputs enter at **Town Sell**;
- same-specialty raw anchors enter at Town Buy/opportunity value;
- labor remains **1 credit / 1,000 calories**;
- prior-tier papers are cross-specialty knowledge inputs when the next tier is made by a different specialty and therefore enter at their Town Sell price.

Research is finite civic demand, so Library purchases should be **quantity-capped procurement**, not unlimited government imports.

Recommended direct-sale research premiums:

- **Basic:** Projected Cost × 1.15
- **Advanced:** Projected Cost × 1.20
- **Modern:** Projected Cost × 1.25

Town Sell then uses Ironwood's ordinary Exchange spread.

## Basic Research Papers

| Research Paper | Producing Specialty / Route | Projected Cost | Town Buys | Town Sells |
|---|---|---:|---:|---:|
| Agriculture Research Paper Basic | Farming 1 | **2.90** | **3.33** | **3.50** |
| Culinary Research Paper Basic | Campfire Cooking route | **1.12** | **1.29** | **1.35** |
| Dendrology Research Paper Basic | Logging 1 | **6.42** | **7.39** | **7.76** |
| Gathering Research Paper Basic | Gathering 1 | **1.46** | **1.68** | **1.76** |
| Geology Research Paper Basic | Mining 1 | **2.42** | **2.79** | **2.93** |
| Metallurgy Research Paper Basic | Smelting 1 | **6.23** | **7.16** | **7.52** |

### Basic route notes

- Agriculture Basic uses the cheapest legitimate current `Raw Food` and `Crop Seed` inputs. `Sunflower Seed` is the least-cost current Farming-produced Crop Seed at about **0.024 projected cost each**.
- Culinary Basic has three Core routes. The Campfire Cooking route is cheaper than the Dried Fish and Dried Meat Hunting routes under current prices.
- Gathering Basic uses cheap raw food plus `NaturalFiber`; Kelp is a valid Natural Fiber.
- Metallurgy Basic uses Iron Bar as the cheapest current `Metal` and low-value crushed rock for `CrushedRock`.
- There is no Engineering-family Basic paper in the supplied Core. **Basic Engineering appears one tier later as the producer of Engineering Research Paper Advanced.**

## Advanced Research Papers

| Research Paper | Producing Specialty / Cheapest Core Route | Projected Cost | Town Buys | Town Sells |
|---|---|---:|---:|---:|
| Agriculture Research Paper Advanced | Fertilizers 1 | **24.72** | **29.66** | **31.14** |
| Culinary Research Paper Advanced | Baking meat route | **19.76** | **23.71** | **24.90** |
| Dendrology Research Paper Advanced | Shipwright hull-plank route | **15.54** | **18.64** | **19.57** |
| Engineering Research Paper Advanced | **Basic Engineering 1** | **29.44** | **35.33** | **37.10** |
| Gathering Research Paper Advanced | Tailoring 1 | **4.91** | **5.89** | **6.18** |
| Geology Research Paper Advanced | Masonry 1 | **6.80** | **8.16** | **8.57** |
| Metallurgy Research Paper Advanced | Blacksmith 1 | **19.82** | **23.79** | **24.98** |

### Advanced route notes

- Agriculture Advanced is expensive because five Berry Extract Fertilizer are required before skill reduction. Spoiled Food is treated at **0 acquisition cost** for the projection rather than assuming a speculative disposal subsidy; any paid waste intake only improves the producer's realized margin.
- Culinary Advanced has a Cooking route and a Baking/meat route. The Baking route is cheaper under current Ironwood inputs.
- Dendrology Advanced has Carpentry/Hewn Log and Shipwright/Wooden Hull Planks routes. The Shipwright route is cheaper under the integrated-specialty rule.
- Gathering Advanced uses Linen Fabric as the cheapest current `Fabric` route.

## Modern Research Papers

| Research Paper | Producing Specialty / Cheapest Route | Projected Cost | Town Buys | Town Sells |
|---|---|---:|---:|---:|
| Agriculture Research Paper Modern | Oil Drilling 1 | **56.23** | **70.29** | **73.80** |
| Culinary Research Paper Modern | Advanced Cooking 2 | **57.09** | **71.36** | **74.93** |
| Dendrology Research Paper Modern | Paper Milling 1 | **43.49** | **54.36** | **57.08** |
| Engineering Research Paper Modern | Mechanics 1 | **62.72** | **78.40** | **82.32** |
| Geology Research Paper Modern | Pottery/Brick route | **23.54** | **29.42** | **30.89** |
| Metallurgy Research Paper Modern | Advanced Smelting 1 | **73.23** | **91.54** | **96.12** |

### Modern route notes

- Agriculture Modern requires Sulfuric Acid, Phosphate Fertilizer, Bio Residue, Compost Fertilizer, Ink, Paper and the Advanced Agriculture paper. Bio Residue is carried at **0 input acquisition cost** rather than using a speculative negative subsidy.
- Culinary Modern requires Boiled Sausage, Bread, Worldly Donut, Smooth Gut Noodle Roll, Ink, Paper and the Advanced Culinary paper.
- Dendrology Modern requires Waxed Paper, Lumber, Ink, Paper and the Advanced Dendrology paper. Paper and Waxed Paper are both Paper Milling outputs and therefore carry internal Projected Cost rather than Paper Milling's own direct-sale markup.
- Engineering Modern uses Mechanics-produced Iron Axles and Iron Gears at Mechanics Projected Cost, while Lubricant, Ink, Paper and the Advanced Engineering paper remain cross-specialty purchases.
- Geology Modern has Pottery/Brick and Glassworking/Glass routes. The **Brick route is materially cheaper** under current Ironwood policy because Pottery carries its own Brick at Brick's Projected Cost rather than the 1.20/1.25 bulk direct-sale policy price.
- Metallurgy Modern uses Steel Bar and Rebar internally inside Advanced Smelting, so neither Steel nor Rebar direct-sale markup is compounded into the paper.
- The supplied Core defines no Gathering Research Paper Modern.

## Future-support projections used only for Modern papers

These are supporting calculations, **not current Steam-era Exchange prices**.

| Supporting item | Producing Specialty | Projected Cost | Reference Buy | Reference Sell |
|---|---|---:|---:|---:|
| Barrel | Advanced Smelting | **1.87** | **2.15** | **2.26** |
| Sulfuric Acid | Recycling | **0.38** | **0.44** | **0.46** |
| Petroleum | Oil Drilling | **2.31** | **2.58** | **2.71** |
| Paraffin | Oil Drilling | **0.32** | **0.36** | **0.38** |
| Waxed Paper | Paper Milling | **0.33** | **0.38** | **0.40** |
| Ceramic Mold | Pottery | **0.05** | **0.05** | **0.06** |
| Steel Bar — charcoal route | Advanced Smelting | **4.36** | **5.02** | **5.27** |
| Rebar | Advanced Smelting | **1.10** | **1.23** | **1.29** |
| Worldly Donut | Baking | **3.45** | **3.97** | **4.17** |
| Smooth Gut Noodle Roll | Cooking | **3.75** | **4.32** | **4.54** |
| Boiled Sausage | Advanced Cooking | **3.90** | — | — |

For foods above, the normal calorie floor was checked; recipe cost controls these three supporting values.

## Source-confirmed paper inventory

The supplied Core contains **19 named Research Paper item classes** through Modern:

- Agriculture: Basic, Advanced, Modern;
- Culinary: Basic, Advanced, Modern;
- Dendrology: Basic, Advanced, Modern;
- Engineering: Advanced, Modern;
- Gathering: Basic, Advanced;
- Geology: Basic, Advanced, Modern;
- Metallurgy: Basic, Advanced, Modern.

Alternative Core recipe families also exist for:

- Culinary Basic via Dried Fish;
- Culinary Basic via Dried Meat;
- Culinary Advanced via the Baking/meat route;
- Dendrology Advanced via Wooden Hull Planks;
- Geology Modern via Glass.

The tables above use the cheapest legitimate route under the stated Ironwood pricing assumptions.

## Market policy

Recommended Library treatment:

1. publish the **Projected Cost** so contributors can see the production burden;
2. use the listed Town Buy as the default **capped procurement** reward;
3. procure only the number of papers needed for an active research project plus a small replacement reserve;
4. Town Sell is a fallback/reference value for surplus paper, not a reason for the Library to accumulate infinite stock;
5. scroll and skill-book pricing remains a separate layer and should use these paper prices as its research inputs.
