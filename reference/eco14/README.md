# Eco 14 Mechanical Reference

This directory stores normalized mechanical facts extracted from the Eco 14 Core snapshot used by the project.

## Purpose

Future chats should not require the Product Owner to re-upload `Eco14-Core.zip` merely to answer economy questions that have already been extracted and recorded here.

The raw Core archive is **evidence**, not project design. Project policy, prices, laws, and server-specific decisions belong elsewhere in the repository.

## Source handling

Do not mirror the full Eco Core source tree into this public repository by default.

Instead:

1. identify the Core snapshot by cryptographic hash;
2. extract normalized mechanical facts;
3. preserve the original Core source path for traceability;
4. commit the normalized facts needed for economy, profession, recycling, government, and progression analysis;
5. replace extracted facts when a newer Core snapshot is deliberately adopted.

## Mechanical facts to extract

At minimum, recipe records should preserve:

- recipe/display name;
- required profession skill and level;
- ingredients and amounts;
- outputs and amounts;
- garbage/byproduct outputs and amounts;
- base labor calories;
- base craft time;
- workstation;
- original Core source path.

Additional reference sets may cover:

- item salvage values;
- power requirements;
- profession and specialty data;
- recycling mechanics;
- civic/law mechanics needed to determine what policies Eco can actually enforce;
- pollution and waste mechanics relevant to economic design.

## Authority

Normalized Core facts describe **what Eco 14 mechanically does**.

They do not determine what the planned economy *should* do. Price and policy decisions remain design decisions governed by the root project doctrine and, where applicable, a specific run profile such as `runs/ironwood/`.
