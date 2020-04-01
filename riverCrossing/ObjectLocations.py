class ObjectLocations:
    """
    This class creates a general layout that can be applied to all versions of the game
    with less than 6 characters and no island. Modify images to set up new games.
    """

    def __init__(self, scene_state):
        self.scene_state = scene_state
        self.character_list = scene_state.get_character_list()

        # These values are based on the current background's size. Be careful when use different background.
        self.river = 660
        self.river_boat_travel_distance = 270
        self.distance_to_other_shore = 750
        self.hor_gap = 10
        self.ver_gap = 0
        self.large_bottom_margin = 470
        self.each_height = 65
        self.each_width = 100


    def set_initial_destinations(self):
        self.scene_state.get_object_by_name("boat")["current_destination"] = [270, 218]
        for i in range(len(self.character_list)):
            character_name = self.character_list[i]
            character_object = self.scene_state.get_object_by_name(character_name)
            calculated_position = self.calculate_shore_position_slot(i)
            character_object["calculated_shore_position"] = calculated_position
            character_object["current_destination"] = calculated_position
            character_object["current_shore"] = self.scene_state.boat_position


    # automatically calculates chequerwise positions for any new character
    def calculate_shore_position_slot(self, character_index):
        character_index = character_index + 1  # starting with 1 and not with 0

        # (character_index % 2) infinitely toggles between 1 and 0 for each incrementing index
        horizontal_position = (character_index % 2) * self.each_width
        x = self.hor_gap + horizontal_position

        # vertical_position increases proportionally with higher character_index
        vertical_position = (character_index) * self.each_height
        y = self.ver_gap + self.large_bottom_margin - vertical_position
        return [x, y]


    def set_destinations_to_other_shore(self, direction):
        self.scene_state.get_object_by_name("boat")["current_destination"][
            0] += direction * self.river_boat_travel_distance
        for character_name in self.character_list:
            if character_name in self.scene_state.characters_on_board:
                character_object = self.scene_state.get_object_by_name(character_name)
                character_object["current_destination"][0] += direction * self.river_boat_travel_distance
                character_object["current_shore"] = self.scene_state.boat_position


    def set_character_destination_to_boat(self, character, offset_x, offset_y):
        boat_position = self.scene_state.get_object_by_name("boat")["current_destination"]
        character["current_destination"] = [boat_position[0] + offset_x, boat_position[1] + offset_y]


    def set_character_destination_to_shore(self, character):
        character["current_destination"] = list(character["calculated_shore_position"])
        if self.scene_state.boat_position == "right":
            character["current_destination"][0] += self.distance_to_other_shore
