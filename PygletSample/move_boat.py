import pyglet

boat_img = pyglet.resource.image("boat.png")
pikachu_img = pyglet.resource.image("pikachu.png")
boat = pyglet.sprite.Sprite(img=boat_img, x=0, y = 100)
pikachu = pyglet.sprite.Sprite(img=pikachu_img, x=100, y = 300)
pikachu.scale = 0.1
boat.scale = 0.2

window = pyglet.window.Window(1400,600)
@window.event
def on_draw():
	window.clear()
	boat.draw()
	pikachu.draw()
def update(duration):
	velocity = 300
	if boat.x < 1000:
		boat.x += velocity * duration
		pikachu.x += velocity * duration
	else:
		boat.x = 0
		pikachu.x = 50
if __name__ == '__main__':
	pyglet.clock.schedule_interval(update, 1/50.0)
	pyglet.app.run()
