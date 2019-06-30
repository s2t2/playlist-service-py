import os
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import spotipy.util as util

load_dotenv() # load environment variables

CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID", "OOPS")
CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET", "OOPS")
REDIRECT_URL = os.environ.get("SPOTIPY_REDIRECT_URI", "OOPS")
USERNAME = os.environ.get("SPOTIFY_USERNAME", "OOPS")
AUTH_SCOPE = "playlist-read-private playlist-modify-private"
#AUTH_TOKEN = os.environ.get("SPOTIFY_AUTH_TOKEN", "OOPS")

PLAYLIST_NAME = os.environ.get("SPOTIFY_PLAYLIST_NAME", "My Pandora Bookmarks III")

def client_auth():
    credentials_filepath = os.path.join(os.path.dirname(__file__), "..", "credentials", "spotify_user.json")
    return SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URL,
        scope=AUTH_SCOPE,
        cache_path=credentials_filepath
    )

# doesn't require user auth
def song_search(search_term):
    client_credentials_manager = SpotifyClientCredentials() # implicitly uses SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET env vars!!
    client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    response = client.search(q=search_term, limit=20)
    tracks = response["tracks"]["items"]
    return tracks

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

# requires user auth token
def add_tracks(playlist_id, track_uris):
    client = authenticated_client()
    parsed_response = client.user_playlist_add_tracks(USERNAME, playlist_id, track_uris)
    return parsed_response #> {'snapshot_id': 'xzy123'}

if __name__ == "__main__":









    #credentials_filepath = os.path.join(os.path.dirname(__file__), "..", "credentials", "spotify_user.json")
    #client_auth = SpotifyOAuth(
    #    client_id=CLIENT_ID,
    #    client_secret=CLIENT_SECRET,
    #    redirect_uri=REDIRECT_URL,
    #    scope=AUTH_SCOPE,
    #    cache_path=credentials_filepath
    #)
    # client_auth.OAUTH_AUTHORIZE_URL #> 'https://accounts.spotify.com/authorize'
    # client_auth.OAUTH_TOKEN_URL #> 'https://accounts.spotify.com/api/token'

    # client_auth.get_authorize_url() #> 'https://accounts.spotify.com/authorize?client_id=_____&response_type=code&redirect_uri=________&scope=playlist-modify-private+playlist-read-private'

    # client_auth.get_cached_token() #> None
    # client_auth.refresh_access_token()
    # client_auth.parse_response_code()

    #auth_code = "xyz"
    #token_info = client_auth.get_access_token(auth_code)
    #print(token_info["access_token"])

    breakpoint()




    quit()




























    exit()


    #
    # GET PLAYLIST
    #

    playlist = find_or_create_playlist() # TODO: consider getting all playlists and asking the user to choose one
    print("PLAYLIST: ", playlist["id"], playlist["name"])

    playlist_id = playlist["id"] #> "2x64ZZ1u32oqgCkSH8eg2g"

    #
    # GET TRACK(S)
    #

    search_term = input("Please specify a search term: ")
    if not search_term:
        search_term = "Springsteen on Broadway"
    print("SEARCH TERM:", search_term)

    tracks = song_search(search_term)

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

    parsed_response = add_tracks(playlist_id, track_uris)
    print("ADDED TRACKS, SNAPSHOT:", parsed_response["snapshot_id"])

    # TODO: consider asking the user if they want to open the playlist in a browser (Y/N)
