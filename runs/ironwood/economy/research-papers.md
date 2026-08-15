# Ironwood Research Papers — Basic through Modern

Source: supplied Eco 14 Core plus the current Ironwood Steam-entry price baselines.

Research papers are a **capped Library procurement** lane. They use the same integrated-specialty accounting as the rest of Ironwood, with one explicit exception for research recipes that destroy commercially useful finished capital.

## Core paper families and producers

| Research family | Basic producer | Advanced producer | Modern producer |
|---|---|---|---|
| Agriculture | Farming | Fertilizers | Oil Drilling |
| Culinary | Campfire Cooking | Baking / Cooking alternate routes | Advanced Cooking |
| Dendrology | Logging | Shipwright / Carpentry alternate routes | Paper Milling |
| Engineering | — | **Basic Engineering** | Mechanics |
| Gathering | Gathering | Tailoring | — |
| Geology | Mining | Masonry | Pottery / Glassworking alternate routes |
| Metallurgy | Smelting | Blacksmith | Advanced Smelting |

There is **no Engineering Research Paper Basic** and **no Gathering Research Paper Modern** in the supplied Core.

## Research pricing rule

Ordinary research papers use:

- same-specialty crafted inputs at **Projected Cost**;
- cross-specialty inputs at **Town Sell**;
- same-specialty raw anchors at Town Buy/opportunity value;
- minimum-unlock skill resource/labor multipliers;
- labor at 1 credit / 1,000 calories;
- **Town Buy = Projected Cost + 20%**;
- normal Exchange spread for Town Sell.

Library buy orders should be quantity-capped to active research demand plus a small reserve.

### Capital-sacrifice research exception

When a research recipe destroys commercially useful finished capital rather than ordinary workshop components, Ironwood values that sacrificed capital at its producer-facing opportunity value instead of pretending it only cost raw internal components.

This applies to **Engineering Research Paper Advanced**, which consumes a Waterwheel, Windmill, and Wooden Gears. Its agreed Library procurement value is **45.00**. That 45.00 research transfer value is also the Advanced-paper input used when calculating Engineering Research Paper Modern.

## Basic Research Papers

| Research Paper | Producing Specialty | Projected Cost | Town Buys | Town Sells |
|---|---|---:|---:|---:|
| Agriculture Research Paper Basic | Farming | **2.79** | **3.35** | **3.52** |
| Culinary Research Paper Basic | Campfire Cooking | **1.03** | **1.24** | **1.30** |
| Dendrology Research Paper Basic | Logging | **6.42** | **7.71** | **8.10** |
| Gathering Research Paper Basic | Gathering | **1.46** | **1.76** | **1.85** |
| Geology Research Paper Basic | Mining | **2.42** | **2.91** | **3.06** |
| Metallurgy Research Paper Basic | Smelting | **6.23** | **7.48** | **7.85** |

## Advanced Research Papers

| Research Paper | Producing Specialty / route | Projected / Opportunity Cost | Town Buys | Town Sells |
|---|---|---:|---:|---:|
| Agriculture Research Paper Advanced | Fertilizers | **24.74** | **29.68** | **31.16** |
| Culinary Research Paper Advanced | Baking meat route | **19.71** | **23.65** | **24.83** |
| Dendrology Research Paper Advanced | Shipwright hull-plank route | **15.88** | **19.05** | **20.00** |
| Engineering Research Paper Advanced | **Basic Engineering** | **37.45** | **45.00** | **47.25** |
| Gathering Research Paper Advanced | Tailoring | **5.02** | **6.02** | **6.32** |
| Geology Research Paper Advanced | Masonry | **6.90** | **8.28** | **8.69** |
| Metallurgy Research Paper Advanced | Blacksmith | **20.15** | **24.18** | **25.39** |

## Modern Research Papers

| Research Paper | Producing Specialty / route | Projected Cost | Town Buys | Town Sells |
|---|---|---:|---:|---:|
| Agriculture Research Paper Modern | Oil Drilling | **56.25** | **67.50** | **70.88** |
| Culinary Research Paper Modern | Advanced Cooking | **57.02** | **68.42** | **71.84** |
| Dendrology Research Paper Modern | Paper Milling | **44.15** | **52.98** | **55.63** |
| Engineering Research Paper Modern | Mechanics | **70.60** | **84.72** | **88.95** |
| Geology Research Paper Modern | Pottery / Brick route | **23.66** | **28.39** | **29.81** |
| Metallurgy Research Paper Modern | Advanced Smelting | **74.04** | **88.84** | **93.28** |

## Current Paraffin / Waxed Paper correction

Paraffin is **not Oil-gated**. The current progression route is the Milling 4 Core recipe named **`Wax`**:

- Bean Paste → Paraffin at the Mill;
- Paraffin: **0.49 projected / 0.55 Buy / 0.58 Sell**.

Paper Milling 2 then uses Paraffin to make Waxed Paper at the Small Paper Machine:

- Waxed Paper: **0.36 projected / 0.42 Buy / 0.44 Sell**.

This current route is used in Dendrology Research Paper Modern. Oil Drilling later provides a cheaper alternate Paraffin route and may justify a future structural reprice.

## Engineering Advanced policy basis

The Core Engineering Advanced recipe consumes:

- 1 Waterwheel;
- 1 Windmill;
- 2 Wooden Gears;
- 120 calories;
- produced by Basic Engineering 1.

Pure same-specialty internal accounting undervalues the recipe because it treats the destroyed Waterwheel and Windmill like anonymous subcomponents. Ironwood therefore uses the capital-sacrifice exception above. The resulting policy target is **45.00 Town Buy** rather than the former 35.33 value.

Engineering Modern is recalculated using **45.00** as the Advanced Engineering paper input, giving **70.60 projected / 84.72 Buy / 88.95 Sell**.

## Modern-only support projections

The following remain projections used only where Modern research requires them; they do not become current Steam Exchange price setters until the relevant technology is normal in the run:

| Supporting item | Projected Cost | Reference Buy | Reference Sell |
|---|---:|---:|---:|
| Barrel | **1.87** | **2.15** | **2.26** |
| Sulfuric Acid | **0.38** | **0.44** | **0.46** |
| Petroleum | **2.31** | **2.58** | **2.71** |
| Ceramic Mold | **0.05** | **0.05** | **0.06** |
| Steel Bar — charcoal route | **4.41** | **5.07** | **5.32** |
| Rebar | **1.11** | **1.24** | **1.30** |
| Worldly Donut | **3.45** | **3.97** | **4.17** |
| Smooth Gut Noodle Roll | **3.75** | **4.32** | **4.54** |
| Boiled Sausage | **3.90** | **4.49** | **4.71** |

## Library treatment

1. Publish Projected/Opportunity Cost so contributors can see the burden of the recipe.
2. Use the listed Town Buy as the capped Library procurement reward.
3. Procure only what an active research project needs plus a small reserve.
4. Town Sell is fallback/reference supply, not a reason to accumulate unlimited research stock.
5. Skill-book and scroll access remains a separate policy layer.
