class InvalidMove(Exception):
    pass

class Move:
    def __init__(self, obj, location):
        self.object = obj
        self.location = location


