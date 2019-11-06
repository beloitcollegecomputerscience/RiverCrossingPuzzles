import unittest 
import LocationTesting.location
  
class testing_location(unittest.TestCase): 
          
    def setUp(self): 
        pass
  
    # Test checkLocation method
    def test_check_location_left(self): 
        loc = LocationTesting.location.location()
        loc.locationDict["Dog"] = "left"
        self.assertEqual(loc.checkLocation("Dog"), "left")
        
    def test_check_location_right(self): 
        loc = LocationTesting.location.location()
        loc.locationDict["Dog"] = "right"
        self.assertEqual(loc.checkLocation("Dog"), "right")

    def test_check_location_boat(self): 
        loc = LocationTesting.location.location()
        loc.locationDict["Dog"] = "boat"
        self.assertEqual(loc.checkLocation("Dog"), "boat")

        
    # Test updateLocation method
    def test_update_location_left(self): 
        loc = LocationTesting.location.location()
        loc.updateLocation("Dog", "left")
        self.assertEqual(loc.locationDict["Dog"], "left")
        
    def test_update_location_right(self): 
        loc = LocationTesting.location.location()
        loc.updateLocation("Dog", "right")
        self.assertEqual(loc.locationDict["Dog"], "right")

    def test_update_location_boat(self): 
        loc = LocationTesting.location.location()
        loc.updateLocation("Dog", "boat")
        self.assertEqual(loc.locationDict["Dog"], "boat")
        
if __name__ == '__main__':
    unittest.main()

