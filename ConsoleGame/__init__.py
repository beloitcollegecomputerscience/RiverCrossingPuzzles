#!/usr/bin/env python3

# How to play:
# When prompted, type an object name to move and press enter. 
# Next type the location to move to and press enter again.
# Objects: man, wolf, goat, hay, boat
# Locations to move characters: boat, shore
# Locations to move boat: left, right

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
    def __init__(self, obj, location):
        self.object = obj
        self.location = location

class GameState:
    def __init__(self):
        self.left_shore = ["man", "wolf", "goat", "hay"]
        self.right_shore = []
        self.boat_position = "left"
        self.boat = []
        self.boat_capacity = 2

    def report(self):
        s = ""
        s += report_shore("left shore", self.left_shore) + "\n"
        s += report_shore("right shore", self.right_shore) + "\n"
        s += report_shore("boat", self.boat) + "\n"
        s += "The boat is on the " + self.boat_position + " shore."
        return s

    def apply_move(self, move):
        if move.object not in self.boat + self.left_shore + self.right_shore + ["boat"]:
            raise InvalidMove("Unknown command object '" + move.object + "'.")
        if move.object == "boat":
            if move.location not in ["left", "right"]:
                raise InvalidMove("Can't move boat anywhere but left or right.")
            self.boat_position = move.location
        else:
            if move.location not in ["boat", "shore"]:
                raise InvalidMove("Can't move objects anywhere but onto boat or shore.")
            if move.location == "boat":
                if len(self.boat) >= self.boat_capacity:
                    raise InvalidMove("Boat is full.")
                try:
                    if self.boat_position == "left":
                        self.left_shore.remove(move.object)
                    elif self.boat_position == "right":
                        self.right_shore.remove(move.object)
                except ValueError as e:
                    raise InvalidMove("Object is not on the same shore as the boat or is already on boat.")
                self.boat += [move.object]
            elif move.location == "shore":
                if move.object not in self.boat:
                    raise InvalidMove("Object is on the shore.")
                self.boat.remove(move.object)
                if self.boat_position == "left":
                    self.left_shore += [move.object]
                elif self.boat_position == "right":
                    self.right_shore += [move.object]
            if self.right_shore.__contains__("man") \
                and self.right_shore.__contains__("wolf") \
                and self.right_shore.__contains__("goat") \
                and self.right_shore.__contains__("hay"):
                    print("GAME OVER!! YOU WON!!!")

state = GameState()
while not (state.right_shore.__contains__("man") \
    and state.right_shore.__contains__("wolf") \
    and state.right_shore.__contains__("goat") \
    and state.right_shore.__contains__("hay")):
        print(state.report())
        state.apply_move(Move(input("move object> "), input("move to> ")))