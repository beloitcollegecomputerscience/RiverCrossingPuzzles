import unittest 
from riverCrossingPuzzles import Location
  
class LocationTest(unittest.TestCase): 
          
    def setUp(self): 
        pass
  
    # Test checkLocation method
    def test_check_location_left(self): 
        loc = Location()
        loc.locationDict["Dog"] = "left"
        self.assertEqual(loc.checkLocation("Dog"), "left")
        
    def test_check_location_right(self): 
        loc = Location()
        loc.locationDict["Dog"] = "right"
        self.assertEqual(loc.checkLocation("Dog"), "right")

    def test_check_location_boat(self): 
        loc = Location()
        loc.locationDict["Dog"] = "boat"
        self.assertEqual(loc.checkLocation("Dog"), "boat")

        
    # Test updateLocation method
    def test_update_location_left(self): 
        loc = Location()
        loc.updateLocation("Dog", "left")
        self.assertEqual(loc.locationDict["Dog"], "left")
        
    def test_update_location_right(self): 
        loc = Location()
        loc.updateLocation("Dog", "right")
        self.assertEqual(loc.locationDict["Dog"], "right")

    def test_update_location_boat(self): 
        loc = Location()
        loc.updateLocation("Dog", "boat")
        self.assertEqual(loc.locationDict["Dog"], "boat")
        
if __name__ == '__main__':
    unittest.main()

