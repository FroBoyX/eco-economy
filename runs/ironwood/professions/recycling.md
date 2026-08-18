# Ironwood Recycling — Current Steam-Era Recovery Table

Rebuilt from the supplied Eco 14 Core under the current Steam-entry boundary.

Recycling is now **operational** in Ironwood. The exact sorted Steam-era recovery lanes below are active. They are not unlimited garbage demand: procurement should be capped or managed to real recovery capacity, and mixed/unsorted waste does not inherit the value of a sorted feedstock.

The permanent current Ironwood Iron Bar baseline is **3.00 Town Buy / 3.15 Town Sell**. Iron Scrap procurement remains **2.75 / 2.89** as a managed feedstock price rather than automatically rising with finished bars.

## Active Steam-era recovery lanes

Current workstations permit:

- Food Scrap / Bio Residue -> Compost at the Farmers Table;
- Wood Scrap -> Cellulose Fiber at the Small Paper Machine;
- Glass Scrap -> Glass at the Glassworks;
- exact Iron/Copper/Gold Scrap -> bars at the Blast Furnace.

The following Recycling recipes are **not current price setters** despite belonging to the Recycling skill:

- Textiles -> Linen Fabric requires the future Automatic Loom / Industry route;
- Plastic Scrap -> Plastic requires future Injection Molding;
- dry/wet Tailings reprocessing and electronic dissolution require future Froth Flotation / Electronics machinery;
- Bio Gasoline requires Petroleum;
- recycled Steel belongs to the later Steel/Coal material transition;
- later recycling/garbage/compost infrastructure requiring Plastic or future chemistry does not set current prices.

## Current active sorted-feedstock prices

| Sorted stream | Town Buys | Town Sells | Current recovery |
|---|---:|---:|---|
| Food Scrap | **0.02** | **0.03** | Compost |
| Bio Residue | **0.02** | **0.03** | Compost |
| Wood Scrap | **0.25** | **0.27** | Cellulose Fiber |
| Glass Scrap | **0.75** | **0.79** | Glass |
| Iron Scrap | **2.75** | **2.89** | Iron Bars |
| Copper Scrap | **2.50** | **2.63** | Copper Bars |
| Gold Scrap | **8.00** | **8.40** | Gold Bars |

These prices deliberately leave a strong Recycler margin while transferring meaningful recovery value to players who sort real waste. They are **managed procurement prices**, not an invitation to manufacture scrap for the Treasury.

## Compost — Recycling 1

Core current routes:

- 1 Food Scrap -> 1 Compost;
- 1 Bio Residue -> 1 Compost;
- 20 calories.

At Recycling 1, feedstock bought publicly at 0.03 gives approximately:

- 0.8 waste × 0.03 = 0.024;
- 16 calories = 0.016;
- total cash cost = **0.040** per Compost.

**Compost: 0.05 Town Buy / 0.06 Town Sell.**

The 0.02 / 0.03 feedstock value is intentionally small so ordinary biological waste becomes worth sorting without becoming a large money faucet.

## Recycled Cellulose Fiber — Recycling 1

Core:

- 2 Wood Scrap;
- 60 calories;
- -> 4 Cellulose Fiber.

At Recycling 1 and Wood Scrap 0.27 public Sell:

- 1.6 Wood Scrap = 0.432;
- 48 calories = 0.048;
- total cash cost = **0.480** per craft;
- current Town Buy value of 4 Cellulose Fiber = **1.92**.

Recycler surplus is about **1.44 Flakes per craft** before broader shop overhead.

**Wood Scrap: 0.25 / 0.27.**

This remains below direct salvage-loop ceilings; a player should not be able to buy an ordinary finished wood good from Ironwood, salvage it, and sell the scrap back for a free profit.

## Recycled Glass — Recycling 1

Core:

- 1 Glass Scrap;
- 60 calories;
- -> 1 Glass.

At Recycling 1:

- 0.8 Glass Scrap × 0.79 = 0.632;
- 48 calories = 0.048;
- cash cost = **0.680**;
- current Glass Town Buy = **1.57**.

Recycler surplus is about **0.89 Flakes**.

**Glass Scrap: 0.75 / 0.79.**

Current Glass salvage does not support buying town Glass merely to recycle it for profit at this scrap price.

## Recycled Iron Bar — Recycling 2

Core effective at Recycling 2:

- 1.5 Iron Scrap;
- 1.5 Clay Mold;
- 45 calories;
- 1.5 Ceramic Scrap disposal;
- -> 6 Iron Bars plus Slag.

At Iron Scrap 2.89 public Sell, current cash cost remains well below the recovered six-bar value. Current Iron Bar Town Buy is **3.00**, so 6 recovered bars are worth **18.00** to the Exchange.

**Iron Scrap: 2.75 / 2.89.**

Keep this below practical salvage-loop ceilings and buy only real sorted scrap.

## Recycled Copper Bar — Recycling 2

The same current Blast Furnace recovery pattern returns 6 Copper Bars. Current Copper Bar Town Buy is **5.14**, so the recovered output is worth **30.84** to the Exchange.

**Copper Scrap: 2.50 / 2.63.**

The recovery margin is intentionally large because Core's yield is generous. Copper Wiring and other salvageable goods remain the key anti-arbitrage checks; town retail goods must not become profitable scrap factories.

## Recycled Gold Bar — Recycling 2

The current Gold recovery route returns 3 Gold Bars. Current Gold Bar Town Buy is **12.51**, so the recovered output is worth **37.53** to the Exchange.

**Gold Scrap: 8.00 / 8.40.**

Gold Scrap is scarce and should remain a managed sorted feedstock rather than an externally infinite import.

## Streams that remain disposal liabilities

Keep the current disposal schedule for streams without a current exact recovery route, including:

- Textiles;
- Mixed Metal Scrap;
- Mixed Construction Scrap;
- Ceramic Scrap;
- Plastic Scrap;
- Electronic Scrap;
- Chemical Waste;
- Mixed Industrial Waste;
- Tailings / Wet Tailings;
- Chemical Pollutant;
- Trash / residual garbage;
- other mixed or unsorted streams.

Exact typed Iron/Copper/Gold Scrap can be valuable while **Mixed Metal Scrap remains negative** because the current recovery recipes do not consume the mixed stream directly.

## Anti-abuse rule

For every active positive scrap price, continuously test:

> finished good purchase -> salvage/recycle -> recovered material -> Treasury sale

If that loop becomes profitable without useful external production, lower the scrap procurement price, cap the feedstock, or change the affected finished-good order. Do not respond by creating unlimited public scrap supply.

## Current market treatment

1. Buy only exact sorted feedstocks at the active prices above.
2. Keep public quantities tied to real recycler throughput/storage.
3. Do not transfer positive sorted-feedstock value to mixed garbage categories.
4. Preserve repair/resale before recycling for durable goods when the intact item still has useful value.
5. Recalculate virgin-material economics only if recycled output becomes a large structural share of supply rather than a recovery side stream.

This keeps Recycling rewarding without letting synthetic scrap arbitrage replace Mining, Smelting, Paper Milling, or Glassworking.
