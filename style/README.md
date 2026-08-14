# Reusable Presentation Style

This directory defines presentation conventions and reusable rendering behavior for Eco Economy outputs.

It must remain server-agnostic.

## Separation rule

Generic renderers may define semantic roles such as:

- primary/accent;
- header background;
- header text;
- section background;
- body background;
- body text;
- grid;
- warning/accent roles where needed.

They should accept a run-specific palette rather than hard-code Ironwood colors.

Run palettes belong under:

`runs/<run-name>/style/`

For example, Ironwood's canonical primary color belongs in `runs/ironwood/style/palette.json`.

## Table style goals

Price tables should remain deterministic and readable:

- clean header band;
- restrained section bands;
- light body background;
- thin muted grid;
- high-contrast text;
- exact numeric values;
- no fake item icons;
- no decorative clutter;
- no unnecessary footer;
- equivalent same-price items may be condensed when that improves readability.

The renderer and palette should be stored in the repository so future tables can be reproduced without relying on conversation memory.
