import pyglet


class GUI(pyglet.window.Window):
    def __init__(self, animation):
        self.animation = animation
        self.boat = animation.boat
        self.scene_state = animation.scene_state

        background_image = self.scene_state.get_object_by_name("background")["image"]
        pyglet.window.Window.__init__(self, width=background_image.width,
                                      height=background_image.height, caption="River Crossing Puzzle")


    def on_draw(self):
        self.scene_state.main_batch.draw()


    def on_mouse_press(self, x, y, button, modifiers):
        if self.scene_state.game_state != "playing":
            return

        if self.scene_state.boat_position == 'left':
            clicked_character = self.get_clicked_character(x, y)
            if clicked_character is not None:
                self.process_clicked_character(clicked_character)
            elif self.boat_clicked(x, y):
                self.boat.boat_try_ride(1)
        elif self.scene_state.boat_position == 'right':
            clicked_character = self.get_clicked_character(x, y)
            if clicked_character is not None:
                self.process_clicked_character(clicked_character)
            elif self.boat_clicked(x, y):
                self.boat.boat_try_ride(-1)


    def get_clicked_character(self, x, y):
        for character_name in self.animation.character_list:
            character_object = self.scene_state.get_object_by_name(character_name)
            collider_radius = character_object["radius"]
            if self.scene_state.boat_position != character_object["current_shore"]:
                continue
            if self.sprite_clicked_within_radius(x, y, character_object["sprite"], collider_radius):
                return character_object
        return None


    def process_clicked_character(self, clicked_character):
        character_name = clicked_character["name"]
        character_is_in_boat = character_name in self.scene_state.characters_on_board
        if character_is_in_boat:
            self.boat.remove_member(character_name)
        else:
            self.boat.add_member(character_name)


    def boat_clicked(self, x, y):
        if not self.animation.check_if_all_stopped():
            return False

        boat_object = self.scene_state.get_object_by_name("boat")
        boat_collider_radius = boat_object["radius"]
        return self.sprite_clicked_within_radius(x, y, boat_object["sprite"], boat_collider_radius)


    def sprite_clicked_within_radius(self, x, y, sprite, collider_radius):
        center_x = sprite.x + collider_radius
        center_y = sprite.y + collider_radius
        if (abs(x - center_x) < collider_radius) and (abs(y - center_y) < collider_radius):
            return True
        return False
