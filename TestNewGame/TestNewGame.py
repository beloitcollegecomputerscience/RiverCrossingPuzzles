#Pathik and Jamie
#@28th October, 2019
import unittest

class testClasses:
    def _init_(self,gameNumber):
        self.gameID = gameNumber
         
    def load(self, gameName):
        print("load Class ") 
    def setNewGame(self, gameName):
        print("setNewGame Class")
    
#checks if the setNewGame method from the Control class sends a game name to the Rules class
class TestNewGame(unittest.TestCase):
    print("start test")
    def test_load(self):
        gameName=5
        temp = testClasses(gameName)
        #checks if load method has a gameName that is chosen
        self.assertIsNotNone(temp.load().gameName, msg='Load method has no game name')
        print("first test")
        
    print('between tests 1')

    def test_setNewGame(self):
        gameName=5
        temp = testClasses(gameName)
        #checks if setNewGame method has a gameName to send
        self.assertIsNotNone(gameName, msg='setNewGame method has no game name ')
        print("second test")
        self.assertEqual(gameName, temp.setNewGame().gameName, msg='the Load method and setNewGame method have different or no game names')
        print("third test")
    print("end test")