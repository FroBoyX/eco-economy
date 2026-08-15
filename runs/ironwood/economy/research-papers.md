# Ironwood Research Papers — Basic through Modern

Source: supplied Eco 14 Core (`Eco14-Core(3).zip`) plus the current Ironwood Steam-entry price ledger.

This is a **research projection lane** built on the current Ironwood economy. Current progression materials use current-era routes where they exist; genuinely later Modern-support materials are projected only far enough to calculate research-paper economics and do **not** become current Steam-era Exchange price setters.

## Naming and producer map

Eco uses two related naming systems here:

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

## Final pricing rule

Research papers use the same integrated-specialty accounting as the rest of Ironwood:

- same-specialty crafted components enter at **Projected Cost**;
- cross-specialty inputs enter at **Town Sell**;
- same-specialty raw anchors enter at Town Buy/opportunity value;
- skill-based ingredient and labor reductions are evaluated at the recipe's minimum required skill;
- prior-tier papers enter the next tier at their Town Sell price when the producing specialty changes;
- labor remains **1 credit / 1,000 calories**.

Research papers are themselves **intermediate knowledge goods** used by later books rather than terminal goods. Their tier already appears in Projected Cost through deeper and more expensive ingredients. Ironwood therefore does **not** apply an additional escalating Basic/Advanced/Modern percentage.

**Canonical research procurement premium: 20% over Projected Cost for every research paper.**

`Town Buy = Projected Cost × 1.20`

Town Sell then uses Ironwood's ordinary Exchange spread.

Library demand remains **quantity-capped civic procurement**, not an unlimited government buy order.

## Basic Research Papers

| Research Paper | Producing Specialty / Cheapest Route | Projected Cost | Town Buys | Town Sells |
|---|---|---:|---:|---:|
| Agriculture Research Paper Basic | Farming 1 | **2.79** | **3.35** | **3.52** |
| Culinary Research Paper Basic | Campfire Cooking route | **1.03** | **1.24** | **1.30** |
| Dendrology Research Paper Basic | Logging 1 | **6.42** | **7.71** | **8.10** |
| Gathering Research Paper Basic | Gathering 1 | **1.46** | **1.76** | **1.85** |
| Geology Research Paper Basic | Mining 1 | **2.42** | **2.91** | **3.06** |
| Metallurgy Research Paper Basic | Smelting 1 | **6.23** | **7.48** | **7.85** |

### Basic cost notes

- **Agriculture Basic:** Farming 1; 5 Dirt, 3 Crushed Limestone, 10 `Raw Food`, 10 `Crop Seed`, 30 calories. Cheapest current Raw Food opportunity value is **0.10**. Sunflower Seed is the cheapest Farming-produced Crop Seed route at about **0.021 projected cost each**. Crushed Limestone crosses from Mining at Town Sell.
- **Culinary Basic:** the Campfire Cooking route is cheapest. The lowest current `FriedVegetable` is Fried Hearts of Palm at about **0.167 projected cost** and the lowest `CampfireSalad` is Beet Campfire Salad at about **0.38 projected cost**. The Dried Fish and Dried Meat Hunting routes are more expensive.
- **Dendrology Basic:** Logging 1; 20 Wood plus 30 calories. Wood is carried at its **0.40** Logging opportunity value.
- **Gathering Basic:** cheapest current `Raw Food` opportunity value is **0.10** and Kelp supplies `NaturalFiber` at **0.03** opportunity value.
- **Geology Basic:** 30 Rock plus labor, with Rock carried at the **0.10** Mining raw anchor.
- **Metallurgy Basic:** Iron Bar is the cheapest current `Metal` and Crushed Mixed Rock is the cheapest normal `CrushedRock` market input.

## Advanced Research Papers

| Research Paper | Producing Specialty / Cheapest Route | Projected Cost | Town Buys | Town Sells |
|---|---|---:|---:|---:|
| Agriculture Research Paper Advanced | Fertilizers 1 | **24.74** | **29.68** | **31.16** |
| Culinary Research Paper Advanced | Baking meat route | **19.71** | **23.65** | **24.83** |
| Dendrology Research Paper Advanced | Shipwright hull-plank route | **15.88** | **19.05** | **20.00** |
| Engineering Research Paper Advanced | **Basic Engineering 1** | **29.44** | **35.33** | **37.10** |
| Gathering Research Paper Advanced | Tailoring 1 | **5.02** | **6.02** | **6.32** |
| Geology Research Paper Advanced | Masonry 1 | **6.90** | **8.28** | **8.69** |
| Metallurgy Research Paper Advanced | Blacksmith 1 | **20.15** | **24.18** | **25.39** |

### Advanced cost notes

- **Agriculture Advanced:** five Berry Extract Fertilizer are carried at Fertilizers' internal Projected Cost; Fur Pelt and Leather Hide cross from Butchery. Spoiled Food is assigned **0 acquisition cost** rather than assuming a speculative waste subsidy. The Basic Agriculture paper enters at Library Town Sell.
- **Culinary Advanced:** the alternate Baking route is cheaper than the Cooking route. Baked Meat is a same-Baking component at Projected Cost; Simmered Meat and Cooking Utensils cross specialty boundaries; the Basic Culinary paper enters at Library Town Sell.
- **Dendrology Advanced:** the Shipwright Wooden Hull Planks route is cheaper than the Carpentry/Hewn Log route under the integrated-workshop rule.
- **Engineering Advanced:** Waterwheel, Windmill and Wooden Gear are all Basic Engineering outputs and therefore enter at their internal Projected Costs.
- **Gathering Advanced:** Linen Fabric is the cheapest current `Fabric` and is carried at Tailoring's Projected Cost.
- **Geology Advanced:** Mortared Stone is a same-Masonry component at Projected Cost.
- **Metallurgy Advanced:** Iron Plate, Copper Plate and Nails are same-Blacksmith components at Projected Cost.

