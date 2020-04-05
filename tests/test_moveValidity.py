import unittest
from riverCrossing import GameState
from riverCrossing.GameState import apply_move

class testMoveValidity(unittest.TestCase):

    left1 = ""
    left2 = ""
    left3 = ""
    left4 = ""
    boat1 = ""
    boat2 = ""
    right1 = ""
    right2 = ""
    right3 = ""
    right4 = ""
    sampleSet = []

    def generateDummyGameStates(self, characters = ["man", "wolf", "goat", "hay"],
    positions = [left1, left2, left3, left4, boat1, boat2, right1, right2, right3, right4]):
        allPossible = []
        if (characters.len() == 0):
            instanceLeft  = [positions[0], positions[1], positions[2], positions[3]]
            instanceRight  = [positions[6], positions[7], positions[8], positions[9]]
            instanceBoat = [positions[4], positions[5]]
            print (instanceLeft + instanceBoat + instanceRight + "/n")
            return GameState(instanceLeft, instanceBoat, instanceRight)
        else:
            for character in characters:
                characters.remove(character)
                for position in positions:
                    if (position == ""):
                        newPositions = positions
                        newPositions[positions.index(position)] = character
                        allPossible.append(generateDummyGameStates(characters, newPositions))
        return allPossible

    def __init__(self):
        sampleSet = generateDummyGameStates

    def test_basic(self):
        self.assertGreater(sampleSet.len(), 0)
