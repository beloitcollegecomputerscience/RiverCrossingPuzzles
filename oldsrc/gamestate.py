"""An unimplemented GameState class."""

from . import Boat

class GameState:
    def __init__(self, rules, numOccupants):
        self.boat = Boat(numOccupants)
        self.rules = rules
