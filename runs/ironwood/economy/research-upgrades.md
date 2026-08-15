# Ironwood Research Upgrades — Basic through Modern

Source: supplied Eco 14 Core (`Eco14-Core(3).zip`) plus the canonical Ironwood research-paper prices in `runs/ironwood/economy/research-papers.md`.

These are the three generic Self Improvement upgrade modules: **Basic Upgrade**, **Advanced Upgrade**, and **Modern Upgrade**.

## Pricing rule

- Craft at the recipe's minimum unlock: **Self Improvement 1**.
- Self Improvement uses its own Core efficiency curve: at level 1, ingredient and labor cost are reduced by **5%**, not the normal 20% used by most specialties.
- All research-paper inputs cross into Self Improvement and therefore use **Library Town Sell** prices.
- Tagged `Basic Research`, `Advanced Research`, and `Modern Research` inputs use the cheapest valid paper in that tier at current Library prices.
- Labor uses the Ironwood calorie anchor: **1 credit / 1,000 calories**.
- The 0.2 Trash output is carried as a small disposal cost under the current garbage policy.
- These are reusable efficiency modules/capital goods, so Ironwood applies the ordinary **30% upgrade/capital margin**.
- Town Sell uses the standard Ironwood spread: 5% when below the cap, otherwise the +10-credit cap for goods over 100 credits.

## Canonical Upgrade Prices

| Upgrade | Projected Cost | Town Buys | Town Sells |
|---|---:|---:|---:|
| Basic Upgrade | **52.50** | **68.25** | **71.66** |
| Advanced Upgrade | **259.83** | **337.78** | **347.78** |
| Modern Upgrade | **526.06** | **683.88** | **693.88** |

## Core recipe basis

### Basic Upgrade

Base Core recipe:

- 2 Dendrology Research Paper Advanced
- 2 Gathering Research Paper Basic
- 1 Agriculture Research Paper Basic
- 5 of any `Basic Research`
- 1,500 calories
- 0.2 Trash

At Self Improvement 1, the 5% reduction produces an effective cost basis of approximately:

- 1.90 × Dendrology Advanced at 20.00 Town Sell
- 1.90 × Gathering Basic at 1.85 Town Sell
- 0.95 × Agriculture Basic at 3.52 Town Sell
- 4.75 × cheapest Basic Research (Culinary Basic at 1.30 Town Sell)
- 1,425 calories
- disposal

**Projected Cost: 52.50**

### Advanced Upgrade

Base Core recipe:

- 2 Engineering Research Paper Modern
- 2 Culinary Research Paper Advanced
- 1 Agriculture Research Paper Advanced
- 5 of any `Advanced Research`
- 3,000 calories
- 0.2 Trash

At Self Improvement 1:

- 1.90 × Engineering Modern at 79.02 Town Sell
- 1.90 × Culinary Advanced at 24.83 Town Sell
- 0.95 × Agriculture Advanced at 31.16 Town Sell
- 4.75 × cheapest Advanced Research (Gathering Advanced at 6.32 Town Sell)
- 2,850 calories
- disposal

**Projected Cost: 259.83**

### Modern Upgrade

Base Core recipe:

- 2 Metallurgy Research Paper Modern
- 2 Agriculture Research Paper Modern
- 1 Culinary Research Paper Modern
- 5 of any `Modern Research`
- 4,500 calories
- 0.2 Trash

At Self Improvement 1:

- 1.90 × Metallurgy Modern at 93.28 Town Sell
- 1.90 × Agriculture Modern at 70.88 Town Sell
- 0.95 × Culinary Modern at 71.84 Town Sell
- 4.75 × cheapest Modern Research (Geology Modern at 29.81 Town Sell)
- 4,275 calories
- disposal

**Projected Cost: 526.06**

## Market treatment

These are not research-paper procurement items. They are reusable production-capital goods and may be handled as normal limited Exchange inventory rather than unlimited civic paper demand. The 30% Town Buy margin is consistent with Ironwood's workstation/upgrade pricing doctrine.