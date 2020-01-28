#!/usr/bin/env python3
def report_shore(name, items):
    s = ""
    s += "On the " + name + ", there is "
    if len(items) == 0:
        s += "nothing."
    else:
        for i in range(0, len(items) - 1):
            s += "a " + items[i] + ", "
        s += "and a " + items[-1] + "."
    return s

class GameState:
    def __init__(self):
        self.left_shore = ["wolf", "goat", "hay"]
        self.right_shore = []
        self.boat_position = "left"
        self.boat = []


    def report(self):
        s = ""
        s += report_shore("left shore", self.left_shore) + "\n"
        s += report_shore("right shore", self.right_shore) + "\n"
        s += report_shore("boat", self.boat) + "\n"
        return s

state = GameState()
print(state.report())

