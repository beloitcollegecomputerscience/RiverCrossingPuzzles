import pyglet
import math
import time

class Button:

    def __init__(self, width, height, name, initial_scale, audio_player):
        self.width = width
        self.height = height
        self.name = name
        self.initial_scale = initial_scale
        self.audio_player = audio_player
        self.image_file = name + ".png"
        self.image = None
        self.sprite = None
        self.sound = None

        self.on_click = None
        self.is_hovered = False

        pyglet.clock.schedule_interval(self.update, 1 / 200.0)


    def is_cursor_on_button(self, x, y):
        sprite_x_start = self.sprite.x - self.sprite.width / 2 
        sprite_y_start = self.sprite.y - self.sprite.height / 2 

        overlap_by_x = (x >= sprite_x_start) and (x <= sprite_x_start + self.width)
        overlap_by_y = (y >= sprite_y_start) and (y <= sprite_y_start + self.height)
        if overlap_by_x and overlap_by_y:
            return True
        return False


    def set_hover(self):
        self.is_hovered = True

    def unset_hover(self):
        self.is_hovered = False


    def update(self, duration):
        if self.is_hovered:
            if self.sprite.scale < self.initial_scale * 1.1:
                self.sprite.scale *= 1.01
        else:
            if self.sprite.scale > self.initial_scale:
                self.sprite.scale /= 1.01
