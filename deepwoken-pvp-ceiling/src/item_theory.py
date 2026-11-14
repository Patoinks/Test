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
AFTER_CUT_RATE_TALENTS = 0.025
AFTER_CUT_RATE_LEGACY = 0.05
BLEED_DOT_RATE = 0.15
STORM_STRIKE_FLAT = 15.0

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
    after_cut_rate: float = AFTER_CUT_RATE_TALENTS,
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
    cast_sear_vs_armor = damage(
        mantra, attribute, songchant, raw_bonus=0.75, target_resistance=sear_res,
        songchant_rate=songchant_rate, base_multiplier_override=specialist_mult,
    )
    nocturnal_sear_flat = nocturnal_brain_flat * (1.0 - sear_res)
    sear_brain_vs_armor = cast_sear_vs_armor + nocturnal_sear_flat
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

    # Secondary passive/DoT channels evaluated against post-Sear resistance (0 at 100% PEN).
    scaled_sear_base = unbuffed_gross * specialist_mult * (1.0 - sear_res)
    after_cut_bonus = scaled_sear_base * after_cut_rate if mantra.get("after_cut_eligible", False) else 0.0
    bleed_dot_bonus = (unbuffed_gross * (1.0 - sear_res) * BLEED_DOT_RATE) if mantra.get("innate_dot") == "bleed_15" else 0.0
    exhaustive_sear_vs_armor = sear_brain_vs_armor + after_cut_bonus + bleed_dot_bonus

    return {
        "id": mantra["id"],
        "skill_group": mantra.get("skill_group", mantra["id"]),
        "name": mantra["name"],
        "type": mantra["type"],
        "status": mantra.get("status", ""),
        "is_oath_mantra": bool(mantra.get("is_oath_mantra", False)),
        "specialist_eligible": bool(mantra.get("specialist_eligible", False)),
        "after_cut_eligible": bool(mantra.get("after_cut_eligible", False)),
        "innate_dot": mantra.get("innate_dot"),
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
        "cast_sear_vs_armor": cast_sear_vs_armor,
        "nocturnal_sear_flat": nocturnal_sear_flat,
        "sear_brain_vs_armor": sear_brain_vs_armor,
        "after_cut_bonus": after_cut_bonus,
        "bleed_dot_bonus": bleed_dot_bonus,
        "exhaustive_sear_vs_armor": exhaustive_sear_vs_armor,
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
        storm_strike = STORM_STRIKE_FLAT if any(r.get("specialist_eligible") for r in picked) else 0.0
        after_cut_sum = sum(r.get("after_cut_bonus", 0.0) for r in picked)
        bleed_dot_sum = sum(r.get("bleed_dot_bonus", 0.0) for r in picked)
        sear_brain_sum = sum(r["sear_brain_vs_armor"] for r in picked)
        aegis_mono_sum = sum(
            0.80 * r["cast_sear_vs_armor"] + r["nocturnal_sear_flat"] for r in picked
        )
        summaries.append({
            "attunement": att_name,
            "skills": picked,
            "count": len(picked),
            "no_item_sum": sum(r["unbuffed_gross"] for r in picked),
            "passive_sum": sum(r["passive_item_gross"] for r in picked),
            "sear_brain_sum": sear_brain_sum,
            "max_item_vs_armor_sum": sum(r["max_item_vs_armor"] for r in picked),
            "grim_brain_vs_armor_sum": sum(r["hypothetical_grim_brain_vs_armor"] for r in picked),
            "after_cut_sum": after_cut_sum,
            "bleed_dot_sum": bleed_dot_sum,
            "specialist_storm_strike": storm_strike,
            "has_burn": any(r.get("innate_dot") == "burn" for r in picked),
            "exhaustive_sear_sum": sear_brain_sum + after_cut_sum + bleed_dot_sum + storm_strike,
            "aegis_mono_sear_sum": aegis_mono_sum + after_cut_sum + bleed_dot_sum + storm_strike,
        })
    sum_key = "exhaustive_sear_sum" if "exhaustive" in sort_key else "sear_brain_sum"
    summaries.sort(key=lambda s: (s["count"], s[sum_key]), reverse=True)
    return summaries


def _format_row(r: dict) -> str:
    tag = f"{r['name']} [*1.15]" if r["specialist_mult"] > 1.0 else r["name"]
    vs_pair = f"{r['unbuffed_vs_armor']:6.1f} -> {r['max_item_vs_armor']:6.1f}"
    return (
        f"{tag:<43} {r['type']:<26} {r['unbuffed_gross']:8.2f} {r['passive_item_gross']:8.2f} "
        f"{r['full_cap_plus_nocturnal_gross']:8.2f} {r['brain_max_gross']:8.2f} {vs_pair:>17} "
        f"{r['effective_pen']*100:4.0f}% {r['sear_brain_vs_armor']:9.2f} {r['hypothetical_grim_brain_vs_armor']:11.2f}"
    )


def _format_exhaustive_top_sections(kits: list[dict], rows: list[dict], top_n: int, after_cut_rate: float) -> list[str]:
    """Build exhaustive secondary-channel (Bleed/After Cut/Storm Strike) and Dawnwalker hybrid summaries."""
    lines = [
        f"EXHAUSTIVE SECONDARY-CHANNEL KIT SUMMARY (Bleed +15%, After Cut +{after_cut_rate*100:.1f}%, Specialist Storm Strike +15, Aegis -20%):",
        f"{'ATTUNEMENT':<26} {'DIRECT SEAR':>11} {'AFTER-CUT':>9} {'BLEED15%':>9} {'STORM+15':>8} {'EXH+DOT':>10} {'AEGIS-20%':>10}  NOTES",
    ]
    for k in sorted(kits, key=lambda x: (x["count"], x["exhaustive_sear_sum"]), reverse=True):
        notes = []
        if k["has_burn"]:
            notes.append("+1x Burn (~14.4-16.25 DPS Deepfire)")
        if k["attunement"] == "Oath Mantra":
            notes.append("Oath slot fits alongside 5-6 attunement mantras")
        lines.append(
            f"{k['attunement']:<26} {k['sear_brain_sum']:11.2f} {k['after_cut_sum']:9.2f} "
            f"{k['bleed_dot_sum']:9.2f} {k['specialist_storm_strike']:8.2f} "
            f"{k['exhaustive_sear_sum']:10.2f} {k['aegis_mono_sear_sum']:10.2f}  {', '.join(notes) or '-'}"
        )

    blinding_dawn = next((r for r in rows if r["id"] == "blinding_dawn"), None)
    if blinding_dawn and top_n >= 2:
        bd_val = blinding_dawn["sear_brain_vs_armor"]
        lines.extend([
            "",
            f"OATH SLOT HYBRID (Best {top_n-1} Attunement + Dawnwalker Blinding Dawn [{bd_val:.2f}], +3 Combat Slots & 0 stat req):",
            f"{'BUILD HYBRID':<40} {'PURE TOP-6':>11} {'EXH TOP-6':>11} {'5 ATT + BLINDING DAWN':>22}  GAIN vs PURE EXH",
        ])
        hybrid_rows = []
        for k in kits:
            if k["count"] < top_n or k["attunement"] in ("Oath Mantra", "Flamecharm (Starkindred)"):
                continue
            top_n_minus_1 = sum(r["exhaustive_sear_vs_armor"] for r in sorted(k["skills"], key=lambda x: x["exhaustive_sear_vs_armor"], reverse=True)[:top_n - 1])
            hybrid_total = top_n_minus_1 + k["specialist_storm_strike"] + bd_val
            hybrid_rows.append((hybrid_total, k["attunement"], k["sear_brain_sum"], k["exhaustive_sear_sum"]))
        for hybrid_total, att, pure_s, exh_s in sorted(hybrid_rows, reverse=True):
            lines.append(
                f"{att + ' + Dawnwalker':<40} {pure_s:11.2f} {exh_s:11.2f} {hybrid_total:22.2f}  {hybrid_total - exh_s:+11.2f}"
            )
    return lines


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
    with_extras: bool = False,
    after_cut_rate: float = AFTER_CUT_RATE_TALENTS,
    exclude_oath_mantras: bool = False,
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
    if exclude_oath_mantras:
        selected = [m for m in selected if not m.get("is_oath_mantra", False)]
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
        "Everything-Goes Cap Saturation (x1.50): Perfect Flash (+25%) + Taunt (+20%) + Strengthening Potion (+27.5%/13.75%) + Isshin's (+15%) + Casters (+5%) + Lose Your Mind (+15%) [+ Rush Hour +15% / Inhale +10% / Dark Hours +15%] -> all cap at x1.50; swap Enchant Food for Brain Food (+15 Nocturnal Gem!).",
        "Optional Gear Bypass: Shock Trooper Specialist Full Set (Head/Arms/Legs -> +15% base on 6 Thundercall/Gale mantras; coexists w/ Prophet's Cloak)",
        "PEN Ceiling vs Target Armor: Passive (60%, Ironsing 90% via Oath +5%, Prophet +20%, Songchant +15%, Piercing Will +15%, Ether Overdrive +5% & uncap) vs Sear Cauterize (+40% -> 100% PEN = SEAR100%) vs Grim? (+25% uncapped hypothesis).",
        f"Params: Attr={attribute:g}, Songchant={songchant:g} (scaling rate={songchant_rate:.3f}, PEN mode={songchant_pen_mode}, After Cut={after_cut_rate*100:.1f}%), Target Pre-PEN Armor={target_armor*100:.0f}%",
    ]
    if attunement or exclude_ids or proven_only or exclude_oath_mantras or top_n or with_extras:
        lines.append(
            f"Filters: attunement={attunement or 'ALL'}, excluded={','.join(exclude_ids) or 'none'}, "
            f"proven_only={proven_only}, no_oath_mantras={exclude_oath_mantras}, top={top_n or 'ALL'}, with_extras={with_extras}"
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
            after_cut_rate=after_cut_rate,
        )
        for m in selected
    ]
    rows.sort(key=lambda r: r["full_cap_plus_nocturnal_gross"], reverse=True)

    if top_n is not None:
        sort_field = "exhaustive_sear_sum" if with_extras else "sear_brain_vs_armor"
        kits = top_n_by_attunement(
            rows,
            top_n=top_n,
            sort_key=("exhaustive_sear_vs_armor" if with_extras else "sear_brain_vs_armor"),
        )
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
        if with_extras:
            lines.append("")
            lines.extend(_format_exhaustive_top_sections(kits, rows, top_n, after_cut_rate))
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
        "- SEAR100% = +BRAIN with Sear Cauterize (+40% incoming PEN via M1 stacks + Ether Overdrive = 100% PEN, bypassing 100% of target armor). Hero's Blades & Curved Blade are unenchantable and thus lose Sear.",
        "- GRIM?ARMOR shows *hypothetical* upper bound vs target armor if Grim (+25% dmg taken, 6s) sits outside the x1.50 cap; if inside, SEAR100% wins on every armored target.",
        "- EXHAUSTIVE CHANNELS (--with-extras): Bleed (+15% scaled on 5 Ironsing skills), After Cut (+2.5% Talents / +5% Gale wiki), Specialist Storm Strike (+15/kit), Everchanging Aegis (-20% repeated mono-element hits vs 25 INT defenders), and Dawnwalker Blinding Dawn hybrid.",
        "- ZERO PvP Mantra Damage comes from Equipment Pips, Armor Enchants (Drowned is PvE-only), Scaling Rings, Races/Aspects, Chain of Perfection (PvE), Ardour (M1 posture), or non-Sear/Grim Weapon Enchants.",
        "- QUARANTINED: Divine Cast Ring (3x mantra) & Belief (+0.15 true dmg/WIL Med) belong to Vow of Iron Relic / Weapon-Mantra modes only (illegal/inapplicable to standard PvP attunement mantras).",
        "- UNQUANTIFIED: Yun'Shul Wind-Up Lv10 Bell exact PvP % and post-Nov 1 Hallowtide hybrid Lv5 cast tables (Alloyblood / Exotherm Sanguine Blaze).",
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
                        help="Exclude unproven hypotheses (Scarlet Cyclone x3) and stale nerfed baselines (Shadow Meteor / Sightless Beam)")
    parser.add_argument("--no-oath-mantras", action="store_true",
                        help="Exclude Oath mantras (Blinding Dawn, Sightless Beam, Starkindred Fire Blade)")
    parser.add_argument("--with-extras", action="store_true",
                        help="Include exhaustive DoT/After-Cut/Storm-Strike/Aegis & Dawnwalker hybrid tables under --top N")
    parser.add_argument("--after-cut-rate", type=float, default=AFTER_CUT_RATE_TALENTS,
                        help="After Cut secondary hit rate (0.025 Talents wiki default vs 0.05 legacy Gale wiki)")
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
        with_extras=args.with_extras,
        after_cut_rate=args.after_cut_rate,
        exclude_oath_mantras=args.no_oath_mantras,
    ))


if __name__ == "__main__":
    main()
