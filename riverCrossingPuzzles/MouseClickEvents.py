import pyglet
from pyglet.window import mouse

#Getting image from the directory
image = pyglet.resource.image('Boy.png')

sprite = pyglet.sprite.Sprite(image, x=100, y=150)

#In order for layer to receive director,window events, we are setting it to true
is_event_handler = True

# setting dimensions for the window terminal
window_width = 1080
window_height = 800
window = pyglet.window.Window(window_width, window_height)


@window.event
def on_draw():
    window.clear()
    sprite.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button & mouse.LEFT:
        if sprite.x + sprite.width > x > sprite.x and sprite.y + sprite.height > y > sprite.y:
            print("Go Away!")


pyglet.app.run()
