# Pathik and Jamie
# @28th October, 2019
import unittest
from riverCrossing import GameState


# this test only applies to the man-goat-hay game;
# change pending: after rules can be imported, initiate temp with correct parameters;

class NewGameTest(unittest.TestCase):
    print("start new game test")

    def test_left_shore(self):
        # checks if left shore has all the characters
        temp = GameState()
        shoreCapacity = len(temp.left_shore)
        self.assertEqual(shoreCapacity, len(temp.left_shore))
        self.assertEqual(temp.left_shore[0], "man")
        self.assertEqual(temp.left_shore[1], "wolf")
        self.assertEqual(temp.left_shore[2], "goat")
        self.assertEqual(temp.left_shore[3], "hay")

    def test_right_shore(self):
        # checks if right shore is empty
        temp = GameState()
        self.assertEqual(len(temp.right_shore), 0, msg='right shore is not empty')

    # checks if boat starts at left shore
    def test_boat_position(self):
        state = GameState()
        self.assertEqual(state.boat_position, "left")

    # checks if boat is empty
    def test_boat(self):
        temp = GameState()
        self.assertEqual(len(temp.boat), 0, msg='boat is not empty')
        print("first test")

    # check if boat capacity is loaded correctly
    def test_boat_capacity(self):
        temp = GameState()
        self.assertEqual(temp.boat_capacity, 2, msg='boat capacity is incorrect')

    # check if default case is false
    def test_lose(self):
        temp = GameState()
        self.assertTrue(not temp.lose)

    def test_violationCombination(self):
        temp = GameState()
        self.assertEqual(temp.violationCombination["wolf"], "goat")
        self.assertEqual(temp.violationCombination["goat"], "hay")

    print("end new game test")
