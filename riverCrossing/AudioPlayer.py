import os
import pyglet
import soundfile


class AudioPlayer:
    def __init__(self):
        working_dir = os.path.dirname(os.path.realpath(__file__))
        sounds_dir = os.path.join(working_dir, 'sounds')
        pyglet.resource.path.append(sounds_dir)
        self.sounds_dir = sounds_dir
        
        self.convert_bit_depth('click.wav')
        self.convert_bit_depth('background_music.wav')
        
        self.click_sound = pyglet.resource.media('click.wav', streaming=False)
        self.background_music = pyglet.resource.media('background_music.wav')
        
        self.media_player = pyglet.media.Player()
        self.media_player.loop = True

        self.play_music_looped()


    def play_click(self):        
        self.click_sound.play()        


    def play_music_looped(self): 
        self.media_player.queue(self.background_music)        
        self.media_player.play()

        
    def convert_bit_depth(self, file_name):
        """
        Pyglet only supports files with 8 or 16 bit depth. This function converts given sound
        file to supported bit depth in case user's system preference modify the file while downloading
        """
        background_path = os.path.join(self.sounds_dir, file_name)
        data, samplerate = soundfile.read(background_path)
        soundfile.write(background_path, data, samplerate, subtype='PCM_16')
        
