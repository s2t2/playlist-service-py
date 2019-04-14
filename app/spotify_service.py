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
AUTH_TOKEN = os.environ.get("SPOTIFY_AUTH_TOKEN", "OOPS")

PLAYLIST_NAME = os.environ.get("SPOTIFY_PLAYLIST_NAME", "My Pandora Bookmarks III")

# doesn't require user auth
def get_springsteen_songs():
    client_credentials_manager = SpotifyClientCredentials() # implicitly uses SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET env vars!!
    client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    search_term = "Springsteen on Broadway"
    #print("---------------")
    #print("SEARCH:", search_term)
    response = client.search(q=search_term, limit=20)
    #print("---------------")
    #print("RESPONSE:", type(response))
    songs = response["tracks"]["items"]
    #print("---------------")
    print(f"SONGS ({len(songs)}):")
    for i, song in enumerate(songs):
        print(f" {song['uri']} {song['name']}")
    return songs

# requires user interaction to get a token to auth on their behalf (auth token)
# do this initially to get a valid token,
# then store that token in an env var SPOTIFY_USER_AUTH_TOKEN
# to enable future programmatic usage
def get_token():
    #AUTH_SCOPE = ["playlist-read-private", "playlist-modify-private"] #> AttributeError: 'list' object has no attribute 'split'
    AUTH_SCOPE = "playlist-read-private playlist-modify-private" # should be split() #> Insufficient client scope
    #AUTH_SCOPE = "playlist-modify-private"

    token = util.prompt_for_user_token(USERNAME, AUTH_SCOPE)
    # might need to use this kind of approach instead...
    #user_credentials_filepath = os.path.join(os.path.dirname(__file__), "..", "credentials", "spotify_user.json")
    #token = util.prompt_for_user_token(USERNAME, AUTH_SCOPE, cache_path=user_credentials_filepath)
    return token

def authenticated_client():
    #client = spotipy.Spotify(auth=AUTH_TOKEN)
    token = get_token()
    client = spotipy.Spotify(auth=token)
    return client

# requires user auth token
def get_playlists():
    #token = get_token()
    #client = spotipy.Spotify(auth=AUTH_TOKEN)
    client = authenticated_client()
    #print("---------------")
    #print("CLIENT:", type(client)) #> <class 'spotipy.client.Spotify'>
    #print(dir(client))
    #print("---------------")
    #print("GETTING PLAYLISTS...")
    playlists = []
    #playlists = client.user_playlists("spotify") # hmm there are > 900 playlists and I needed to quit the program... need to try a different request
    response = client.current_user_playlists() #> requests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://api.spotify.com/v1/me/playlists?limit=50&offset=0
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
        # count songs
    else:
        #print("PLAYLIST NOT FOUND")
        client = authenticated_client()
        playlist = client.user_playlist_create(user=USERNAME, name=PLAYLIST_NAME, public=False)
        #playlist.keys() #> dict_keys(['collaborative', 'description', 'external_urls', 'followers', 'href', 'id', 'images', 'name', 'owner', 'primary_color', 'public', 'snapshot_id', 'tracks', 'type', 'uri'])
        #print(f"CREATED PLAYLIST: '{playlist['name']}' ({playlist['id']})")
        # count songs

    return playlist

def add_tracks(track_uris):
    client = authenticated_client()

    playlist = find_or_create_playlist()
    print("PLAYLIST: ", playlist["id"], playlist["name"])
    playlist_id = playlist["id"]

    parsed_response = client.user_playlist_add_tracks(USERNAME, playlist_id, track_uris)
    return parsed_response #> {'snapshot_id': 'xzy123'}

if __name__ == "__main__":

    songs = get_springsteen_songs()
    #print(songs[0])
    ###songs[0]["id"] #> '7G7UNs17d0Grqk63M2MAwu'
    ###songs[0]["uri"] #> 'spotify:track:7G7UNs17d0Grqk63M2MAwu'
    ###songs[0]["name"] #> 'My Hometown - Springsteen on Broadway'
    track_uris = [songs[0]["uri"]] #> spotify:track:7G7UNs17d0Grqk63M2MAwu"

    #track_uris = ["spotify:track:4912tpbfCZEcSqPvmQVu1W"]

    print("TRACKS:", track_uris)
    parsed_response = add_tracks(track_uris)
    print("ADDED TRACKS, SNAPSHOT:", parsed_response["snapshot_id"])
