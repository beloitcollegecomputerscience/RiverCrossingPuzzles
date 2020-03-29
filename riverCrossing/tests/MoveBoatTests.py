import unittest

from riverCrossing import Move, InvalidMove
from riverCrossing import GameState

class TestGameState(unittest.TestCase):
    def test_boat_shore_to_shore(self):
        state = GameState()
        self.assertEqual(state.boat_position, "left")

        move = Move("boat", "right")
        state.apply_move(move)
        self.assertEqual(state.boat_position, "right")

        move = Move("boat", "left")
        state.apply_move(move)
        self.assertEqual(state.boat_position, "left")

