import unittest

from Move import Move, InvalidMove
from GameState import GameState

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
        
    def test_win_condition(self):
        state = GameState()
        state.apply_move("goat", "onto boat")
        state.apply_move("hay", "onto boat")
        state.apply_move("man", "onto boat")
        state.apply_move("wolf", "onto boat")
        state.apply_move("boat", "right")
        state.apply_move("man", "off of boat")
        state.apply_move("wolf", "off of boat")
        state.apply_move("goat", "off of boat")
        state.apply_move("hay", "off of boat")
        self.assertEqual(state.right_shore, ["man","wolf", "goat", "hay"])    
    