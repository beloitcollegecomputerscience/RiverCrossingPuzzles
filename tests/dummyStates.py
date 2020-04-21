from riverCrossing import GameState

class DummyStates ():

    def __init__(self):
        self.left1 = ""
        left2 = ""
        left3 = ""
        left4 = ""
        boat1 = ""
        boat2 = ""
        right1 = ""
        right2 = ""
        right3 = ""
        right4 = ""
        print ("Line 16 reached.")
        sampleSet = generate()

    def generate (self, characters = ["man", "wolf", "goat", "hay"], positions = None):
        if positions == None:
            positions = [self.left1, self.left2, self.left3, self.left4, self.boat1, self.boat2, self.right1, self.right2, self.right3, self.right4]
        print (positions)
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
                        allPossible.append(generate(characters, newPositions))
        return allPossible
