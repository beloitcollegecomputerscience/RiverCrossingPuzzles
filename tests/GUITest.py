import unittest
from riverCrossing import GUI

class GUITest(unittest.TestCase):

    def testInitializePosition(self, charID): 
        gui = GUI()
        gui.initializePosition(charID, 0, 0)
        self.assertEqual(gui.charID.x, 0, "Wrong x value")
        self.assertEqual(gui.charID.y, 0, "Wrong y value")
