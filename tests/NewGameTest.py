# Rita
# April 2020
import unittest
from riverCrossing import GameState
from riverCrossing.Rules import Rules


# this test only applies to the man-goat-hay game;
# change pending: after rules can be imported, initiate temp with correct parameters;

class NewGameTest(unittest.TestCase):
    print("start new game test")

    def test_left_shore(self):
        # checks if left shore has all the characters
        manGoatWolfRules = Rules('ManGoatWolf.json').rules;
        manGoatWolfGame = GameState(manGoatWolfRules)
        self.assertEqual(len(manGoatWolfGame.left_shore), len(manGoatWolfRules["left_shore"]))
        self.assertEqual(manGoatWolfGame.left_shore, manGoatWolfRules["left_shore"])
        
        twoGoatRules = Rules('2goat.json').rules
        twoGoatGame = GameState(twoGoatRules)
        self.assertEqual(len(twoGoatGame.left_shore), len(twoGoatRules["left_shore"]))
        self.assertEqual(twoGoatGame.left_shore, twoGoatRules["left_shore"])

    # checks if right shore is empty
    def test_right_shore(self):
        manGoatWolfRules = Rules('ManGoatWolf.json').rules;
        manGoatWolfGame = GameState(manGoatWolfRules)
        self.assertEqual(len(manGoatWolfGame.right_shore), 0, msg='right shore is not empty')

    # checks if boat starts at left shore
    def test_boat_position(self):
        manGoatWolfRules = Rules('ManGoatWolf.json').rules;
        manGoatWolfGame = GameState(manGoatWolfRules)
        self.assertEqual(manGoatWolfGame.boat_position, manGoatWolfRules["boat_position"])

    # checks if boat is empty
    def test_boat(self):
        manGoatWolfRules = Rules('ManGoatWolf.json').rules;
        manGoatWolfGame = GameState(manGoatWolfRules)
        self.assertEqual(len(manGoatWolfGame.boat), 0, msg='boat is not empty')

    # check if boat capacity is loaded correctly
    def test_boat_capacity(self):
        manGoatWolfRules = Rules('ManGoatWolf.json').rules;
        manGoatWolfGame = GameState(manGoatWolfRules)
        self.assertEqual(manGoatWolfGame.boat_capacity, 2, msg='boat capacity is incorrect')

    # check if default case is false
    def test_lose(self):
        manGoatWolfRules = Rules('ManGoatWolf.json').rules;
        manGoatWolfGame = GameState(manGoatWolfRules)
        self.assertTrue(not manGoatWolfGame.lose)

    def test_violationCombination(self):
        manGoatWolfRules = Rules('ManGoatWolf.json').rules;
        manGoatWolfGame = GameState(manGoatWolfRules)
        self.assertEqual(manGoatWolfGame.violationCombination["wolf"], "goat")
        self.assertEqual(manGoatWolfGame.violationCombination["goat"], "hay")

    print("end new game test")
