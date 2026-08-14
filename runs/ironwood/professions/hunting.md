# Ironwood Hunting — Carcass and Fish Foundation

Derived from the supplied Eco 14 Core.

Hunted animals and caught fish are **Depth 0 gathered goods**. Their Town Buy prices are effort/rarity anchors, not cost-plus manufactured prices. Processing recipes then create specialist margin for Hunting/Butchery.

## Carcass anchors

Current Core carcass tags establish the practical butchery classes:

- Tiny Fur: Agouti, Otter;
- Tiny Leather: Prairie Dog, Snapping Turtle, Turkey;
- Hare: dedicated Hare recipe;
- Small: Coyote, Fox;
- Medium Leather: Alligator, Deer, Elk, Jaguar;
- Medium Wooly: Bighorn Sheep, Mountain Goat;
- Wolf: dedicated medium recipe yielding Fur rather than Leather;
- Bison: dedicated large recipe.

Ironwood import anchors:

| Hunting output | Town Buys | Town Sells | Purpose |
|---|---:|---:|---|
| Tiny Fur Carcass | **0.50** | **0.53** | small hunting cash outlet |
| Tiny Leather Carcass | **0.55** | **0.58** | slightly higher because Leather is strategic |
| Hare Carcass | **0.65** | **0.68** | meat + fur + wool butchery route |
| Small Carcass | **0.80** | **0.84** | Coyote/Fox class |
| Medium Leather Carcass | **1.50** | **1.58** | Deer/Elk/Alligator/Jaguar class |
| Medium Wooly Carcass | **1.75** | **1.84** | adds wool value |
| Wolf Carcass | **1.50** | **1.58** | medium meat + fur route |
| **Bison Carcass** | **3.50** | **3.68** | rare/high-output hunting windfall |

These anchors intentionally give hunters useful direct currency without applying downstream manufacturing multipliers to the kill itself.

## Fish and marine anchors

| Gathered catch | Town Buys | Town Sells |
|---|---:|---:|
| Pacific Sardine | **0.08** | **0.09** |
| Clam | **0.08** | **0.09** |
| Urchin | **0.08** | **0.09** |
| Crab Carcass | **0.15** | **0.16** |
| Moon Jellyfish | **0.15** | **0.16** |
| Medium Fish | **0.35** | **0.37** |
| Large Fish | **0.65** | **0.68** |
| Kelp | **0.03** | **0.04** |

## Cleaned fish

Raw Fish has 200 calories, so the food-energy anchor is **0.20 Town Buy / 0.21 Town Sell**.

Current Core Hunting 1 routes:

- 2 Pacific Sardines → 1 Raw Fish;
- 1 Crab Carcass → 1 Raw Fish;
- 1 Moon Jellyfish → 1 Raw Fish;
- 2 Urchins → 1 Raw Fish;
- 2 Clams → 1 Raw Fish;
- 1 Medium Fish → 2 Raw Fish;
- 1 Large Fish → 4 Raw Fish.

At Hunting 1's 0.80 recipe multiplier, the catch anchors above leave a positive but modest processing margin while preserving Raw Fish's calorie value.

**Raw Fish: 0.20 / 0.21.**

## Kelp → Plant Fiber

Core Hunting 0:

- 8 Kelp
- 25 calories
- → 7 Plant Fibers

At Kelp 0.04 public Sell, the cash cost is approximately 0.345 and seven Plant Fibers return 0.35 at the 0.05 Town Buy. This is intentionally close to break-even: shredding Kelp is a fallback fiber route, not a currency printer.

## Preserved hunting food

Core Hunting 2:

- 1 Raw Meat → 1 Dried Meat;
- 1 Raw Fish → 1 Dried Fish;
- 25 calories each.

Dried Meat contains 550 calories and Dried Fish 450 calories, so the locked calorie anchor itself provides a healthy preservation margin:

| Item | Town Buys | Town Sells |
|---|---:|---:|
| Dried Meat | **0.55** | **0.58** |
| Dried Fish | **0.45** | **0.47** |

## Deferred Hunting outputs

Fish Trap, Fishery, Fish Rack, Flax/Nylon Trawler Nets, Recurve/Composite Bow, mounts and taxidermy objects remain for the complete profession-output pass. Their required dependencies are now being resolved rather than guessed.
