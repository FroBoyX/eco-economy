# Reusable Profession Pricing Model

This file defines the pricing method used by Eco server/run profiles. It does not contain server-specific prices.

## Objective

Set stable prices that allow a producer using the **first intended profession recipe at the minimum skill level required to craft it** to make a shallow positive margin, while allowing additional skill levels, modules, talents, improved workstations, logistics, and organization to increase that producer's effective margin over time.

Prices should not automatically rise because a player becomes more efficient.

## Price Classes

Every run may distinguish four values:

- **Anchor value** — an intentionally selected value for a raw material, calorie, or other foundational input. Anchors are design choices, not recipe outputs.
- **Derived producer value** — the target value of a crafted output based on its canonical inputs, labor, waste/byproducts, workstation operating cost, and desired entry margin.
- **Public buy price** — what a government/exchange shop pays a player who supplies the item.
- **Public sell price** — what a government/exchange shop charges a player who consumes the item.

A run does not need to use public buy/sell prices for every item. They are separate from the underlying producer value so public-market spreads do not accidentally become recipe costs everywhere.

## Canonical Recipe Baseline

For profession pricing, use the **first intended specialized recipe for that profession evaluated at the minimum skill level required by that recipe** unless there is a specific design reason to use another path.

Do not use the printed recipe quantities as though they are necessarily the player's actual entry quantities. Eco specialties apply their multiplicative skill strategy immediately. In the current Eco 14 Core snapshot, common crafting specialties use multipliers of 1.00 at level 0, 0.80 at level 1, 0.75 at level 2, 0.70 at level 3, 0.65 at level 4, 0.60 at level 5, 0.55 at level 6, and 0.50 at level 7. Skill-modified ingredients, labor, and craft time must therefore be evaluated at the recipe's unlock level before calculating entry cost.

Do not price a professional good from an unskilled or primitive fallback merely because the fallback exists. Such recipes may intentionally be convenience paths that are economically inferior to specialization.

When several intended professional recipes make the same output, use the cheapest credible path available at that progression stage as the arbitrage floor. More expensive alternative recipes do not automatically receive their own higher output price.

Later skill levels, resource-efficiency bonuses, modules, talents, and improved infrastructure may reduce effective production cost while the canonical output price stays fixed. That is the intended source of growing professional profit.

## Base Cost

For one entry-level craft:

`base cost = effective input value + effective labor value + workstation operating cost + waste liability - byproduct credit`

Where:

- skill-modified ingredient quantities use the multiplier at the recipe's minimum required skill level;
- static ingredients remain at their actual static quantity;
- labor is evaluated at that same entry skill level and valued using the run's calorie anchor;
- workstation fuel or other operating consumption is included when material to the recipe;
- garbage is a cost when disposal has a negative value;
- useful byproducts may reduce effective cost only when there is a credible buyer/use for them;
- a byproduct is not credited merely because it theoretically has a recipe somewhere.

## Margin Placement Across Chains

Do not blindly add the full target producer margin **and** the full public-market spread at every intermediate processing step and then recursively use those retail prices as the next profession's cost basis. That compounds friction through deep chains and can inflate advanced goods far beyond the intended shallow-margin economy.

Instead, audit the whole dependency chain. Allocate enough value at each stage for every participating profession to earn a useful entry margin, while keeping the final downstream price coherent. Public Exchange spreads are liquidity/anti-cycling tools and may be narrower on intermediate industrial goods where a larger spread would distort the chain.

## Base Margin

The initial producer value should normally be only modestly above effective entry cost.

The exact target is a run policy. The important rule is that the producer can participate at the minimum skill level where the recipe unlocks without needing later bonuses, but the entry recipe should not create excessive profit.

As efficiency improves, fewer inputs and/or less labor/time are consumed for the same output. The output price remains stable, so the producer's profit grows naturally.

## Tag Inputs

Eco recipes often accept tags such as `Wood`, `Rock`, or `WoodBoard` rather than one specific item.

A run must explicitly define the economic value used for important input tags. Do not assume every member of a tag has the same economic value.

When substitution is unrestricted, pricing should normally protect against the cheapest practical accepted input, because players can choose that input. Strategic materials such as Limestone may therefore need their own policy even when they also satisfy a broader recipe tag.

## Public Market Spread

Government shops are stabilizers, not the source of the underlying economic value.

A shallow public buy/sell spread may be used to:

- guarantee liquidity;
- discourage pointless shop cycling;
- import scarce goods;
- export bottleneck goods;
- establish a visible price reference.

Do not recursively calculate downstream producer values from an arbitrary government resale markup unless that is deliberately how the run wants inter-profession trade to work.

## Recycling

Garbage and recycling outputs are part of recipe economics.

Before a useful recycling path exists, garbage may be a disposal liability with a negative value. Once recycling creates a credible recovered output, the value chain should be recalculated so collection, sorting, recycling, and consuming the recovered material can all participate without making virgin extraction irrelevant.

## Profession Tables

A profession table should be generated from the same canonical run ledger and Eco mechanical reference used by every other profession.

Each priced recipe should be able to show:

- output and quantity;
- skill and required level;
- workstation;
- printed inputs;
- **entry-effective inputs at the recipe's unlock level**;
- entry-effective labor calories;
- workstation operating cost where applicable;
- garbage/byproducts;
- calculated entry cost;
- selected producer/public price;
- entry margin;
- later-efficiency notes or policy overrides.

Hand-entered display tables are outputs. They are not the source of truth.
