
class GUI:
    charID = (-1,-1)
   
    # parameterized constructor 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    
    
    def initializePosition(self, charID, x, y):
        charID.x = x
        charID.y = y
                