# from PIL import Image
import ctypes
import PIL.Image
from graphics import *

# Query DPI Awareness (Windows 10 and 8)
# This is required so that the image in the window is not zoomed in/out based on desktop scale %
awareness = ctypes.c_int()
errorCode = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
# print(awareness.value)

# Set DPI Awareness  (Windows 10 and 8)
errorCodeWindows = ctypes.windll.shcore.SetProcessDpiAwareness(2)

# Set DPI Awareness  (Windows 7 and Vista)
success = ctypes.windll.user32.SetProcessDPIAware()

image = PIL.Image.open('background.png')

man = PIL.Image.open('man.png')
new_man = man.resize((132, 200))

hay = PIL.Image.open('hay.png')
new_hay = hay.resize((100, 100))

wolf = PIL.Image.open('wolf.png')
new_wolf = wolf.resize((209, 140))

image_copy = image.copy()
position_man = (100, 100)
position_hay = (200, 230)
position_wolf = (300, 280)

image_copy.paste(new_man, position_man, new_man)
image_copy.paste(new_hay, position_hay, new_hay)
image_copy.paste(new_wolf, position_wolf, new_wolf)

image_copy.save('pasted_image.png')

# image_copy.show()

img_height = 850
img_width = 1920
win = GraphWin("My Window", img_width, img_height)
img = Image(Point(img_width/2, img_height/2), "pasted_image.png")
img.draw(win)
# Keep the window open even if we click on it
win.mainloop()
# Windows closes when clicked
# win.getMouse()
# win.close()
