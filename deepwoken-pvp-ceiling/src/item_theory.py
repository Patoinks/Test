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
    CEASELESS_IDS,
    DATA as MANTRAS_PATH,
    SONGCHANT_SCALING_RATE,
    damage,
    effective_pen,
    filter_mantras,
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
    nocturnal_brain_flat = by_id["nocturnal_gem"]["flat_damage_with_brain"]
    grim_mult = 1.0 + by_id["grim_weapon_enchant"]["percent"] / 100.0
    sear_cauterize_pen = by_id["sear_weapon_enchant"]["cauterize_max_pen_fraction"]

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
    sear_pen_effective = effective_pen(
        max_raw_pen + sear_cauterize_pen,
        uncapped=uncapped,
        base_cap=items["pen_sources"]["base_cap_without_ether_overdrive"],
    )

    unbuffed_gross = damage(
        mantra, attribute, songchant, raw_bonus=0.0, target_resistance=0.0,
        songchant_rate=songchant_rate, base_multiplier_override=1.0,
    )
    passive_item_gross = damage(
        mantra, attribute, songchant, raw_bonus=passive_raw, target_resistance=0.0,
        songchant_rate=songchant_rate, base_multiplier_override=specialist_mult,
    )
    full_cap_cast = damage(
        mantra, attribute, songchant, raw_bonus=0.75, target_resistance=0.0,
        songchant_rate=songchant_rate, base_multiplier_override=specialist_mult,
    )
    full_cap_gross = full_cap_cast + nocturnal_enchant_flat
    brain_max_gross = full_cap_cast + nocturnal_brain_flat

    unbuffed_res = net_armor_resistance(target_armor, no_gear_pen)
    max_item_res = net_armor_resistance(target_armor, max_gear_pen)
    sear_res = net_armor_resistance(target_armor, sear_pen_effective)

    unbuffed_vs_armor = unbuffed_gross * (1.0 - unbuffed_res)
    # Uses uniform post-PEN target armor resistance across both cast and Nocturnal slash proc.
    max_item_vs_armor = (
        damage(
            mantra, attribute, songchant, raw_bonus=0.75, target_resistance=max_item_res,
            songchant_rate=songchant_rate, base_multiplier_override=specialist_mult,
        )
        + nocturnal_enchant_flat * (1.0 - max_item_res)
    )
    sear_brain_vs_armor = (
        damage(
            mantra, attribute, songchant, raw_bonus=0.75, target_resistance=sear_res,
            songchant_rate=songchant_rate, base_multiplier_override=specialist_mult,
        )
        + nocturnal_brain_flat * (1.0 - sear_res)
    )
    hypothetical_grim_sep_gross = (
        damage(
            mantra, attribute, songchant, raw_bonus=0.75, target_resistance=0.0,
            extra_final_multiplier=grim_mult,
            songchant_rate=songchant_rate, base_multiplier_override=specialist_mult,
        )
        + nocturnal_enchant_flat
    )
    hypothetical_grim_brain_vs_armor = (
        damage(
            mantra, attribute, songchant, raw_bonus=0.75, target_resistance=max_item_res,
            extra_final_multiplier=grim_mult,
            songchant_rate=songchant_rate, base_multiplier_override=specialist_mult,
        )
        + nocturnal_brain_flat * (1.0 - max_item_res)
    )

    return {
        "id": mantra["id"],
        "skill_group": mantra.get("skill_group", mantra["id"]),
        "name": mantra["name"],
        "type": mantra["type"],
        "status": mantra.get("status", ""),
        "specialist_mult": specialist_mult,
        "passive_raw_bonus": passive_raw,
        "effective_pen": max_gear_pen,
        "sear_effective_pen": sear_pen_effective,
        "raw_pen": max_raw_pen,
        "pen_uncapped": uncapped,
        "unbuffed_gross": unbuffed_gross,
        "passive_item_gross": passive_item_gross,
        "full_cap_plus_nocturnal_gross": full_cap_gross,
        "brain_max_gross": brain_max_gross,
        "unbuffed_vs_armor": unbuffed_vs_armor,
        "max_item_vs_armor": max_item_vs_armor,
        "sear_brain_vs_armor": sear_brain_vs_armor,
        "hypothetical_grim_sep_gross": hypothetical_grim_sep_gross,
        "hypothetical_grim_brain_vs_armor": hypothetical_grim_brain_vs_armor,
    }


