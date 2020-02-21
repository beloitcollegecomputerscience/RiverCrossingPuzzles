import unittest
from riverCrossingPuzzles import Rules

class RulesTest(unittest.TestCase):
    def test_read_rules(self):
        testRules = Rules('ManWolfGoatHayRules.txt')
        rules = Rules.readRules(testRules)
        # Checks if one of the required game attributes from the file is in the dictionary
        self.assertIn('pilot', rules)