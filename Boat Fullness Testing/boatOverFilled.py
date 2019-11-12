# by Aidan and Amine

import unittest

class dummyGame:

    def __init__(self, capacity, occupants):
        self.boat_capacity = capacity
        self.numOccupants = occupants
        self.boat_population = [None] * self.numOccupants

    def boat_is_full(self):
        print("Boat size  = ", len(self.boat_population), ". Boat capacity = ", self.boat_capacity,
              ". \n ~~~~~~~~~~~~~~~~~~")
        if len(self.boat_population) >= self.boat_capacity:
            return True
        else:
            return False


class Testing(unittest.TestCase):

    def test_fullness(self):
        for b_occupants in range(11):
            for b_size in range (11):
                temp = dummyGame(b_size, b_occupants)
                print("b_occupants = ", b_occupants, ". b_size = ", b_size, ".")
                self.assertIs(temp.boat_is_full(), b_occupants >= b_size)

if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()