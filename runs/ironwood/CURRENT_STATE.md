# Ironwood Current State

This file is the short-form recovery checkpoint for the current Ironwood run.

It is intentionally overwritten as the run changes. It is not a historical log and must not accumulate obsolete assumptions for preservation purposes.

The repository remains canonical. Chat sessions are working sessions.

## Current progression

Ironwood is **entering the Steam era**.

Live pricing is based on the best normal routes actually available in the current run. Future Oil, Electronics, Industry, advanced food, Composites, Advanced Masonry, and other later efficiencies do not back-propagate into current prices.

The **Ironwood Flake is live**. Baking, Cooking and Recycling are also now operational.

## Active profession coverage

### Canonical-current

- Gathering
- Farming
- Milling
- Fertilizers
- Hunting
- Butchery
- Campfire Cooking
- **Baking — operational; ordinary distinct outputs fully published**
- **Cooking — operational; ordinary distinct outputs fully published**
- Logging
- Carpentry
- Shipwright
- Paper Milling
- Tailoring
- Mining
- Masonry
- Glassworking
- Pottery
- Smelting
- Blacksmith
- Basic Engineering
- Mechanics
- Painting
- **Recycling — operational for current exact sorted Steam-era recovery lanes**

Self Improvement remains a policy/special lane rather than an ordinary commodity profession.

### Future-transition, not current price setters

- Advanced Baking
- Advanced Cooking
- Cutting Edge Cooking
- Composites
- Advanced Masonry
- later economy-wide Advanced Smelting / Steel transition where not yet normal
- Electronics
- Industry
- Oil Drilling
- later petroleum / Plastic / Epoxy routes
- later Nylon / industrial textile routes

Future routes may be inspected for planning without becoming current price setters.

## Current canonical publication

`economy/steam-era-exchange-tables.md` is the shop-facing Steam-entry publication.

The latest publication pass now includes:

- full Baking ordinary-output coverage;
- full Cooking ordinary-output coverage;
- active sorted Recycling procurement and residual disposal separation;
- corrected current Paper Milling values;
- corrected Crushed Limestone / Glassworking values;
- corrected current Smelting bar anchors used by Recycling;
- current civic-reference prices for Town Bell, Bank, Currency Exchange and Mint.

Baking/Cooking alternate recipes that produce the same final output are grouped rather than duplicated. Specialty modules/upgrades remain limited capital rather than unlimited food imports.

Recycling positive feedstock prices are **managed/capped procurement**, not unlimited garbage demand.

Research papers remain **capped Library procurement**, not unlimited Exchange demand.

## Current pricing doctrine

- Stable nominal prices; increasing player efficiency creates increasing margin.
- Same-specialty intermediates enter deeper same-specialty recipes at Projected Cost.
- Cross-specialty inputs enter at Town Sell.
- Same-specialty raw anchors enter at Town Buy / opportunity value.
- Direct-sale markup is applied once rather than recursively compounded through a specialty.
- Bulk construction materials may retain explicit policy prices.
- Civic allocations, research, recycling, garbage, emergency interventions, and other exceptional goods may use policy pricing rather than ordinary recipe markup.

## Current Recycling lanes

Active exact sorted feedstocks:

| Sorted stream | Town Buys | Town Sells | Recovery |
|---|---:|---:|---|
| Food Scrap | **0.02** | **0.03** | Compost |
| Bio Residue | **0.02** | **0.03** | Compost |
| Wood Scrap | **0.25** | **0.27** | Cellulose Fiber |
| Glass Scrap | **0.75** | **0.79** | Glass |
| Iron Scrap | **2.75** | **2.89** | Iron Bars |
| Copper Scrap | **2.50** | **2.63** | Copper Bars |
| Gold Scrap | **8.00** | **8.40** | Gold Bars |

Mixed and future-tech waste streams remain disposal-priced. Do not infer positive value for Mixed Metal Scrap, Textiles, Plastic Scrap, Electronics, Tailings, chemical streams or residual garbage from the activated exact lanes.

## Private paper shop — run-specific retail

The private paper shop is separate from Exchange/reference pricing.

Current shop policy:

- Natural Fiber input: **0.06**;
- Paper retail: **0.23**;
- Paraffin input: **0.55**;
- Waxed Paper retail: **0.75**.

These private-shop prices do not rewrite the Exchange Paper Milling ledger.

## Flake monetary policy — live

Canonical policy: `economy/flake-monetary-policy.md`.

Current decisions:

