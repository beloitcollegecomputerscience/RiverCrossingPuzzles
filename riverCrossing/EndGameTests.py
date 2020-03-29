import unittest

from riverCrossing import Move, InvalidMove
from riverCrossing import GameState

class EndGameTests(unittest.TestCase):
    def test_win_condition(self):
        state = GameState()
        state.apply_move(Move("hay", "boat"))
        state.apply_move(Move("goat", "boat"))
        state.apply_move(Move("boat", "right"))
        state.apply_move(Move("goat", "shore"))
        state.apply_move(Move("hay", "shore"))
        state.apply_move(Move("boat", "left"))
        state.apply_move(Move("man", "boat"))
        state.apply_move(Move("wolf", "boat"))
        state.apply_move(Move("boat", "right"))
        state.apply_move(Move("man", "shore"))
        state.apply_move(Move("wolf", "shore"))
        self.assertEqual(state.has_won(), True)    
    
    def test_violating_conditions(self):
        state = GameState()
        state.left_shore = []
        state.right_shore = []
        locations = [state.left_shore, state.right_shore]
        checkconditions = [['wolf','hay'], ['goat','hay']]
        for location in locations:
            for curr_check in checkconditions:
                location = curr_check
                state.checkIfObjectsClash(location)
                self.assertEqual(state.lost(), True)
                state.lose = False