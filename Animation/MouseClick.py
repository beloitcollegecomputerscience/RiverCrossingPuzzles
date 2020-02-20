import pyglet
from pyglet.window import mouse

#Getting image from the directory
farmerimage = pyglet.resource.image("images/farmer.png")
hayimage = pyglet.resource.image("images/cabbage.png")
boatimage = pyglet.resource.image("images/boat.png")
goatimage = pyglet.resource.image("images/goat.png")
wolfimage = pyglet.resource.image("images/wolf.png")

farmer = pyglet.sprite.Sprite(farmerimage, x=100, y=150)
hay = pyglet.sprite.Sprite(hayimage, x=250, y=150)
boat = pyglet.sprite.Sprite(boatimage, x=350, y=50)
goat = pyglet.sprite.Sprite(goatimage, x=150 , y=400)
wolf = pyglet.sprite.Sprite(wolfimage, x=400, y=400)


farmer.scale=0.15
hay.scale=0.15
boat.scale=0.15
goat.scale=0.15
wolf.scale=0.15
#In order for layer to receive director,window events, we are setting it to true
is_event_handler = True

# setting dimensions for the window terminal
window_width = 1080
window_height = 800
window = pyglet.window.Window(window_width, window_height)

@window.event
def on_draw():
    window.clear()
    farmer.draw()
    hay.draw()
    boat.draw()
    goat.draw()
    wolf.draw()

def checkClicked(sprite,name,button,mouse,x,y):
    if button & mouse.LEFT:
        if sprite.x + sprite.width > x > sprite.x and sprite.y + sprite.height > y > sprite.y:
            return name

#Mouse Click Event
@window.event
def on_mouse_press(x, y, button, modifiers):
    print(checkClicked(farmer,"farmer",button,mouse,x,y))

pyglet.app.run()