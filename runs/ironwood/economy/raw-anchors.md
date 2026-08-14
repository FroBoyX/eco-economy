# Ironwood Raw Commodity Anchors

These are the first ground-up commodity anchors for the current Ironwood rebuild.

They are intentionally limited to resources that enter the economy through harvesting, digging, mining, or gathering rather than through a priced profession recipe.

All downstream processed goods should be derived from these values and Eco 14 Core recipes.

## Public Exchange convention

For these foundational commodities:

- **Buy** is the value paid by the Ironwood Exchange to a player supplying the resource.
- **Sell** is the Exchange resale/import price to a player consuming the resource.
- the spread is deliberately shallow and exists for liquidity and anti-cycling rather than profit maximization;
- downstream recipe calculations use the producer/input value appropriate to real player trade, not an arbitrary high government markup.

## Phase-one industrial anchors

| Resource | Exchange buys | Exchange sells | Role |
|---|---:|---:|---|
| Permitted Logs / `Wood` | 0.40 | 0.45 | Core Logging input. Higher than ordinary stone because cutting, hauling, regrowth, and forestry participation should remain worthwhile. |
| Basalt | 0.15 | 0.17 | Ordinary rock family. |
| Gneiss | 0.15 | 0.17 | Ordinary rock family. |
| Granite | 0.15 | 0.17 | Ordinary rock family. |
| Sandstone | 0.15 | 0.17 | Ordinary rock family. |
| Shale | 0.15 | 0.17 | Ordinary rock family. |
| Stone / generic rock | 0.15 | 0.17 | Ordinary rock family. |
| Limestone | 0.20 | 0.23 | Strategic mineral with dedicated downstream quicklime/cement/steel use; kept distinct from ordinary rock. |
| Clay | 0.15 | 0.17 | Shovel-extracted foundational masonry, mold, and ceramic input. |
| Sand | 0.15 | 0.17 | High-quality construction/glass sand; Core explicitly describes it as sought after rather than treating all desert sand as equivalent. |
| Peat | 0.10 | 0.12 | Early gathered fuel/charcoal feedstock; deliberately below logs. |
| Coal | 0.20 | 0.23 | Fuel and advanced industrial feedstock. |
| Sulfur | 0.20 | 0.23 | Chemical/explosive industrial feedstock. |
| Iron Ore | 0.30 | 0.34 | Foundational metal ore. Chosen to keep the early Mining→Smelting chain valuable without forcing inflated tool prices. |
| Copper Ore | 0.35 | 0.40 | Later metal ore with a somewhat higher extraction/scarcity premium and less favorable processing ratios than iron. |
| Gold Ore | 0.40 | 0.45 | Scarce ore. The Core processing chain already gives gold a much poorer ore-to-bar conversion, so the raw premium remains moderate rather than extreme. |
| Plant Fibers | 0.10 | 0.12 | Generic gathered natural-fiber input. |
| Kelp | 0.15 | 0.17 | Gathered marine input used in both production and food chains; kept above generic fiber because it requires a distinct gathering environment. |

## Not anchored here

The following should **not** be assigned arbitrary values in this sheet:

- Boards, Hewn Logs, Lumber and Charcoal — Logging outputs;
- Crushed ores, concentrates and bars — Mining/Smelting outputs;
- Mortar, bricks, quicklime and glass — processing outputs;
- Flax Stem, Cotton Boll, crops and cultivated seeds — Farming/Gathering progression requiring a dedicated agriculture table;
- carcasses, raw meat, hides and fish — Hunting/Fishing chains;
- petroleum and late industrial resources — price when the relevant progression chain is built;
- garbage and scrap — value through the Recycling/disposal model;
- Dirt and Water — no default central commodity market unless a concrete server need appears.

## Sanity checks these anchors must pass

The anchors are retained only if the profession tables built from Core remain coherent. In particular:

1. Logging 1 should profit slightly on Boards at base recipe efficiency.
2. Mining should profit on crushing/concentrating rather than having raw ore capture all value.
3. Smelting should profit on bars without making iron tools unaffordable.
4. Copper and Gold should become more valuable substantially through their worse processing ratios, not only by assigning huge raw-ore premiums.
5. Limestone should support Quicklime and later steel/glass without overwhelming those prices.
6. Coal and Peat should not create a trivial infinite-profit charcoal path.
7. Recycling outputs must later be priced against these virgin-resource values rather than independently.

If one of those tests fails, change the anchor directly and propagate the correction. Do not preserve it for continuity.
