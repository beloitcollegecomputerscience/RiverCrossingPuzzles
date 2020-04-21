import pyglet
import os
from os import listdir
from os.path import isfile, join
import pprint
from .Rules import Rules
from .Button import Button
from .Animation import Animation
from .Boat import Boat
from .ObjectLocations import ObjectLocations


class MainMenu:	
    def __init__(self, scene_state):
        self.scene_state = scene_state
        self.config_directory = "configs"
        self.config_directory_full = join( os.path.dirname(os.path.realpath(__file__)), self.config_directory )
        self.all_config_buttons = {}

        self.menu_background = self.init_menu_background()
        self.build_menu()


    def init_sprites(self):
        pass


    def build_menu(self):        
        all_config_files = self.find_configs()
        
        # deleting old sprites explicitly, to remove them from video memory and avoid overlapping
        for config_name, button_object in self.all_config_buttons.items():
            button_object.sprite.delete()

        self.init_menu_buttons(all_config_files)
        self.add_menu_buttons_handlers()


    def init_menu_background(self):
        background_sprite = pyglet.sprite.Sprite(
                img=pyglet.resource.image("background_menu.png"),
                x=0,
                y=0,
                batch=self.scene_state.menu_batch,
                group=pyglet.graphics.OrderedGroup(500))
        return background_sprite


    def init_menu_buttons(self, all_config_files):
        x_position = 200
        self.all_config_buttons = {}
        for config_name in all_config_files:
            splitted_name_and_extension = os.path.splitext(config_name)
            config_button_name = splitted_name_and_extension[0]
            config_file_extension = splitted_name_and_extension[1]
            # ingore non-json files!
            if (config_file_extension != ".json"):
                continue

            config_button_object = Button(200, 200, config_button_name, 0.75, self.scene_state.audio_player)

            config_button_object.image = pyglet.resource.image(config_button_object.image_file)
            config_button_object.image.anchor_x = config_button_object.image.width / 2
            config_button_object.image.anchor_y = config_button_object.image.height / 2
            config_button_object.sprite = pyglet.sprite.Sprite(
                img=config_button_object.image,
                x=x_position,
                y=450,
                batch=self.scene_state.menu_batch,
                group=pyglet.graphics.OrderedGroup(1000))
            config_button_object.sprite.scale = config_button_object.initial_scale

            self.all_config_buttons[config_button_name] = config_button_object
            x_position += 209


    def add_menu_buttons_handlers(self):
        for config_name, button_object in self.all_config_buttons.items():

            def menu_buttons_actions(config_name=config_name):
                self.scene_state.audio_player.play_click()
                self.load_new_game_with_config(config_name)

            button_object.on_click = menu_buttons_actions


    def find_configs(self):
        config_files = []        
        for directory_item in listdir(self.config_directory_full):
            if isfile( join(self.config_directory_full, directory_item) ):
                config_files.append(directory_item)

        print("found configs: ", config_files)
        return config_files


    def load_new_game_with_config(self, config_name):
        print("loading new game with config: " + config_name)
        config_full_path = join( self.config_directory_full, config_name) + ".json"
        rules = Rules(config_full_path).rules

        self.scene_state.boat_position = "left"
        self.scene_state.game_state = "playing"
        self.scene_state.current_batch = self.scene_state.main_batch
        self.scene_state.characters_on_board = {}

        # deleting old sprites explicitly, to remove them from video memory and avoid overlapping
        for scene_object in self.scene_state.scene_objects:            
            if "sprite" in scene_object:
                scene_object["sprite"].delete()
        self.scene_state.scene_objects = rules["scene_objects"]
        self.scene_state.violations = rules["violations"]
        self.scene_state.object_locations = ObjectLocations(self.scene_state)

        self.scene_state.init_sprites()

        self.scene_state.animation = Animation(self.scene_state)
        self.scene_state.boat = Boat(rules["boat_capacity"], rules["driver_name"],
                    self.scene_state.get_object_by_name("boat")["radius"], self.scene_state)

        self.scene_state.audio_player.play_music_looped()

        
    def load_main_menu_screen(self):
        self.scene_state.current_batch = self.scene_state.menu_batch
        self.scene_state.game_state = "menu"
        self.scene_state.audio_player.stop_music()

        # it's crucially important to unschedule the update, pyglet is not doing this automatically
        # otherwise each time we start the game we'll have a new looping update each time we start a game
        self.scene_state.animation.unschedule_update()

        # dynamically scan configs folder again
        self.build_menu()