## Modern Research Papers

| Research Paper | Producing Specialty / Cheapest Route | Projected Cost | Town Buys | Town Sells |
|---|---|---:|---:|---:|
| Agriculture Research Paper Modern | Oil Drilling 1 | **56.25** | **67.50** | **70.88** |
| Culinary Research Paper Modern | Advanced Cooking 2 | **57.02** | **68.42** | **71.84** |
| Dendrology Research Paper Modern | Paper Milling 1 | **44.15** | **52.98** | **55.63** |
| Engineering Research Paper Modern | Mechanics 1 | **62.72** | **75.26** | **79.02** |
| Geology Research Paper Modern | Pottery / Brick route | **23.66** | **28.39** | **29.81** |
| Metallurgy Research Paper Modern | Advanced Smelting 1 | **74.04** | **88.84** | **93.28** |

### Modern cost notes

- **Agriculture Modern:** Sulfuric Acid, Phosphate Fertilizer and Compost Fertilizer cross specialty boundaries. Bio Residue is assigned **0 acquisition cost**. Ink, Paper and the Advanced Agriculture paper enter at their applicable market values.
- **Culinary Modern:** Boiled Sausage is an Advanced Cooking internal component; Bread, Worldly Donut and Smooth Gut Noodle Roll cross from Baking/Cooking; Ink, Paper and the Advanced Culinary paper are full-count inputs.
- **Dendrology Modern:** Paraffin is **not** Oil-gated. Core's Milling 4 recipe named `Wax` converts Bean Paste into Paraffin at the Mill. Paper Milling 2 then makes Waxed Paper on the Small Paper Machine. Waxed Paper and Paper are Paper Milling internal components and therefore use Projected Cost; Lumber and Ink cross specialties; the Advanced Dendrology paper enters at Town Sell.
- **Engineering Modern:** Iron Axle and Iron Gear are Mechanics internal components at Projected Cost; Lubricant, Ink, Paper and the Advanced Engineering paper cross specialty boundaries.
- **Geology Modern:** the Pottery/Brick route remains cheaper than the Glassworking/Glass route because Brick is a Pottery internal component and therefore uses its **0.574 projected cost**, not the **1.20 / 1.25** direct-sale bulk policy price.
- **Metallurgy Modern:** Rebar and Steel Bar are Advanced Smelting internal components and therefore do not recursively carry their own sale markups.

## Current progression-support materials used by Modern research

These are current Steam-era commodities because their actual Core routes are available in current specialties/workstations.

| Supporting item | Current route | Projected Cost | Town Buy | Town Sell |
|---|---|---:|---:|---:|
| Paraffin | Milling 4 `Wax`: Bean Paste → Paraffin at Mill | **0.49** | **0.55** | **0.58** |
| Waxed Paper | Paper Milling 2 at Small Paper Machine | **0.36** | **0.42** | **0.44** |

Oil Drilling later provides an alternate Paraffin route and may justify a future structural reprice, but it does not erase the current Milling progression route.

## Future-support projections used only for Modern research

These support the remaining Modern-paper calculations only. They are **not current Steam-era Exchange price setters** unless/until their technology becomes normal in the run.

| Supporting item | Producing Specialty | Projected Cost | Reference Buy | Reference Sell |
|---|---|---:|---:|---:|
| Barrel | Advanced Smelting | **1.87** | **2.15** | **2.26** |
| Sulfuric Acid | Recycling | **0.38** | **0.44** | **0.46** |
| Petroleum | Oil Drilling | **2.31** | **2.58** | **2.71** |
| Ceramic Mold | Pottery | **0.05** | **0.05** | **0.06** |
| Steel Bar — charcoal route | Advanced Smelting | **4.41** | **5.07** | **5.32** |
| Rebar | Advanced Smelting | **1.11** | **1.24** | **1.30** |
| Worldly Donut | Baking | **3.45** | **3.97** | **4.17** |
| Smooth Gut Noodle Roll | Cooking | **3.75** | **4.32** | **4.54** |
| Boiled Sausage | Advanced Cooking | **3.90** | **4.49** | **4.71** |

The Steel projection uses the current Ironwood Charcoal baseline. If Ironwood deliberately reprices Charcoal, the future Metallurgy Modern projection should be recalculated; this does not alter the current Steam-era economy until that transition is adopted.

## Source-confirmed paper inventory

The supplied Eco 14 Core contains **19 named Research Paper item classes** through Modern:

- Agriculture: Basic, Advanced, Modern;
- Culinary: Basic, Advanced, Modern;
- Dendrology: Basic, Advanced, Modern;
- Engineering: Advanced, Modern;
- Gathering: Basic, Advanced;
- Geology: Basic, Advanced, Modern;
- Metallurgy: Basic, Advanced, Modern.

Alternative Core recipe families also exist for Culinary Basic via Dried Fish, Culinary Basic via Dried Meat, Culinary Advanced via the Baking/meat route, Dendrology Advanced via Wooden Hull Planks, and Geology Modern via Glass. The final tables use the cheapest legitimate route under Ironwood's established component-cost rules.

## Library policy

1. The listed **Projected Cost** is the production baseline.
2. **Town Buy = Projected Cost + 20%** is the default capped research reward.
3. Procure only the quantity required for an active research project plus a small replacement reserve.
4. Town Sell is a fallback/reference price for surplus papers, not a reason for the Library to accumulate unlimited inventory.
5. Skill books and scrolls are a separate pricing layer and should use these paper prices as their research inputs.
