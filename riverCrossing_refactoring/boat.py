import pyglet
import time
import math
import sys
import pprint
import animation

class boat():

	def __init__(self, boat_capacity, driver_name, boat_radius, animation, gameState):
		
		self.animation = animation
		self.gameState = gameState

		self.boat_capacity = boat_capacity
		self.driver_name = driver_name
		self.boat_radius = radius
		self.boat_has_driver = False
		self.characters_on_board = {}


	def add_member(character_name):
		current_boat_members = self.get_number_of_boat_members()
		if current_boat_members >= self.boat_capacity:
			return
		seat_number = self.get_available_seat_number()
		one_seat_size = (boat_radius * 2) / self.boat_capacity
		boat_seat_offset_y = boat_radius/2
		boat_seat_offset_x = (seat_number * one_seat_size)
		# centering the seat
		boat_seat_offset_x += one_seat_size/2 - self.animation.clicked_character["radius"]
		self.animation.set_character_destination_to_boat(clicked_character, boat_seat_offset_x, boat_seat_offset_y)
		self.characters_on_board.update({character_name: seat_number})

	def remove_member(character_name):
		self.animation.set_character_destination_to_shore(clicked_character)
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
			self.gameState.global_state = 'left_shore'
		elif direction == 1:
			self.gameState.global_state = 'right_shore'
		self.animation.set_destinations_to_other_shore(direction)

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
