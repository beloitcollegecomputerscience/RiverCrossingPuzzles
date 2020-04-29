
def checkForDriver():
	for i in range(0, thingsInBoat-1):
		 if thingsInBoat[i].isDriver():
 return true
else:
		return false

def test_no_occupants_no_drivers(self):
   #code to set number of occupants in boat to 0.
    self.assertEqual(checkForDriver, false, "Empty has no drivers fail")
 
def test_things_in_boat_no_drivers(self):
   #code to put occupants in boat that aren't drivers
    self.assertEqual(checkForDriver, false, "Things in boat, no drivers fail")
 
def test_things_in_boat_yes_drivers(self):
   #code to put occupants in boat that are drivers
    self.assertEqual(checkForDriver, true, "Things in boat, yes drivers fail")
