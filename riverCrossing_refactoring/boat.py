import pyglet
import time
import math
import sys
import pprint

class boat():
	characters_on_board = {}
	boat_capacity = 0
	boat_has_driver = False
	driver_name = ''
	boat_state = 'left_shore'

	def __init__(boat_capacity, driver_name):
		self.boat_capacity = boat_capacity
		self.driver_name = driver_name

	def add_member(character_name):
		current_boat_members = self.get_number_of_boat_members()
		if current_boat_members >= self.boat_capacity:
			return
		seat_number = self.get_available_seat_number()
		boat_radius = self.get_object_by_name("boat")["radius"]
		one_seat_size = (boat_radius * 2) / self.boat_capacity
		boat_seat_offset_y = boat_radius/2
		boat_seat_offset_x = (seat_number * one_seat_size)
		# centering the seat
		boat_seat_offset_x += one_seat_size/2 - clicked_character["radius"]
		self.set_character_destination_to_boat(clicked_character, boat_seat_offset_x, boat_seat_offset_y)
		self.characters_on_board.update({character_name: seat_number})

	def remove_member(character_name):
		self.set_character_destination_to_shore(clicked_character)
		del self.characters_on_board[character_name]

	def get_available_seat_number(self):
		occupied_seats = self.characters_on_board.values()
		for possible_seat in range(self.boat_capacity):
			if possible_seat not in occupied_seats:
				return possible_seat
		return None

	def boat_try_ride(self, direction, x, y):
		print('\nBoat was clicked, trying to ride!')
		if not self.is_allowed_to_ride():
			return		
		if direction == -1:
			self.boat_state = 'left_shore'
		elif direction == 1:
			self.boat_state = 'right_shore'
		self.set_destinations_to_other_shore(direction)

	def is_allowed_to_ride(self):
		number_of_boat_members = self.get_number_of_boat_members()
		boat_has_driver = self.if_boat_has_driver()

		print(str(number_of_boat_members) + " characters on board!")
		print("Passengers and seats:", self.characters_on_board)
		print("Is driver present? " + str(boat_has_driver))

		return number_of_boat_members <= self.boat_capacity and boat_has_driver

	def get_number_of_boat_members(self):
		return len(self.characters_on_board)

	def if_boat_has_driver(self):
		return driver_name in self.characters_on_board
