import os
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

load_dotenv() # load environment variables

CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID", "OOPS")
CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET", "OOPS")
REDIRECT_URL = os.environ.get("SPOTIPY_REDIRECT_URI", "OOPS")
USERNAME = os.environ.get("SPOTIFY_USERNAME", "OOPS")
AUTH_SCOPE = "playlist-read-private playlist-modify-private"
#AUTH_TOKEN = os.environ.get("SPOTIFY_AUTH_TOKEN", "OOPS")

PLAYLIST_NAME = os.environ.get("SPOTIFY_PLAYLIST_NAME", "OOPS")

class SpotifyService(object):
    """Uses the Spotify API to act on behalf of the authenticated user."""

    def __init__(self, login=True):
        self.public_client = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials()) # implicitly uses SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET env vars!!
        if login:
            self.username = USERNAME
            self.auth_scope = AUTH_SCOPE
            self.client = spotipy.Spotify(auth=self.get_token())
            #self.playlist_name = PLAYLIST_NAME
            self.playlists = None

    def song_search(self, search_term):
        """Search for songs matching a given term. Doesn't require user auth."""
        response = self.public_client.search(q=search_term, limit=20)
        tracks = response["tracks"]["items"]
        return tracks

    def get_token(self):
        """Prompts user to login to spotify and paste a callback url into the terminal."""
        token = util.prompt_for_user_token(self.username, self.auth_scope)
        # might need to use this kind of approach instead...
        #credentials_filepath = os.path.join(os.path.dirname(__file__), "..", "credentials", "spotify_user.json")
        #token = util.prompt_for_user_token(USERNAME, AUTH_SCOPE, cache_path=credentials_filepath)
        return token

    def get_playlists(self):
        """Get the authenticated user's playlists. Requires user auth token."""
        if self.playlists == None:
            self.playlists = []
            response = self.client.current_user_playlists()
            while response:
                #print(type(response)) #> dict
                for i, playlist in enumerate(response['items']):
                    #print(f"{i + 1 + response['offset']} {playlist['uri']} {playlist['name']}")
                    self.playlists.append(playlist)
                if response["next"]:
                    response = self.client.next(response)
                else:
                    response = None
        return self.playlists

    def get_playlist(self, playlist_name=PLAYLIST_NAME):
        """Find the specified playlist. Requires user auth token."""
        try:
            playlist = [p for p in self.get_playlists() if p["name"] == playlist_name][0]
        except IndexError as err:
            playlist = None
        return playlist

    def find_or_create_playlist(self, playlist_name=PLAYLIST_NAME):
        """Find or create the specified playlist. Requires user auth token."""
        playlist = self.get_playlist(playlist_name)
        if playlist:
            #playlist.keys() #> dict_keys(['collaborative', 'external_urls', 'href', 'id', 'images', 'name', 'owner', 'primary_color', 'public', 'snapshot_id', 'tracks', 'type', 'uri'])
            #print(f"FOUND PLAYLIST: '{playlist['name']}' ({playlist['id']})")
            pass
        else:
            #print("PLAYLIST NOT FOUND")
            playlist = self.client.user_playlist_create(user=self.username, name=playlist_name, public=False)
            #playlist.keys() #> dict_keys(['collaborative', 'description', 'external_urls', 'followers', 'href', 'id', 'images', 'name', 'owner', 'primary_color', 'public', 'snapshot_id', 'tracks', 'type', 'uri'])
            #print(f"CREATED PLAYLIST: '{playlist['name']}' ({playlist['id']})")
        return playlist

    def add_tracks(self, playlist_id, track_uris):
        """Add tracks to a given playlist. Requires user auth token."""
        parsed_response = self.client.user_playlist_add_tracks(self.username, playlist_id, track_uris)
        return parsed_response #> {'snapshot_id': 'xzy123'}

if __name__ == "__main__":

    service = SpotifyService()

    #
    # GET PLAYLIST
    #

    playlist = service.find_or_create_playlist() # TODO: consider getting all playlists and asking the user to choose one
    print("PLAYLIST: ", playlist["id"], playlist["name"])

    playlist_id = playlist["id"] #> "2x64ZZ1u32oqgCkSH8eg2g"

    #
    # GET TRACK(S)
    #

    search_term = input("Please specify a search term: ")
    if not search_term:
        search_term = "Springsteen on Broadway"
    print("SEARCH TERM:", search_term)

    tracks = service.song_search(search_term)

    print(f"TRACKS ({len(tracks)}):")
    for i, trk in enumerate(tracks):
        print(f" {trk['uri']} {trk['name']}")

    track_uri = input("Please choose a track, paste the URI and press enter: ")
    if not track_uri:
        track_uri = tracks[0]["uri"]
    print("YOU CHOSE", track_uri)

    track_uris = [track_uri] #> ["spotify:track:4912tpbfCZEcSqPvmQVu1W"]

    #
    # ADD TRACK(S) TO PLAYLIST
    #

    parsed_response = service.add_tracks(playlist_id, track_uris)
    print("ADDED TRACKS, SNAPSHOT:", parsed_response["snapshot_id"])

    # TODO: consider asking the user if they want to open the playlist in a browser (Y/N)
