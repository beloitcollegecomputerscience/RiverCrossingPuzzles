# Rita
# April 2020
import unittest
from riverCrossing import GameState
from riverCrossing.Rules import Rules


class NewGameTest(unittest.TestCase):
    print("start new game test")

    def test_left_shore(self):
        # checks if left shore has all the characters
        manGoatWolfRules = Rules('../riverCrossing/ManGoatWolf.json').rules
        manGoatWolfGame = GameState(manGoatWolfRules)
        self.assertEqual(len(manGoatWolfGame.left_shore), len(manGoatWolfRules["left_shore"]))
        self.assertEqual(manGoatWolfGame.left_shore, manGoatWolfRules["left_shore"])

        twoGoatRules = Rules('../riverCrossing/2goat.json').rules
        twoGoatGame = GameState(twoGoatRules)
        self.assertEqual(len(twoGoatGame.left_shore), len(twoGoatRules["left_shore"]))
        self.assertEqual(twoGoatGame.left_shore, twoGoatRules["left_shore"])

    # checks if right shore is empty
    def test_right_shore(self):
        manGoatWolfRules = Rules('../riverCrossing/ManGoatWolf.json').rules;
        manGoatWolfGame = GameState(manGoatWolfRules)
        self.assertEqual(len(manGoatWolfGame.right_shore), 0, msg='right shore is not empty')

    # checks if boat starts at left shore
    def test_boat_position(self):
        manGoatWolfRules = Rules('../riverCrossing/ManGoatWolf.json').rules;
        manGoatWolfGame = GameState(manGoatWolfRules)
        self.assertEqual(manGoatWolfGame.boat_position, manGoatWolfRules["boat_position"])

    # checks if boat is empty
    def test_boat(self):
        manGoatWolfRules = Rules('../riverCrossing/ManGoatWolf.json').rules;
        manGoatWolfGame = GameState(manGoatWolfRules)
        self.assertEqual(len(manGoatWolfGame.boat), 0, msg='boat is not empty')

    # check if boat capacity is loaded correctly
    def test_boat_capacity(self):
        manGoatWolfRules = Rules('../riverCrossing/ManGoatWolf.json').rules;
        manGoatWolfGame = GameState(manGoatWolfRules)
        self.assertEqual(manGoatWolfGame.boat_capacity, 2, msg='boat capacity is incorrect')

    # check if default case is false
    def test_lose(self):
        manGoatWolfRules = Rules('../riverCrossing/ManGoatWolf.json').rules;
        manGoatWolfGame = GameState(manGoatWolfRules)
        self.assertTrue(not manGoatWolfGame.lose)

    def test_violationCombination(self):
        manGoatWolfRules = Rules('../riverCrossing/ManGoatWolf.json').rules;
        manGoatWolfGame = GameState(manGoatWolfRules)
        self.assertEqual(manGoatWolfGame.violation_combination[0][0], ['goat', 'hay'])
        self.assertEqual(manGoatWolfGame.violation_combination[1][0], ['wolf','hay'])

    def test_drivers(self):
        # code to be added after driver detection code is available
        return True

    print("end new game test")
