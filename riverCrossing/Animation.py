import pyglet


class Animation:
    def __init__(self, scene_state):
        self.scene_state = scene_state
        self.boat = None
        self.scene_objects = scene_state.scene_objects

        self.character_list = scene_state.get_character_list()
        print("Character list: ", self.character_list)

        pyglet.clock.schedule_interval(self.update, 1 / 200.0)


    def update(self, duration):
        velocity = 300

        if self.scene_state.game_state == "win":
            self.announce_winner()
        if self.scene_state.game_state == "loss":
            self.announce_game_over()

        for scene_object in self.scene_objects:
            scene_object["is_animating"] = self.animate(scene_object["sprite"], scene_object["current_destination"],
                                                        duration, velocity)

        if self.scene_state.has_won(self.check_if_all_stopped(), self.boat.get_number_of_boat_members()):
            self.scene_state.game_state = "win"


    def announce_winner(self):
        announcement = self.scene_state.get_object_by_name("winning_announcement")
        announcement["sprite"].group = pyglet.graphics.OrderedGroup(30)


    def announce_game_over(self):
        announcement = self.scene_state.get_object_by_name("game_over_announcement")
        announcement["sprite"].group = pyglet.graphics.OrderedGroup(30)


    def animate(self, sprt, destination, duration, velocity):
        if self.check_if_sprite_at_destination(sprt, destination):
            return False
        if sprt.x < destination[0] - 1:
            sprt.x += velocity * duration
        if sprt.x > destination[0] + 1:
            sprt.x -= velocity * duration
        if sprt.y < destination[1] - 1:
            sprt.y += velocity * duration
        if sprt.y > destination[1] + 1:
            sprt.y -= velocity * duration
        return True


    def check_if_sprite_at_destination(self, sprt, destination):
        if abs(sprt.x - destination[0]) > 5:
            return False
        if abs(sprt.y - destination[1]) > 5:
            return False
        return True


    def check_if_all_stopped(self):
        for name in self.character_list:
            character_object = self.scene_state.get_object_by_name(name)
            if character_object["is_animating"] == True:
                return False
        return True


    def move_sprite_to(self, sprite, x, y):
        sprite.x = x
        sprite.y = y
        return sprite
