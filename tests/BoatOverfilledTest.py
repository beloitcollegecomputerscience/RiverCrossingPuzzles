# by Aidan and Amine
import unittest
from riverCrossing import GameState

class BoatOverfilledTest(unittest.TestCase):

    def test_fullness(self):
        for b_occupants in range(11):
            for b_size in range (11):
                temp = GameState({'boat_capacity':b_size}, b_occupants)
                print("b_occupants = ", b_occupants, ". b_size = ", b_size, ".")
                self.assertIs(temp.boat.isFull(), b_occupants >= b_size)