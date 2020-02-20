import pyglet
import time
from pyglet.window import mouse

class Animation(pyglet.window.Window):
	"""
	This class creates a general layout that can be applied to all versions of the game 
	with less than 6 characters and no island. Modify images to set up new games.
	"""
	def __init__(self):
		self.images = {
    		"wolf": pyglet.resource.image("images/wolf.png"),
    		"goat": pyglet.resource.image("images/goat.png"),
    		"farmer": pyglet.resource.image("images/farmer.png"),
    		"cabbage": pyglet.resource.image("images/cabbage.png"),
    		"boat": pyglet.resource.image("images/boat.png"),
    		"background": pyglet.resource.image("images/background.png")
		}
		pyglet.window.Window.__init__(self, width = self.images["background"].width, height = self.images["background"].height)
		#These coordinates have been approved and can be used for any set of characters
		self.background = pyglet.sprite.Sprite(img=self.images["background"], x=0, y = 0)
		self.boat = pyglet.sprite.Sprite(img=self.images["boat"], x=270, y = 218)
		self.sprite_goat = pyglet.sprite.Sprite(img=self.images["goat"], x=0, y = 450)
		self.sprite_wolf = pyglet.sprite.Sprite(img=self.images["wolf"], x=0, y = 450)
		self.sprite_farmer = pyglet.sprite.Sprite(img=self.images["farmer"], x=0, y = 450)
		self.sprite_cabbage = pyglet.sprite.Sprite(img=self.images["cabbage"], x=0, y = 450)

		#These scales are based on original sizes of the source images. Be careful when use different images.
		self.sprite_goat.scale = 0.15
		self.sprite_wolf.scale = 0.15
		self.sprite_farmer.scale = 0.15
		self.sprite_cabbage.scale = 0.15
		self.boat.scale = 0.2

		#These values are based on the current background's size. Be careful when use different background.
		self.river = 660
		self.river_boat_travel_distance = 270
		self.hor_gap = 10
		self.ver_gap = 0
		self.large_bottom_margin = 150
		self.small_bottom_margin = 100
		self.each_height = 130
		self.each_width = 100

		self.global_state = 'left_shore'
		self.last_time = 0
		self.characters_on_board = []

		self.set_destinations_initial()
		pyglet.clock.schedule_interval(self.update, 1/200.0)

	def on_draw(self):
		self.clear()
		self.background.draw()
		self.boat.draw()
		self.sprite_goat.draw()
		self.sprite_farmer.draw()
		self.sprite_cabbage.draw()
		self.sprite_wolf.draw()

	def on_mouse_press(self,x, y, button, modifiers):
		if self.global_state == 'left_shore':
			if self.goat_clicked(x, y):
				self.goat_clicked_actions(x, y)
			elif self.farmer_clicked(x, y):
				self.farmer_clicked_actions(x, y)
			elif self.wolf_clicked(x, y):
				self.wolf_clicked_actions(x, y)
			elif self.cabbage_clicked(x, y):
				self.cabbage_clicked_actions(x, y)
			elif self.boat_clicked(x, y):
				self.boat_try_ride(1, x, y)

		elif self.global_state == 'right_shore':
			if self.boat_clicked(x, y):
				self.boat_try_ride(-1, x, y)

		pass

	def update(self, duration):
		# print(global_state)
		velocity = 300

		# # these states aren't used for now
		# if self.global_state == 'timeout_before_win':
		# 	if self.timeout_ended(1):
		# 		self.global_state = 'game_win'
		# 	return

		# if self.global_state == 'game_win':
		# 	out_from_screen = 300
		# 	self.set_destinations()
		# 	self.destination_goat[0] += self.river + out_from_screen
		# 	self.destination_wolf[0] += self.river + out_from_screen
		# 	self.destination_farmer[0] += self.river + self.hor_gap * 2 + self.each_width * 2 + out_from_screen
		# 	self.destination_cabbage[0] += self.river + self.hor_gap * 2 + self.each_width * 2 + out_from_screen

		self.is_animating_1 = self.animate(self.sprite_goat, self.destination_goat, duration, velocity)
		self.is_animating_2 = self.animate(self.sprite_wolf, self.destination_wolf, duration, velocity)
		self.is_animating_3 = self.animate(self.sprite_farmer, self.destination_farmer, duration, velocity)
		self.is_animating_4 = self.animate(self.sprite_cabbage, self.destination_cabbage, duration, velocity)
		self.is_animating_boat = self.animate(self.boat, self.destination_boat, duration, velocity)

		# # not used for now
		# if self.global_state == 'game_win' and self.check_if_all_stopped(self.is_animating_1, self.is_animating_2, self.is_animating_3, self.is_animating_4):
		# 	self.global_state = 'left_shore'
		# 	self.reset_sprites_positions()


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
		if sprt.x < destination[0] - 5:
			return False
		if sprt.x > destination[0] + 5:
			return False
		if sprt.y < destination[1] - 5:
			return False
		if sprt.y > destination[1] + 5:
			return False
		return True

	def check_if_all_stopped(self, is_animating_1, is_animating_2, is_animating_3, is_animating_4):
		self.still_animating = is_animating_1 or is_animating_2 or is_animating_3 or is_animating_4
		return not self.still_animating

	def timeout_ended(self, timeout_seconds):
		return (time.time() - self.last_time) > timeout_seconds

	def reset_sprites_positions(self):
		off_screen_y = 450
		self.move_sprite_to(self.sprite_goat, 0, off_screen_y)
		self.move_sprite_to(self.sprite_wolf, 0, off_screen_y)
		self.move_sprite_to(self.sprite_farmer, 0, off_screen_y)
		self.move_sprite_to(self.sprite_cabbage, 0, off_screen_y)
		self.move_sprite_to(self.boat, 270, 218)

	def set_destinations_initial(self):
		self.destination_goat = [self.hor_gap + self.each_width, self.large_bottom_margin + self.each_height + self.ver_gap]
		self.destination_wolf = [self.hor_gap + self.each_width, self.large_bottom_margin + self.each_height * 2 + self.ver_gap * 2]
		self.destination_farmer = [self.hor_gap, self.small_bottom_margin + self.each_height * 2 + self.ver_gap * 2]
		self.destination_cabbage = [self.hor_gap, self.small_bottom_margin + self.each_height + self.ver_gap]
		self.destination_boat = [270, 218]

	def set_destinations_to_other_shore(self, direction):
		self.destination_boat[0] += direction * self.river_boat_travel_distance
		if 'goat' in self.characters_on_board:
			self.destination_goat[0] += direction * self.river_boat_travel_distance
		if 'wolf' in self.characters_on_board:
			self.destination_wolf[0] += direction * self.river_boat_travel_distance
		if 'farmer' in self.characters_on_board:
			self.destination_farmer[0] += direction * self.river_boat_travel_distance
		if 'cabbage' in self.characters_on_board:
			self.destination_cabbage[0] += direction * self.river_boat_travel_distance

	def move_sprite_to(self, sprite, x, y):
		sprite.x = x
		sprite.y = y
		return sprite

	def set_goat_destination_to_boat(self, offset_x, offset_y):
		self.destination_goat = [self.destination_boat[0] + offset_x, self.destination_boat[1] + offset_y]

	def set_wolf_destination_to_boat(self, offset_x, offset_y):
		self.destination_wolf = [self.destination_boat[0] + offset_x, self.destination_boat[1] + offset_y]

	def set_farmer_destination_to_boat(self, offset_x, offset_y):
		self.destination_farmer = [self.destination_boat[0] + offset_x, self.destination_boat[1] + offset_y]

	def set_cabbage_destination_to_boat(self, offset_x, offset_y):
		self.destination_cabbage = [self.destination_boat[0] + offset_x, self.destination_boat[1] + offset_y]

	def set_goat_destination_to_shore(self):
		self.destination_goat = [self.hor_gap + self.each_width, self.large_bottom_margin + self.each_height + self.ver_gap]

	def set_wolf_destination_to_shore(self):
		self.destination_wolf = [self.hor_gap + self.each_width, self.large_bottom_margin + self.each_height * 2 + self.ver_gap * 2]

	def set_farmer_destination_to_shore(self):
		self.destination_farmer = [self.hor_gap, self.small_bottom_margin + self.each_height * 2 + self.ver_gap * 2]

	def set_cabbage_destination_to_shore(self):
		self.destination_cabbage = [self.hor_gap, self.small_bottom_margin + self.each_height + self.ver_gap]

	def goat_clicked(self,x, y):
		goat_collider_radius = 40
		return self.sprite_clicked_within_radius(x, y, self.sprite_goat, goat_collider_radius)

	def wolf_clicked(self,x, y):
		wolf_collider_radius = 50
		return self.sprite_clicked_within_radius(x, y, self.sprite_wolf, wolf_collider_radius)

	def cabbage_clicked(self,x, y):
		cabbage_collider_radius = 40
		return self.sprite_clicked_within_radius(x, y, self.sprite_cabbage, cabbage_collider_radius)

	def farmer_clicked(self,x, y):
		farmer_collider_radius = 40
		return self.sprite_clicked_within_radius(x, y, self.sprite_farmer, farmer_collider_radius)

	def boat_clicked(self,x, y):
		boat_collider_radius = 80
		return self.sprite_clicked_within_radius(x, y, self.boat, boat_collider_radius)

	def goat_clicked_actions(self, x, y):
		character_name = 'goat'
		goat_is_in_boat = character_name in self.characters_on_board
		if goat_is_in_boat:
			self.set_goat_destination_to_shore()
			self.characters_on_board.remove(character_name)
		else:
			self.set_goat_destination_to_boat(0, 30)
			self.characters_on_board.append(character_name)
		print("\nGoat was clicked")

	def farmer_clicked_actions(self, x, y):
		character_name = 'farmer'
		farmer_is_in_boat = character_name in self.characters_on_board
		if farmer_is_in_boat:
			self.set_farmer_destination_to_shore()
			self.characters_on_board.remove(character_name)
		else:
			self.set_farmer_destination_to_boat(70, 90)
			self.characters_on_board.append(character_name)
		print("\nFarmer was clicked")

	def wolf_clicked_actions(self, x, y):
		character_name = 'wolf'
		wolf_is_in_boat = character_name in self.characters_on_board
		if wolf_is_in_boat:
			self.set_wolf_destination_to_shore()
			self.characters_on_board.remove(character_name)
		else:
			self.set_wolf_destination_to_boat(-20, 80)
			self.characters_on_board.append(character_name)
		print("\nWolf was clicked")

	def cabbage_clicked_actions(self, x, y):
		character_name = 'cabbage'
		cabbage_is_in_boat = character_name in self.characters_on_board
		if cabbage_is_in_boat:
			self.set_cabbage_destination_to_shore()
			self.characters_on_board.remove(character_name)
		else:
			self.set_cabbage_destination_to_boat(70, 30)
			self.characters_on_board.append(character_name)
		print("\nCabbage was clicked")

	def boat_try_ride(self, direction, x, y):
		print('\nBoat was clicked, trying to ride!')
		if not self.is_allowed_to_ride():
			return
		self.set_destinations_to_other_shore(direction)
		if direction == -1:
			self.global_state = 'left_shore'
		elif direction == 1:
			self.global_state = 'right_shore'


	def is_allowed_to_ride(self):
		number_of_boat_members = self.get_number_of_boat_members()
		boat_has_driver = self.if_boat_has_driver()

		print(str(number_of_boat_members) + " characters on board!")
		print("Is driver present? " + str(boat_has_driver))

		return number_of_boat_members <= 2 and boat_has_driver

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

if __name__ =='__main__':
	window = Animation()
	pyglet.app.run()
