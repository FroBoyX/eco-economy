# Ironwood Commercial Viability Policy

Ironwood prices must support a functioning player economy, not merely prove that crafting is technically above zero.

## Role of the Ironwood Exchange

The Exchange's **Town Buy** price is a guaranteed wholesale/import outlet. It is not intended to equal a producer's cost and it is not intended to be the highest price a producer can earn.

A player may instead operate their own shop and sell above the Town Buy price when local supply and demand support it. The government outlet exists so producing a useful good always has a reliable path back into currency.

That guaranteed outlet must therefore pay enough that a specialist can do more than replace ingredients. Producer surplus is expected to finance food, replacement inputs, shop inventory, material buy orders, workshop buildings, workstations, transport, storage, mistakes, downtime and later specialization.

A Town Buy price that merely reimburses ingredients is not a viable downstream import price.

## Current-run era rule

For the active Ironwood run, **current prices are authoritative for the technology era the settlement has actually reached**.

Future recipes and future technologies do not retroactively determine today's prices. A later Petroleum, Electronics, Industry, Recycling or other route may prove that a commodity can eventually be produced more cheaply, but that future efficiency is ignored until the relevant technology is actually present and broadly usable in the current economy.

Ironwood therefore prices from the **best normal route available in the current run**, not from the cheapest route anywhere in the full Eco technology tree.

Future work may define a full transition scale with explicit era boundaries and adoption thresholds. That transition model is a separate planning artifact and must not silently overwrite the current-run Exchange tables.

## Same-specialty internal component rule

A specialty does **not** pay its own commercial markup repeatedly as it turns its own intermediate products into deeper products.

For pricing purposes, each Eco specialty is treated as an integrated workshop. If a recipe in specialty `P` consumes an item also produced by specialty `P`, that ingredient enters the downstream recipe at the component's **Projected Cost**, before the component's Town Buy markup and before the Exchange spread.

If the ingredient is produced by a **different specialty**, it enters the downstream recipe at that upstream item's **Town Sell** price. That preserves the upstream specialist's commercial margin and models the downstream producer actually purchasing from another profession.

This rule is applied at the **specialty level**, not merely the broad profession family. For example, Logging and Carpentry are separate specialties even though both belong to the Carpenter family; a Carpenter buying Boards from a Logger pays the Logging market price. Mechanics using its own Iron Gears internally uses Iron Gear Projected Cost.

The intended accounting is:

`Projected Cost = external-specialty inputs at Town Sell + same-specialty inputs at their Projected Cost + labor + fuel + disposal/operating costs`

### Same-specialty raw-anchor opportunity value

A gathered/raw item has no craft recipe from which to derive a Projected Cost. When a specialty consumes a raw anchor that it itself produces or directly controls, Ironwood carries that raw input internally at its **Town Buy anchor**, not its Town Sell price and not zero.

This is an opportunity-cost value: using the raw material internally means giving up the guaranteed Town Buy sale. It preserves the value of raw labor and extraction while avoiding the fiction that a specialty paid itself the Exchange spread. Examples include Logging consuming its own Wood and Mining consuming its own raw ore.

An intermediate item still receives its normal commercial markup when it is sold directly. The markup is simply not recursively charged to another recipe inside the same specialty.

This is the canonical rule for the final output-table **Projected Cost** column.

## Depth-sensitive pricing

The commercial uplift scales with **production depth, cash exposure, turnover and whether the output is itself a downstream input**. It is not applied uniformly to the economy.

### Depth 0 — gathered and raw commodities

Examples: Wood, Sand, Clay, Rock, Limestone, raw ores, crops, seeds and other directly gathered resources.

These remain **anchor-priced**. They do not receive a manufactured-goods markup simply because gathering takes time. Raw anchors are set by abundance, gathering incentive, scarcity, environmental policy and downstream economic effects.

### Depth 1 — simple processing

Examples: Boards, Mortar, basic crushed material, simple bars, plates, Nails and similarly shallow conversions.

These should earn a **modest specialist margin**, normally around **8–12% over realistic Projected Cost** where that test is meaningful.

The purpose is to make specialization worthwhile without compounding large margins at every stage.

### Depth 2 — multi-step intermediates and ordinary finished goods

Examples: components or finished goods that consume multiple processed inputs but are still relatively common or high-turnover.

Target roughly **12–18% over Projected Cost**, depending on depth, throughput and absolute surplus.

### Depth 3 — deep manufactured goods

Examples: Boilers, complex machine components, deep furniture/workshop outputs and similar goods containing substantial purchased value from several professions.

Town Buy should normally target approximately:

`Projected Cost × 1.25`

This creates enough operating surplus for food, working capital, material buy orders and continued production without forcing vertical integration across professions.

### Ordinary capital goods, workstations and machinery

Town Buy should normally target approximately:

`Projected Cost × 1.30`

Examples include Lathes, Stamp Mills and comparable workstations that are expensive and low-turnover but may still participate in later production chains.

### Late capital goods and terminal manufactured goods

Very deep, low-volume goods may justify a larger guaranteed windfall when most of their value has already accumulated through multiple specialties and the item has little or no downstream use.

Typical target:

`Projected Cost × 1.40 to 1.50`

Use the lower end for late capital equipment that still becomes an input to later production. Use the upper end for true terminal/end-use goods such as completed vehicles or similarly deep consumer/capital products.

This larger margin is deliberately concentrated at the **end of the chain**, where it creates player wealth without recursively inflating later recipes.

A completed Steam Truck, for example, should normally receive this terminal-capital treatment. A Steam Truck Flatbed or other attachment is still a component and should receive a smaller uplift unless evidence shows it is itself extremely low-turnover.

### Bulk construction materials

Ironwood's separate construction-band policy applies to Brick, Glass, Lumber and similar bulk structural goods.

Their direct-sale prices are judged by recipe floor, gathering/hauling burden, workstation throughput, storage burden, perceived technology tier and whether producing stacks is economically attractive.

If a bulk material is consumed by another recipe **inside the same specialty that makes it**, its internal component value is still its Projected Cost rather than its policy-marked direct-sale price.

### Exceptional goods

Research, civic procurement, megaprojects, garbage/recycling streams, deliberate subsidies and emergency shortage imports may use separate policy prices.

## Required cost views

Every final Exchange table should expose at least these three values:

1. **Projected Cost** — current-era minimum-unlock production cost under the same-specialty internal component rule above.
2. **Town Buys** — the guaranteed wholesale price after the appropriate direct-sale commercial margin or policy adjustment.
3. **Town Sells** — the Exchange fallback supply price after the public spread.

Projected Cost is the factual/structural baseline; Town Buy is the economic policy choice. This lets the town manually tune an outlier without hiding the actual production burden.
