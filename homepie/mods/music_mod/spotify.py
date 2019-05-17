import os
import spotipy
import spotipy.util as util


class Spotify:

    def __init__(self, config=None):
        self.config = config

    def show_tracks(self, tracks):
        for i, item in enumerate(tracks['items']):
            track = item['track']
            print("%d %32.32s %s" % (i, track['artists'][0]['name'],track['name']))

    def test(self):
        scope = "user-library-read"
        token = util.prompt_for_user_token("donkeyco", scope, self.config["SPOTIFY"]["CLIENT_ID"],
                                           self.config["SPOTIFY"]["CLIENT_SECRET"], self.config["SPOTIFY"]["REDIRECT"])
        if token:
            sp = spotipy.Spotify(auth=token)
            playlists = sp.user_playlists("donkeyco")
            for playlist in playlists['items']:
                if playlist['owner']['id'] == "donkeyco":
                    print
                    print
                    playlist['name']
                    print
                    '  total tracks', playlist['tracks']['total']
                    results = sp.user_playlist("donkeyco", playlist['id'],
                                               fields="tracks,next")
                    tracks = results['tracks']
                    self.show_tracks(tracks)
                    while tracks['next']:
                        tracks = sp.next(tracks)
                        self.show_tracks(tracks)
        else:
            print("fuck")