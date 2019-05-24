import spotipy
import spotipy.util as util


class Spotify:

    def __init__(self, config=None):
        self.config = config
        self.scope = config["SPOTIFY"]["SCOPES"]
        self.token = util.prompt_for_user_token(self.config["SPOTIFY"]["USER"], self.scope,
                                                self.config["SPOTIFY"]["CLIENT_ID"],
                                                self.config["SPOTIFY"]["CLIENT_SECRET"],
                                                self.config["SPOTIFY"]["REDIRECT"])
        self.spotify = spotipy.Spotify(auth=self.token)
        self.user_playlists = self.load_user_all_playlist()

    def load_user_all_playlist(self):
        """Loads all available user playlists into an instance variable"""
        s_playlists = self.get_user_all_playlist()
        playlists = []
        for playlist in s_playlists["items"]:
            playlists.append((playlist["name"], playlist["uri"], playlist["href"]))

        return playlists

    def get_user_all_playlist(self):
        """Returns an object with information for all user playlists"""
        return self.spotify.user_playlists(self.config["SPOTIFY"]["USER"])

    def play(self):
        """Starts playback"""
        self.spotify.start_playback()

    def play_songs(self, songs):
        """Starts playback for a list of songs"""
        self.spotify.start_playback(uris=songs)

    def play_single_track(self, query):
        """Starts playback for the first track in the search query"""
        found_items = self.spotify.search(q=query, type="track")
        uri = ""
        if len(found_items["tracks"]["items"]) > 0:
            item = found_items["tracks"]["items"][0]
            uri = item["uri"]

        if "" != uri:
            self.spotify.start_playback(uris=[uri])
        else:
            print("ERROR: Couldn't find the requested track.")

    def play_user_playlist(self, playlist_name, shuffle_state=False):
        """Playback for the playlist being started. Shuffle state determines if the playlist is being shuffled"""
        playlist_uri = ""
        for playlist in self.user_playlists:
            if playlist_name in playlist[0]:
                playlist_uri = playlist[1]
                break
        self.toggle_shuffle(shuffle_state)
        self.spotify.start_playback(context_uri=playlist_uri)

    def next_track(self):
        """Next track is being played"""
        self.spotify.next_track()

    def pause(self):
        """Playback is being paused"""
        self.spotify.pause_playback()

    def change_volume(self, volume):
        """Change of volume"""
        self.spotify.volume(volume)

    def toggle_shuffle(self, state):
        """Toggles shuffling"""
        self.spotify.shuffle(state)

    def get_devices(self):
        """Returns a list of all available devices"""
        return self.spotify.devices()
