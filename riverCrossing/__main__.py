#!/usr/bin/env python3
import pyglet
from .Move import Move
from .GameState import GameState
from .SceneState import SceneState
from .Animation import Animation
from .Boat import Boat
from .GUI import GUI
from .Rules import Rules
from .MainMenu import MainMenu
from .AudioPlayer import AudioPlayer
import sys


game_to_play = "console"

if len(sys.argv) > 1:
    game_to_play = sys.argv[1]

if game_to_play == "console":
    state = GameState()
    while not state.has_won() and not state.lost():
            print(state.report())
            state.apply_move(Move(input("move object> "), input("move to> ")))
elif game_to_play == "gui":
    audio_player = AudioPlayer()
    scene_state = SceneState(audio_player)
    menu = MainMenu(scene_state)
    window = GUI(scene_state, audio_player, menu)
    pyglet.app.run()
