class GUI :
    
    class charId:
        x = -1; 
        y = -1;
        
        # parameterized constructor 
        def __init__(self, x, y): 
            self.x = x 
            self.y = y 
    
    
    def initializePosition(self, charId, x, y):
        charId.x = x;
        charId.y = y;
                