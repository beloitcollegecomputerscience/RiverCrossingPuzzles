import unittest
from .Move import Move, InvalidMove
from .GameState import GameState
from .SceneState import SceneState
from .Animation import Animation
from .Boat import Boat
from .GUI import GUI
from .Rules import Rules
import sys


class TestGameState(unittest.TestCase):
	def set_up_GUI_game(self):
		rules = Rules("rules.json").rules # "farmer, goat, wolf, and hay" variation
		scene_state = SceneState(rules)
		animation = Animation(scene_state)
		animation.boat = Boat(rules["boat_capacity"], rules["driver_name"],
								scene_state.get_object_by_name("boat")["radius"], animation, scene_state)
		return [rules, scene_state, animation, animation.boat]


	def test_boat_shore_to_shore(self):
		state = GameState()
		self.assertEqual(state.boat_position, "left")

		move = Move("boat", "right")
		state.apply_move(move)
		self.assertEqual(state.boat_position, "right")

		move = Move("boat", "left")
		state.apply_move(move)
		self.assertEqual(state.boat_position, "left")


	# Tests for boat class
	def test_boat_add_member(self):
		rules, scene_state, animation, animation.boat = self.set_up_GUI_game()
		self.assertEqual(animation.boat.if_boat_has_driver(), False)
		self.assertEqual(animation.boat.get_number_of_boat_members(), 0)
		self.assertEqual(animation.boat.is_allowed_to_ride(), False)

		animation.boat.add_member("farmer") # add driver
		self.assertEqual(animation.boat.if_boat_has_driver(), True)
		self.assertEqual(animation.boat.get_number_of_boat_members(), 1)
		self.assertEqual(animation.boat.is_allowed_to_ride(), True)

		animation.boat.add_member("goat") # add second member
		self.assertEqual(animation.boat.if_boat_has_driver(), True)
		self.assertEqual(animation.boat.get_number_of_boat_members(), 2)
		self.assertEqual(animation.boat.is_allowed_to_ride(), True)

		animation.boat.add_member("wolf") # add third member (overload, should refuse)
		self.assertEqual(animation.boat.if_boat_has_driver(), True)
		self.assertEqual(animation.boat.get_number_of_boat_members(), 2)
		self.assertEqual(animation.boat.is_allowed_to_ride(), True)


	def test_boat_remove_member(self):
		rules, scene_state, animation, animation.boat = self.set_up_GUI_game()

		animation.boat.add_member("farmer") # add driver
		animation.boat.add_member("goat") # add second member
		self.assertEqual(animation.boat.if_boat_has_driver(), True)
		self.assertEqual(animation.boat.get_number_of_boat_members(), 2)
		self.assertEqual(animation.boat.is_allowed_to_ride(), True)

		animation.boat.remove_member("goat") # remove a passenger
		self.assertEqual(animation.boat.if_boat_has_driver(), True)
		self.assertEqual(animation.boat.get_number_of_boat_members(), 1)
		self.assertEqual(animation.boat.is_allowed_to_ride(), True)

		animation.boat.remove_member("farmer") # remove driver
		self.assertEqual(animation.boat.if_boat_has_driver(), False)
		self.assertEqual(animation.boat.get_number_of_boat_members(), 0)
		self.assertEqual(animation.boat.is_allowed_to_ride(), False)

		animation.boat.remove_member("wolf") # remove character that isn't on boat, should refuse
		self.assertEqual(animation.boat.if_boat_has_driver(), False)
		self.assertEqual(animation.boat.get_number_of_boat_members(), 0)
		self.assertEqual(animation.boat.is_allowed_to_ride(), False)


	def test_boat_get_available_seat_number(self):
		rules, scene_state, animation, animation.boat = self.set_up_GUI_game()      

		self.assertEqual(animation.boat.get_available_seat_number(), 0)
		animation.boat.add_member("farmer")
		self.assertEqual(animation.boat.get_available_seat_number(), 1)
		animation.boat.add_member("goat") # overload, should refuse
		self.assertEqual(animation.boat.get_available_seat_number(), None)


	def test_boat_try_ride(self):
		rules, scene_state, animation, animation.boat = self.set_up_GUI_game()

		# allow to ride - boat_position should change according to the direction
		animation.boat.add_member("farmer")
		animation.boat.boat_try_ride(1)
		self.assertEqual(scene_state.boat_position, "right")
		animation.boat.boat_try_ride(-1)
		self.assertEqual(scene_state.boat_position, "left")

		# not allow to ride - boat_position should remain left
		animation.boat.remove_member("farmer")
		animation.boat.boat_try_ride(1)
		self.assertEqual(scene_state.boat_position, "left")


	def test_is_any_rule_violated(self):
		rules, scene_state, animation, animation.boat = self.set_up_GUI_game()

		self.assertEqual(animation.boat.is_any_rule_violated(1), False)
		self.assertEqual(animation.boat.is_any_rule_violated(-1), False)

		animation.boat.add_member("farmer")
		animation.boat.add_member("hay")

		self.assertEqual(animation.boat.is_any_rule_violated(1), False)
		self.assertEqual(animation.boat.is_any_rule_violated(-1), False)

		animation.boat.boat_try_ride(1)

		self.assertEqual(animation.boat.is_any_rule_violated(1), True)
		self.assertEqual(animation.boat.is_any_rule_violated(-1), False)


	# Tests for SceneState
	def test_get_character_list(self):
		rules, scene_state, animation, animation.boat = self.set_up_GUI_game()
		self.assertEqual(len(scene_state.get_character_list()), 4)


	def test_get_object_by_name(self):
		rules, scene_state, animation, animation.boat = self.set_up_GUI_game()
		farmer = scene_state.get_object_by_name("farmer")
		self.assertEqual(farmer["name"], "farmer")


	def test_has_won(self):
		rules, scene_state, animation, animation.boat = self.set_up_GUI_game()

		self.assertEqual(scene_state.has_won(True, 0), False) # no one on right shore

		for name in scene_state.get_character_list(): # put all characters on right shore
			character_object = scene_state.get_object_by_name(name)
			character_object["current_shore"] = "right"

		self.assertEqual(scene_state.has_won(True, 1), False)
		self.assertEqual(scene_state.has_won(False, 0), False)
		self.assertEqual(scene_state.has_won(True, 0), True)


	#Tests for ObjectLocation
	def test_set_destinations_to_other_shore(self):
		rules, scene_state, animation, animation.boat = self.set_up_GUI_game()

		scene_state.object_locations.set_destinations_to_other_shore(1)
		for character_name in scene_state.object_locations.character_list:
			if character_name in scene_state.characters_on_board:
				character_object = scene_state.get_object_by_name(character_name)
				self.assertEqual(character_object["current_destination"][0], scene_state.object_locations.river_boat_travel_distance)
				self.assertEqual(character_object["current_shore"], scene_state.boat_position)
