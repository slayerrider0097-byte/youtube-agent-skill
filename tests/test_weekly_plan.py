import unittest
from datetime import date, timedelta

import generate_weekly_plan as planner


class WeeklyPlanTests(unittest.TestCase):
    def test_config_loads(self):
        config = planner.load_config()
        self.assertIsInstance(config, dict)
        self.assertTrue(config)

    def test_plan_is_text(self):
        config = planner.load_config()
        plan = planner.generate_plan(config, date(2026, 10, 12))
        self.assertIsInstance(plan, str)
        self.assertTrue(plan.strip())

    def test_plan_has_weekly_header(self):
        config = planner.load_config()
        plan = planner.generate_plan(config, date(2026, 10, 12))
        self.assertIn("Weekly YouTube Content Plan", plan)

    def test_plan_has_safety_note(self):
        config = planner.load_config()
        plan = planner.generate_plan(config, date(2026, 10, 12))
        self.assertIn("Before posting", plan)
        self.assertIn("footage", plan.lower())


if __name__ == "__main__":
    unittest.main()
