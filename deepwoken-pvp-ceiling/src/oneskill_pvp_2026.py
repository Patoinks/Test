#!/usr/bin/env python3
"""Deepwoken PvP: one skill / one cast, NOT a full combo.

Documented 2026 Builder Lv5 bases. 100 main attribute, 6 Songchant.
Sources and patch caveats: docs/ONESKILL_PVP_2026-11-14.md.
This is an arithmetic audit; NOT an in-game damage test.
"""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Candidate:
    name: str
    level5_base: float
    scaling: float
    hits: int
    category: str
    source: str
    caveat: str = ""

CANDIDATES = [
    Candidate("Eclipse Kick",115,2.75,1,"single_hit","https://deepwoken.co/wiki/mantra/Eclipse%20Kick","Reduced damage if target already stunned"),
    Candidate("Skyshatter Kick",120,1.65,2,"short_multi","https://deepwoken.co/wiki/mantra/Skyshatter%20Kick","Two consecutive kicks, both must connect"),
    Candidate("Flame Ballista",96,2.75,1,"single_hit","https://deepwoken.co/wiki/mantra/Flame%20Ballista","Full charge; Isshin requires close quarters"),
    Candidate("Ice Flock",105.6,2.75,8,"multi_hit","https://deepwoken.co/wiki/mantra/Ice%20Flock","All eight birds must hit one victim"),
    Candidate("Ice Carve Round Spark",100,2.75,20,"channel","https://deepwoken.co/wiki/mantra/Ice%20Carve","20 ticks; parry interrupts; old Spring Spark bug excluded"),
    Candidate("Tornado",186.48,2.75,12,"channel","https://deepwoken.co/wiki/mantra/Tornado","Builder aggregate may already include +5% After Cut; no double counting"),
    Candidate("Scarlet Cyclone",130,2.75,10,"channel","https://deepwoken.co/wiki/mantra/Scarlet%20Cyclone","10 ticks full-hit theoretical"),
    Candidate("Scarlet Cyclone Multiplying",156,2.75,30,"unproven_overlap","https://deepwoken.co/wiki/mantra/Scarlet%20Cyclone","3 cyclones same target NOT verified"),
    Candidate("Tornado Kick",112,2.75,4,"short_multi","https://deepwoken.co/wiki/mantra/Tornado%20Kick","Follow-ups only after opener hits"),
]

def mantra_scale(base:float, scaling:float, investment:float=100, songchant:int=6)->float:
    if base<0 or scaling<0 or not 0<=investment<=100 or not 0<=songchant<=6:
        raise ValueError("Invalid level/stat/scaling")
    return base*(1+(scaling/1000)*investment*(1+songchant*0.075))

def common_damage_multiplier(nominal:float)->float:
    """nominal is 0.75 for +75%; cap formula is conditional PvP pool model."""
    if nominal<0: raise ValueError("Negative buffs unsupported")
    return 1+min(0.50,min(0.25,nominal)+max(0,nominal-0.25)/2)

def gross(c:Candidate, nominal:float=0)->float:
    return mantra_scale(c.level5_base,c.scaling)*common_damage_multiplier(nominal)

def flat_gem_extra(brain_food:bool=False,gem_procs:bool=True)->float:
    """Delayed, independently dodgeable single proc, not same-impact damage."""
    return (15 if brain_food else 10) if gem_procs else 0

def illustrative_post_pen(gross_value:float,base_armor:float=.35,pen:float=.5)->float:
    """DELIBERATELY simplistic target model: does not equal Deepwoken full EHP formula."""
    if not(0<=base_armor<=1 and 0<=pen<=1):raise ValueError("Armor/PEN 0..1")
    return gross_value*(1-base_armor*(1-pen))

def rows():
    return [dict(name=c.name,category=c.category,hits=c.hits,base=c.level5_base,
        no_buff=gross(c),passive_25=gross(c,.25),hard_cap=gross(c,.75),
        illustrative_armor=gross(c,.75)*(1-.35*(1-.50)),note=c.caveat) for c in CANDIDATES]

def main():
    print("POWER20 L5 100stat 6song — 1 CAST, not 1 HIT — pre-resist gross HP")
    print("Mantra                         Hits       No buff    +25%      Hard cap     35%armor 50%PEN")
    for r in sorted(rows(),key=lambda x:x["hard_cap"],reverse=True):
        print(f'{r["name"]:<30} {r["hits"]:>4} {r["no_buff"]:>11.2f} {r["passive_25"]:>11.2f} {r["hard_cap"]:>11.2f} {r["illustrative_armor"]:>15.2f}')
    e=next(c for c in CANDIDATES if c.name=="Eclipse Kick")
    print("\nSTRICT SINGLE HIT (no external attacker debuff): Eclipse Kick, Lv5 base 115")
    print(f'passive ring+isshin+food +25%: {gross(e,.25):.2f}')
    print(f'perfect flash + dark hours + rings + food +65%: {gross(e,.65):.2f}')
    print(f'full cap with >95%HP, night/Depths, 0 sanity Lose Your Mind (+75% raw without food): {gross(e,.75):.2f}')
    print(f'plus optional Nocturnal Gem with Brain food: {gross(e,.75)+flat_gem_extra(True):.2f} TWO EVENTS (1 second delayed)')
    print("Source limits: no live Roblox playtests; all ticks land assumption, no resistant player proof.")

if __name__=="__main__":
    main()
