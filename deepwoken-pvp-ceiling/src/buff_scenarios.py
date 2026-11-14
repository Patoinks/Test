#!/usr/bin/env python3
"""Conditional buff-pool audit backed by data/buffs.json.

Models PvP common-pool modifier combinations under HP state rules,
attunement restrictions, exclusive groups, and single-phase build budgets.
Respects Strengthening Potion Nov-2025 nerf uncertainty (recipe_model 27.5%
vs halved 13.75% vs excluded).

Usage: python deepwoken-pvp-ceiling/src/buff_scenarios.py
"""
from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

from ceiling import pvp_damage_modifier

BUFFS_PATH = Path(__file__).resolve().parent.parent / "data" / "buffs.json"
MAX_BUILD_POINTS = 330  # Power 20 total attribute points (excluding Shrine-of-Order tricks)


def _resolve_percent(entry: dict, potion_mode: str) -> float | None:
    """Resolve effective nominal percent for an eligible buff entry."""
    if entry["id"] == "strengthening_potion":
        if entry.get("live_pvp_percent") is not None:
            return float(entry["live_pvp_percent"])
        recipe = entry.get("model_recipe_percent_before_patch_adjustment", entry.get("percent"))
        if recipe is None or potion_mode == "exclude":
            return None
        if potion_mode == "halved_2025_nerf":
            return float(recipe) / 2.0
        if potion_mode == "recipe_model":
            return float(recipe)
        raise ValueError(f"Unknown potion_mode: {potion_mode}")
    pct = entry.get("percent", entry.get("percent_max"))
    return float(pct) if pct is not None else None


def load_common_buffs(
    path: Path = BUFFS_PATH,
    potion_mode: str = "recipe_model",
) -> dict[str, dict]:
    """Load eligible common-pool mantra buffs from data/buffs.json."""
    raw = json.loads(path.read_text(encoding="utf-8"))
    out: dict[str, dict] = {}
    for entry in raw["buffs"]:
        if not entry.get("model_in_common_pool"):
            continue
        pct = _resolve_percent(entry, potion_mode)
        if pct is None:
            continue
        out[entry["id"]] = {**entry, "effective_percent": pct}
    return out


COMMON_BUFFS = load_common_buffs()


def required_attribute_sum(
    selected_ids: tuple[str, ...] | list[str],
    attunement: str = "Light Weapon",
    primary_investment: int = 100,
    buffs: dict[str, dict] | None = None,
) -> dict[str, int]:
    """Compute naive single-phase attribute minimums for the selected buffs."""
    catalog = buffs if buffs is not None else COMMON_BUFFS
    reqs: dict[str, int] = {attunement: primary_investment} if primary_investment > 0 else {}
    for bid in selected_ids:
        for attr, val in catalog[bid].get("required_stats", {}).items():
            reqs[attr] = max(reqs.get(attr, 0), int(val))
    return reqs


def valid(
    selected_ids: tuple[str, ...] | list[str],
    attunement: str = "Light Weapon",
    caster_hp_percent: float = 100,
    *,
    is_night_or_depths: bool = True,
    strict_hp: bool = True,
    max_build_points: int | None = MAX_BUILD_POINTS,
    primary_investment: int = 100,
    buffs: dict[str, dict] | None = None,
) -> bool:
    """Validate state compatibility, mutual exclusions, and build point budget."""
    catalog = buffs if buffs is not None else COMMON_BUFFS
    chosen = set(selected_ids)
    exclusive_seen: dict[str, str] = {}

    for bid in chosen:
        meta = catalog[bid]
        incompat = set(meta.get("incompatible_with", []))
        if incompat & chosen:
            return False

        group = meta.get("exclusive_group")
        if group:
            if group in exclusive_seen:
                return False
            exclusive_seen[group] = bid

        allowed_types = meta.get("attunements")
        if allowed_types and attunement not in allowed_types:
            return False

        if bid == "dark_hours" and not is_night_or_depths:
            return False

        min_hp_gt = meta.get("min_hp_gt")
        if min_hp_gt is not None and caster_hp_percent <= min_hp_gt:
            return False

        max_hp_lt = meta.get("max_hp_lt")
        if max_hp_lt is not None and caster_hp_percent >= max_hp_lt:
            return False

    if strict_hp and "perfect_flash" in chosen:
        for bid in chosen:
            if catalog[bid].get("breaks_full_hp_without_heal"):
                return False

    if max_build_points is not None:
        reqs = required_attribute_sum(selected_ids, attunement, primary_investment, catalog)
        if sum(reqs.values()) > max_build_points:
            return False

    return True


