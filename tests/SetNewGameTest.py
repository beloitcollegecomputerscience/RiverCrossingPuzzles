#Pathik and Jamie
#@28th October, 2019
import unittest
from riverCrossingPuzzles import Control

#checks if the setNewGame method from the Control class sends a game name to the Rules class
class SetNewGameTest(unittest.TestCase):
    print("start test")
    def test_load(self):
        #checks if load method has a gameName that is chosen
        self.assertIsNotNone(Control.gameName, msg='Load method has no game name')
        print("first test")
        
    print('between tests 1')

    def test_setNewGame(self):
        #checks if setNewGame method has a gameName to send
        self.assertIsNotNone(Control.gameName, msg='setNewGame method has no game name ')
        print("second test")
        self.assertEqual(Control.gameName, Control.setNewGame().gameName, msg='the Load method and setNewGame method have different or no game names')
        print("third test")
    print("end test")