def _is_unproven_or_stale(status: str) -> bool:
    low = status.lower()
    return ("unproven" in low) or ("stale" in low)


def deduplicate_skill_groups(rows: list[dict], *, sort_key: str = "sear_brain_vs_armor") -> list[dict]:
    """Keep the highest-damage variant per canonical skill_group so one mantra cannot take two slots."""
    best_by_group: dict[tuple[str, str], dict] = {}
    for r in sorted(rows, key=lambda x: x[sort_key], reverse=True):
        key = (r["type"], r.get("skill_group", r["id"]))
        if key not in best_by_group:
            best_by_group[key] = r
    return list(best_by_group.values())


def top_n_by_attunement(
    rows: list[dict],
    top_n: int = 6,
    *,
    sort_key: str = "sear_brain_vs_armor",
) -> list[dict]:
    """Group deduplicated mantras by attunement and summarize top-N kit ceilings."""
    grouped: dict[str, list[dict]] = {}
    for r in deduplicate_skill_groups(rows, sort_key=sort_key):
        grouped.setdefault(r["type"], []).append(r)

    summaries = []
    for att_name, grp in grouped.items():
        grp.sort(key=lambda r: r[sort_key], reverse=True)
        picked = grp[:top_n]
        summaries.append({
            "attunement": att_name,
            "skills": picked,
            "count": len(picked),
            "no_item_sum": sum(r["unbuffed_gross"] for r in picked),
            "passive_sum": sum(r["passive_item_gross"] for r in picked),
            "sear_brain_sum": sum(r["sear_brain_vs_armor"] for r in picked),
            "max_item_vs_armor_sum": sum(r["max_item_vs_armor"] for r in picked),
            "grim_brain_vs_armor_sum": sum(r["hypothetical_grim_brain_vs_armor"] for r in picked),
        })
    summaries.sort(key=lambda s: (s["count"], s["sear_brain_sum"]), reverse=True)
    return summaries


def _format_row(r: dict) -> str:
    tag = f"{r['name']} [*1.15]" if r["specialist_mult"] > 1.0 else r["name"]
    vs_pair = f"{r['unbuffed_vs_armor']:6.1f} -> {r['max_item_vs_armor']:6.1f}"
    return (
        f"{tag:<43} {r['type']:<26} {r['unbuffed_gross']:8.2f} {r['passive_item_gross']:8.2f} "
        f"{r['full_cap_plus_nocturnal_gross']:8.2f} {r['brain_max_gross']:8.2f} {vs_pair:>17} "
        f"{r['effective_pen']*100:4.0f}% {r['sear_brain_vs_armor']:9.2f} {r['hypothetical_grim_brain_vs_armor']:11.2f}"
    )


