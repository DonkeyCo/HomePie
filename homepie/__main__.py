import configparser
import time
from homepie.mods.sound_mod.recognition import Recognition


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    news_api_key = config["NEWS"]["API_KEY"]
    spotify_client_secret = config["SPOTIFY"]["CLIENT_SECRET"]

    r = Recognition(config)
    r.listen_background()

    while True:
        time.sleep(0.1)


def init():
    if __name__ == "__main__":
        main()


init()
