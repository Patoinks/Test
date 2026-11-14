#!/usr/bin/env python3
"""Theoretical maximum PvP item + PEN + mantra damage ceiling calculator.

Reads data/items.json and data/mantras.json to model how legal standard-PvP gear
(Prophet's Cloak, Shock Trooper Specialist Full Set, Ring of Casters, Isshin's
Ring, Enchant vs Brain food, Nocturnal Gem, Grim weapon enchant debuff, and
Oath/Songchant/Piercing Will/Ether Overdrive Armor PEN) combines with mantra
scaling and the 1.25x/1.50x PvP common-pool modifier caps.

Usage: python deepwoken-pvp-ceiling/src/item_theory.py --target-armor 35
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from ceiling import (
    DATA as MANTRAS_PATH,
    SONGCHANT_SCALING_RATE,
    damage,
    effective_pen,
    net_armor_resistance,
)

ITEMS_PATH = Path(__file__).resolve().parent.parent / "data" / "items.json"

SHOWCASE_MANTRA_IDS = (
    "ceaseless",
    "ceaseless_builder",
    "tornado",
    "electro_carve",
    "champions_whirlthrow",
    "metal_rain",
    "flame_ballista",
    "eclipse_kick",
    "grand_javelin",
)


def load_items(path: Path = ITEMS_PATH) -> dict:
    """Load the PvP items, enchants, and PEN catalog."""
    return json.loads(path.read_text(encoding="utf-8"))


def passive_item_common_bonus(items: dict, *, include_food: bool = True) -> float:
    """Return passive/no-condition common-pool fraction from legal standard PvP items."""
    by_id = {entry["id"]: entry for entry in items["equipment_and_items"]}
    total = (by_id["ring_of_casters"]["percent"] + by_id["isshins_ring"]["percent"]) / 100.0
    if include_food:
        total += by_id["enchant_food"]["percent"] / 100.0
    return total


def max_pen_fraction(
    items: dict,
    *,
    mantra_type: str = "",
    songchant: float = 6,
    songchant_pen_mode: str = "traits_wiki",
    include_oath: bool = True,
    include_prophets_cloak: bool = True,
    include_piercing_will: bool = True,
    include_ether_overdrive: bool = True,
) -> tuple[float, float, bool]:
    """Compute (effective_pen, raw_pen, uncapped) for a PvP mantra setup."""
    pen = items["pen_sources"]
    raw_pen = 0.0
    if include_oath:
        raw_pen += pen["all_oaths_pen"]["pen_fraction"]
    if include_prophets_cloak:
        raw_pen += pen["prophets_cloak"]["pen_fraction"]
    if songchant > 0:
        key = ("songchant_6_uncollapsed_may31"
               if songchant_pen_mode == "uncollapsed_may31"
               else "songchant_6_traits_wiki")
        raw_pen += pen[key]["per_point"] * songchant
    if include_piercing_will:
        raw_pen += pen["piercing_will"]["pen_fraction"]
    if include_ether_overdrive:
        raw_pen += pen["ether_overdrive"]["pen_fraction"]
    if "Ironsing" in mantra_type:
        raw_pen += pen["ironsing_innate"]["pen_fraction"]
    eff = effective_pen(
        raw_pen,
        uncapped=include_ether_overdrive,
        base_cap=pen["base_cap_without_ether_overdrive"],
    )
    return eff, raw_pen, include_ether_overdrive


def evaluate_mantra_with_items(
    mantra: dict,
    items: dict,
    *,
    target_armor: float = 0.35,
    attribute: float = 100,
    songchant: float = 6,
    songchant_rate: float = SONGCHANT_SCALING_RATE,
    songchant_pen_mode: str = "traits_wiki",
) -> dict:
    """Compute PvP item-theory ceilings across gross and armored scenarios for one mantra."""
    if not 0 <= target_armor <= 1:
        raise ValueError("target_armor must be in [0, 1]")

    by_id = {entry["id"]: entry for entry in items["equipment_and_items"]}
    specialist_mult = (
        by_id["specialist_full_set"]["base_damage_multiplier"]
        if mantra.get("specialist_eligible", False)
        else 1.0
    )
    passive_raw = passive_item_common_bonus(items, include_food=True)
    nocturnal_enchant_flat = by_id["nocturnal_gem"]["flat_damage"]
    grim_mult = 1.0 + by_id["grim_weapon_enchant"]["percent"] / 100.0

    # Baseline without Prophet's Cloak or PvP items (only innate Ironsing PEN if any).
    no_gear_pen, _, _ = max_pen_fraction(
        items,
        mantra_type=mantra["type"],
        songchant=songchant,
        songchant_pen_mode=songchant_pen_mode,
        include_oath=False,
        include_prophets_cloak=False,
        include_piercing_will=False,
        include_ether_overdrive=False,
    )
    max_gear_pen, max_raw_pen, uncapped = max_pen_fraction(
        items,
        mantra_type=mantra["type"],
        songchant=songchant,
        songchant_pen_mode=songchant_pen_mode,
        include_oath=True,
        include_prophets_cloak=True,
        include_piercing_will=True,
        include_ether_overdrive=True,
    )

    unbuffed_gross = damage(
        mantra, attribute, songchant, raw_bonus=0.0, target_resistance=0.0,
        songchant_rate=songchant_rate, base_multiplier_override=1.0,
    )
    passive_item_gross = damage(
        mantra, attribute, songchant, raw_bonus=passive_raw, target_resistance=0.0,
        songchant_rate=songchant_rate, base_multiplier_override=specialist_mult,
    )
    full_cap_gross = damage(
        mantra, attribute, songchant, raw_bonus=0.75, target_resistance=0.0,
        songchant_rate=songchant_rate, base_multiplier_override=specialist_mult,
    ) + nocturnal_enchant_flat

    unbuffed_res = net_armor_resistance(target_armor, no_gear_pen)
    max_item_res = net_armor_resistance(target_armor, max_gear_pen)

    unbuffed_vs_armor = unbuffed_gross * (1.0 - unbuffed_res)
    # Uses uniform post-PEN target armor resistance across both cast and Nocturnal slash proc.
    max_item_vs_armor = (
        damage(
            mantra, attribute, songchant, raw_bonus=0.75, target_resistance=max_item_res,
            songchant_rate=songchant_rate, base_multiplier_override=specialist_mult,
        )
        + nocturnal_enchant_flat * (1.0 - max_item_res)
    )
    hypothetical_grim_sep_gross = (
        damage(
            mantra, attribute, songchant, raw_bonus=0.75, target_resistance=0.0,
            extra_final_multiplier=grim_mult,
            songchant_rate=songchant_rate, base_multiplier_override=specialist_mult,
        )
        + nocturnal_enchant_flat
    )

    return {
        "id": mantra["id"],
        "name": mantra["name"],
        "specialist_mult": specialist_mult,
        "passive_raw_bonus": passive_raw,
        "effective_pen": max_gear_pen,
        "raw_pen": max_raw_pen,
        "pen_uncapped": uncapped,
        "unbuffed_gross": unbuffed_gross,
        "passive_item_gross": passive_item_gross,
        "full_cap_plus_nocturnal_gross": full_cap_gross,
        "unbuffed_vs_armor": unbuffed_vs_armor,
        "max_item_vs_armor": max_item_vs_armor,
        "hypothetical_grim_sep_gross": hypothetical_grim_sep_gross,
    }


def format_report(
    *,
    target_armor: float = 0.35,
    attribute: float = 100,
    songchant: float = 6,
    songchant_rate: float = SONGCHANT_SCALING_RATE,
    songchant_pen_mode: str = "traits_wiki",
) -> str:
    """Format a complete human-readable report of PvP item theory + mantra ceiling."""
    items = load_items()
    mantras_by_id = {
        m["id"]: m for m in json.loads(MANTRAS_PATH.read_text(encoding="utf-8"))["mantras"]
    }
    passive_pct = passive_item_common_bonus(items, include_food=True) * 100.0
    lines = [
        "=== MAX PVP ITEM THEORY + MANTRA CEILING ===",
        f"Loadout (Legal Standard PvP): Prophet's Cloak (+20% PEN Outfit)"
        f" + Ring of Casters (+5%) + Isshin's Ring (+15%) + Enchant Food (+5%) = +{passive_pct:.0f}% passive (exact 1.25x soft cap!)",
        "Optional Gear Bypass: Shock Trooper Specialist Full Set (Head/Arms/Legs -> +15% base on 6 Thundercall/Gale mantras; coexists w/ Prophet's Cloak)",
        "Capped + Gem Max: Full Cap Pool x1.50 (via items + Perfect Flash/Taunt/Potion) + Nocturnal Gem (+10 fixed slash proc, 1-proc conservative) + Armor PEN stack (Oath +5%, Songchant +15%, Piercing Will +15%, Ether Overdrive +5% & uncap)",
        f"Params: Attr={attribute:g}, Songchant={songchant:g} (scaling rate={songchant_rate:.3f}, PEN mode={songchant_pen_mode}), Target Pre-PEN Armor={target_armor*100:.0f}%\n",
        f"{'MANTRA':<43} {'NO-ITEM':>8} {'PASSIVE':>8} {'MAX+NOC':>8} {'VS ARMOR(0->MAX)':>17} {'PEN':>5} {'GRIM?':>8}",
    ]
    rows = [
        evaluate_mantra_with_items(
            mantras_by_id[mid],
            items,
            target_armor=target_armor,
            attribute=attribute,
            songchant=songchant,
            songchant_rate=songchant_rate,
            songchant_pen_mode=songchant_pen_mode,
        )
        for mid in SHOWCASE_MANTRA_IDS
        if mid in mantras_by_id
    ]
    rows.sort(key=lambda r: r["full_cap_plus_nocturnal_gross"], reverse=True)
    for r in rows:
        tag = f"{r['name']} [*1.15]" if r["specialist_mult"] > 1.0 else r["name"]
        vs_pair = f"{r['unbuffed_vs_armor']:6.1f} -> {r['max_item_vs_armor']:6.1f}"
        lines.append(
            f"{tag:<43} {r['unbuffed_gross']:8.2f} {r['passive_item_gross']:8.2f} "
            f"{r['full_cap_plus_nocturnal_gross']:8.2f} {vs_pair:>17} "
            f"{r['effective_pen']*100:4.0f}% {r['hypothetical_grim_sep_gross']:8.2f}"
        )

    lines.extend([
        "",
        "NOTES & EXCLUSIONS:",
        "- [*1.15] marks Shock Trooper Specialist Full Set +15% base bypass (cannot use 3 Armor Enchants, which already give 0 PvP mantra dmg).",
        "- GRIM? shows *hypothetical* upper bound if Grim weapon enchant (+25% dmg taken, 6s) sits outside the x1.50 cap; if inside, it adds +0% above saturated cap.",
        "- NO PvP Mantra Damage comes from Equipment Pips, Armor Enchants (Drowned is PvE-only), or Scaling Rings (weapon scaling only).",
        "- QUARANTINED: Divine Cast Ring (3x mantra) is Vow of Iron Relic ONLY (illegal in standard PvP).",
        "- UNQUANTIFIED: Yun'Shul Wind-Up Lv10 Bell (exact % unknown on Wiki) and Brain Food (+5 per Nocturnal proc vs Enchant +5% mantra).",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target-armor", type=float, default=35.0,
                        help="Target pre-PEN armor resistance in percent (default: 35)")
    parser.add_argument("--attribute", type=float, default=100)
    parser.add_argument("--songchant", type=float, default=6)
    parser.add_argument("--songchant-rate", type=float, default=SONGCHANT_SCALING_RATE)
    parser.add_argument("--songchant-pen-mode", choices=("traits_wiki", "uncollapsed_may31"),
                        default="traits_wiki")
    args = parser.parse_args()
    print(format_report(
        target_armor=args.target_armor / 100.0,
        attribute=args.attribute,
        songchant=args.songchant,
        songchant_rate=args.songchant_rate,
        songchant_pen_mode=args.songchant_pen_mode,
    ))


if __name__ == "__main__":
    main()
