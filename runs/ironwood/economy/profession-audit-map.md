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

- **canonical-current** — current Core audited and the currently relevant profession outputs are canonical.
- **canonical-foundation** — current Core audited for major upstream inputs; full profession output table still pending.
- **legacy-only** — prior Ironwood work exists but still requires validation under the current source/margin model.
- **untouched** — no current canonical audit yet.
- **policy/outside normal market** — requires a specialized treatment rather than ordinary commodity pricing.

## Farmer

| Specialty | Tier | Status |
|---|---:|---|
| Gathering | 1 | **canonical-foundation** |
| Farming | 2 | **canonical-foundation** |
| Milling | 2 | **canonical-foundation** |
| Fertilizers | 3 | untouched |

## Hunter

| Specialty | Tier | Status |
|---|---:|---|
| Hunting | 1 | **canonical-foundation** |
| Butchery | 2 | **canonical-foundation** |

## Chef

| Specialty | Tier | Status |
|---|---:|---|
| Campfire Cooking | 2 | legacy-only |
| Baking | 3 | legacy-only |
| Cooking | 3 | legacy-only |
| Advanced Baking | 4 | untouched |
| Advanced Cooking | 4 | untouched |
| Cutting Edge Cooking | 5 | untouched |

## Carpenter

| Specialty | Tier | Status |
|---|---:|---|
| Logging | 1 | **canonical-current** |
| Carpentry | 2 | canonical-current for Lumber/current wood economy; full output repricing pending |
| Shipwright | 2 | **canonical-foundation** |
| Paper Milling | 3 | untouched |
| Composites | 5 | untouched |

## Tailor

| Specialty | Tier | Status |
|---|---:|---|
| Tailoring | 2 | **canonical-foundation** — Linen/Cotton/Wool chains locked; full clothing/furniture table pending |

Tailor/Tailoring is a distinct Core profession family. It must never again be folded implicitly into Farmer or Carpenter coverage.

## Mason

| Specialty | Tier | Status |
|---|---:|---|
| Mining | 1 | **canonical-current** |
| Masonry | 2 | **canonical-current** |
| Glassworking | 3 | canonical-current foundation including Glass/Light Bulb; remaining decor pending |
| Pottery | 3 | canonical-current Brick/Glassworks foundation; remaining ceramics/furniture pending |
| Advanced Masonry | 5 | untouched |

## Smith

| Specialty | Tier | Status |
|---|---:|---|
| Smelting | 2 | **canonical-current** — bars and Iron/Copper Pipe |
| Blacksmith | 3 | canonical-current industrial/tool foundation; remaining civic/decor/Steel rows pending |
| Advanced Smelting | 4 | untouched |

## Engineer

| Specialty | Tier | Status |
|---|---:|---|
| Basic Engineering | 2 | **canonical-current** for current infrastructure/vehicles; a few cross-profession rows pending |
| Mechanics | 3 | **canonical-current** through the Steam Truck/Tractor and major steam machinery |
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

- raw edible crops use the **1 credit / 1,000 calories** anchor unless another material/recipe constraint controls value;
- Flax Seed is Farming-derived: 2 Flax Stems → 6 seeds; current **0.04 / 0.05**;
- Flax Fiber and Cotton Lint are Gathering outputs;
- Linen/Cotton/Wool textile intermediates are now sourced through Tailoring rather than guessed;
- Leather Hide, Fur Pelt, Wool and Tallow are canonical Butchery outputs;
- early Lubricant comes from Butchery Grease: 2 Tallow → 4 Lubricant; current **0.28 / 0.29**;
- Flaxseed Oil is Milling-derived and currently **0.66 / 0.69**;
- Iron/Copper Pipe are canonical Smelting outputs;
- Wooden Hull Planks, Hemp Mooring Rope and Iron Hull Sheet are canonical Shipwright bridge materials;
- Light Bulb is Glassworking 2, not Electronics;
- current Steam Truck and Steam Tractor recipes are identical and are now priceable without Electronics.

## Current industrial milestone

The current dependency chain is canonical through:

**raw gathering → Farming/Hunting → Butchery/Milling/Tailoring → Logging/Mining → Smelting/Blacksmith/Masonry/Pottery/Glassworking/Shipwright → Basic Engineering → Mechanics → completed Steam Truck / Steam Tractor.**

That does **not** mean the full economy is complete. It means this production spine no longer contains guessed material prices.

## Next profession-output order

1. reprice the complete current Carpentry output table from the corrected Lumber/metal/component inputs;
2. finish Campfire Cooking, Baking and Cooking under calorie + recipe-cost rules;
3. finish full Tailoring clothing/furniture outputs;
4. finish Hunting/Butchery/Farming/Milling non-foundation outputs;
5. Fertilizers;
6. Paper Milling;
7. complete Shipwright boats/shipyards and terminal-vessel windfalls;
8. Pottery/Glassworking decorative and utility outputs;
9. Advanced Smelting / Steel;
10. Electronics;
11. Recycling current-era transition prices;
12. Oil Drilling petroleum era;
13. Advanced Masonry, Composites and Industry;
14. Painting and remaining specialty furniture/decor;
15. advanced/cutting-edge food professions.

The final public Exchange tables should only be called complete after every row above is either priced or explicitly marked outside Ironwood's unlimited import/export scope.
