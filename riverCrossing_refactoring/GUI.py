import pyglet
import time
from pyglet.window import mouse
import math
import sys
import pprint
import animation

class GUI(pyglet.window.Window):

	def __init__(self, animation, boat, gameState):

		self.animation = animation
		self.boat = boat
		self.gameState = gameState

		self.scene_objects = self.Animation.get_scene_objects()
		background_image = self.animation.get_object_by_name("background")["image"]
		pyglet.window.Window.__init__(self, width = background_image.width, height = background_image.height)

	def on_draw(self):
		animation.main_batch.draw()

	def on_mouse_press(self, x, y, button, modifiers):
		if self.gameState.global_state == 'left_shore':
			clicked_character = self.animation.get_clicked_character(x, y)
			if clicked_character != None:
				self.animation.process_clicked_character(x, y, clicked_character)
			elif animation.boat_clicked(x, y):
				self.boat.boat_try_ride(1, x, y)

		elif gameState.global_state == 'right_shore':
			clicked_character = self.animation.get_clicked_character(x, y)
			if clicked_character != None:
				self.animation.process_clicked_character(x, y, clicked_character)
			elif self.boat_clicked(x, y):
				self.boat.boat_try_ride(-1, x, y)