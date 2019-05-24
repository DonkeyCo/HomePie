import configparser
import time
from homepie.mods.sound_mod.recognition import Recognition
from homepie.mods.music_mod.spotify import Spotify
import homepie.mods.weather_mod.weather as weather


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    s = Spotify(config)
    print("Playing...")
    s.play_playlist("spotify:playlist:1nudUWVKFvqveeWZdjoyph")
    time.sleep(15)
    print("Next track...")
    s.next_track()


def init():
    if __name__ == "__main__":
        main()


init()
