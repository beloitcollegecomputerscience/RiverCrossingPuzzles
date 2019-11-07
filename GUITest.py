from GUI import GUI as GUI
from cgi import test

class testGUI :

    def testInitializePosition(self, charId): 
        gui = GUI()
        gui.initializePosition(charId, 0, 0)
        assert (charId.x == 0), "Wrong x value"
        assert (charId.y == 0), "Wrong y value"
        

t= testGUI()
chID = GUI.charId(2,3)
t.testInitializePosition(chID)
