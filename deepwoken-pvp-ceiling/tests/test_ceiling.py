"""Regression checks for sourced Deepwoken PvP calculations."""
import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("ceiling", ROOT / "src" / "ceiling.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)
MANTRAS = {m["id"]: m for m in json.loads((ROOT / "data" / "mantras.json").read_text())["mantras"]}


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
        self.assertAlmostEqual(module.damage(MANTRAS["tornado"]), 372.627)
        self.assertAlmostEqual(module.damage(MANTRAS["tornado_kick"]), 234.99)
        self.assertAlmostEqual(module.damage(MANTRAS["metal_rain"]), 231.633)
        self.assertAlmostEqual(module.damage(MANTRAS["scarlet_cyclone_triple"]), 327.3075)

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
