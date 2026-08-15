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

## Active unresolved lane — land allocation and monetary reserve

The next policy/economy decision is pricing and distribution of settlement-generated land resources:

- Town/Country Claim Papers;
- Town/Country Claim Stakes;
- Homestead Support Claim Papers;
- the separately craftable Homestead Claim Stake item where relevant.

Settlement-generated claims and stakes are **high-value limited civic assets**. They must not be priced as ordinary commodities simply because they can appear in a store. The craftable Homestead Claim Stake remains a separate manufactured-good calculation.

### Player and property mechanics — Product Owner confirmed in-game

- A player begins the game with **16 personal claims** that can initially be used anywhere.
- Once the player joins a Town, those personal 16 claims can only be used within that Town.
- Those initial 16 claims therefore provide the player's baseline land access; Town-issued claims are additional expansion capacity, not the player's starter allotment.
- A **new Claim Stake is required to create a new property**.
- A settlement Claim Stake comes with **5 claims** of its own.
- Additional Claim Papers expand claim capacity without themselves creating another property.

This observed run behavior overrides prior recovery assumptions that starter land needed to be solved through cheap Town-issued claims.

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

The difference between spawned total and Foundation inventory is already outside the Foundation; do not assume all spawned assets remain available for new sale.

### Currency-policy relationship

The Ironwood Flake is intended to become the fiat currency. The planned initial active-player capitalization remains **150 Flakes**.

The issuing authority must also provide a path for other Towns to acquire currency. Land claims/stakes therefore interact with monetary policy as well as land policy:

- currency is issued outward through useful spending, procurement, capitalization, public works, research, and inter-settlement activity;
- scarce civic assets sold for Flakes can pull currency back toward the issuing authority;
- claim pricing can create durable demand for the currency without relying on arbitrary recurring taxes;
- claim sales must not remove so much liquidity that new players or member Towns cannot conduct ordinary trade.

A future Country's large portable claim reserve makes this monetary role more important, not less. Country claims should function as a strategic reserve/backstop and monetary sink rather than cheap national inventory that destroys the member Town claim market.

Do **not** assume the current `FroBoyX Credit` report converts to Flakes at 1:1 until that conversion policy is explicitly decided.

### Pricing status

Current working proposal:

- **Town Claim Paper: 150 Flakes**;
- **Homestead Support Claim Paper: 100 Flakes**.

These remain provisional until explicitly locked.

Because each new settlement Claim Stake includes 5 claims, a Town Claim Stake has at least **750 Flakes of embedded claim-paper value** at the 150-Flake claim price before assigning any premium for the scarce right to create an additional property.

Claim Stake and future Country prices remain unresolved.

## Next action

Resolve the Town Claim Stake price from its 5 included claims plus the new-property premium, then define Country claim/stake prices and reserve policy so the additive cross-town Country supply cannot undercut member Town land policy.
