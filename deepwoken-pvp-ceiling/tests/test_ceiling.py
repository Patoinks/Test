"""Regression checks for sourced Deepwoken PvP calculations."""
import importlib.util
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC_DIR = str(ROOT / "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

SPEC = importlib.util.spec_from_file_location("ceiling", ROOT / "src" / "ceiling.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)

SCENARIOS_SPEC = importlib.util.spec_from_file_location("buff_scenarios", ROOT / "src" / "buff_scenarios.py")
buff_scenarios = importlib.util.module_from_spec(SCENARIOS_SPEC)
SCENARIOS_SPEC.loader.exec_module(buff_scenarios)

MANTRAS = {m["id"]: m for m in json.loads((ROOT / "data" / "mantras.json").read_text(encoding="utf-8"))["mantras"]}
RAW_BUFFS = json.loads((ROOT / "data" / "buffs.json").read_text(encoding="utf-8"))["buffs"]


class TestPvPCeiling(unittest.TestCase):
    def test_soft_cap_and_hard_cap(self):
        self.assertAlmostEqual(module.pvp_damage_modifier(0.25), 1.25)
        self.assertAlmostEqual(module.pvp_damage_modifier(0.50), 1.375)
        self.assertAlmostEqual(module.pvp_damage_modifier(0.75), 1.50)
        self.assertAlmostEqual(module.pvp_damage_modifier(0.825), 1.50)
        self.assertAlmostEqual(module.pvp_damage_modifier(10.0), 1.50)

    def test_lv5_mantra_scaling(self):
        self.assertAlmostEqual(module.scaling_multiplier(100, 6, 1.65), 1.23925)
        self.assertAlmostEqual(module.scaling_multiplier(100, 6, 2.75), 1.39875)

    def test_ceaseless_total_hits_and_damage(self):
        b, n = module.base_damage(MANTRAS["ceaseless"])
        self.assertEqual(n, 20)
        self.assertAlmostEqual(b, 310.05)
        self.assertAlmostEqual(module.damage(MANTRAS["ceaseless"]), 576.34419375)

    def test_other_full_hit_candidates(self):
        self.assertAlmostEqual(module.damage(MANTRAS["ceaseless_builder"]), 539.07375)
        self.assertAlmostEqual(module.damage(MANTRAS["tornado"]), 372.627)
        self.assertAlmostEqual(module.damage(MANTRAS["tornado_kick"]), 234.99)
        self.assertAlmostEqual(module.damage(MANTRAS["metal_rain"]), 231.633)
        self.assertAlmostEqual(module.damage(MANTRAS["ice_flock"]), 221.562)
        self.assertAlmostEqual(module.damage(MANTRAS["flame_ballista"]), 201.42)
        self.assertAlmostEqual(module.damage(MANTRAS["crimson_rain"]), 195.125625)
        self.assertAlmostEqual(module.damage(MANTRAS["eclipse_kick"]), 193.0275)
        self.assertAlmostEqual(module.damage(MANTRAS["scarlet_cyclone_triple"]), 327.3075)

    def test_unbuffed_and_capped_are_distinct(self):
        m = MANTRAS["ceaseless"]
        self.assertAlmostEqual(module.damage(m, raw_bonus=0.0), 384.2294625)
        self.assertAlmostEqual(module.damage(m, raw_bonus=0.75), 576.34419375)

    def test_songchant_75_percent_and_not_proficiency_65(self):
        # Wiki Traits / Mantras: Songchant +7.5% investment scaling
        self.assertAlmostEqual(module.scaling_multiplier(100, 6, 2.75), 1.39875)
        self.assertNotAlmostEqual(module.scaling_multiplier(100, 6, 2.75), 1.38225)

    def test_oath_factor_is_separate_and_not_on_regular_mantras(self):
        m = MANTRAS["tornado"]
        self.assertFalse(m.get("oath_or_monster", False))
        fake_oath = {**m, "oath_or_monster": True}
        self.assertAlmostEqual(module.damage(fake_oath, raw_bonus=0),
                               module.damage(m, raw_bonus=0) * 1.12)

    def test_base_damage_mult_bypasses_common_damage_cap(self):
        m = MANTRAS["tornado"]
        hypothetical_base = {**m, "base_damage_multiplier": 1.15}
        self.assertAlmostEqual(module.damage(hypothetical_base),
                               module.damage(m) * 1.15)
        # Even when the *common* bonus is already capped, base damage rises.
        self.assertAlmostEqual(module.damage(hypothetical_base, raw_bonus=5),
                               module.damage(m, raw_bonus=5) * 1.15)

    def test_buff_scenarios_reads_json_and_excludes_non_mantras(self):
        common = buff_scenarios.COMMON_BUFFS
        for excluded in ("reinforce", "overflowing_dam", "shade_devour",
                         "nullifying_clarity", "charged_return", "nocturnal_gem",
                         "food_brain", "arcwarder_enhance_beam", "specialist_full_set"):
            self.assertNotIn(excluded, common)
        for expected in ("lose_your_mind", "dark_hours", "perfect_flash",
                         "strengthening_potion", "fan_the_flames"):
            self.assertIn(expected, common)
        halved = buff_scenarios.load_common_buffs(potion_mode="halved_2025_nerf")
        self.assertAlmostEqual(halved["strengthening_potion"]["effective_percent"], 13.75)
        no_pot = buff_scenarios.load_common_buffs(potion_mode="exclude")
        self.assertNotIn("strengthening_potion", no_pot)
        self.assertEqual(len(RAW_BUFFS), 23)

    def test_buff_scenarios_constraints(self):
        self.assertFalse(buff_scenarios.valid(["perfect_flash", "last_resort"], "Light Weapon", 100))
        self.assertFalse(buff_scenarios.valid(["perfect_flash", "flame_within"], "Light Weapon", 100, strict_hp=True))
        self.assertTrue(buff_scenarios.valid(["perfect_flash", "flame_within"], "Light Weapon", 100, strict_hp=False, max_build_points=None))
        self.assertFalse(buff_scenarios.valid(["dark_hours"], "Light Weapon", 100))
        self.assertTrue(buff_scenarios.valid(["dark_hours"], "Shadowcast", 100, is_night_or_depths=True))
        self.assertFalse(buff_scenarios.valid(["dark_hours"], "Shadowcast", 100, is_night_or_depths=False))
        self.assertFalse(buff_scenarios.valid(["inhale"], "Shadowcast", 100))
        self.assertTrue(buff_scenarios.valid(["inhale"], "Galebreathe", 100))
        self.assertFalse(buff_scenarios.valid(["fan_the_flames"], "Shadowcast", 100))
        self.assertTrue(buff_scenarios.valid(["fan_the_flames"], "Flamecharm", 100))

    def test_required_attribute_sum_deduplicates_shared_stats(self):
        reqs = buff_scenarios.required_attribute_sum(
            ["taunt", "tough_love", "inhale"], attunement="Galebreathe", primary_investment=100
        )
        self.assertEqual(reqs["Galebreathe"], 100)
        self.assertEqual(reqs["Charisma"], 25)
        self.assertEqual(sum(reqs.values()), 125)
        self.assertFalse(buff_scenarios.valid(["perfect_flash"], "Light Weapon", 100, max_build_points=120))

    def test_potion_100_int_apothecary(self):
        self.assertAlmostEqual(module.potion_damage_buff(), 0.275)
        self.assertAlmostEqual(module.potion_damage_buff(brewer_int=0, apothecary=False), 0.10)

    def test_target_resistance_is_net_post_pen(self):
        m = MANTRAS["ceaseless"]
        self.assertAlmostEqual(module.damage(m, target_resistance=0.25),
                               module.damage(m) * 0.75)

    def test_invalid_values_rejected(self):
        with self.assertRaises(ValueError):
            module.scaling_multiplier(101, 6, 2.75)
        with self.assertRaises(ValueError):
            module.pvp_damage_modifier(-0.5)
        with self.assertRaises(ValueError):
            module.damage(MANTRAS["ceaseless"], target_resistance=1.01)


if __name__ == "__main__":
    unittest.main()