- existing FroBoyX Credit is permanently redeemable into Flakes at **1:1**;
- no new FroBoyX Credit is issued after cutover;
- **1 physical Paper banknote represents 25 Flakes**; the Paper item is the note medium, not commodity backing;
- each player Active at cutover receives a **one-time 175-Flake capitalization grant**;
- a player not Active at cutover receives the same **one-time 175-Flake grant on first becoming Active**;
- losing and regaining Active status does not create another grant;
- Active is a server-wide status, not Ironwood residency; the cutover Active population was **114 players**;
- observed legacy FroBoyX Credit economy at planning was **9,236.39**;
- 114 × 175 capitalization = **19,950 Flakes**;
- combined conversion + capitalization requirement = **29,186.39 Flakes**;
- minimum physical printing at 25 Flakes/Paper = **1,168 Paper (29,200 Flakes)**;
- initial print run = **1,600 Paper = 40,000 Flakes**;
- the issuing authority limits net Flake circulation outside sterilized issuer reserves to **60% of the current face value of unsold sellable civic land instruments it actually controls**;
- reserve capacity is a ceiling, not a requirement to issue;
- unissued printed Paper held by the Treasury is not circulation;
- land-sale receipts are sterilized/retired rather than immediately recycled as ordinary spending while required to preserve the reserve rule;
- the Flake is intended to circulate outside Ironwood; other players and future Towns can acquire it through Exchange trade, procurement, public works, research, and other authorized transactions with the issuing authority.

## Current Town real-estate prices — LOCKED

| Civic land instrument | Treasury Buy | Treasury Sell |
|---|---:|---:|
| Town Claim Paper | **150 Flakes** | **150 Flakes** |
| Homestead Support Claim Paper | **100 Flakes** | **100 Flakes** |
| Town Claim Stake | **1,000 Flakes** | **1,000 Flakes** |

There is no Treasury spread on civic land instruments.

A Town Claim Stake includes 5 claims. At 150 Flakes per Town Claim, 750 Flakes of the 1,000-Flake stake price is embedded claim value and **250 Flakes** is the stake/new-property premium.

## Land mechanics and reserve scale

### Player and property mechanics — Product Owner confirmed in-game

- A player begins the game with **16 personal claims** that can initially be used anywhere.
- Once the player joins a Town, those personal 16 claims can only be used within that Town.
- Those initial 16 claims provide baseline land access; Town-issued claims are additional expansion capacity.
- A **new Claim Stake is required to create a new property**.
- A settlement Claim Stake comes with **5 claims** of its own.
- Additional Claim Papers expand claim capacity without themselves creating another property.

### Settlement generation mechanics

Current settlement defaults used for reserve-scale planning:

- settlement claims per citizen: Town `10`, Country `20`, Federation `40`;
- homestead-support claims per citizen: `5` at Town/Country/Federation;
- settlement claim stakes per citizen: `1.5` at Town/Country/Federation.

A higher-tier settlement's claim supply is additive to claims generated by its member settlements. Country claims/stakes are materially more flexible because they can be used across member Towns, so do not model Country inventory as merely a larger copy of local Town inventory.

### Observed Ironwood Town reserve — 2026-08-15 snapshot

- non-abandoned Ironwood citizens: `33`;
- spawned Town Claim Papers: `330`;
- spawned Homestead Support Claim Papers: `165`;
- spawned Town Claim Stakes: `49`;
- visible Foundation inventory: `167` Town Claim Papers, `140` Homestead Support Claim Papers, `35` Town Claim Stakes.

At locked prices, that visible issuer-controlled inventory had face value **74,050 Flakes** and a 60% circulation ceiling of **44,430 Flakes**.

This is a snapshot only; recalculate as inventory or prices change.

## Future Country — unresolved pricing, participation-dependent monetary treatment

Country claim/stake prices are not yet set.

The Flake reserve does **not** automatically expand merely because any Country forms. It expands when a **Country with a stake in Flakes** formally commits its government-controlled claim/stake assets to the Flake reserve framework.

When a Country takes a stake in Flakes:

- generated claims/stakes are additive to member-Town land resources;
- Country claims/stakes may be usable across member Towns and therefore have greater jurisdictional flexibility;
- only participating issuer-controlled Country land assets with published prices enter the reserve calculation;
- 60% of that additional face value may increase the circulation ceiling;
- additional reserve capacity permits but does not require additional issuance;
- Country pricing/allocation must not make member-Town claims economically irrelevant or create cheap national inventory that bypasses local land policy.

## Remaining economy consolidation

The active recipe-discovery problem is largely complete. Remaining work is administrative and transition-driven:

1. continue synchronizing older stale profession sections in the central Exchange publication when discrepancies are found;
2. normalize grouped/tag-product naming where required;
3. keep civic one-offs, research, Recycling feedstocks and other bounded lanes out of unlimited ordinary Buy orders;
4. recalculate affected chains when a true economy-wide technology transition occurs.

Do not reopen completed profession chains merely because an older table or chat used a different number. Reopen when current Core evidence, live run conditions, or Product Owner direction changes the model.

## Next action

Operate the newly published Baking/Cooking/Recycling markets, continue central-ledger synchronization, and define Country claim/stake prices and allocation policy before a participating Country contributes reserve assets to the Flake framework.
