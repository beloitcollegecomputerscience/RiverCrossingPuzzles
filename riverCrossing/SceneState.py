import pyglet
import os
from .ObjectLocations import ObjectLocations
from .Button import Button


class SceneState:
    def __init__(self, rules, audio_player):
        self.boat_position = "left"
        self.game_state = "playing"
        self.main_batch = pyglet.graphics.Batch()
        self.scene_objects = rules["scene_objects"]
        self.violations = rules["violations"]
        self.init_sprites()

        self.audio_player = audio_player
        self.buttons_batch = pyglet.graphics.Batch()
        self.gameplay_buttons = {}
        self.init_gameplay_buttons()

        self.object_locations = ObjectLocations(self)
        self.object_locations.set_initial_destinations()
        self.characters_on_board = {}


    def init_sprites(self):
        working_dir = os.path.dirname(os.path.realpath(__file__))
        image_dir = os.path.join(working_dir, 'images')        
        pyglet.resource.path.append(image_dir)
        pyglet.resource.reindex()
        for scene_object in self.scene_objects:
            scene_object["image"] = pyglet.resource.image(scene_object["image_filename"])
            scene_object["sprite"] = pyglet.sprite.Sprite(
                img=scene_object["image"],
                x=scene_object["initial_position"][0],
                y=scene_object["initial_position"][1],
                batch=self.main_batch,
                group=pyglet.graphics.OrderedGroup(scene_object["draw_layer"]))
            scene_object["sprite"].scale = scene_object["initial_scale"]


    def init_gameplay_buttons(self):
        buttons_names = ["restart", "home", "help"]
        x_position = 375;
        for button_name in buttons_names:
            button_object = Button(50, 50, "button_" + button_name + ".png", 0.1, self.audio_player)

            button_object.image = pyglet.resource.image(button_object.image_file)
            button_object.image.anchor_x = button_object.image.width / 2
            button_object.image.anchor_y = button_object.image.height / 2
            button_object.sprite = pyglet.sprite.Sprite(
                img=button_object.image,
                x=x_position,
                y=50,
                batch=self.buttons_batch,
                group=pyglet.graphics.OrderedGroup(1000))
            button_object.sprite.scale = button_object.initial_scale

            self.gameplay_buttons[button_name] = button_object
            x_position += 100


    def get_character_list(self):
        character_list = []
        for scene_object in self.scene_objects:
            if scene_object["is_character"]:
                character_list.append(scene_object["name"])
        return character_list


    def get_object_by_name(self, name):
        for scene_object in self.scene_objects:
            if scene_object["name"] == name:
                return scene_object
                break
        return None


    # Check if the player has won based on several conditions
    def has_won(self, all_stopped, boat_members):
        if not all_stopped:
            return False
        if boat_members != 0:
            return False
        for name in self.get_character_list():
            character_object = self.get_object_by_name(name)
            if character_object["current_shore"] != "right":
                return False
        return True
