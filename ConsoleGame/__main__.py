#!/usr/bin/env python3
from Move import Move, InvalidMove
from GameState import GameState

state = GameState()
while not state.has_won() and not state.lost():
        print(state.report())
        state.apply_move(Move(input("move object> "), input("move to> ")))