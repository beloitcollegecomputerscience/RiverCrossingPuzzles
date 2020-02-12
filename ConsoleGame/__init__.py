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
        self.left_shore = ["man", "wolf", "goat", "hay"]
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
            if move.object not in ["boat", "shore"]:
                raise InvalidMove("Can't move subjects anywhere but onto boat or shore.")
            if move.object == "boat":
                if len(self.boat) ==2:
                    raise InvalidMove("Boat is full.")
                try:
                    if self.boat_position == "left":
                        self.left_shore.remove(move.subject)
                    elif self.boat_position == "right":
                        self.right_shore.remove(move.subject)
                except ValueError as e:
                    raise InvalidMove("Subject is not on the same shore as the boat or is already on boat.")
                self.boat += [move.subject]
            elif move.object == "shore":
                if move.subject not in self.boat:
                    raise InvalidMove("Subject is on the shore.")
                self.boat.remove(move.subject)
                if self.boat_position == "left":
                    self.left_shore += [move.subject]
                elif self.boat_position == "right":
                    self.right_shore += [move.subject]
            if self.right_shore == ["man","wolf", "goat", "hay"]:
                print("GAME OVER!! YOU WON!!!")
state = GameState()
while state.right_shore != ["man","wolf", "goat", "hay"]:
    print(state.report())
    state.apply_move(Move(input("move object> "), input("move to> ")))