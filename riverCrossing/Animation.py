import pyglet
import math
import time


class Animation:    
    def __init__(self, scene_state):
        self.scene_state = scene_state
        self.scene_objects = scene_state.scene_objects
        self.boat = None

        self.character_list = scene_state.get_character_list()
        print("Character list: ", self.character_list)

        pyglet.clock.schedule_interval(self.update, 1 / 200.0)


    def unschedule_update(self):
        pyglet.clock.unschedule(self.update)


    def update(self, duration):
        velocity = 250

        for scene_object in self.scene_objects:
            scene_object["is_animating"] = self.animate_character(scene_object["sprite"], scene_object["current_destination"],
                                                        duration, velocity)

        if self.scene_state.game_state == "win":
            self.announce_winner()
        if self.scene_state.game_state == "violation_detected":
            if self.check_if_all_stopped():
                self.scene_state.game_state = "attack"
        if self.scene_state.game_state == "attack":
            self.animate_attack()
        if self.scene_state.game_state == "loss":
            self.announce_game_over()

        if self.scene_state.has_won(self.check_if_all_stopped()):
            self.scene_state.game_state = "win"


    def announce_winner(self):
        announcement = self.scene_state.get_object_by_name("winning_announcement")
        announcement["sprite"].group = pyglet.graphics.OrderedGroup(30)


    def move_predator(self):
        violation = self.scene_state.current_violation
        predator_object = self.scene_state.get_object_by_name(violation[0])
        victim_object = self.scene_state.get_object_by_name(violation[1])
        predator_object["current_destination"] = victim_object["current_destination"]


    def animate_attack(self):
        violation = self.scene_state.current_violation
        victim_object = self.scene_state.get_object_by_name(violation[1])
        victim_object["sprite"].scale /= 1.2

        if victim_object["sprite"].scale < 0.005:
            self.scene_state.game_state = "loss"


    def announce_game_over(self):
        announcement = self.scene_state.get_object_by_name("game_over_announcement")
        announcement["sprite"].group = pyglet.graphics.OrderedGroup(30)


    def animate_character(self, sprt, destination, duration, velocity, oscillate = True):
        difference_by_x, difference_by_y = destination[0] - sprt.x, destination[1] - sprt.y
        distance_to_destination = math.sqrt(pow(difference_by_x, 2) + pow(difference_by_y, 2))
        if distance_to_destination < 5:
            return False

        normalization_coefficient = velocity * duration / distance_to_destination
        sprt.x += difference_by_x * normalization_coefficient
        sprt.y += difference_by_y * normalization_coefficient

        if oscillate:
            oscillator_amplitude = 2
            oscillator_frequency = 15
            oscillator_move_value = oscillator_amplitude * math.sin(oscillator_frequency * time.time())
            sprt.y += oscillator_move_value
        return True


    def check_if_all_stopped(self):
        for name in self.character_list:
            character_object = self.scene_state.get_object_by_name(name)
            if character_object["is_animating"]:
                return False
        return True


    def move_sprite_to(self, sprite, x, y):
        sprite.x = x
        sprite.y = y
        return sprite
