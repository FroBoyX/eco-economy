# Ironwood Economy

This directory contains the current economic implementation for the Ironwood Eco 14 run.

The reusable pricing method lives in `/economy/pricing-model.md`. Eco mechanical facts live under `/reference/eco14/`.

## Source of truth

`prices.json` is the canonical live price ledger for this run.

Profession tables, Exchange tables, shop signs, PNG exports, and economic audits should be generated from or reconciled against that ledger. Do not treat an old screenshot or chat table as more authoritative than the current ledger.

## Status

The ledger begins with values that are currently supported strongly enough to use while the larger profession-by-profession overhaul proceeds.

A value marked `locked` is an intentional current Ironwood decision.

A value marked `working` is usable now but should be revisited when its full input chain is audited from Eco 14 Core.

Unresolved prices should remain absent rather than being filled with legacy guesses.

## Immediate build order

1. foundational anchors and tags;
2. gathering/logging/mining inputs;
3. basic processed materials: boards, masonry, smelting;
4. carpentry, blacksmithing, basic engineering;
5. mechanics and larger workstations;
6. food chains and agriculture;
7. tailoring and later material chains;
8. recycling interactions and recovered-material substitution;
9. remaining advanced professions.

This order may be interrupted when the live server needs a price immediately. Emergency prices should still be recorded in `prices.json` and marked `working` until their dependency chain is audited.
