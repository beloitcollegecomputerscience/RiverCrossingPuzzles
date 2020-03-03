#!/usr/bin/env python3
import pyglet

from .Move import Move, InvalidMove
from .GameState import GameState
from .animation import Animation
import sys

game_to_play = "console"
if len(sys.argv) > 1:
    game_to_play = sys.argv[1]

if game_to_play == "console":
    state = GameState()
    while not state.has_won():
            print(state.report())
            state.apply_move(Move(input("move object> "), input("move to> ")))
elif game_to_play == "gui":
    window = Animation()
    pyglet.app.run()


