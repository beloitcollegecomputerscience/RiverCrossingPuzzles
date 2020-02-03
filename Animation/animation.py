import pyglet
import time
from pyglet.window import mouse

img_1 = pyglet.resource.image("images/goat.png")
img_2 = pyglet.resource.image("images/wolf.png")
img_3 = pyglet.resource.image("images/farmer.png")
img_4 = pyglet.resource.image("images/cabbage.png")
img_background = pyglet.resource.image("images/background.png")
img_boat = pyglet.resource.image("images/boat.png")

background = pyglet.sprite.Sprite(img=img_background, x=0, y = 0)
boat = pyglet.sprite.Sprite(img=img_boat, x=230, y = 150)
sprite_1 = pyglet.sprite.Sprite(img=img_1, x=0, y = 450)
sprite_2 = pyglet.sprite.Sprite(img=img_2, x=0, y = 450)
sprite_3 = pyglet.sprite.Sprite(img=img_3, x=0, y = 450)
sprite_4 = pyglet.sprite.Sprite(img=img_4, x=0, y = 450)

sprite_1.scale = 0.15
sprite_2.scale = 0.15
sprite_3.scale = 0.15
sprite_4.scale = 0.15
boat.scale = 0.2

river = 660
hor_gap = 10
ver_gap = 0
large_bottom_margin = 150
small_bottom_margin = 100
each_height = 130
each_width = 100
clicked = False
window = pyglet.window.Window(img_background.width, img_background.height)
@window.event
def on_draw():
	window.clear()
	background.draw()
	boat.draw()
	sprite_1.draw()
	sprite_2.draw()
	sprite_3.draw()
	sprite_4.draw()
@window.event
def on_mouse_press(x, y, button, modifiers):
	global clicked 
	clicked = True
	pass

def update(duration):
	global clicked
	velocity = 300

	destination_3_x = hor_gap
	destination_4_x = hor_gap
	destination_2_x = hor_gap + each_width
	destination_1_x = hor_gap + each_width

	destination_1_y = large_bottom_margin + each_height + ver_gap
	destination_4_y = small_bottom_margin + each_height + ver_gap
	destination_2_y= large_bottom_margin + each_height * 2 + ver_gap * 2
	destination_3_y = small_bottom_margin + each_height * 2 + ver_gap * 2
	destination_boat_x = 500

	if clicked == True:
		destination_1_x += river
		destination_2_x += river
		destination_3_x += river + hor_gap * 2 + each_width * 2
		destination_4_x += river + hor_gap * 2 + each_width * 2
		animate(boat, destination_boat_x, boat.y, duration, velocity)

	animate(sprite_1, destination_1_x, destination_1_y, duration, velocity)
	animate(sprite_2, destination_2_x, destination_2_y, duration, velocity)
	animate(sprite_3, destination_3_x, destination_3_y, duration, velocity)
	animate(sprite_4, destination_4_x, destination_4_y, duration, velocity)

def animate(sprt, destination_x, destination_y, duration, velocity):
	if sprt.x < destination_x - 1:
		sprt.x += velocity * duration
	if sprt.x > destination_x + 1:
		sprt.x -= velocity * duration
	if sprt.y < destination_y - 1:
		sprt.y += velocity * duration
	if sprt.y > destination_y + 1:
		sprt.y -= velocity * duration

def check(sprt, destination_x, destination_y):
	if sprt.x < destination_x - 3:
		return False
	if sprt.x > destination_x + 3:
		return False
	if sprt.y < destination_y - 3:
		return False
	if sprt.y > destination_y + 3:
		return False
	return True

if __name__ =='__main__':
	pyglet.clock.schedule_interval(update, 1/200.0)
	pyglet.app.run()