def ranked(
    attunement: str = "Light Weapon",
    caster_hp_percent: float = 100,
    *,
    is_night_or_depths: bool = True,
    strict_hp: bool = True,
    max_build_points: int | None = MAX_BUILD_POINTS,
    primary_investment: int = 100,
    buffs: dict[str, dict] | None = None,
) -> list[tuple[float, float, int, tuple[str, ...]]]:
    """Return valid combinations sorted by effective multiplier, fewest buffs, lowest stat cost."""
    catalog = buffs if buffs is not None else COMMON_BUFFS
    entries = list(catalog)
    outcomes = []
    for n in range(1, len(entries) + 1):
        for selected in combinations(entries, n):
            if not valid(
                selected,
                attunement,
                caster_hp_percent,
                is_night_or_depths=is_night_or_depths,
                strict_hp=strict_hp,
                max_build_points=max_build_points,
                primary_investment=primary_investment,
                buffs=catalog,
            ):
                continue
            nominal = sum(catalog[s]["effective_percent"] / 100.0 for s in selected)
            stat_total = sum(
                required_attribute_sum(selected, attunement, primary_investment, catalog).values()
            )
            outcomes.append((pvp_damage_modifier(nominal), nominal, stat_total, selected))
    return sorted(outcomes, key=lambda x: (x[0], -len(x[3]), -x[2], -x[1]), reverse=True)


def _format_scenario(
    attunement: str,
    hp: float,
    *,
    strict_hp: bool,
    potion_mode: str = "recipe_model",
) -> None:
    catalog = load_common_buffs(potion_mode=potion_mode)
    max_pts = MAX_BUILD_POINTS if strict_hp else None
    result = ranked(
        attunement,
        hp,
        strict_hp=strict_hp,
        max_build_points=max_pts,
        buffs=catalog,
    )
    mode = f"strict (<= {MAX_BUILD_POINTS} pts, {potion_mode})" if strict_hp else f"unconstrained ({potion_mode})"
    if not result:
        print(f"\n{attunement}, HP={hp}% [{mode}]: NO valid combinations")
        return
    effective, nominal, stat_total, buff_ids = result[0]
    print(f"\n{attunement}, HP={hp}% [{mode}]: x{effective:.3f} (raw +{nominal*100:.1f}%, {stat_total} min attr pts)")
    for bid in buff_ids:
        b = catalog[bid]
        print(f" - {b['name']} (+{b['effective_percent']:g}%)")


if __name__ == "__main__":
    for element in ("Light Weapon", "Galebreathe", "Shadowcast", "Flamecharm"):
        _format_scenario(element, 100, strict_hp=True, potion_mode="recipe_model")
        _format_scenario(element, 100, strict_hp=True, potion_mode="halved_2025_nerf")
        _format_scenario(element, 20, strict_hp=True, potion_mode="recipe_model")
    print("\nNote: Shadowcast assumes night/Depths (+15% Dark Hours). Flamecharm Lv5 Fan the Flames needs 80 Galebreathe.")
    print("Strengthening potion 27.5% vs 13.75% reflects Nov-2025 50% potion-nerf patch uncertainty (verify in-game).")
