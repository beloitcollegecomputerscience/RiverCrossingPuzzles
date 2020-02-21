import unittest
from riverCrossingPuzzles import Rules

class RulesTest(unittest.TestCase):
    def test_read_rules(self):
        testRules = Rules('ManWolfGoatHayRules.txt')
        rules = Rules.readRules(testRules)
        self.assertIn('items', rules)
        # print(rules)