class Control:
    
    #takes charID from rules and sends to Location
    def initializeCharacters(self,charID): 
        Control.l.addID(charID)
        print("charid added to location")
        
    #pass a reference to the Location class so that we can access it.
    def __init__(self,L):
        Control.l=L