# Ironwood Current State

This file is the short-form recovery checkpoint for the current Ironwood run.

It is intentionally overwritten as the run changes. It is not a historical log and must not accumulate obsolete assumptions for preservation purposes.

## Recovery checkpoint

Recovered against `main` after commit `b88dfbd40977e57ec07ef3ef0bdc8e4ef0cee493` (`Rebuild Steam-era Exchange publication with full Tailoring and research`).

The repository remains canonical. Chat sessions are working sessions.

## Current progression

Ironwood is **entering the Steam era**.

Live pricing is based on the best normal routes actually available in the current run. Future Oil, Electronics, Industry, advanced food, Composites, Advanced Masonry, and other later efficiencies do not back-propagate into current prices.

## Active profession coverage

The active Tier 1-3 economy is source-audited and priced/scoped far enough for live public use.

### Canonical-current

- Gathering
- Farming
- Milling
- Fertilizers
- Hunting
- Butchery
- Campfire Cooking
- Baking
- Cooking
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
- Recycling (activation-sensitive by recovery stream)

Self Improvement remains a policy/special lane rather than an ordinary commodity profession.

### Future-transition, not current price setters

- Advanced Baking
- Advanced Cooking
- Cutting Edge Cooking
- Composites
- Advanced Masonry
- Advanced Smelting
- Electronics
- Industry
- Oil Drilling
- later petroleum / Plastic / Epoxy routes
- later Nylon / industrial textile routes

Steel and other later outputs may be inspected for planning without becoming current Steam-entry price setters.

## Current canonical publication

`economy/steam-era-exchange-tables.md` is the current shop-facing Steam-entry publication.

It includes:

- raw/gathering anchors;
- active production specialties;
- current Tailoring outputs;
- current research-paper procurement prices;
- generic Basic / Advanced / Modern research upgrades;
- current disposal/reference rows where appropriate.

Research papers use **capped Library procurement**, not unlimited Exchange demand.

## Current pricing doctrine

- Stable nominal prices; increasing player efficiency creates increasing margin.
- Same-specialty intermediates enter deeper same-specialty recipes at Projected Cost.
- Cross-specialty inputs enter at Town Sell.
- Same-specialty raw anchors enter at Town Buy / opportunity value.
- Direct-sale markup is applied once rather than recursively compounded through a specialty.
- Bulk construction materials may retain explicit policy prices.
- Civic allocations, research, recycling, garbage, emergency interventions, and other exceptional goods may use policy pricing rather than ordinary recipe markup.

## Remaining economy consolidation

The active recipe-discovery problem is substantially complete. Remaining work is mainly administrative/presentation:

1. keep the central price ledger synchronized with the current profession files and publication;
2. normalize grouped/tag-product naming where required;
3. keep civic one-offs and unopened Recycling streams out of unlimited ordinary Buy orders;
4. produce/update player-facing profession tables as needed from the current canonical values.

Do not reopen completed profession chains merely because an older table or chat used a different number. Reopen only when current Core evidence, run conditions, or Product Owner direction changes the model.

## Flake monetary policy — current

Canonical policy: `economy/flake-monetary-policy.md`.

The **Ironwood Flake** replaces FroBoyX Credit as the run's fiat currency under a land-reserve issuance rule.

Current decisions:

- existing FroBoyX Credit is permanently redeemable into Flakes at **1:1**;
- no new FroBoyX Credit is issued after cutover;
- each player Active at cutover receives a **one-time 180-Flake capitalization grant**;
- a player not Active at cutover receives the same **one-time 180-Flake grant on first becoming Active**;
- losing and regaining Active status does not create another grant;
- the issuing authority limits net Flake circulation outside sterilized issuer reserves to **60% of the current face value of unsold sellable civic land instruments it actually controls**;
- reserve capacity is a ceiling, not a requirement to print;
- land-sale receipts are sterilized/retired rather than immediately recycled as ordinary spending while required to preserve the reserve rule;
- the Flake is intended to circulate outside Ironwood; other players and future Towns can acquire it through Exchange trade, procurement, public works, research, and other authorized transactions with the issuing authority.

### Current Town real-estate prices — LOCKED

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
- Those initial 16 claims therefore provide the player's baseline land access; Town-issued claims are additional expansion capacity, not the player's starter allotment.
- A **new Claim Stake is required to create a new property**.
- A settlement Claim Stake comes with **5 claims** of its own.
- Additional Claim Papers expand claim capacity without themselves creating another property.

### Settlement generation mechanics

Current settlement defaults used for reserve-scale planning:

- settlement claims per citizen: Town `10`, Country `20`, Federation `40`;
- homestead-support claims per citizen: `5` at Town/Country/Federation;
- settlement claim stakes per citizen: `1.5` at Town/Country/Federation.

A higher-tier settlement's claim supply is **additive** to the claims generated by its member settlements. A future Country therefore creates a large additional Country claim/stake reserve on top of the existing Town reserves.

Country claims and stakes are materially more flexible because they can be used across the Country's member Towns. Do not model Country inventory as merely a larger copy of a local Town inventory or price it cheaply enough to bypass member-Town land policy.

### Observed Ironwood Town reserve — 2026-08-15

In-game Foundation screenshot:

- non-abandoned citizens: `33`;
- spawned Town Claim Papers: `330`;
- spawned Homestead Support Claim Papers: `165`;
- spawned Town Claim Stakes: `49`;
- currently visible Foundation inventory: `167` Town Claim Papers, `140` Homestead Support Claim Papers, `35` Town Claim Stakes.

At the locked prices, the visible issuer-controlled inventory has a face value of **74,050 Flakes** and a 60% printable reserve ceiling of **44,430 Flakes**.

This is a snapshot only; recalculate as inventory or prices change.

## Future Country — unresolved pricing, resolved monetary treatment

Country claim/stake prices are not yet set.

When a Country forms:

- its generated claims/stakes are additive to member-Town land resources;
- Country claims/stakes may be usable across member Towns and therefore have greater jurisdictional flexibility;
- only Country land assets actually controlled by the issuing authority and assigned published Country prices enter the reserve calculation;
- 60% of that additional face value may increase the printable reserve ceiling;
- additional reserve capacity permits but does not require additional issuance;
- Country pricing/allocation must not make member-Town claims economically irrelevant or create cheap national inventory that bypasses local land policy.

## Next action

Implement/publish the Flake cutover and Town real-estate schedule, then define Country claim/stake prices and allocation policy before Country reserve assets are placed into ordinary sale.
