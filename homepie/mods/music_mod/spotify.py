import os
import spotipy
import spotipy.util as util


class Spotify:

    def __init__(self, config=None):
        self.config = config
        self.scope = "user-library-read streaming"
        self.token = util.prompt_for_user_token("donkeyco", self.scope, self.config["SPOTIFY"]["CLIENT_ID"],
                                                self.config["SPOTIFY"]["CLIENT_SECRET"], self.config["SPOTIFY"]["REDIRECT"])
        self.spotify = spotipy.Spotify(auth=self.token)

    def test_play(self):
        print(self.token)
        self.spotify.start_playback()
