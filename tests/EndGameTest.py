'''
Created on Oct 31, 2019

@author: sauga, wadood, and mashfik
'''
import unittest
from riverCrossing import Control, Animation, Location, Rules, Validation


class EndGameTest(unittest.TestCase):
    
    def testendCurrentGame(self):
        testgameNumber = 12
        testCharID = 300
        testhasWon = True
        # We are assuming move to be coordinates
        move = "leftShore"
        x1 = 0
        x = 10
        y = 32434
        x1 = 20
        y1 = -1
        y2 = -4
        x2 = 20
        C = Control()  
        Validation.isLegal(self, move, testCharID)
        Animation.moveBoat(self, x1, y1, x2, y2)
        Animation.moveChar(self, x, y)
        C.endCurrentGame(testhasWon, testgameNumber)
        
        print(C.endCurrentGame)
        assert testCharID in C.endCurrentGame, "Error, ID not found in location"
        assert testgameNumber in C.endCurrentGame, "Invalid Game Number"
        assert testhasWon in C.endCurrentGame, "Game is neither won or lost"       
        