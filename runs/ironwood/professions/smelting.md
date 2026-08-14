# Ironwood Smelting Prices

Ground-up Smelting table derived from the rebuilt Mining outputs, Logging inputs, initial garbage-disposal schedule, and Eco 14 Core.

## Cross-profession inputs established here

### Clay Mold — Gathering 1

Core: 1 Clay + 50 calories → 4 Clay Molds.

- Clay consumer cost: 0.17
- labor: 0.05
- craft cost: 0.22
- cost per mold: 0.055
- **Exchange buys: 0.06**
- **Exchange sells: 0.07**

This should later appear in the Gathering table but is established now because every base metal bar depends on it.

### Slag

Slag is a normal Smelting byproduct tagged as a waste product, not a GarbageMaterial. Core describes Crushed Slag as a later concrete input.

Current modest commodity value:

- **Exchange buys: 0.05**
- **Exchange sells: 0.08**

This gives Smelting a small byproduct credit without pretending slag is a premium product.

## Garbage cost used by Smelting

Current Ceramic Scrap disposal charge: **0.15 per unit**.

The Bloomery metal recipes generate 1.5 Ceramic Scrap per craft, adding **0.225** to craft cost. The later Blast Furnace versions generate only 0.2 Ceramic Scrap, making cleaner infrastructure economically better as well as more resource-efficient.

## Metal bars

The early **Bloomery** recipe sets the fixed bar price. Later Blast Furnace recipes retain the same output price and create progression margin.

| Output | Bloomery Core recipe | Inputs + labor + disposal - slag credit | Cost / bar | Exchange buys | Exchange sells |
|---|---|---:|---:|---:|---:|
| **Iron Bar** | 2 Iron Concentrate + 2 Clay Molds + 60 cal → 6 Bars + 2 Slag; 1.5 Ceramic Scrap | 13.325 | 2.221 | **2.45** | **2.75** |
| **Copper Bar** | 2 Copper Concentrate + 2 Clay Molds + 60 cal → 6 Bars + 2 Slag; 1.5 Ceramic Scrap | 24.725 | 4.121 | **4.55** | **5.10** |
| **Gold Bar** | 2 Gold Concentrate + 2 Clay Molds + 60 cal → 3 Bars + 2 Slag; 1.5 Ceramic Scrap | 40.925 | 13.642 | **15.00** | **16.80** |

### Blast Furnace progression check

At the same fixed bar prices, the later Blast Furnace recipes are far cheaper per bar:

- Iron: about 1.65 base cost/bar before further skill effects;
- Copper: about 3.08 base cost/bar;
- Gold: about 10.21 base cost/bar.

That increased margin is intentional progression profit, not a reason to lower bar prices.

## Other Smelting products priced now

| Product | Core basis | Conservative cost | Exchange buys | Exchange sells |
|---|---|---:|---:|---:|
| Iron Pipe | 1 Iron Bar + 15 cal | 2.765 | **3.05** | **3.42** |
| Copper Pipe | 1 Copper Bar + 15 cal | 5.115 | **5.65** | **6.33** |
| Anvil | 12 Iron Bars + 10 Hewn Logs + 180 cal | 46.68 | **51.35** | **57.50** |
| Cast Iron Plaque | 4 Iron Concentrate + 80 cal | 26.08 | **28.70** | **32.15** |
| Cast Iron Chair | 4 Iron Bars + 1 Clay Mold + 60 cal | 11.13 | **12.25** | **13.72** |
| Cast Iron Bench | 6 Iron Bars + 1 Clay Mold + 60 cal | 16.63 | **18.30** | **20.50** |
| Cast Iron Table | 8 Iron Bars + 3 Clay Molds + 60 cal | 22.27 | **24.50** | **27.45** |
| Smelting Upgrade | 8 Iron Bars + 6000 cal + 0.2 Trash disposal | 28.04 | **30.85** | **34.55** |
| Metallurgy Research Paper Basic | 4 cheapest `Metal` (Iron Bars) + 10 cheapest `CrushedRock` + 30 cal | 19.03 | **20.95** | **23.45** |

## Dependencies not yet priced

- Cast Iron Stove — needs Cooking Utensils and Lumber;
- Town Bell — needs Lumber in addition to the rebuilt metal bars;
- Blacksmith / Advanced Smelting skill books — research economy;
- Steel and Advanced Smelting products — build after Masonry/Quicklime and the advanced fuel chain.

## Pollution / recycling consequence

Smelting's current price includes disposal of Ceramic Scrap. When Recycling opens a usable Ceramic Scrap recovery path, that disposal charge can be reconsidered. Do not retroactively pretend the waste was free before the recovery service existed.
