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
		self.boat = pyglet.sprite.Sprite(img=self.images["boat"], x=230, y = 150)
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
		self.hor_gap = 10
		self.ver_gap = 0
		self.large_bottom_margin = 150
		self.small_bottom_margin = 100
		self.each_height = 130
		self.each_width = 100

		self.global_state = 'initialized'
		self.last_time = 0

		pyglet.clock.schedule_interval(self.update, 1/200.0)

	def on_draw(self):
		self.clear()
		self.background.draw()
		self.boat.draw()
		self.sprite_goat.draw()
		self.sprite_wolf.draw()
		self.sprite_farmer.draw()
		self.sprite_cabbage.draw()

	def on_mouse_press(self,x, y, button, modifiers):
		if self.global_state == 'initialized':
			self.global_state = 'clicked'

		if self.goat_clicked(x, y):
			print("Goat was clicked")
		pass

	def update(self, duration):
		velocity = 300

		if self.global_state != 'timeout_before_win':
			self.destination_goat = [self.hor_gap + self.each_width, self.large_bottom_margin + self.each_height + self.ver_gap]
			self.destination_wolf = [self.hor_gap + self.each_width, self.large_bottom_margin + self.each_height * 2 + self.ver_gap * 2]
			self.destination_farmer = [self.hor_gap, self.small_bottom_margin + self.each_height * 2 + self.ver_gap * 2]
			self.destination_cabbage = [self.hor_gap, self.small_bottom_margin + self.each_height + self.ver_gap]
			self.destination_boat = [500, 150]

		# Positions of characters and boat on the right side of the river
		if self.global_state == 'clicked':
			self.destination_goat[0] += self.river
			self.destination_wolf[0] += self.river
			self.destination_farmer[0] += self.river + self.hor_gap * 2 + self.each_width * 2
			self.destination_cabbage[0] += self.river + self.hor_gap * 2 + self.each_width * 2
			self.animate(self.boat, self.destination_boat, duration, velocity)

		if self.global_state == 'timeout_before_win':
			if self.timeout_ended(1):
				self.global_state = 'game_win'
			return

		if self.global_state == 'game_win':
			out_from_screen = 300
			self.destination_goat[0] += self.river + out_from_screen
			self.destination_wolf[0] += self.river + out_from_screen
			self.destination_farmer[0] += self.river + self.hor_gap * 2 + self.each_width * 2 + out_from_screen
			self.destination_cabbage[0] += self.river + self.hor_gap * 2 + self.each_width * 2 + out_from_screen

		self.is_animating_1 = self.animate(self.sprite_goat, self.destination_goat, duration, velocity)
		self.is_animating_2 = self.animate(self.sprite_wolf, self.destination_wolf, duration, velocity)
		self.is_animating_3 = self.animate(self.sprite_farmer, self.destination_farmer, duration, velocity)
		self.is_animating_4 = self.animate(self.sprite_cabbage, self.destination_cabbage, duration, velocity)
		# print(is_animating_1)
		if self.global_state == 'clicked' and self.check_if_all_stopped(self.is_animating_1, self.is_animating_2, self.is_animating_3, self.is_animating_4):
			self.global_state = 'timeout_before_win'
			self.last_time = time.time()

		if self.global_state == 'game_win' and self.check_if_all_stopped(self.is_animating_1, self.is_animating_2, self.is_animating_3, self.is_animating_4):
			self.global_state = 'initialized'
			self.reset_sprites_positions()

		# print(global_state)

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
		if sprt.x < destination[0] - 3:
			return False
		if sprt.x > destination[0] + 3:
			return False
		if sprt.y < destination[1] - 3:
			return False
		if sprt.y > destination[1] + 3:
			return False
		return True

	def check_if_all_stopped(self, is_animating_1, is_animating_2, is_animating_3, is_animating_4):
		self.still_animating = is_animating_1 or is_animating_2 or is_animating_3 or is_animating_4
		return not self.still_animating

	def timeout_ended(self,timeout_seconds):
		return (time.time() - self.last_time) > timeout_seconds

	def reset_sprites_positions(self):
		off_screen_y = 450
		self.move_sprite_to(self.sprite_goat, 0, off_screen_y)
		self.move_sprite_to(self.sprite_wolf, 0, off_screen_y)
		self.move_sprite_to(self.sprite_farmer, 0, off_screen_y)
		self.move_sprite_to(self.sprite_cabbage, 0, off_screen_y)
		self.move_sprite_to(self.boat, 230, 150)

	def move_sprite_to(self,sprite, x, y):
		sprite.x = x
		sprite.y = y
		return sprite

	def goat_clicked(self,x, y):
		goat_collider_radius = 40
		goat_center_x = self.sprite_goat.x + goat_collider_radius
		goat_center_y = self.sprite_goat.y + goat_collider_radius
	
		if (abs(x - goat_center_x) < goat_collider_radius) and (abs(y - goat_center_y) < goat_collider_radius):
			return True
		return False

def check_if_all_stopped(is_animating_1, is_animating_2, is_animating_3, is_animating_4):
	still_animating = is_animating_1 or is_animating_2 or is_animating_3 or is_animating_4
	return not still_animating

def timeout_ended(timeout_seconds):
	return (time.time() - last_time) > timeout_seconds

def reset_sprites_positions():
	off_screen_y = 450
	move_sprite_to(sprite_goat, 0, off_screen_y)
	move_sprite_to(sprite_wolf, 0, off_screen_y)
	move_sprite_to(sprite_farmer, 0, off_screen_y)
	move_sprite_to(sprite_cabbage, 0, off_screen_y)
	move_sprite_to(boat, 230, 150)

def move_sprite_to(sprite, x, y):
	sprite.x = x
	sprite.y = y
	return sprite

def goat_clicked(x, y):
	goat_collider_radius = 40
	goat_center_x = sprite_goat.x + goat_collider_radius
	goat_center_y = sprite_goat.y + goat_collider_radius
	
	if (abs(x - goat_center_x) < goat_collider_radius) and (abs(y - goat_center_y) < goat_collider_radius):
		return True
	return False


if __name__ =='__main__':
	window = Animation()
	pyglet.app.run()
