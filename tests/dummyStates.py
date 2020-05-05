from riverCrossing import GameState
from riverCrossing.Rules import Rules

class DummyStates ():

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
    print ("Line 16 reached.")

    def generate (self, characters = ["man", "wolf", "goat", "hay"], positions = None):
        if positions == None:
            positions = [DummyStates.left1, DummyStates.left2, DummyStates.left3, DummyStates.left4, DummyStates.boat1,
            DummyStates.boat2, DummyStates.right1, DummyStates.right2, DummyStates.right3, DummyStates.right4]
        print (positions)
        allPossible = []
        if (len(characters) == 0):
            instanceLeft  = [positions[0], positions[1], positions[2], positions[3]]
            instanceRight  = [positions[6], positions[7], positions[8], positions[9]]
            instanceBoat = [positions[4], positions[5]]
            #print (''.join(instanceLeft).join(instanceBoat).join(instanceRight) + "/n")
            return GameState(self.makeRulesList(instanceLeft, instanceBoat, instanceRight))
        else:
            for character in characters:
                characters.remove(character)
                for position in positions:
                    if (position == ""):
                        newPositions = positions
                        newPositions[positions.index(position)] = character
                        allPossible.append(self.generate(characters, newPositions))
        print("Done generating.")
        return allPossible
    
    def makeRulesList (self, instanceLeft, instanceBoat, instanceRight):
        rawWolfGoatRules = Rules("riverCrossing/ManGoatWolf.json").rules
        rawWolfGoatRules["beginLeft"] = instanceLeft
        rawWolfGoatRules["beginBoat"] = instanceBoat
        rawWolfGoatRules["beginRight"] = instanceRight
        return rawWolfGoatRules
