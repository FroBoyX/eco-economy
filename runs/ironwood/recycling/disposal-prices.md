# Ironwood Initial Garbage Disposal Prices

This is the pre-Recycling/opening disposal schedule for the current Ironwood run.

A **negative Exchange buy price means the player pays the public waste system to accept the garbage**.

These values are disposal charges, not recovered-material values. When Recycling creates a legitimate recovered output, the relevant sorted/recycled material can receive a positive price while unsorted waste may remain a disposal liability.

## Design goal

Dumping or abandoning garbage should be economically worse than using the public disposal system, but ordinary production should remain viable after paying its waste cost.

Polluting and terminal residual streams carry higher disposal charges than biodegradable or easily recoverable streams.

## Initial schedule

| Garbage material | Public intake price | Producer pays | Reason |
|---|---:|---:|---|
| Mixed Biowaste | **-0.10** | 0.10 / unit | Low-to-moderate cleanup burden. |
| Food Scrap | **-0.05** | 0.05 / unit | Biodegradable and compostable once Recycling participates. |
| Wood Scrap | **-0.08** | 0.08 / unit | Recoverable at Recycling 1; still a disposal burden before collection/processing is active. |
| Textiles | **-0.10** | 0.10 / unit | Recoverable at Recycling 1 but not free to collect/sort. |
| Mixed Metal Scrap | **-0.15** | 0.15 / unit | Valuable later, but requires sorting/recycling work. |
| Iron Scrap | **-0.15** | 0.15 / unit | Soil-polluting garbage material in Core; becomes a strong Recycling input at level 2. |
| Copper Scrap | **-0.15** | 0.15 / unit | Same initial disposal posture as iron scrap. |
| Gold Scrap | **-0.15** | 0.15 / unit | Same initial disposal posture; positive recovery price comes later from Recycling economics. |
| Mixed Construction Scrap | **-0.15** | 0.15 / unit | Construction cleanup burden. |
| Ceramic Scrap | **-0.15** | 0.15 / unit | Soil-polluting construction garbage; important immediate Smelting waste cost. |
| Glass Scrap | **-0.15** | 0.15 / unit | Recoverable at Recycling 1 but hazardous/awkward waste before collection. |
| Stone Rubble garbage | **-0.05** | 0.05 / unit | Low-pollution cleanup burden. The sorted `Crushed Mixed Rock` output is a separate positive commodity. |
| Mixed Industrial Waste | **-0.25** | 0.25 / unit | Chemical/industrial handling burden. |
| Plastic Scrap | **-0.25** | 0.25 / unit | Chemical-pollution class and later Recycling 4 feedstock. |
| Electronic Scrap | **-0.25** | 0.25 / unit | Chemical-pollution class with later specialist handling. |
| Chemical Waste | **-0.40** | 0.40 / unit | Degrades into Chemical Pollutant in Core; strong reason to capture it correctly. |
| Mixed Residuals | **-0.35** | 0.35 / unit | Heavy-mineral residual sink. |
| Tailings | **-0.35** | 0.35 / unit | Heavy-mineral pollutant; later Recycling 5 reprocessing does not erase the initial handling burden. |
| Wet Tailings | **-0.35** | 0.35 / unit | Same heavy-mineral posture as dry Tailings. |
| Chemical Pollutant | **-0.50** | 0.50 / unit | Terminal chemical pollutant; highest ordinary disposal charge. |
| Generic Garbage / Trash | **-0.20** | 0.20 / unit | Terminal soil-polluting trash. |
| Bio Residue | **-0.05** | 0.05 / unit | Low-grade residual that can become useful through Recycling/compost loops. |
| Compost as waste stream | **-0.02** | 0.02 / unit | Minimal handling charge until a positive fertilizer/soil-use market is explicitly opened. |

## Important accounting rule

Recipe garbage cost is added to production cost using the absolute value of the disposal charge.

Example: a recipe producing 1.5 Ceramic Scrap carries **0.225 credits of disposal cost** at the current -0.15 intake price.

Recovered or normal crafting byproducts are treated separately. For example, Smelting also outputs Slag as a normal item; Slag receives its own commodity price and is not priced as Ceramic Scrap.

## Recycling transition

When a Recycling recipe is opened economically:

1. calculate the value of the recovered output from the existing virgin-material economy;
2. preserve a margin for the Recycler;
3. determine the maximum positive purchase price the Recycler can pay for sorted scrap;
4. decide whether the public disposal charge should remain, fall toward zero, or be replaced by a positive collection price;
5. ensure the recovered path does not undercut virgin professions so severely that extraction/processing stops being meaningful.

Do not convert all garbage to positive value merely because Recycling exists. Each stream must earn its positive value through an actual usable recovery path.
