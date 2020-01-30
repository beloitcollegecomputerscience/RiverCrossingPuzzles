'''
Created on Oct 30, 2019

@author: sauga, wadood, mashfik
'''
from Rules import Rules
from Validation import Validation
from Location import Location
from Animation import Animation

class Control:
    '''
    classdocs
    '''   
    gameNumber = -1
    def setNewGame(self,gameNumber):
        Rules.Reader(self) #Tells Rules Class to load the game from txt file
        
        #takes charID from rules and sends to Location
    def initializeCharacters(self,charID, L): 
        Control.l.addID(charID)
        Control.l = L
        
    def makeMove(self, charID):
        a = Validation().isLegal(move, charID)
        # 1 denotes that the move is legal
        if a ==  1:
            #Update Location 
            Location.addID():
            #Calling Animation
            Animation.Animation.moveChar(self, x, y):
            Animation.Animation.updateImage(self, charID, imageID):
            Animation.Animation.moveBoat(self, x1, y1, x2, y2):
            
        else 
           print("Invalid Move")  
           
    def endCurrentGame(self, hasWon, gameNumber):
        x1 = -1
        y1 = -1
        x2 = -1
        y2 = -1 
        c = Validation.isLegal(self, move, charID)
        #assuming the initial coordinate to be (0,0) and final destination to be (10,10) and assuming it is a legal move
        b = Animation.moveBoat(self, 0, 0, 10, 10)
        if Animation.moveBoat(self, x1, y1, x2, y2) == b and c = 1
            # Call GUI to update the score
            # Reset the Screen
        else 
            Animation.moveBoat(self, 0, 0, 0, 0)     #This means that boat is stable
                     
            
        
        
        
            
         
         
        