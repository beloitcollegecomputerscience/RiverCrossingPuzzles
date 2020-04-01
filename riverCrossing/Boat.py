class Boat:
    def __init__(self, boat_capacity, driver_name, boat_radius, animation, scene_state):
        self.animation = animation
        self.scene_state = scene_state
        self.boat_capacity = boat_capacity
        self.driver_name = driver_name
        self.boat_radius = boat_radius
        self.boat_has_driver = False


    def add_member(self, character_name):
        character_object = self.scene_state.get_object_by_name(character_name)
        current_boat_members = self.get_number_of_boat_members()
        if current_boat_members >= self.boat_capacity:
            return
        seat_number = self.get_available_seat_number()
        one_seat_size = (self.boat_radius * 2) / self.boat_capacity
        boat_seat_offset_y = self.boat_radius / 2
        boat_seat_offset_x = (seat_number * one_seat_size)
        # centering the seat
        boat_seat_offset_x += one_seat_size / 2 - character_object["radius"]
        self.scene_state.object_locations.set_character_destination_to_boat(character_object,
                                                                             boat_seat_offset_x, boat_seat_offset_y)
        self.scene_state.characters_on_board.update({character_name: seat_number})


    def remove_member(self, character_name):
        character_object = self.scene_state.get_object_by_name(character_name)
        self.scene_state.object_locations.set_character_destination_to_shore(character_object)
        del self.scene_state.characters_on_board[character_name]


    def get_available_seat_number(self):
        occupied_seats = self.scene_state.characters_on_board.values()
        for possible_seat in range(self.boat_capacity):
            if possible_seat not in occupied_seats:
                return possible_seat
        return None


    def boat_try_ride(self, direction, x, y):
        print('\nBoat was clicked, trying to ride!')
        if not self.is_allowed_to_ride():
            return
        if direction == -1:
            self.scene_state.boat_position = 'left'
        elif direction == 1:
            self.scene_state.boat_position = 'right'
        self.scene_state.object_locations.set_destinations_to_other_shore(direction)

        rule_violated = self.is_any_rule_violated(direction)
        if rule_violated:
            self.scene_state.game_state = "loss"


    def is_allowed_to_ride(self):
        number_of_boat_members = self.get_number_of_boat_members()
        boat_has_driver = self.if_boat_has_driver()

        print(str(number_of_boat_members) + " characters on board!")
        print("Passengers and seats:", self.scene_state.characters_on_board)
        print("Is driver present? " + str(boat_has_driver))

        return number_of_boat_members <= self.boat_capacity and boat_has_driver


    def is_any_rule_violated(self, direction):
        violations = self.scene_state.violations
        characters_left = []

        if direction == -1:
            check_shore = "right"
        else:
            check_shore = "left"

        for character_name in self.scene_state.get_character_list():
            character_object = self.scene_state.get_object_by_name(character_name)
            if check_shore == character_object["current_shore"]:
                characters_left.append(character_name)

        # Check if any characters left on the shore correspond to the violating combinations
        for violation in violations:
            if set(characters_left) == set(violation):
                return True
        return False


    def get_number_of_boat_members(self):
        return len(self.scene_state.characters_on_board)


    def if_boat_has_driver(self):
        return self.driver_name in self.scene_state.characters_on_board
