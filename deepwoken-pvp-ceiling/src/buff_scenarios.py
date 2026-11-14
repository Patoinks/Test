#!/usr/bin/env python3
"""Conditional buff-pool audit (not a legal-build validator).

Usage: python3 src/buff_scenarios.py
"""
from itertools import combinations
from ceiling import pvp_damage_modifier, potion_damage_buff

# These are NOMINAL common modifiers under a TESTABLE assumption:
# actual cap placement, activation windows and inter-buff stacking need testing.
COMMON = {
    "Ring of Casters": 0.05,
    "Enchant food": 0.05,
    "Strengthening potion max": potion_damage_buff(),
    "Taunt on target": 0.20,
    "Tough Love (mantra vs Charmed)": 0.05,
    "Perfect Flash (>95% HP, near)": 0.25,
    "Flame Within (may break HP threshold)": 0.10,
    "Last Resort (<25% HP)": 0.05,
    "Inhale Lv5 (Galebreathe next cast only)": 0.10,
}
CONFLICTS = [
    {"Perfect Flash (>95% HP, near)", "Last Resort (<25% HP)"},
]


def valid(selected, attunement="Light Weapon", caster_hp_percent=100):
    chosen = set(selected)
    if any(c.issubset(chosen) for c in CONFLICTS):
        return False
    if "Perfect Flash (>95% HP, near)" in chosen and caster_hp_percent <= 95:
        return False
    if "Last Resort (<25% HP)" in chosen and caster_hp_percent >= 25:
        return False
    if "Inhale Lv5 (Galebreathe next cast only)" in chosen and attunement != "Galebreathe":
        return False
    return True


def ranked(attunement="Light Weapon", caster_hp_percent=100):
    entries = list(COMMON)
    outcomes = []
    for n in range(len(entries)+1):
        for selected in combinations(entries, n):
            if not valid(selected, attunement, caster_hp_percent):
                continue
            nominal = sum(COMMON[s] for s in selected)
            outcomes.append((pvp_damage_modifier(nominal), nominal, selected))
    return sorted(outcomes, key=lambda x: (x[0], -len(x[2]), -x[1]), reverse=True)


if __name__ == "__main__":
    for hp in (100, 20):
        for element in ("Light Weapon", "Galebreathe"):
            result = ranked(element, hp)
            effective, nominal, buffs = result[0]
            print(f"\n{element}, HP={hp}%: upper common-pool x{effective:.3f} (raw +{nominal*100:.1f}%)")
            for b in buffs:
                print(f" - {b}")
    print("\nAll results are candidates only: not all may be active simultaneously.")
    print("Check hidden restrictions, food/potion duration and perfect-flash cap separately.")
