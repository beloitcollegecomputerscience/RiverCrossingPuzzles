'''
Test code for boat class' getSpaces() method which would return a list of the available spaces in the boat
'''
import unittest
from riverCrossingPuzzles import Boat

class BoatSpacesTests(unittest.TestCase):
     
    # Test if the boat is empty by comparing the size of the list of empty spaces (list returned by getSpaced) versus the total number
    def test_empty_boat(self):
        self.assertEqual(len(Boat.getSpaces(self)), Boat.boatSize, "Empty boat fail: not empty")
        
    # Test if the boat is not empty nor full
    def test_is_partially_full(self):
        self.assertNotEqual(len(Boat.getSpaces(self)), 0, "Partial boat fail: 0 empty spaces")
        self.assertNotEqual(len(Boat.getSpaces(self)), Boat.boatSize, "Partial boat fail: all empty spaces")
            
    # Test if the boat is full
    def test_is_full(self):
        self.assertEqual(len(Boat.getSpaces(self)), 0, "Full boat fail: not full")
           
    # Loop through the IDs in the list of empty spaces and check if they are valid 
    def test_valid_id(self):
        for spaceID in Boat.getSpaces(self):
            self.assertLess(spaceID, Boat.boatSize, "Invalid ID: greater than maximum capacity")
            self.assertGreaterEqual(spaceID, 0, "Invalid ID: less than 0")
       
    # Check for duplicate IDs in the list of empty spaces
    # The length of the original list is compared against the length of the list that resulted after applying the "set" function (which returns a list w/o duplicates)  
    def test_duplicates(self):
        self.assertEqual(len(Boat.getSpaces(self)), len(set(Boat.getSpaces(self))), "There are duplicate IDs in the list")
     
    # Test if the result of getSpaces() is indeed a list object
    def test_is_list(self):
        self.assertTrue(isinstance(Boat.getSpaces(self), list), "The method getSpaces() did not return a list but a different data type")


if __name__ == "__main__":
    unittest.main()
