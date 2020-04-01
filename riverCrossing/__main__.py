#!/usr/bin/env python3
import pyglet

from .Move import Move, InvalidMove
from .GameState import GameState
from .animation import Animation
from .TextInterface import TextInterface
import sys

interface_type = "console"
game_to_play = ""

if len(sys.argv) < 2:
    print("Please provide the interface you'd like to use, and optionally the game you'd like to play.")
    exit(1)
else:
    interface_type = sys.argv[1]
    if len(sys.argv) > 2:
        game_to_play = sys.argv[2]

if interface_type == "console":
    interface = TextInterface()
    interface.intro()
    while not interface.finished():
        interface.pump()
    interface.outro()
elif interface_type == "gui":
    window = Animation()
    pyglet.app.run()


