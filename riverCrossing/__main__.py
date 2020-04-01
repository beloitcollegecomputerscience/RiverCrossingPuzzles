#!/usr/bin/env python3
import pyglet
from .Move import Move
from .GameState import GameState
from .SceneState import SceneState
from .Animation import Animation
from .Boat import Boat
from .GUI import GUI
from .Rules import Rules
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
    # Play the "farmer, goat, wolf, and hay" variation of the game
    rules = Rules("rules.json").rules
    scene_state = SceneState(rules)
    animation = Animation(scene_state)
    animation.boat = Boat(rules["boat_capacity"], rules["driver_name"],
                          scene_state.get_object_by_name("boat")["radius"], animation, scene_state)
    window = GUI(animation)

    pyglet.app.run()
