from Control import Control
from Location import Location
import unittest

class Testing(unittest.TestCase):
    
    def testInitializeCharacters(self):
        testID=1212 #assume a random testID
        l=Location()
        C=Control(l)
        C.initializeCharacters(testID)
        assert testID in l.ids, "Error, ID not found in location"