import unittest

from riverCrossingPuzzles import Location, Validation

"""Checks with Validation class if the move is valid. If yes, update the Location class and call the Animation."""


class ControlTestForMakeMove(unittest.TestCase):

    def test_make_move(self, char_id=2, move='move'):
        """Checks that this is the character we want to work with"""
        self.assertEqual(char_id, 2)
        """Checks that the character is in the right place"""
        self.assertEqual(Location.checkLocation(self, char_id), None)
        """Checks that the move is legal"""
        self.assertEqual(Validation.isLegal(self, move, char_id), None)
        """Updates location"""
        self.assertEqual(Location.updateLocation(self, char_id, 'new location'), None)
