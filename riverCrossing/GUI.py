import pyglet


class GUI(pyglet.window.Window):
    def __init__(self, animation, audio_player):
        self.animation = animation
        self.boat = animation.boat
        self.scene_state = animation.scene_state

        background_image = self.scene_state.get_object_by_name("background")["image"]
        pyglet.window.Window.__init__(self, width=background_image.width,
                                      height=background_image.height, caption="River Crossing Puzzle")

        self.audio_player = audio_player
        self.add_gameplay_buttons_handlers()


    def on_draw(self):
        self.scene_state.main_batch.draw()
        self.scene_state.buttons_batch.draw()


    def on_mouse_press(self, x, y, button, modifiers):
        self.handle_button_presses(x, y)

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


    def on_mouse_motion(self, x, y, dx, dy):
        self.handle_button_hovers(x, y)
        pass


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
        self.audio_player.play_click()


    def boat_clicked(self, x, y):
        if not self.animation.check_if_all_stopped():
            return False

        boat_object = self.scene_state.get_object_by_name("boat")
        boat_collider_radius = boat_object["radius"]

        boat_was_clicked = self.sprite_clicked_within_radius(x, y, boat_object["sprite"], boat_collider_radius)
        if boat_was_clicked: self.audio_player.play_click()
        return boat_was_clicked


    def sprite_clicked_within_radius(self, x, y, sprite, collider_radius):
        center_x = sprite.x + collider_radius
        center_y = sprite.y + collider_radius
        if (abs(x - center_x) < collider_radius) and (abs(y - center_y) < collider_radius):
            return True
        return False
    

    def add_gameplay_buttons_handlers(self):
        buttons = self.scene_state.gameplay_buttons

        def restart_button_actions():
            print('restart clicked')
            self.audio_player.play_click()
        buttons["restart"].on_click = restart_button_actions

        def home_button_actions():
            print('home clicked')
            self.audio_player.play_click()
        buttons["home"].on_click = home_button_actions

        def help_button_actions():
            print('help clicked')
            self.audio_player.play_click()
        buttons["help"].on_click = help_button_actions


    def handle_button_presses(self, x, y):
        for button_name, button_object in self.scene_state.gameplay_buttons.items():
            if button_object.is_cursor_on_button(x, y):
                button_object.on_click()


    def handle_button_hovers(self, x, y):
        for button_name, button_object in self.scene_state.gameplay_buttons.items():
            if button_object.is_cursor_on_button(x, y):
                button_object.set_hover()
            else:
                button_object.unset_hover()
