import configparser


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    news_api_key = config["NEWS"]["API_KEY"]
    spotify_client_secret = config["SPOTIFY"]["CLIENT_SECRET"]


def init():
    if __name__ == "__main__":
        main()


init()