def format_report(
    *,
    target_armor: float = 0.35,
    attribute: float = 100,
    songchant: float = 6,
    songchant_rate: float = SONGCHANT_SCALING_RATE,
    songchant_pen_mode: str = "traits_wiki",
    attunement: str | None = None,
    exclude_ids: tuple[str, ...] | list[str] | set[str] = (),
    by_attunement: bool = False,
    top_n: int | None = None,
    proven_only: bool = False,
    showcase_only: bool = False,
) -> str:
    """Format a complete human-readable report of PvP item theory + mantra ceiling."""
    items = load_items()
    all_mantras = json.loads(MANTRAS_PATH.read_text(encoding="utf-8"))["mantras"]
    if showcase_only:
        mantras_by_id = {m["id"]: m for m in all_mantras}
        selected = [mantras_by_id[mid] for mid in SHOWCASE_MANTRA_IDS if mid in mantras_by_id]
    else:
        selected = all_mantras
    selected = filter_mantras(selected, attunement=attunement, exclude_ids=exclude_ids)
    if proven_only:
        selected = [m for m in selected if not _is_unproven_or_stale(m.get("status", ""))]

    passive_pct = passive_item_common_bonus(items, include_food=True) * 100.0
    header = (
        f"{'MANTRA':<43} {'ATTUNEMENT':<26} {'NO-ITEM':>8} {'PASSIVE':>8} "
        f"{'MAX+NOC':>8} {'+BRAIN':>8} {'VS ARMOR(0->MAX)':>17} {'PEN':>5} {'SEAR100%':>9} {'GRIM?ARMOR':>11}"
    )
    lines = [
        "=== MAX PVP ITEM THEORY + MANTRA CEILING ===",
        f"Loadout (Legal Standard PvP): Prophet's Cloak (+20% PEN Outfit)"
        f" + Ring of Casters (+5%) + Isshin's Ring (+15%) + Enchant Food (+5%) = +{passive_pct:.0f}% passive (exact 1.25x soft cap!)",
        "Everything-Goes Cap Saturation (x1.50): Perfect Flash (+25%) + Taunt (+20%) + Strengthening Potion (+27.5%/13.75%) + Isshin's (+15%) + Casters (+5%) + Lose Your Mind (+15%) [+ Vow Fight +20% / Inhale +10% / Dark Hours +15%] -> all cap at x1.50; swap Enchant Food for Brain Food (+15 Nocturnal Gem!).",
        "Optional Gear Bypass: Shock Trooper Specialist Full Set (Head/Arms/Legs -> +15% base on 6 Thundercall/Gale mantras; coexists w/ Prophet's Cloak)",
        "PEN Ceiling vs Target Armor: Passive (60%, Ironsing 90% via Oath +5%, Prophet +20%, Songchant +15%, Piercing Will +15%, Ether Overdrive +5% & uncap) vs Sear Cauterize (+40% -> 100% PEN = SEAR100%!) vs Grim? (+25% uncapped hypothesis).",
        f"Params: Attr={attribute:g}, Songchant={songchant:g} (scaling rate={songchant_rate:.3f}, PEN mode={songchant_pen_mode}), Target Pre-PEN Armor={target_armor*100:.0f}%",
    ]
    if attunement or exclude_ids or proven_only or top_n:
        lines.append(
            f"Filters: attunement={attunement or 'ALL'}, excluded={','.join(exclude_ids) or 'none'}, "
            f"proven_only={proven_only}, top={top_n or 'ALL'}"
        )
    lines.append("")

    rows = [
        evaluate_mantra_with_items(
            m,
            items,
            target_armor=target_armor,
            attribute=attribute,
            songchant=songchant,
            songchant_rate=songchant_rate,
            songchant_pen_mode=songchant_pen_mode,
        )
        for m in selected
    ]
    rows.sort(key=lambda r: r["full_cap_plus_nocturnal_gross"], reverse=True)

    if top_n is not None:
        kits = top_n_by_attunement(rows, top_n=top_n)
        lines.append(f"TOP-{top_n} UNIQUE-SKILL KIT COMPARISON BY ATTUNEMENT (deduped by skill_group; 1-proc Nocturnal+Brain per cast):")
        lines.append(
            f"{'ATTUNEMENT':<26} {'SKILLS':>6} {'NO-ITEM SUM':>11} {'PASSIVE SUM':>11} "
            f"{'60/90% ARM':>11} {'SEAR100% SUM':>12} {'GRIM?ARM SUM':>12}  TOP SKILL (#1 -> #{top_n})"
        )
        for k in kits:
            sk = k["skills"]
            rng_txt = f"{sk[0]['name']} ({sk[0]['sear_brain_vs_armor']:.1f}) -> {sk[-1]['name']} ({sk[-1]['sear_brain_vs_armor']:.1f})"
            lines.append(
                f"{k['attunement']:<26} {k['count']:>3}/{top_n:<2} {k['no_item_sum']:11.2f} {k['passive_sum']:11.2f} "
                f"{k['max_item_vs_armor_sum']:11.2f} {k['sear_brain_sum']:12.2f} {k['grim_brain_vs_armor_sum']:12.2f}  {rng_txt}"
            )
        lines.append("")
        lines.append(f"TOP {top_n} SKILLS PER ATTUNEMENT:")
        for k in kits:
            lines.append(f"\n[{k['attunement']}] ({k['count']} unique skills shown)")
            lines.append(header)
            lines.extend(_format_row(r) for r in k["skills"])
    elif by_attunement:
        grouped: dict[str, list[dict]] = {}
        for r in rows:
            grouped.setdefault(r["type"], []).append(r)

        best_rows = [grp[0] for grp in grouped.values()]
        best_rows.sort(key=lambda r: r["full_cap_plus_nocturnal_gross"], reverse=True)
        lines.append("BEST PER ATTUNEMENT (highest listed mantra in each single attunement):")
        lines.append(header)
        lines.extend(_format_row(r) for r in best_rows)
        lines.append("")
        lines.append("BREAKDOWN BY ATTUNEMENT:")
        for att_name, grp in sorted(grouped.items(), key=lambda kv: kv[1][0]["full_cap_plus_nocturnal_gross"], reverse=True):
            lines.append(f"\n[{att_name}]")
            lines.append(header)
            lines.extend(_format_row(r) for r in grp)
    else:
        lines.append(header)
        lines.extend(_format_row(r) for r in rows)

    lines.extend([
        "",
        "NOTES & EXCLUSIONS:",
        "- [*1.15] marks Shock Trooper Specialist Full Set +15% base bypass (cannot use 3 Armor Enchants, which already give 0 PvP mantra dmg).",
        "- +BRAIN swaps redundant Enchant Food (+5% already saturated by Potion+Flash+Taunt+Rings) for Brain Food (+15 Nocturnal Gem instead of +10).",
        "- SEAR100% = +BRAIN with Sear Cauterize (+40% incoming PEN via M1 stacks + Ether Overdrive = 100% PEN, bypassing 100% of target armor).",
        "- GRIM?ARMOR shows *hypothetical* upper bound vs target armor if Grim (+25% dmg taken, 6s) sits outside the x1.50 cap; if inside, SEAR100% wins on every armored target.",
        "- NO PvP Mantra Damage comes from Equipment Pips, Armor Enchants (Drowned is PvE-only), Scaling Rings, Chain of Perfection (PvE), or Ardour (M1 posture/guardbreak).",
        "- QUARANTINED: Divine Cast Ring (3x mantra) is Vow of Iron Relic ONLY (illegal in standard PvP).",
        "- EXTRAS / UNQUANTIFIED: Galebreathe After Cut (+2.5% Talents / +5% legacy secondary hit) sits outside cap; Vow of Mastery 'Fight' (+20%) saturates the same x1.50 cap; Yun'Shul Wind-Up Lv10 Bell % is undocumented on Wiki.",
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
    parser.add_argument("--attunement", type=str, default=None,
                        help="Filter mantras by attunement/type substring (e.g. Galebreathe, Ironsing, Bloodrend)")
    parser.add_argument("--exclude", type=str, default="",
                        help="Comma-separated mantra IDs to exclude (e.g. ceaseless,ceaseless_builder)")
    parser.add_argument("--no-ceaseless", action="store_true",
                        help="Exclude Ceaseless Slashes entries from output")
    parser.add_argument("--by-attunement", action="store_true",
                        help="Show best-per-attunement summary plus grouped tables")
    parser.add_argument("--top", type=int, default=None,
                        help="Rank unique skills and summarize Top-N kit ceiling per attunement (e.g. --top 6)")
    parser.add_argument("--proven-only", action="store_true",
                        help="Exclude unproven hypotheses (Scarlet Cyclone x3) and stale nerfed baselines (Shadow Meteor)")
    parser.add_argument("--showcase", action="store_true",
                        help="Restrict output to original 9 showcase mantras")
    args = parser.parse_args()
    exclude_ids = [x.strip() for x in args.exclude.split(",") if x.strip()]
    if args.no_ceaseless:
        exclude_ids.extend(CEASELESS_IDS)
    print(format_report(
        target_armor=args.target_armor / 100.0,
        attribute=args.attribute,
        songchant=args.songchant,
        songchant_rate=args.songchant_rate,
        songchant_pen_mode=args.songchant_pen_mode,
        attunement=args.attunement,
        exclude_ids=exclude_ids,
        by_attunement=args.by_attunement,
        top_n=args.top,
        proven_only=args.proven_only,
        showcase_only=args.showcase,
    ))


if __name__ == "__main__":
    main()
