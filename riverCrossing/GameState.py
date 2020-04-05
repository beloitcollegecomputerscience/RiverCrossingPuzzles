from .Move import InvalidMove

class GameState:
    def __init__(self, leftShore = ["man", "wolf", "goat", "hay"], boatShore = [], rightShore = []):
        self.left_shore = leftShore
        self.right_shore = rightShore
        self.boat_position = "left"
        self.boat = boatShore
        self.boat_capacity = 2
        self.lose=False
        self.violationCombination={"wolf":"goat","goat":"hay"}

    def report(self):
        s = ""
        s += report_shore("left shore", self.left_shore) + "\n"
        s += report_shore("right shore", self.right_shore) + "\n"
        s += report_shore("boat", self.boat) + "\n"
        s += "The boat is on the " + self.boat_position + " shore."
        return s

    def checkIfObjectsClash(self,location):
        if 'man' not in location:
            for object1 in self.violationCombination:
                object2=self.violationCombination[object1]
                if(object1 in location and object2 in location):
                    print('%s ate the %s'%(object1,object2))
                    print('You lost :(')
                    self.lose=True
                    return True

    def apply_move(self, move):
        if move.object not in self.boat + self.left_shore + self.right_shore + ["boat"]:
            raise InvalidMove("Unknown command object '" + move.object + "'.")
        if move.object == "boat":
            if move.location not in ["left", "right"]:
                raise InvalidMove("Can't move boat anywhere but left or right.")
            self.boat_position = move.location
            toCheck=[self.left_shore,self.right_shore,self.boat]
            for location in toCheck:
                if self.checkIfObjectsClash(location):
                    break
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
    
    def has_won(self):
        "Returns true if the game is won and false otherwise."
        # check if the set of items on the right shore is a subset of the set of
        # required items.
        return set(["man", "wolf", "goat", "hay"]).issubset(self.right_shore)

    def lost(self):
        #returns the lose variable which is 'false' when no clash between entities and 'True' otherwise
        return self.lose

def report_shore(name, items):
    "Return a sentence representing the items on the given logical shore."
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
