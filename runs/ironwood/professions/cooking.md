# Ironwood Cooking — Current Mid-Tier Food Table

Rebuilt from Eco 14 Core using current Gathering, Milling, Butchery and Baking inputs.

Cooking food uses the higher of its calorie floor or Exchange-sourced recipe cost plus a modest food-specialist margin. Cast Iron Stove fuel is included at 10 W.

Many Cooking items have several biome-specific recipes that produce the same final item. Ironwood uses the **least-cost legitimate current recipe** as the structural price setter. More expensive alternate recipes remain useful when local ingredients differ but do not force the central market to pay the inefficient route's cost.

## Cooking 1 staples

| Item | Calories | Structural recipe cash cost | Town Buys | Town Sells |
|---|---:|---:|---:|---:|
| Basic Salad | 800 | 1.969 | **2.32** | **2.44** |
| Fruit Salad | 900 | 2.577 | **3.04** | **3.19** |
| Vegetable Medley | 900 | 1.965 | **2.32** | **2.44** |
| Rice Noodles | 200 | 0.674 | **0.80** | **0.84** |

Current controlling routes:

- Basic Salad: Exotic Salad is cheapest among the current salad variants;
- Fruit Salad: Mixed Fruit Salad is cheapest;
- Vegetable Medley: Mixed Vegetable Medley is cheapest.

Forest/Grassland/Rainforest/Exotic variants can cost more and are resource-substitution recipes rather than separate market items.

## Cooking 2

| Item | Calories | Cash cost | Town Buys | Town Sells |
|---|---:|---:|---:|---:|
| Autumn Stew | 1,200 | 1.262 | **1.51** | **1.59** |
| Meat Stock | 600 | 0.684 ea | **0.82** | **0.86** |
| Shark Fillet Soup | 1,400 | 2.047 | **2.46** | **2.58** |
| Simmered Meat | 900 | 1.726 | **2.07** | **2.17** |

Meat Stock can also be made from fish later; the Scrap Meat route is slightly cheaper and therefore controls the current structural price.

## Cooking 3

| Item | Calories | Cash cost | Town Buys | Town Sells |
|---|---:|---:|---:|---:|
| Crispy Bacon | 800 | 0.763 net | **0.92** | **0.97** |
| Taro Fries | 600 | 1.444 | **1.73** | **1.82** |
| Vegetable Stock | 700 | 1.787 ea | **2.14** | **2.25** |
| Vegetable Soup | 1,200 | 3.410 | **4.09** | **4.29** |

Crispy Bacon produces **2 Tallow** as a byproduct. Its net cash cost credits those outputs at the canonical Tallow Town Buy value.

## Cooking 4–6

| Item | Level | Calories | Cash cost | Town Buys | Town Sells |
|---|---:|---:|---:|---:|---:|
| Mochi | 4 | 750 | 3.343 | **4.01** | **4.21** |
| Pupusas | 4 | 900 | 8.945 | **10.73** | **11.27** |
| Smooth Gut Noodle Roll | 4 | 1,200 | 4.512 | **5.41** | **5.68** |
| Clam Chowder | 5 | 800 | 0.590 | **0.80** | **0.84** |
| Loaded Taro Fries | 5 | 1,200 | 7.670 | **9.20** | **9.66** |
| Phad Thai | 6 | 1,200 | 4.390 | **5.27** | **5.53** |

## Sun Cheese dependency

Current Milling 3 Sun Cheese uses Sunflower Seed, Yeast, Rice and Oil. Expensive early Yeast makes it a high-value ingredient:

**Sun Cheese: 4.57 Town Buy / 4.80 Town Sell.**

That is why Pupusas and Loaded Taro Fries are expensive in the current Huckleberry-Sugar era.

## Sugar-era warning

Mochi, Phad Thai and several cheese/baking dependencies currently inherit **early Sugar/Yeast** prices. When Beet Sugar becomes the broad Milling supply, these recipes must be recalculated as an economy-wide technology transition.

## Food-market interpretation

The prepared-food table intentionally has two behaviors:

- simple calorie-rich foods often sit close to the 1 credit / 1,000 calorie anchor;
- nutrition-dense or deeply processed meals can cost several credits because they consume several specialist inputs.

This gives cooks a recurring commercial outlet without forcing every citizen to buy expensive advanced meals merely to avoid starvation. Campfire staples remain the public fallback.

Research papers, skill books and Cooking Upgrade remain under the separate research-economy policy.
