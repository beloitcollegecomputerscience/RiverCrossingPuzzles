#!/usr/bin/env python3
import unittest
from game_object_mocks import GameState, Boat

class TestBoatMethods(unittest.TestCase):

    def test_boat_unmoved_starts_left_stays_left(self):
        state = GameState()
        self.assertEqual(state.boat.getShore(), "left")

    def test_boat_explicitly_left_is_left(self):
        state = GameState()
        state.boat.move_to_shore("left")
        self.assertEqual(state.boat.getShore(), "left")

    def test_boat_explicitly_right_is_right(self):
        state = GameState()
        state.boat.move_to_shore("right")
        self.assertEqual(state.boat.getShore(), "right")
        
if __name__ == '__main__':
    unittest.main()
