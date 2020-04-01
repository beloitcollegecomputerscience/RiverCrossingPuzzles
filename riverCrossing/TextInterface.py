from . import InvalidMove, GameState, Move

class TextInterface:
    """Analagous to the GUI class, TextInterface drives a GameState
    with text printing of results and text inputs."""
    def __init__(self):
        self.game_state = GameState()

    def intro(self):
        print("Welcome to River Crossing Puzzles.")
        print("This is the textual interface. Each round asks you to move something.")
        print("You can move the boat from shore to shore (left or right).")
        print("Or, you can move object to the boat or to the closest shore.")
        print("")
        print(self.game_state.report())

    def pump(self):
        "Run a single request/response cycle, handling InvalidMove exceptions."
        try:
            self.game_state.apply_move(Move(input("move what? "), input("move it where? ")))
        except InvalidMove as e:
            print("I don't know how to do that: ", e)
        else:
            print(self.game_state.report())

    def finished(self):
        "Returns true if the game is over for any reason."
        return self.game_state.has_won() or self.game_state.has_lost()

    def outro(self):
        if self.game_state.has_won():
            print("Congratulations! You win.")
        elif self.game_state.has_lost():
            print("Game over! Too bad.")
        else:
            print("Game interrupted.")
        

