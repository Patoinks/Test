"""One-skill arithmetic regression tests; no live Roblox environment."""
import importlib.util
from pathlib import Path
import unittest

PATH=Path(__file__).resolve().parents[1]/"src"/"oneskill_pvp_2026.py"
spec=importlib.util.spec_from_file_location("oneskill_pvp_2026", PATH)
import sys
module=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=module
spec.loader.exec_module(module)

class TestOneCast(unittest.TestCase):
    def c(self,name):
        return next(x for x in module.CANDIDATES if x.name==name)

    def test_75_percent_nominal_reaches_hard_cap(self):
        self.assertAlmostEqual(module.common_damage_multiplier(.25),1.25)
        self.assertAlmostEqual(module.common_damage_multiplier(.65),1.45)
        self.assertAlmostEqual(module.common_damage_multiplier(.75),1.50)
        self.assertAlmostEqual(module.common_damage_multiplier(.85),1.50)

    def test_eclipse_updated_builder_base(self):
        c=self.c("Eclipse Kick")
        self.assertEqual(c.level5_base,115)
        self.assertAlmostEqual(module.gross(c),160.85625)
        self.assertAlmostEqual(module.gross(c,.25),201.0703125)
        self.assertAlmostEqual(module.gross(c,.65),233.2415625)
        self.assertAlmostEqual(module.gross(c,.75),241.284375)

    def test_quick_hit_comparators(self):
        self.assertAlmostEqual(module.gross(self.c("Flame Ballista"),.75),201.42)
        self.assertAlmostEqual(module.gross(self.c("Skyshatter Kick"),.75),223.065)

    def test_full_cast_is_not_one_impact(self):
        self.assertAlmostEqual(module.gross(self.c("Tornado"),.75),391.25835)
        self.assertEqual(self.c("Tornado").hits,12)
        self.assertEqual(self.c("Ice Carve Round Spark").hits,20)
        self.assertAlmostEqual(module.gross(self.c("Ice Carve Round Spark"),.75),209.8125)

    def test_nocturnal_delayed_second_event(self):
        self.assertAlmostEqual(module.gross(self.c("Eclipse Kick"),.75)
          +module.flat_gem_extra(True),256.284375)

    def test_resistance_illustration(self):
        e=self.c("Eclipse Kick")
        self.assertAlmostEqual(module.illustrative_post_pen(module.gross(e,.75)),199.059609375)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):module.mantra_scale(-1, 2.75)
        with self.assertRaises(ValueError):module.common_damage_multiplier(-.2)
        with self.assertRaises(ValueError):module.illustrative_post_pen(100,1.1,.5)

if __name__=="__main__":
    unittest.main()
