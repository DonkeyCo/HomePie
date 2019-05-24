import os
import spotipy
import spotipy.util as util


class Spotify:

    def __init__(self, config=None):
        self.config = config
        self.scope = config["SPOTIFY"]["SCOPES"]
        self.token = util.prompt_for_user_token("donkeyco", self.scope, self.config["SPOTIFY"]["CLIENT_ID"],
                                                self.config["SPOTIFY"]["CLIENT_SECRET"], self.config["SPOTIFY"]["REDIRECT"])
        self.spotify = spotipy.Spotify(auth=self.token)

    def play(self):
        self.spotify.start_playback()

    def play_songs(self, songs):
        self.spotify.start_playback(uris=songs)

    def play_playlist(self, playlist):
        self.spotify.start_playback(context_uri=playlist)

    def get_devices(self):
        return self.spotify.devices()

    def next_track(self):
        self.spotify.next_track()

