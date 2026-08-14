#!/usr/bin/env python3
"""Extract normalized recipe facts from an Eco 14 Core zip.

This intentionally extracts facts rather than copying source code. The output is
suitable for committing under reference/eco14/ and can be regenerated whenever
a new Core snapshot is deliberately adopted.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path


def _number(value: str) -> float:
    return float(value.rstrip("fF"))


def parse_recipe(path: str, text: str) -> dict | None:
    families = re.findall(
        r"public\s+partial\s+class\s+(\w+Recipe)\s*:\s*RecipeFamily", text
    )
    if not families or "recipe.Init(" not in text:
        return None

    display = re.search(r'displayName:\s*Localizer\.DoStr\("([^"]+)"\)', text)
    required = re.search(
        r"\[RequiresSkill\(typeof\((\w+Skill)\),\s*(\d+)\)\]", text
    )
    labor = re.search(
        r"LaborInCalories\s*=\s*CreateLaborInCaloriesValue\("
        r"([-\d.]+),\s*typeof\((\w+Skill)\)\)",
        text,
    )
    craft = re.search(
        r"CreateCraftTimeValue\([^;]*?start:\s*([\d.]+)", text, re.S
    )
    table = re.search(
        r"CraftingComponent\.AddRecipe\(tableType:\s*typeof\((\w+Object)\)", text
    )

    ingredients: list[dict] = []
    ingredient_block = re.search(
        r"ingredients:\s*new List<IngredientElement>\s*\{(.*?)\}\s*,\s*garbages:",
        text,
        re.S,
    )
    if ingredient_block:
        block = ingredient_block.group(1)
        for match in re.finditer(
            r"new IngredientElement\(typeof\((\w+Item)\),\s*([\d.]+)(?:f)?"
            r"(?:,\s*typeof\((\w+Skill)\))?",
            block,
        ):
            ingredients.append(
                {
                    "item": match.group(1),
                    "amount": _number(match.group(2)),
                    "skill": match.group(3),
                }
            )
        for match in re.finditer(
            r'new IngredientElement\("([^"]+)"\s*,\s*([\d.]+)(?:f)?'
            r"(?:,\s*typeof\((\w+Skill)\))?",
            block,
        ):
            ingredients.append(
                {
                    "tag": match.group(1),
                    "amount": _number(match.group(2)),
                    "skill": match.group(3),
                }
            )

    garbage_outputs: list[dict] = []
    garbage_block = re.search(
        r"garbages:\s*new List<GarbageOutput>\s*\{(.*?)\}\s*,\s*"
        r"// Define our recipe output items",
        text,
        re.S,
    )
    if garbage_block:
        block = garbage_block.group(1)
        for match in re.finditer(
            r"new GarbageOutput\(typeof\((\w+)\),\s*([\d.]+)(?:f)?\)", block
        ):
            garbage_outputs.append(
                {"item": match.group(1), "amount": _number(match.group(2))}
            )
        for match in re.finditer(
            r'new GarbageOutput\("([^"]+)"\s*,\s*([\d.]+)(?:f)?\)', block
        ):
            garbage_outputs.append(
                {"tag": match.group(1), "amount": _number(match.group(2))}
            )

    outputs: list[dict] = []
    output_block = re.search(
        r"items:\s*new List<CraftingElement>\s*\{(.*?)\}\s*\)\s*;", text, re.S
    )
    if output_block:
        for match in re.finditer(
            r"new CraftingElement<([^>]+)>\(\s*([^)]*)\)", output_block.group(1)
        ):
            argument = match.group(2).strip()
            amount_match = re.search(r"([\d.]+)(?:f)?", argument) if argument else None
            outputs.append(
                {
                    "item": match.group(1),
                    "amount": _number(amount_match.group(1)) if amount_match else 1.0,
                }
            )

    return {
        "recipe_class": families[0],
        "display_name": display.group(1) if display else families[0].removesuffix("Recipe"),
        "required_skill": required.group(1) if required else None,
        "required_level": int(required.group(2)) if required else None,
        "labor_calories_base": _number(labor.group(1)) if labor else None,
        "craft_minutes_base": _number(craft.group(1)) if craft else None,
        "workstation": table.group(1) if table else None,
        "ingredients": ingredients,
        "garbage_outputs": garbage_outputs,
        "outputs": outputs,
        "source_path": path,
    }


def extract(zip_path: Path) -> dict:
    digest = hashlib.sha256(zip_path.read_bytes()).hexdigest()
    recipes: list[dict] = []

    with zipfile.ZipFile(zip_path) as archive:
        for path in archive.namelist():
            if not path.lower().endswith(".cs"):
                continue
            text = archive.read(path).decode("utf-8", "replace")
            recipe = parse_recipe(path, text)
            if recipe:
                recipes.append(recipe)

    recipes.sort(key=lambda row: (row["display_name"], row["recipe_class"]))
    return {
        "schema_version": 1,
        "source_sha256": digest,
        "recipe_count": len(recipes),
        "recipes": recipes,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("core_zip", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    data = extract(args.core_zip)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"Wrote {data['recipe_count']} recipes to {args.output}")


if __name__ == "__main__":
    main()
