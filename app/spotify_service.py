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

PLAYLIST_NAME = os.environ.get("SPOTIFY_PLAYLIST_NAME", "My Pandora Bookmarks III")

# doesn't require user auth
def get_springsteen_songs():
    client_credentials_manager = SpotifyClientCredentials() # implicitly uses SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET env vars!!
    client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    search_term = "Springsteen on Broadway"
    response = client.search(q=search_term, limit=20)
    songs = response["tracks"]["items"]
    return songs

# prompts user to login to spotify and paste a callback url into the terminal
def get_token():
    token = util.prompt_for_user_token(USERNAME, AUTH_SCOPE)
    # might need to use this kind of approach instead...
    #credentials_filepath = os.path.join(os.path.dirname(__file__), "..", "credentials", "spotify_user.json")
    #token = util.prompt_for_user_token(USERNAME, AUTH_SCOPE, cache_path=credentials_filepath)
    return token

def authenticated_client():
    #client = spotipy.Spotify(auth=AUTH_TOKEN)
    token = get_token()
    client = spotipy.Spotify(auth=token)
    return client

# requires user auth token
def get_playlists():
    client = authenticated_client()
    playlists = []
    response = client.current_user_playlists()
    while response:
        #print(type(response)) #> dict
        for i, playlist in enumerate(response['items']):
            #print(f"{i + 1 + response['offset']} {playlist['uri']} {playlist['name']}")
            playlists.append(playlist)
        if response["next"]:
            response = client.next(response)
        else:
            response = None
    return playlists

# requires user auth token
def find_or_create_playlist():
    playlists = get_playlists()

    if PLAYLIST_NAME in [p["name"] for p in playlists]:
        playlist = [p for p in playlists if p["name"] == PLAYLIST_NAME ][0]
        #playlist.keys() #> dict_keys(['collaborative', 'external_urls', 'href', 'id', 'images', 'name', 'owner', 'primary_color', 'public', 'snapshot_id', 'tracks', 'type', 'uri'])
        #print(f"FOUND PLAYLIST: '{playlist['name']}' ({playlist['id']})")
    else:
        #print("PLAYLIST NOT FOUND")
        client = authenticated_client()
        playlist = client.user_playlist_create(user=USERNAME, name=PLAYLIST_NAME, public=False)
        #playlist.keys() #> dict_keys(['collaborative', 'description', 'external_urls', 'followers', 'href', 'id', 'images', 'name', 'owner', 'primary_color', 'public', 'snapshot_id', 'tracks', 'type', 'uri'])
        #print(f"CREATED PLAYLIST: '{playlist['name']}' ({playlist['id']})")
    return playlist

def add_tracks(playlist_id, track_uris):
    client = authenticated_client()
    parsed_response = client.user_playlist_add_tracks(USERNAME, playlist_id, track_uris)
    return parsed_response #> {'snapshot_id': 'xzy123'}

if __name__ == "__main__":

    #
    # GET PLAYLIST
    #

    playlist = find_or_create_playlist()
    print("PLAYLIST: ", playlist["id"], playlist["name"])

    playlist_id = playlist["id"] #> "2x64ZZ1u32oqgCkSH8eg2g"

    #
    # GET TRACK(S)
    #

    tracks = get_springsteen_songs()
    # TODO: accept user search term
    # search_term = "My Favorite Song, by Artist XYZ"
    # tracks = song_search(search_term)

    print(f"TRACKS ({len(tracks)}):")
    for i, trk in enumerate(tracks):
        print(f" {trk['uri']} {trk['name']}")

    track_uris = [tracks[0]["uri"]] #> ["spotify:track:4912tpbfCZEcSqPvmQVu1W"]

    #
    # ADD TRACK(S) TO PLAYLIST
    #

    parsed_response = add_tracks(playlist_id, track_uris)
    print("ADDED TRACKS, SNAPSHOT:", parsed_response["snapshot_id"])

    # TODO: consider asking the user if they want to open the playlist in a browser (Y/N)
