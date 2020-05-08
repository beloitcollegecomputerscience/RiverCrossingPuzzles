import unittest
from .Move import Move, InvalidMove
from .GameState import GameState
from .SceneState import SceneState
from .Animation import Animation
from .Boat import Boat
from .GUI import GUI
from .Rules import Rules
from .MainMenu import MainMenu
from .AudioPlayer import AudioPlayer
import sys


class TestGameState(unittest.TestCase):
	def set_up_GUI_game(self):
		audio_player = AudioPlayer()
		scene_state = SceneState(audio_player)
		menu = MainMenu(scene_state)
		menu.load_new_game_with_config("config_01")
		animation = scene_state.animation
		boat = scene_state.boat
		return [scene_state, animation, boat]

	# Tests for boat class
	def test_boat_add_member(self):
		scene_state, animation, animation.boat = self.set_up_GUI_game()
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
		scene_state, animation, animation.boat = self.set_up_GUI_game()

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
		scene_state, animation, animation.boat = self.set_up_GUI_game()      

		self.assertEqual(animation.boat.get_available_seat_number(), 0)
		animation.boat.add_member("farmer")
		self.assertEqual(animation.boat.get_available_seat_number(), 1)
		animation.boat.add_member("goat") # overload, should refuse
		self.assertEqual(animation.boat.get_available_seat_number(), None)


	def test_boat_try_ride(self):
		scene_state, animation, animation.boat = self.set_up_GUI_game()

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
		scene_state, animation, animation.boat = self.set_up_GUI_game()

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
		scene_state, animation, animation.boat = self.set_up_GUI_game()
		self.assertEqual(len(scene_state.get_character_list()), 4)


	def test_get_object_by_name(self):
		scene_state, animation, animation.boat = self.set_up_GUI_game()
		farmer = scene_state.get_object_by_name("farmer")
		self.assertEqual(farmer["name"], "farmer")


	def test_has_won(self):
		scene_state, animation, animation.boat = self.set_up_GUI_game()

		self.assertEqual(scene_state.has_won(True), False) # no one on right shore & no one on boat

		for name in scene_state.get_character_list(): # put all characters on right shore
			character_object = scene_state.get_object_by_name(name)
			character_object["current_shore"] = "right"

		animation.boat.add_member("farmer") # 1 characer on boat
		self.assertEqual(scene_state.has_won(True), False)

		animation.boat.remove_member("farmer") # no one on boat
		self.assertEqual(scene_state.has_won(False), False)
		self.assertEqual(scene_state.has_won(True), True)


	#Tests for ObjectLocation
	def test_set_destinations_to_other_shore(self):
		scene_state, animation, animation.boat = self.set_up_GUI_game()

		scene_state.object_locations.set_destinations_to_other_shore(1)
		for character_name in scene_state.object_locations.character_list:
			if character_name in scene_state.characters_on_board:
				character_object = scene_state.get_object_by_name(character_name)
				self.assertEqual(character_object["current_destination"][0], scene_state.object_locations.river_boat_travel_distance)
				self.assertEqual(character_object["current_shore"], scene_state.boat_position)
