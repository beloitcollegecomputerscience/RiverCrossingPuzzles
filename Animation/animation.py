import pyglet
import time
from pyglet.window import mouse

img_goat = pyglet.resource.image("images/goat.png")
img_wolf = pyglet.resource.image("images/wolf.png")
img_farmer = pyglet.resource.image("images/farmer.png")
img_cabbage = pyglet.resource.image("images/cabbage.png")
img_background = pyglet.resource.image("images/background.png")
img_boat = pyglet.resource.image("images/boat.png")

background = pyglet.sprite.Sprite(img=img_background, x=0, y = 0)
boat = pyglet.sprite.Sprite(img=img_boat, x=230, y = 150)
sprite_goat = pyglet.sprite.Sprite(img=img_goat, x=0, y = 450)
sprite_wolf = pyglet.sprite.Sprite(img=img_wolf, x=0, y = 450)
sprite_farmer = pyglet.sprite.Sprite(img=img_farmer, x=0, y = 450)
sprite_cabbage = pyglet.sprite.Sprite(img=img_cabbage, x=0, y = 450)

sprite_goat.scale = 0.15
sprite_wolf.scale = 0.15
sprite_farmer.scale = 0.15
sprite_cabbage.scale = 0.15
boat.scale = 0.2

river = 660
hor_gap = 10
ver_gap = 0
large_bottom_margin = 150
small_bottom_margin = 100
each_height = 130
each_width = 100
global_state = 'initialized'

last_time = 0

window = pyglet.window.Window(img_background.width, img_background.height)
@window.event
def on_draw():
	window.clear()
	background.draw()
	boat.draw()
	sprite_goat.draw()
	sprite_wolf.draw()
	sprite_farmer.draw()
	sprite_cabbage.draw()
@window.event
def on_mouse_press(x, y, button, modifiers):
	global global_state 
	if global_state == 'initialized':
		global_state = 'clicked'

	if goat_clicked(x, y):
		print("Goat was clicked")
	pass

def update(duration):
	global global_state
	global last_time
	velocity = 300

	if global_state != 'timeout_before_win':
		destination_3_x = hor_gap
		destination_4_x = hor_gap
		destination_2_x = hor_gap + each_width
		destination_1_x = hor_gap + each_width

		destination_1_y = large_bottom_margin + each_height + ver_gap
		destination_4_y = small_bottom_margin + each_height + ver_gap
		destination_2_y= large_bottom_margin + each_height * 2 + ver_gap * 2
		destination_3_y = small_bottom_margin + each_height * 2 + ver_gap * 2
		destination_boat_x = 500

	if global_state == 'clicked':
		destination_1_x += river
		destination_2_x += river
		destination_3_x += river + hor_gap * 2 + each_width * 2
		destination_4_x += river + hor_gap * 2 + each_width * 2
		animate(boat, destination_boat_x, boat.y, duration, velocity)

	if global_state == 'timeout_before_win':
		if timeout_ended(1):
			global_state = 'game_win'
		return

	if global_state == 'game_win':
		out_from_screen = 300
		destination_1_x += river + out_from_screen
		destination_2_x += river + out_from_screen
		destination_3_x += river + hor_gap * 2 + each_width * 2 + out_from_screen
		destination_4_x += river + hor_gap * 2 + each_width * 2 + out_from_screen


	is_animating_1 = animate(sprite_goat, destination_1_x, destination_1_y, duration, velocity)
	is_animating_2 = animate(sprite_wolf, destination_2_x, destination_2_y, duration, velocity)
	is_animating_3 = animate(sprite_farmer, destination_3_x, destination_3_y, duration, velocity)
	is_animating_4 = animate(sprite_cabbage, destination_4_x, destination_4_y, duration, velocity)
	# print(is_animating_1)
	if global_state == 'clicked' and check_if_all_stopped(is_animating_1, is_animating_2, is_animating_3, is_animating_4):
		global_state = 'timeout_before_win'
		last_time = time.time()

	if global_state == 'game_win' and check_if_all_stopped(is_animating_1, is_animating_2, is_animating_3, is_animating_4):
		global_state = 'initialized'
		reset_sprites_positions()
		

	# print(global_state)

def animate(sprt, destination_x, destination_y, duration, velocity):
	if check_if_sprite_at_destination(sprt, destination_x, destination_y):
		return False

	if sprt.x < destination_x - 1:
		sprt.x += velocity * duration
	if sprt.x > destination_x + 1:
		sprt.x -= velocity * duration
	if sprt.y < destination_y - 1:
		sprt.y += velocity * duration
	if sprt.y > destination_y + 1:
		sprt.y -= velocity * duration

	return True	

def check_if_sprite_at_destination(sprt, destination_x, destination_y):
	if sprt.x < destination_x - 3:
		return False
	if sprt.x > destination_x + 3:
		return False
	if sprt.y < destination_y - 3:
		return False
	if sprt.y > destination_y + 3:
		return False
	return True

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
	pyglet.clock.schedule_interval(update, 1/200.0)
	pyglet.app.run()
