# Reusable Profession Pricing Model

This file defines the pricing method used by Eco server/run profiles. It does not contain server-specific prices.

## Objective

Set stable prices that allow a producer using the **first intended profession recipe at base efficiency** to make a shallow positive margin, while allowing specialization, resource efficiency, modules, improved workstations, logistics, and organization to increase that producer's effective margin over time.

Prices should not automatically rise because a player becomes more efficient.

## Price Classes

Every run may distinguish four values:

- **Anchor value** — an intentionally selected value for a raw material, calorie, or other foundational input. Anchors are design choices, not recipe outputs.
- **Derived producer value** — the target value of a crafted output based on its canonical inputs, labor, waste/byproducts, and desired base margin.
- **Public buy price** — what a government/exchange shop pays a player who supplies the item.
- **Public sell price** — what a government/exchange shop charges a player who consumes the item.

A run does not need to use public buy/sell prices for every item. They are separate from the underlying producer value so public-market spreads do not accidentally become recipe costs everywhere.

## Canonical Recipe Baseline

For profession pricing, use the **first intended specialized recipe for that profession at its base, unmodified resource efficiency** unless there is a specific design reason to use another path.

Do not price a professional good from an unskilled or primitive fallback merely because the fallback exists. Such recipes may intentionally be convenience paths that are economically inferior to specialization.

When several intended professional recipes make the same output, use the cheapest credible path available at that progression stage as the arbitrage floor. More expensive alternative recipes do not automatically receive their own higher output price.

Later recipes, resource-efficiency bonuses, modules, talents, and improved logistics may reduce effective production cost while the canonical output price stays fixed. That is the intended source of growing professional profit.

## Base Cost

For one base craft:

`base cost = input value + labor value + waste liability - byproduct credit`

Where:

- input quantities use the unmodified Eco recipe quantities for the selected profession baseline;
- labor is valued using the run's calorie anchor;
- garbage is a cost when disposal has a negative value;
- useful byproducts may reduce effective cost only when there is a credible buyer/use for them;
- a byproduct is not credited merely because it theoretically has a recipe somewhere.

## Base Margin

The initial producer value should normally be only modestly above base cost.

The exact target is a run policy. The important rule is that the producer can participate at entry professional efficiency without needing late-game bonuses, but the base recipe should not create excessive profit.

As resource efficiency improves, fewer inputs are consumed for the same output. The output price remains stable, so the producer's profit grows naturally.

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
- base inputs;
- base labor calories;
- garbage/byproducts;
- calculated base cost;
- selected producer/public price;
- base margin;
- notes or policy overrides.

Hand-entered display tables are outputs. They are not the source of truth.
