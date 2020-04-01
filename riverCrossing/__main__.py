#!/usr/bin/env python3
import pyglet

from .Move import Move, InvalidMove
from .GameState import GameState
from .animation import Animation
from .TextInterface import TextInterface
import sys

game_to_play = "console"
if len(sys.argv) > 1:
    game_to_play = sys.argv[1]

if game_to_play == "console":
    interface = TextInterface()
    interface.intro()
    while not interface.finished():
        interface.pump()
    interface.outro()
elif game_to_play == "gui":
    window = Animation()
    pyglet.app.run()


