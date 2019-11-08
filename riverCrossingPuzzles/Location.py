class Location:
    
    #Location has a array of ID
    def addID(self,charID):
        Location.ids.append(charID);
    
    def __init__(self):
        global ids
        Location.ids=[]
        