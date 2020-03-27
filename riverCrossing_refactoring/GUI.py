import pyglet
import time
from pyglet.window import mouse
import math
import sys
import pprint

class GUI(pyglet.window.Window):
	"""
	This class creates a general layout that can be applied to all versions of the game 
	with less than 6 characters and no island. Modify images to set up new games.
	"""
	def __init__(self):
		

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