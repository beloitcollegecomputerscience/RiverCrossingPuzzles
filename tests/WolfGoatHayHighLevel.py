import unittest
from riverCrossing import Move, InvalidMove, GameState

class WolfGoatHayHighLevel(unittest.TestCase):
    def test_select_game(self):
        """Select the Wolf/Goat/Hay game. This tests a speculative mechanism,
        and may need to be changed!"""
        state = GameState.select_game("wolf_goat_hay")
        self.assertEqual(state.game(), "wolf_goat_hay")

    def test_wolf_goat_violation(self):
        "The player should lose if the wolf and goat are alone."
        state = GameState()
        state.apply_move(Move("hay", "boat"))
        state.apply_move(Move("man", "boat"))
        state.apply_move(Move("boat", "right"))
        self.assertEqual(state.has_won(), False);
        self.assertEqual(state.lost(), True);

    def test_hay_goat_violation(self):
        "The player should lose if the hay and goat are alone."
        state = GameState()
        state.apply_move(Move("wolf", "boat"))
        state.apply_move(Move("man", "boat"))
        state.apply_move(Move("boat", "right"))
        self.assertEqual(state.has_won(), False);
        self.assertEqual(state.lost(), True);

    def test_hay_wolf_non_violation(self):
        "The player should not lose if the hay and wolf are alone."
        state = GameState()
        state.apply_move(Move("goat", "boat"))
        state.apply_move(Move("man", "boat"))
        state.apply_move(Move("boat", "right"))
        self.assertEqual(state.has_won(), False);
        self.assertEqual(state.lost(), False);


    def test_move_boat_without_man_fails(self):
        "The boat should not be allowed to move if there's nobody to pilot it."
        state = GameState()
        with self.assertRaises(InvalidMove):
            state.apply_move(Move("boat", "right"))
 
    def test_move_object_to_far_shore_fails(self):
        "The hay should not be allowed to move shores without the boat."
        state = GameState()
        with self.assertRaises(InvalidMove):
            state.apply_move(Move("hay", "right"))   

    def test_win_game_sequence(self):
        state = GameState()
        moves = [Move("goat", "boat"), Move("man", "boat"), Move("boat", "right"),
         Move("goat", "shore"), Move("boat", "left"),
         Move("hay", "boat"), Move("boat", "right"), Move("man", "shore"),
         Move("hay", "shore"), Move("goat", "boat"), Move("man", "boat"),
         Move("boat", "left"), Move("man", "shore"), Move("goat", "shore"),
         Move("wolf", "boat"), Move("man", "boat"), Move("boat", "right"),
         Move("wolf", "shore"), Move("boat", "left"), Move("goat", "boat"),
         Move("boat", "right"), Move("man", "shore"), Move("goat", "shore")]

        for move in moves:
            state.apply_move(move)

        self.assertEqual(state.has_won(), True);
        self.assertEqual(state.lost(), False);

