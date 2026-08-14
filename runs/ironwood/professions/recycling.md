# Ironwood Recycling — Steam-Era Activation Table

Rebuilt from the supplied Eco 14 Core under the current Steam-entry boundary.

Recycling is Tier 3 and is technically inside the current era, but its garbage markets are **activation-sensitive**. The existing negative disposal schedule remains authoritative until a recycler actually opens a usable recovery stream. This file defines the prices Ironwood can switch to when each current recovery lane becomes operational.

## Current Steam-era recovery lanes

Current workstations permit:

- Food Scrap / Bio Residue -> Compost at the Farmers Table;
- Wood Scrap -> Cellulose Fiber at the Small Paper Machine;
- Glass Scrap -> Glass at the Glassworks;
- exact Iron/Copper/Gold Scrap -> bars at the Blast Furnace.

The following Recycling recipes are **not current price setters** despite belonging to the Recycling skill:

- Textiles -> Linen Fabric requires the future Automatic Loom / Industry;
- Plastic Scrap -> Plastic requires future Injection Molding;
- dry/wet Tailings reprocessing and electronic dissolution require future Froth Flotation / Electronics;
- Bio Gasoline requires Petroleum;
- recycled Steel depends on the later Steel/Coal material era;
- modern recycling/garbage/compost bins require Plastic and future chemistry.

## Activation rule

Until a specific recovery lane is operating, keep the existing disposal intake price.

Once it is operating, Ironwood may replace the disposal charge with the following **recovery-backed public Buy/Sell price** for that exact sorted stream.

Mixed/unsorted garbage does not inherit the value of a sorted stream.

## Proposed Steam-era activation prices

| Sorted stream | Pre-activation intake | Activated Town Buy | Activated Town Sell | Current recovery |
|---|---:|---:|---:|---|
| Food Scrap | **-0.05** | **0.02** | **0.03** | Compost |
| Bio Residue | **-0.05** | **0.02** | **0.03** | Compost |
| Wood Scrap | **-0.08** | **0.25** | **0.27** | Cellulose Fiber |
| Glass Scrap | **-0.15** | **0.75** | **0.79** | Glass |
| Iron Scrap | **-0.15** | **2.75** | **2.89** | Iron Bars |
| Copper Scrap | **-0.15** | **2.50** | **2.63** | Copper Bars |
| Gold Scrap | **-0.15** | **8.00** | **8.40** | Gold Bars |

These prices deliberately leave a strong Recycler profit while transferring a meaningful share of recovery value back to the players who generate and sort the waste.

## Compost — Recycling 1

Core current routes:

- 1 Food Scrap -> 1 Compost;
- 1 Bio Residue -> 1 Compost;
- 20 calories.

At Recycling 1, an activated waste stream selling publicly for 0.03 costs:

- 0.8 waste × 0.03 = 0.024
- 16 calories = 0.016
- total = 0.040

Current Compost Town Buy is **0.05**, leaving about 0.01 credit per unit to the Recycler.

This supports the small **0.02 / 0.03** positive waste price without turning food waste into a large money faucet.

## Recycled Cellulose Fiber — Recycling 1

Core:

- 2 Wood Scrap
- 60 calories
- -> 4 Cellulose Fiber

At Recycling 1 and activated Wood Scrap 0.27 public Sell:

- 1.6 Wood Scrap = 0.432
- 48 calories = 0.048
- total cash cost = **0.480**
- Town Buy value of 4 Cellulose Fiber = **1.92**

Recycler surplus = about **1.44 credits per craft**.

**Wood Scrap activation: 0.25 / 0.27.**

This stays below direct salvage-loop ceilings; for example, a 0.06 Dowel salvages only 0.1 Wood Scrap.

## Recycled Glass — Recycling 1

Core:

- 1 Glass Scrap
- 60 calories
- -> 1 Glass

At Recycling 1:

- 0.8 Glass Scrap × 0.79 = 0.632
- 48 calories = 0.048
- cash cost = **0.680**
- current Glass Town Buy = **1.57**

Recycler surplus ≈ **0.89**.

**Glass Scrap activation: 0.75 / 0.79.**

Current Glass itself salvages only 0.5 Glass Scrap, so buying Glass at 1.65 and salvaging it cannot profit against the 0.75 scrap Town Buy.

## Recycled Iron Bar — Recycling 2

Core effective at level 2:

- 1.5 Iron Scrap
- 1.5 Clay Mold
- 45 calories
- 1.5 Ceramic Scrap disposal
- -> 6 Iron Bars + about 1.5 Slag

At Iron Scrap 2.89 public Sell, cash cost after Slag credit is about **4.605**.

Town Buy value of 6 Iron Bars = **15.24**.

Recycler surplus ≈ **10.64 credits**.

**Iron Scrap activation: 2.75 / 2.89.**

The value is intentionally below the cheapest practical salvage loop. Current Screws sell for 0.63 and salvage to only 0.2 Iron Scrap; at 2.75 scrap Buy that salvage value is 0.55, below the purchase cost.

## Recycled Copper Bar — Recycling 2

At activated Copper Scrap 2.63 public Sell, the same current Blast Furnace pattern costs about **4.215** per craft and returns 6 Copper Bars worth **30.84** to Town Buy.

**Copper Scrap activation: 2.50 / 2.63.**

The resulting Recycler surplus is very large because Core's recovery yield is generous. Copper Wiring is the important anti-arbitrage check: it sells for 1.70 and salvages 0.6 Copper Scrap, worth 1.50 at the proposed scrap Buy. Direct purchase-and-salvage therefore remains unprofitable.

## Recycled Gold Bar — Recycling 2

Core returns 3 Gold Bars rather than 6.

At activated Gold Scrap 8.40 public Sell:

- current cash cost ≈ **12.87**
- Town Buy value of 3 Gold Bars = **37.53**
- Recycler surplus ≈ **24.66**

**Gold Scrap activation: 8.00 / 8.40.**

Gold Scrap is scarce and current salvage ratios remain well below an immediate purchase-and-salvage arbitrage.

## Streams that remain disposal liabilities

Until their actual current workstations exist, keep the pre-Recycling disposal schedule for:

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
- generic Garbage / Trash.

Exact typed Iron/Copper/Gold Scrap can become valuable while **Mixed Metal Scrap remains negative** because current recovery recipes do not consume the mixed stream directly.

## Economic warning

Current Core metal-recycling yields create unusually large margins. Ironwood should therefore:

1. buy only real sorted scrap generated in the world;
2. keep activation prices below salvage-loop ceilings;
3. never create an unlimited external supply of scrap at these prices;
4. revisit virgin metal prices only if Recycling becomes a large, economy-wide source of bars rather than a scarce recovery side business.

This preserves Recycling as a rewarding specialty without allowing synthetic scrap arbitrage to replace Mining and Smelting.
