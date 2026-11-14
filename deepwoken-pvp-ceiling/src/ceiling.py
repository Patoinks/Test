#!/usr/bin/env python3
"""Deepwoken PvP mantra theoretical full-hit model.

This script reports community-wiki-based single-cast calculations.
Songchant mantra scaling is 7.5% per point (not 6.5%, which is Proficiency).
It is NOT a proof of in-game achievable damage or of a global maximum.
Requires Python 3.10+, standard library only.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data" / "mantras.json"


def scaling_multiplier(attribute: float, songchant: float, scaling: float) -> float:
    """BaseDamage * (1 + (Scaling/1000)*Investment*(1 + Songchant*0.075))."""
    if not 0 <= attribute <= 100 or not 0 <= songchant <= 6 or scaling < 0:
        raise ValueError("Investment: 0..100; Songchant: 0..6; scaling >= 0.")
    return 1.0 + (scaling / 1000.0) * attribute * (1.0 + 0.075 * songchant)


def pvp_damage_modifier(raw_bonus: float) -> float:
    """Soft cap at +25%, excess half-effective, hard cap +50%.

    raw_bonus is FRACTION (e.g. 0.825 for +82.5%).
    This is for the common damage-modifier pool; not all effects use it.
    """
    if raw_bonus < 0:
        raise ValueError("Model only accepts nonnegative common bonuses")
    effective = min(raw_bonus, 0.25)
    effective += max(0.0, raw_bonus - 0.25) / 2.0
    return 1.0 + min(0.50, effective)


def potion_damage_buff(base_percent: float = 10, brewer_int: int = 100,
                       apothecary: bool = True) -> float:
    """Strengthening 3 Plumfruits + 2 Browncaps = 5 * 2% = +10%.

    Returns a FRACTION. Potency is brewer INT/2 percent (max 50%);
    Apothecary adds +125% additively to potion potency, not multiplicatively.
    """
    if not 0 <= brewer_int <= 100:
        raise ValueError("Brewer intelligence must be 0..100")
    return (base_percent / 100.0) * (1 + (brewer_int / 200.0) + (1.25 if apothecary else 0.0))


def base_damage(mantra: dict) -> tuple[float, int]:
    """Each segment is an array of distinct hits OR same-base repeated ticks."""
    total, hits = 0.0, 0
    for segment in mantra["segments"]:
        if "damages" in segment:
            ds = segment["damages"]
            total += sum(ds)
            hits += len(ds)
        else:
            total += segment["count"] * segment["damage"]
            hits += segment["count"]
    return total, hits


def damage(mantra: dict, attribute: float = 100, songchant: float = 6,
           raw_bonus: float = 0.75, target_resistance: float = 0.0,
           extra_final_multiplier: float = 1.0) -> float:
    """Potential gross HP damage; all hits connect; no parry/blocks/DOT/procs.

    target_resistance is simplified net damage resistance fraction [0,1],
    AFTER any PEN. In-game resistance interactions are more complex.
    extra_final_multiplier is OFF by default and is purely hypothetical.
    """
    if not 0 <= target_resistance <= 1:
        raise ValueError("Target net resistance must be 0..1")
    if extra_final_multiplier < 0:
        raise ValueError("Extra multiplier must not be negative")
    b, _ = base_damage(mantra)
    # Oath/Monster mantras gain a separate 2% per Songchant. Ordinary
    # Ceaseless Slashes and Tornado do not. Set "oath_or_monster": true
    # only after confirming the mantra's actual classification.
    oath_factor = (1 + 0.02 * songchant) if mantra.get("oath_or_monster", False) else 1.0
    # A mantra's base-damage modifier is a *different* channel from
    # the pool affected by pvp_damage_modifier (e.g. Arcwarder Enhance).
    base_factor = mantra.get("base_damage_multiplier", 1.0)
    return (b * base_factor * scaling_multiplier(attribute, songchant, mantra["scaling"])
            * oath_factor * pvp_damage_modifier(raw_bonus) * (1 - target_resistance)
            * extra_final_multiplier)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attribute", type=float, default=100)
    parser.add_argument("--songchant", type=float, default=6)
    parser.add_argument("--raw-bonus", type=float, default=75,
                        help="Common pre-cap damage bonus in percent, e.g. 82.5")
    parser.add_argument("--net-resistance", type=float, default=0,
                        help="Target effective post-PEN resistance in percent")
    parser.add_argument("--extra-final-multiplier", type=float, default=1.0,
                        help="Experimental separate-channel multiplier. DEFAULT 1.0.")
    parser.add_argument("--show-buffs", action="store_true")
    parser.add_argument("--compare", action="store_true",
                        help="Show damage with NO common buffs alongside damage at selected cap pool")
    args = parser.parse_args()
    data = json.loads(DATA.read_text(encoding="utf-8"))
    if args.show_buffs:
        print("Enchant food: +5% mantra (Carnivore must use Fish Omelette); Ring of Casters: +5% mantra")
        print(f"Strengthening potion RECIPE MODEL: +{potion_damage_buff()*100:.2f}% (Nov-2025 50% potion nerf unverified; Browncap hurts caster)")
        print("Perfect Flash: +25% near target only >95% HP (cap channel requires testing)")
        print("Taunt target: +20%, explicitly subject to damage modifier cap")
        print("Tough Love: +5% mantras; Lose Your Mind: up to +15% at 0% sanity; Dark Hours: +15% Shadowcast at night/Depths")
        print("Base-dmg bypasses (outside cap): Arcwarder Enhance (Arc Beam +50%, Arc Wave +25%); Specialist Full Set (+15% 6 mantras)")
        print("Reinforce, Overflowing Dam, Shade Devour, Nullifying Clarity & Charged Return: NOT for mantras")
        print("Mantra PEN (effective dmg vs armor): Prophet's Cloak +20%, 6 Songchant +15%, Ironsing +30%; PEN caps at 50% without Ether Overdrive")
        print("Food buffs replace each other. One potion effect active at a time.")
    rows = []
    for m in data["mantras"]:
        b, hits = base_damage(m)
        d = damage(m, args.attribute, args.songchant, args.raw_bonus / 100,
                   args.net_resistance / 100, args.extra_final_multiplier)
        raw = damage(m, args.attribute, args.songchant, 0,
                     args.net_resistance / 100, args.extra_final_multiplier)
        hits_str = "?" if m.get("unverified_ticks") else str(hits)
        rows.append((d, raw, m["name"], hits_str, b, m["status"]))
    print("MODEL: PvP single-cast all-hit potential; NOT a proven absolute ceiling")
    print(f"Attribute={args.attribute:g} Songchant={args.songchant:g} raw_bonus={args.raw_bonus:g}% "
          f"effective_common_x{pvp_damage_modifier(args.raw_bonus/100):.3f}")
    if args.compare:
        print(f"{'NO BUFFS':>10}  {'WITH BUFFS':>10}  {'HITS':>4}  {'BASE':>8}  {'MANTRA':<42}  STATUS")
    else:
        print(f"{'DAMAGE':>10}  {'HITS':>4}  {'BASE':>8}  {'MANTRA':<42}  STATUS")
    for d, raw, name, hits_str, b, status in sorted(rows, reverse=True):
        if args.compare:
            print(f"{raw:10.2f}  {d:10.2f}  {hits_str:>4}  {b:8.2f}  {name:<42}  {status}")
        else:
            print(f"{d:10.2f}  {hits_str:>4}  {b:8.2f}  {name:<42}  {status}")
    print("\nWARNINGS: all hits assumed to land, pre-resistance default, procs/Everchanging Aegis excluded.")
    print("DISPUTED CEASELESS: 310.05 Fandom ticks (576.34) vs 290 Deepwoken Builder Lv5 (539.07); verify on current patch.")
    print("Incompatible >95% HP Perfect Flash with <=40% HP Shadow Assault Blast.")
    print("Scarlet Cyclone triple projectiles same-target overlap is UNPROVEN.")


if __name__ == "__main__":
    main()
