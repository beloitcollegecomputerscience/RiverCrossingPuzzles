import os
from os import listdir
from os.path import isfile, join

class ConfigLoader:
    def __init__(self, scene_state, config_dir = "configs"):
        self.scene_state = scene_state
        self.config_directory = config_dir
        self.config_directory_full = join( os.path.dirname(os.path.realpath(__file__)), self.config_directory )

    def find_configs(self):
        config_files = []        
        for directory_item in listdir(self.config_directory_full):
            if isfile( join(self.config_directory_full, directory_item) ):
                config_files.append(directory_item)

        print("found configs: ", config_files)
        return config_files


