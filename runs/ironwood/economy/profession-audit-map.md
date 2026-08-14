# Ironwood Eco 14 Profession Audit Map

Source: supplied Eco 14 Core (`Eco14-Core(3).zip`).

This is the master completeness checklist for Ironwood. It is generated from all **44 current Core Skill classes**, not from remembered profession names.

Eco 14 currently has **10 top-level profession families** represented in Core:

- Farmer
- Hunter
- Chef
- Carpenter
- Tailor
- Mason
- Smith
- Engineer
- Scientist
- Survivalist

A specialty is not considered complete merely because one dependency has been priced.

## Status meanings

- **canonical-current** — current Core audited and the currently relevant outputs are canonical.
- **canonical-foundation** — major upstream inputs are current; full profession output table still pending.
- **legacy-only** — prior work exists but has not been revalidated under the current source/margin model.
- **untouched** — no current canonical audit yet.
- **policy/outside normal market** — specialized treatment rather than ordinary commodity pricing.

## Farmer

| Specialty | Tier | Status |
|---|---:|---|
| Gathering | 1 | **canonical-foundation** |
| Farming | 2 | **canonical-foundation** |
| Milling | 2 | **canonical-foundation** — core flours/oils/Sugar/Yeast/Sun Cheese/industrial inputs locked |
| Fertilizers | 3 | untouched |

## Hunter

| Specialty | Tier | Status |
|---|---:|---|
| Hunting | 1 | **canonical-foundation** |
| Butchery | 2 | **canonical-foundation** — Meat/Leather/Fur/Wool/Tallow/Lubricant locked |

## Chef

| Specialty | Tier | Status |
|---|---:|---|
| Campfire Cooking | 2 | **canonical-current** except research/upgrade objects |
| Baking | 3 | **canonical-current** except research/upgrade objects |
| Cooking | 3 | **canonical-current** except research/upgrade objects |
| Advanced Baking | 4 | untouched |
| Advanced Cooking | 4 | untouched |
| Cutting Edge Cooking | 5 | untouched |

## Carpenter

| Specialty | Tier | Status |
|---|---:|---|
| Logging | 1 | **canonical-current** |
| Carpentry | 2 | **canonical-current** for all current rows not blocked by Paper/Steel/research |
| Shipwright | 2 | **canonical-foundation** |
| Paper Milling | 3 | untouched |
| Composites | 5 | untouched |

## Tailor

| Specialty | Tier | Status |
|---|---:|---|
| Tailoring | 2 | **canonical-foundation** — Linen/Cotton/Wool chains locked; clothing/furniture pending |

Tailor/Tailoring is a distinct Core profession family and must not be folded implicitly into Farmer or Carpenter coverage.

## Mason

| Specialty | Tier | Status |
|---|---:|---|
| Mining | 1 | **canonical-current** |
| Masonry | 2 | **canonical-current** |
| Glassworking | 3 | canonical-current foundation including Glass/Light Bulb; remaining decor pending |
| Pottery | 3 | canonical-current foundation including Brick/Glassworks/Bakery Oven; remaining ceramics/furniture pending |
| Advanced Masonry | 5 | untouched |

## Smith

| Specialty | Tier | Status |
|---|---:|---|
| Smelting | 2 | **canonical-current** — bars, Pipes and Cast Iron Stove |
| Blacksmith | 3 | canonical-current industrial/tool foundation; remaining civic/decor/Steel rows pending |
| Advanced Smelting | 4 | untouched |

## Engineer

| Specialty | Tier | Status |
|---|---:|---|
| Basic Engineering | 2 | **canonical-current** for current infrastructure/vehicle outputs |
| Mechanics | 3 | **canonical-current** through completed Steam Truck/Tractor and major steam machinery |
| Electronics | 4 | untouched |
| Industry | 5 | untouched |

## Scientist

| Specialty | Tier | Status |
|---|---:|---|
| Painting | 3 | untouched |
| Recycling | 3 | legacy-only / separate garbage-policy work |
| Oil Drilling | 4 | untouched; later petroleum Lubricant transition known |

## Survivalist

| Specialty | Tier | Status |
|---|---:|---|
| Self Improvement | 1 | policy/outside normal commodity market except craftable upgrade objects |

## Foundation discoveries now canonical

- ordinary raw edible crops use **1 credit / 1,000 calories** unless another material/recipe constraint controls value;
- Flax Seed is Farming-derived; current **0.04 / 0.05**;
- Flax Fiber and Cotton Lint are Gathering outputs;
- Linen/Cotton/Wool textile intermediates are sourced through Tailoring rather than guessed;
- Leather Hide, Fur Pelt, Wool and Tallow are canonical Butchery outputs;
- Campfire `Render Fat` proved Tallow must sit near its calorie floor: **0.20 / 0.21**;
- early Butchery Grease Lubricant is therefore **0.14 / 0.15**, replacing the provisional 0.28/0.29;
- Flaxseed Oil is Milling-derived at **0.66 / 0.69**;
- early Huckleberry Sugar is **1.16 / 1.22**, while later Beet Sugar supports roughly **0.32 / 0.34** and will trigger a bakery/cooking transition when broadly adopted;
- Iron/Copper Pipe are canonical Smelting outputs;
- Wooden Hull Planks, Hemp Mooring Rope and Iron Hull Sheet are canonical Shipwright bridge materials;
- Light Bulb is Glassworking 2, not Electronics;
- current Steam Truck and Steam Tractor recipes are identical and currently support **955.62 / 965.62** under the terminal-capital policy.

## Current industrial milestone

The current dependency spine is canonical through:

**raw gathering → Farming/Hunting → Butchery/Milling/Tailoring → Logging/Mining → Smelting/Blacksmith/Masonry/Pottery/Glassworking/Shipwright → Basic Engineering → Mechanics → completed Steam Truck / Steam Tractor.**

The basic food spine is also current through:

**raw crops/meat/fish → Campfire Cooking / Baking / Cooking.**

That does **not** mean the full economy is complete. It means these spines no longer contain guessed foundational inputs.

## Next profession-output order

1. finish full Tailoring clothing/furniture outputs;
2. finish Hunting/Butchery/Farming/Milling non-foundation objects;
3. Fertilizers;
4. Paper Milling;
5. complete Shipwright boats/shipyards and terminal-vessel windfalls;
6. Pottery/Glassworking remaining decorative/utility outputs;
7. Advanced Smelting / Steel;
8. Electronics;
9. Recycling current-era transition prices;
10. Oil Drilling petroleum era;
11. Advanced Masonry, Composites and Industry;
12. Painting and remaining specialty furniture/decor;
13. Advanced Baking, Advanced Cooking and Cutting Edge Cooking;
14. research/skill-book/upgrade economy across specialties.

The final public Exchange tables should only be called complete after every specialty above is either priced or explicitly marked outside Ironwood's unlimited import/export scope.
