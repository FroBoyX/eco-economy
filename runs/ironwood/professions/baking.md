# Ironwood Baking — Current Steam-Era Food Table

Rebuilt from Eco 14 Core using current crop, Milling, Butchery and Campfire prices.

Baking is now operational in the run. The ordinary recipe audit is complete by **distinct market output**: all current Baking food/intermediate outputs represented by the Core-derived recipe pass are priced below. Recipes that create an already-priced output, such as `Melting Fat -> Tallow`, are documented without fabricating a duplicate market item. Specialty-module/upgrade craftables are limited capital rather than ordinary food inventory and remain in the upgrade/research lane.

Baked food uses the higher of the calorie floor or Exchange-sourced recipe cost plus a modest food-specialist margin. Bakery Oven fuel is included at 10 W using current Charcoal value.

## Important current-era dependency: Yeast

Current Milling 4 Yeast recipe:

- 2 Sugar
- 15 calories
- -> 1 Yeast

At Milling 4 and current **early Huckleberry Sugar 1.16 / 1.22**, Yeast costs about 1.596 to make from public inputs.

**Yeast: 1.84 Town Buy / 1.93 Town Sell.**

This makes early dough and bread expensive. When Beet Sugar becomes the normal economy-wide Sugar route, Yeast/Bread should undergo a structural repricing.

## Basic baked foods — Baking 1

| Item | Calories | Cash cost | Town Buys | Town Sells |
|---|---:|---:|---:|---:|
| Baked Agave | 700 | 0.754 | **0.89** | **0.93** |
| Baked Beet | 700 | 0.850 | **1.00** | **1.05** |
| Baked Corn | 700 | 0.850 | **1.00** | **1.05** |
| Baked Heart of Palm | 700 | 0.434 | **0.70** | **0.74** |
| Baked Meat | 700 | 0.514 | **0.70** | **0.74** |
| Baked Taro | 700 | 0.914 | **1.08** | **1.13** |
| Baked Tomato | 700 | 0.882 | **1.04** | **1.09** |
| Camas Bulb Bake | 700 | 0.594 | **0.70** | **0.74** |
| Flatbread | 500 | 0.882 | **1.04** | **1.09** |
| Leavened Dough | 10 | 2.376 | **2.80** | **2.94** |
| Pastry Dough | 10 | 2.312 | **2.73** | **2.87** |

The dough items are industrial food intermediates rather than meaningful calorie purchases; their value is controlled by expensive early Yeast rather than their own calories.

## Baking 2–5 outputs

| Item | Level | Calories | Cash cost | Town Buys | Town Sells |
|---|---:|---:|---:|---:|---:|
| Fruit Muffin | 2 | 800 | 1.157 | **1.39** | **1.46** |
| Baked Roast | 3 | 1,000 | 0.513 | **1.00** | **1.05** |
| Roast Pumpkin | 3 | 1,400 | 2.284 | **2.74** | **2.88** |
| Bread | 4 | 750 | 3.914 | **4.70** | **4.94** |
| Worldly Donut | 4 | 750 | 4.091 | **4.91** | **5.16** |
| Camas Bread | 5 | 800 | 2.203 | **2.64** | **2.77** |
| Huckleberry Fritter | 5 | 900 | 7.268 | **8.72** | **9.16** |
| Huckleberry Pie | 5 | 1,300 | 1.874 | **2.25** | **2.36** |
| Meat Pie | 5 | 1,300 | 1.634 | **1.96** | **2.06** |

## Melting Fat — Baking 2

Core:

- 6 Scrap Meat
- 15 calories
- -> 5 Tallow

At Baking 2 this is an especially efficient fat-rendering route. It reinforces the canonical **Tallow 0.20 / 0.21** price and confirms that Tallow cannot safely remain near the old provisional 0.50 value.

This route intentionally creates substantial value from Scrap Meat; cooking in Eco increases usable food energy dramatically. The Exchange should not raise Tallow above its calorie floor merely because it also has industrial uses.

## Recipe coverage status

The current ordinary Baking market therefore contains **20 distinct Baking food/intermediate outputs**, plus the Melting Fat route into the already-canonical Tallow market. Equivalent-output recipes are not duplicated as separate Exchange rows.

Specialty module/upgrade craftables are limited capital and are intentionally not treated as an unlimited food import merely because Baking can craft them.

## Structural Sugar transition

The current table reflects early Huckleberry Sugar at **1.16 / 1.22**. Milling 6 Beet Sugar can support roughly **0.32 / 0.34** Sugar.

Once Beet Sugar is broadly available, Ironwood should recalculate at least:

- Yeast;
- Leavened Dough;
- Pastry Dough;
- Bread;
- Roast Pumpkin;
- Worldly Donut;
- Huckleberry Fritter;
- downstream Cooking recipes using Sugar.

That is an economy-wide technology transition, not a personal-efficiency discount.

Research, skill-book, scroll and limited specialty-module procurement remain under their separate policy lanes.
