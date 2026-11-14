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

ITEMS_SPEC = importlib.util.spec_from_file_location("item_theory", ROOT / "src" / "item_theory.py")
item_theory = importlib.util.module_from_spec(ITEMS_SPEC)
ITEMS_SPEC.loader.exec_module(item_theory)

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

    def test_patch_candidates_and_mantra_warnings_integrity(self):
        patch_data = json.loads((ROOT / "data" / "patch_candidates_2026_11.json").read_text(encoding="utf-8"))
        terms = set(patch_data["confidence_terms"].keys())
        self.assertGreaterEqual(len(patch_data["patches"]), 8)
        for key, patch in patch_data["patches"].items():
            self.assertIn("source", patch, key)
            self.assertIn(patch.get("confidence"), terms, key)
        for cand in patch_data["candidate_mantras"]:
            self.assertIn("source", cand, cand["id"])
            self.assertIn(cand.get("confidence"), terms, cand["id"])
            self.assertIsNone(cand["base_damage_level5"], cand["id"])

        checks = {row["id"]: row for row in patch_data["fresh_reference_checks"]}
        for mid in ("ceaseless", "tornado", "shadow_meteor", "crimson_rain"):
            self.assertIn(mid, checks)
            self.assertIn("caveat", MANTRAS[mid])
            self.assertIn("other_current_source_base_level_5", MANTRAS[mid])
        self.assertEqual(checks["crimson_rain"]["builder_L5_base"], 46.5)
        self.assertEqual(checks["tornado"]["builder_L5_base"], 186.48)
        self.assertIsNone(checks["shadow_meteor"]["builder_L5_base"])

    def test_legacy_065_songchant_and_wiki_worked_examples(self):
        # Legacy Mantras wiki worked examples (pre-May-2026 0.065 vs current Traits 0.075)
        strong_left = {"segments": [{"count": 1, "damage": 60}], "scaling": 1.65, "oath_or_monster": False}
        celestial = {"segments": [{"count": 1, "damage": 20}], "scaling": 1.65, "oath_or_monster": True}

        self.assertEqual(round(module.damage(strong_left, 95, 2, raw_bonus=0.0, songchant_rate=0.065), 2), 70.63)
        self.assertEqual(round(module.damage(strong_left, 95, 2, raw_bonus=0.0, songchant_rate=0.075), 2), 70.82)
        self.assertEqual(round(module.damage(celestial, 80, 4, raw_bonus=0.0, songchant_rate=0.065), 2), 25.19)
        self.assertEqual(round(module.damage(celestial, 80, 4, raw_bonus=0.0, songchant_rate=0.075), 2), 25.31)
        self.assertEqual(round(module.damage(MANTRAS["ceaseless"], songchant_rate=0.065), 2), 571.74)
        self.assertEqual(round(module.damage(MANTRAS["tornado"], songchant_rate=0.065), 2), 368.23)

    def test_pvp_item_theory_and_pen_math(self):
        items = item_theory.load_items()
        excluded = {e["id"]: e for e in items["excluded_or_zero_pvp_mantra_damage"]}
        self.assertFalse(excluded["divine_cast_ring"]["legal_standard_pvp"])
        self.assertAlmostEqual(item_theory.passive_item_common_bonus(items, include_food=True), 0.25)

        capped_pen, raw_pen_no_eo, uncapped_no_eo = item_theory.max_pen_fraction(
            items, mantra_type="Galebreathe", include_ether_overdrive=False,
        )
        self.assertFalse(uncapped_no_eo)
        self.assertAlmostEqual(raw_pen_no_eo, 0.55)
        self.assertAlmostEqual(capped_pen, 0.50)

        uncapped_pen, _, uncapped_eo = item_theory.max_pen_fraction(
            items, mantra_type="Galebreathe", include_ether_overdrive=True,
        )
        self.assertTrue(uncapped_eo)
        self.assertAlmostEqual(uncapped_pen, 0.60)

        ironsing_pen, _, _ = item_theory.max_pen_fraction(
            items, mantra_type="Ironsing", include_ether_overdrive=True,
        )
        self.assertAlmostEqual(ironsing_pen, 0.90)

        electro_res = item_theory.evaluate_mantra_with_items(MANTRAS["electro_carve"], items, target_armor=0.35)
        ceaseless_res = item_theory.evaluate_mantra_with_items(MANTRAS["ceaseless"], items, target_armor=0.35)
        self.assertAlmostEqual(electro_res["specialist_mult"], 1.15)
        self.assertAlmostEqual(ceaseless_res["specialist_mult"], 1.0)
        self.assertAlmostEqual(electro_res["passive_item_gross"], 70.0 * 1.15 * 1.39875 * 1.25)
        self.assertAlmostEqual(ceaseless_res["full_cap_plus_nocturnal_gross"], 576.34419375 + 10.0)
        self.assertAlmostEqual(ceaseless_res["brain_max_gross"], 576.34419375 + 15.0)
        self.assertAlmostEqual(ceaseless_res["sear_effective_pen"], 1.0)
        self.assertAlmostEqual(ceaseless_res["sear_brain_vs_armor"], 576.34419375 + 15.0)

    def test_attunement_filter_and_exclude_ceaseless(self):
        all_mantras = list(MANTRAS.values())
        no_ceaseless = module.filter_mantras(all_mantras, exclude_ids=module.CEASELESS_IDS)
        self.assertTrue(all(m["id"] not in module.CEASELESS_IDS for m in no_ceaseless))

        gale_only = module.filter_mantras(all_mantras, attunement="galebreathe", exclude_ids=module.CEASELESS_IDS)
        self.assertEqual({m["id"] for m in gale_only}, {"tornado", "tornado_kick", "champions_whirlthrow"})

        report = item_theory.format_report(exclude_ids=module.CEASELESS_IDS, by_attunement=True)
        self.assertNotIn("Ceaseless Slashes", report)
        self.assertIn("BEST PER ATTUNEMENT", report)
        self.assertIn("Scarlet Cyclone", report)
        self.assertIn("Ice Flock", report)
        self.assertIn("Tornado Kick", report)


if __name__ == "__main__":
    unittest.main()
