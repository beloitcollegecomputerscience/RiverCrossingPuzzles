import pyglet
import time
from pyglet.window import mouse
import math
import sys
import pprint

class Animation(pyglet.window.Window):
	"""
	This class creates a general layout that can be applied to all versions of the game 
	with less than 6 characters and no island. Modify images to set up new games.
	"""
	def __init__(self):

		self.images_folder = "images/"

		self.scene_objects = self.get_scene_objects()
		self.init_sprites()
		background_image = self.get_object_by_name("background")["image"]
		pyglet.window.Window.__init__(self, width = background_image.width, height = background_image.height)

		#These values are based on the current background's size. Be careful when use different background.
		self.river = 660
		self.river_boat_travel_distance = 270
		self.distance_to_other_shore = 750
		self.hor_gap = 10
		self.ver_gap = 0
		self.large_bottom_margin = 470
		self.each_height = 65
		self.each_width = 100

		self.character_list = self.get_character_list()
		print("Character list: ", self.character_list)
		self.characters_on_board = {}
		self.boat_capacity = 2

		self.global_state = 'left_shore'
		self.set_initial_destinations()
		pyglet.clock.schedule_interval(self.update, 1/200.0)

	def on_draw(self):
		self.main_batch.draw()

	def on_mouse_press(self,x, y, button, modifiers):
		if self.global_state == 'left_shore':
			clicked_character = self.get_clicked_character(x, y)
			if clicked_character != None:
				self.process_clicked_character(x, y, clicked_character)
			elif self.boat_clicked(x, y):
				self.boat_try_ride(1, x, y)

		elif self.global_state == 'right_shore':
			clicked_character = self.get_clicked_character(x, y)
			if clicked_character != None:
				self.process_clicked_character(x, y, clicked_character)
			elif self.boat_clicked(x, y):
				self.boat_try_ride(-1, x, y)

	def update(self, duration):
		# print(global_state)
		velocity = 300

		if self.global_state == "won":
			self.announce_winner()

		for scene_object in self.scene_objects:
			scene_object["is_animating"] = self.animate(scene_object["sprite"],	scene_object["current_destination"], 
														duration, velocity)

		if self.has_won():
			self.global_state = "won"

	def announce_winner(self):
		announcement = self.get_object_by_name("winning_announcement")
		announcement["sprite"].group = pyglet.graphics.OrderedGroup(30)

	def animate(self, sprt, destination, duration, velocity):
		if self.check_if_sprite_at_destination(sprt, destination):
			return False
		if sprt.x < destination[0] - 1:
			sprt.x += velocity * duration
		if sprt.x > destination[0] + 1:
			sprt.x -= velocity * duration
		if sprt.y < destination[1] - 1:
			sprt.y += velocity * duration
		if sprt.y > destination[1] + 1:
			sprt.y -= velocity * duration
		return True	

	def check_if_sprite_at_destination(self, sprt, destination):
		if abs(sprt.x - destination[0]) > 5:
			return False
		if abs(sprt.y - destination[1]) > 5:
			return False
		return True

	def check_if_all_stopped(self):
		for name in self.character_list:
			character_object = self.get_object_by_name(name)
			if character_object["is_animating"] == True:
				return False
		return True

	def reset_sprites_positions(self):
		# TODO: should be rewritten using the list approach
		off_screen_y = 450
		self.move_sprite_to(self.sprite_goat, 0, off_screen_y)
		self.move_sprite_to(self.sprite_wolf, 0, off_screen_y)
		self.move_sprite_to(self.sprite_farmer, 0, off_screen_y)
		self.move_sprite_to(self.sprite_cabbage, 0, off_screen_y)
		self.move_sprite_to(self.boat, 270, 218)

	def set_initial_destinations(self):
		self.get_object_by_name("boat")["current_destination"] = [270, 218]
		for i in range(len(self.character_list)):			
			character_name = self.character_list[i]
			character_object = self.get_object_by_name(character_name)
			calculated_position = self.calculate_shore_position_slot(i)			
			character_object["calculated_shore_position"] = calculated_position
			character_object["current_destination"] = calculated_position
			character_object["current_shore"] = self.global_state

		# self.destination_goat = [self.hor_gap + self.each_width, self.large_bottom_margin + self.each_height + self.ver_gap]
		# self.destination_wolf = [self.hor_gap + self.each_width, self.large_bottom_margin + self.each_height * 2 + self.ver_gap * 2]
		# self.destination_farmer = [self.hor_gap, self.small_bottom_margin + self.each_height * 2 + self.ver_gap * 2]
		# self.destination_cabbage = [self.hor_gap, self.small_bottom_margin + self.each_height + self.ver_gap]

	# automatically calculates chequerwise positions for any new character 
	def calculate_shore_position_slot(self, character_index):
		character_index = character_index + 1 # starting with 1 and not with 0

		# (character_index % 2) infinitely toggles between 1 and 0 for each incrementing index
		horizontal_position = (character_index % 2) * self.each_width
		x = self.hor_gap + horizontal_position

		# vertical_position increases proportionally with higher character_index
		vertical_position = (character_index) * self.each_height
		y = self.ver_gap + self.large_bottom_margin - vertical_position
		return [x, y]

	def set_destinations_to_other_shore(self, direction):
		self.get_object_by_name("boat")["current_destination"][0] += direction * self.river_boat_travel_distance
		for character_name in self.character_list:
			if character_name in self.characters_on_board:
				character_object = self.get_object_by_name(character_name)
				character_object["current_destination"][0] += direction * self.river_boat_travel_distance
				character_object["current_shore"] = self.global_state

	def move_sprite_to(self, sprite, x, y):
		sprite.x = x
		sprite.y = y
		return sprite

	def set_character_destination_to_boat(self, character, offset_x, offset_y):
		boat_position = self.get_object_by_name("boat")["current_destination"]
		character["current_destination"] = [boat_position[0] + offset_x, boat_position[1] + offset_y]

	def set_character_destination_to_shore(self, character):
		character["current_destination"] = list(character["calculated_shore_position"])
		if self.global_state == "right_shore":
			character["current_destination"][0] += self.distance_to_other_shore

	def get_clicked_character(self,x, y):
		for character_name in self.character_list:
			character_object = self.get_object_by_name(character_name)
			collider_radius = character_object["radius"]
			if self.global_state != character_object["current_shore"]:
				continue
			if self.sprite_clicked_within_radius(x, y, character_object["sprite"], collider_radius):
				return character_object
		return None

	def process_clicked_character(self, x, y, clicked_character):
		character_name = clicked_character["name"]
		character_is_in_boat = character_name in self.characters_on_board
		if character_is_in_boat:
			self.set_character_destination_to_shore(clicked_character)
			del self.characters_on_board[character_name]
		else:
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
		print("\nGoat was clicked")	

	def get_available_seat_number(self):
		occupied_seats = self.characters_on_board.values()
		for possible_seat in range(self.boat_capacity):
			if possible_seat not in occupied_seats:
				return possible_seat
		return None
			

	def boat_clicked(self, x, y):
		boat_object = self.get_object_by_name("boat")
		boat_collider_radius = boat_object["radius"]		
		return self.sprite_clicked_within_radius(x, y, boat_object["sprite"], boat_collider_radius)

	def boat_try_ride(self, direction, x, y):
		print('\nBoat was clicked, trying to ride!')
		if not self.is_allowed_to_ride():
			return		
		if direction == -1:
			self.global_state = 'left_shore'
		elif direction == 1:
			self.global_state = 'right_shore'
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
		driver_name = 'farmer'
		return driver_name in self.characters_on_board

	def sprite_clicked_within_radius(self, x, y, sprite, collider_radius):
		center_x = sprite.x + collider_radius
		center_y = sprite.y + collider_radius
		if (abs(x - center_x) < collider_radius) and (abs(y - center_y) < collider_radius):
			return True
		return False

	# initial_position are coordinates that have been approved and can be used for any set of characters
	# initial_scale is based on original sizes of the source images. Be careful when use different images.
	# Objects are dynamically created from this configuration array, make sure objects names are unique!
	def get_scene_objects(self):
		return [
			{
				"name": "farmer",
				"image_filename": "farmer.png",
				"draw_layer": 20,
				"initial_position": [0, 450],
				"current_destination": [0, 0],
				"initial_scale": 0.15,
				"is_animating": False,
				"is_character": True,
				"radius": 40
			},			
			{
				"name": "wolf",
				"image_filename": "wolf.png",
				"draw_layer": 20,
				"initial_position": [0, 450],
				"current_destination": [0, 0],
				"initial_scale": 0.15,
				"is_animating": False,
				"is_character": True,
				"radius": 55
			},
			{
				"name": "goat",
				"image_filename": "goat.png",
				"draw_layer": 20,
				"initial_position": [0, 450],
				"current_destination": [0, 0],
				"initial_scale": 0.15,
				"is_animating": False,
				"is_character": True,
				"radius": 40
			},			
			{
				"name": "cabbage",
				"image_filename": "cabbage.png",
				"draw_layer": 20,
				"initial_position": [0, 450],
				"current_destination": [0, 0],
				"initial_scale": 0.15,
				"is_animating": False,
				"is_character": True,
				"radius": 40
			},
			{
				"name": "boat",
				"image_filename": "boat.png",
				"draw_layer": 10,
				"initial_position": [270,218],
				"current_destination": [0, 0],
				"initial_scale": 0.2,
				"is_animating": False,
				"is_character": False,
				"radius": 75
			},
			{
				"name": "background",
				"image_filename": "background.png",
				"draw_layer": 5,
				"initial_position": [0, 0],
				"current_destination": [0, 0],
				"initial_scale": 1,
				"is_animating": False,
				"is_character": False,
				"radius": None
			},
			{
				"name": "winning_announcement",
				"image_filename": "you-win.png",
				"draw_layer": 0,
				"initial_position": [200, 180],
				"current_destination": [200, 180],
				"initial_scale": 1,
				"is_animating": False,
				"is_character": False,
				"radius": None
			}
		]

	def get_character_list(self):
		character_list = []
		for scene_object in self.scene_objects:
			if scene_object["is_character"]:
				character_list.append(scene_object["name"])
		return character_list

	def get_object_by_name(self, name):
		for scene_object in self.scene_objects:
			if scene_object["name"] == name:
				return scene_object
				break
		return None

	def init_sprites(self):
		self.main_batch = pyglet.graphics.Batch()
		for scene_object in self.scene_objects:
			scene_object["image"] = pyglet.resource.image(self.images_folder + scene_object["image_filename"])
			scene_object["sprite"] = pyglet.sprite.Sprite(
					img=scene_object["image"],
					x=scene_object["initial_position"][0],
					y=scene_object["initial_position"][1],
					batch=self.main_batch,
					group=pyglet.graphics.OrderedGroup(scene_object["draw_layer"]))
			scene_object["sprite"].scale = scene_object["initial_scale"]

	def has_won(self):
		if self.check_if_all_stopped() == False:
			return False
		if self.get_number_of_boat_members() != 0:
			return False
		for name in self.character_list:
			character_object = self.get_object_by_name(name)
			if character_object["current_shore"] != "right_shore":
				return False
		return True

if __name__ =='__main__':
	window = Animation()
	pyglet.app.run()
