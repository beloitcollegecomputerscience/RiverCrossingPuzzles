from . import Boat

class GameState:
    def __init__(self, rules, numOccupants):
        self.boat = Boat(numOccupants)
        this.rules = rules
