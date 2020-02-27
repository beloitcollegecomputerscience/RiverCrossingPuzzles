#!/usr/bin/env python3
def report_shore(name, items):
    s = ""
    s += "On the " + name + ", there is "
    if len(items) == 0:
        s += "nothing."
    elif len(items) == 1:
        s += "a " + items[-1] + "."
    else:
        for i in range(0, len(items) - 1):
            s += "a " + items[i] + ", "
        s += "and a " + items[-1] + "."
    return s

class InvalidMove(Exception):
    pass

class Move:
    def __init__(self, subject, obj):
        self.subject = subject
        self.object = obj

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
        s += "The boat is on the " + self.boat_position + " shore."
        return s

    def apply_move(self, move):
        if move.subject not in self.boat + self.left_shore + self.right_shore + ["boat"]:
            raise InvalidMove("Unknown command subject '" + move.subject + "'.")
        if move.subject == "boat":
            if move.object not in ["left", "right"]:
                raise InvalidMove("Can't move boat anywhere but left or right.")
            self.boat_position = move.object
        else:
            if move.object == "onto boat":
                try:
                    if self.boat_position == "left":
                        self.left_shore.remove(move.subject)
                    elif self.boat_position == "right":
                        self.right_shore.remove(move.subject)
                except ValueError as e:
                    raise InvalidMove("Subject was not on the same shore as the boat.")
                self.boat += [move.subject]
            elif move.object == "off of boat":
                self.boat.remove(move.subject)
                if self.boat_position == "left":
                    self.left_shore += [move.subject]
                if self.boat_position == "right":
                    self.right_shore += [move.subject]
            else:
                raise InvalidMove("Can't move items anywhere but onto or off of boat.")

state = GameState()
while True:
    print(state.report())
    state.apply_move(Move(input("subject> "), input("object> ")))

