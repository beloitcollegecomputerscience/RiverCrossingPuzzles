import pyglet
import time
from pyglet.window import mouse

images = {
    "wolf": pyglet.resource.image("images/wolf.png"),
    "goat": pyglet.resource.image("images/goat.png"),
    "farmer": pyglet.resource.image("images/farmer.png"),
    "cabbage": pyglet.resource.image("images/cabbage.png"),
    "boat": pyglet.resource.image("images/boat.png"),
    "background": pyglet.resource.image("images/background.png")
}

#These coordinates have been approved and can be used for any set of characters
background = pyglet.sprite.Sprite(img=images["background"], x=0, y = 0)
boat = pyglet.sprite.Sprite(img=images["boat"], x=230, y = 150)
sprite_goat = pyglet.sprite.Sprite(img=images["goat"], x=0, y = 450)
sprite_wolf = pyglet.sprite.Sprite(img=images["wolf"], x=0, y = 450)
sprite_farmer = pyglet.sprite.Sprite(img=images["farmer"], x=0, y = 450)
sprite_cabbage = pyglet.sprite.Sprite(img=images["cabbage"], x=0, y = 450)

#These scales are based on original sizes of the source images. Be careful when use different images.
sprite_goat.scale = 0.15
sprite_wolf.scale = 0.15
sprite_farmer.scale = 0.15
sprite_cabbage.scale = 0.15
boat.scale = 0.2

#These values are true with any version of the game that has less than 6 characters and no island
river = 660
hor_gap = 10
ver_gap = 0
large_bottom_margin = 150
small_bottom_margin = 100
each_height = 130
each_width = 100

global_state = 'initialized'
last_time = 0

window = pyglet.window.Window(images["background"].width, images["background"].height)
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
		destination_goat = [hor_gap + each_width, large_bottom_margin + each_height + ver_gap]
		destination_wolf = [hor_gap + each_width, large_bottom_margin + each_height * 2 + ver_gap * 2]
		destination_farmer = [hor_gap, small_bottom_margin + each_height * 2 + ver_gap * 2]
		destination_cabbage = [hor_gap, small_bottom_margin + each_height + ver_gap]
		destination_boat = [500, 150]

	if global_state == 'clicked':
		destination_goat[0] += river
		destination_wolf[0] += river
		destination_farmer[0] += river + hor_gap * 2 + each_width * 2
		destination_cabbage[0] += river + hor_gap * 2 + each_width * 2
		animate(boat, destination_boat, duration, velocity)

	if global_state == 'timeout_before_win':
		if timeout_ended(1):
			global_state = 'game_win'
		return

	if global_state == 'game_win':
		out_from_screen = 300
		destination_goat[0] += river + out_from_screen
		destination_wolf[0] += river + out_from_screen
		destination_farmer[0] += river + hor_gap * 2 + each_width * 2 + out_from_screen
		destination_cabbage[0] += river + hor_gap * 2 + each_width * 2 + out_from_screen

	is_animating_1 = animate(sprite_goat, destination_goat, duration, velocity)
	is_animating_2 = animate(sprite_wolf, destination_wolf, duration, velocity)
	is_animating_3 = animate(sprite_farmer, destination_farmer, duration, velocity)
	is_animating_4 = animate(sprite_cabbage, destination_cabbage, duration, velocity)
	# print(is_animating_1)
	if global_state == 'clicked' and check_if_all_stopped(is_animating_1, is_animating_2, is_animating_3, is_animating_4):
		global_state = 'timeout_before_win'
		last_time = time.time()

	if global_state == 'game_win' and check_if_all_stopped(is_animating_1, is_animating_2, is_animating_3, is_animating_4):
		global_state = 'initialized'
		reset_sprites_positions()

	# print(global_state)

def animate(sprt, destination, duration, velocity):
	if check_if_sprite_at_destination(sprt, destination):
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

def check_if_sprite_at_destination(sprt, destination):
	if sprt.x < destination[0] - 3:
		return False
	if sprt.x > destination[0] + 3:
		return False
	if sprt.y < destination[1] - 3:
		return False
	if sprt.y > destination[1] + 3:
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
