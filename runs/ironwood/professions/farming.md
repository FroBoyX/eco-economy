# Ironwood Farming — Crop and Seed Foundation

Derived from the supplied Eco 14 Core using the current Gathering crop anchors.

Farming itself does not create a separate permanent markup on harvested crops. Harvested crops remain Depth-0/gathered anchors because the farm converts land, time and seed into new raw supply rather than buying a deep manufactured input chain.

Farming's direct priced outputs are primarily **seed recipes and farm objects**.

## Farming 1 seed economics

Farming 1 uses the 0.80 recipe/labor multiplier. Most crop seed recipes convert harvested crop back into a larger fixed number of seeds, making seed value derive naturally from the crop rather than requiring arbitrary seed anchors.

Town Buy below uses a shallow ~10% specialist margin over Exchange-sourced crop input cost at Farming 1.

| Seed / Spore | Source crop | Town Buys | Town Sells |
|---|---|---:|---:|
| Agave Seed | Agave Leaves | **0.13** | **0.14** |
| Amanita Mushroom Spores | Amanita Mushrooms | **0.04** | **0.05** |
| Beet Seed | Beet | **0.15** | **0.16** |
| Bolete Mushroom Spores | Bolete Mushrooms | **0.13** | **0.14** |
| Cookeina Mushroom Spores | Cookeina Mushrooms | **0.13** | **0.14** |
| Corn Seed | Corn | **0.15** | **0.16** |
| Cotton Seed | Cotton Boll | **0.14** | **0.15** |
| Creosote Bush Seed | Creosote Flower | **0.03** | **0.04** |
| Crimini Mushroom Spores | Crimini Mushrooms | **0.13** | **0.14** |
| Daisy Seed | Daisy | **0.03** | **0.04** |
| Fern Spore | Fiddleheads | **0.10** | **0.11** |
| Fireweed Seed | Fireweed Shoots | **0.10** | **0.11** |
| **Flax Seed** | **Flax Stem** | **0.04** | **0.05** |
| Huckleberry Seed | Huckleberries | **0.20** | **0.21** |
| Orchid Seed | Orchid | **0.03** | **0.04** |
| Papaya Seed | Papaya | **0.26** | **0.27** |
| Pineapple Seed | Pineapple | **0.13** | **0.14** |
| Prickly Pear Seed | Prickly Pear Fruit | **0.24** | **0.25** |
| Pumpkin Seed | Pumpkin | **0.22** | **0.23** |
| Rose Seed | Rose | **0.03** | **0.04** |
| Sunflower Seed | Sunflower | **0.03** | **0.04** |
| Taro Seed | Taro Root | **0.16** | **0.17** |
| Tomato Seed | Tomato | **0.30** | **0.32** |
| Trillium Seed | Trillium Flower | **0.03** | **0.04** |
| Tulip Seed | Tulip | **0.03** | **0.04** |
| Wheat Seed | Wheat | **0.06** | **0.07** |

## Flax Seed correction

Core Farming 1 recipe:

- 2 Flax Stems
- 60 calories
- output 6 Flax Seeds

At Farming 1:

- 1.6 Flax Stems × 0.11 Exchange Sell = 0.176
- 48 calories = 0.048
- total cash cost = 0.224
- cost/seed ≈ 0.037

**Flax Seed: 0.04 Town Buy / 0.05 Town Sell.**

This supersedes the provisional 0.10/0.11 seed assumption that had been used only to unblock Lumber discovery.

## Farming and Gathering relationship

Farmed plants are still harvested through Gathering. Common crop items in current Core use a Gathering yield progression from 1.0× at level 0 to 2.0× at level 7.

That means a dedicated farmer/gatherer earns additional profit through physical yield rather than through a continuously increasing government crop price.

## Farm objects and research

Scarecrow, Carved Pumpkin, Tallow Candle, Salt Basket, Garden Pond, Farming Upgrade and research outputs will be priced with the full profession output pass. The crop/seed table is canonical now because it is required by Milling, Tailoring, food and Engineering dependencies.
