import configparser
import time
from homepie.mods.sound_mod.recognition import Recognition
from homepie.mods.music_mod.spotify import Spotify


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    news_api_key = config["NEWS"]["API_KEY"]
    spotify_client_secret = config["SPOTIFY"]["CLIENT_SECRET"]

    s = Spotify(config)
    s.test()


def init():
    if __name__ == "__main__":
        main()


init()
