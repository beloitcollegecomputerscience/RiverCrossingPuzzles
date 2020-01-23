#run 'pip install pynput'
#https://nitratine.net/blog/post/how-to-get-mouse-clicks-with-python/
#Mouse events are printed on the 'mouselog.txt' file that is created in the same directory.

import pynput
from pynput.mouse import Listener
import logging

logging.basicConfig(filename="mouselog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_move(x,y):
    logging.info("X:{0} , Y:{1}".format(x,y))
    
def on_click(x,y,button,pressed):
    if not pressed:
        return
    if x==0 and y==0:
        listener.stop()
    else:
        logging.info("Clicked on: x:{0},y:{1}".format(x,y))
        return

def on_scroll(x,y,dx,dy):
    logging.info("Scroll :: X:{0} , Y:{1}".format(x,y))

with Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listener:
    listener.join()

print("Listener Stopped")