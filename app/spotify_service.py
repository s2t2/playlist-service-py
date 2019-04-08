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

# doesn't require user auth
def get_springsteen_songs():
    client_credentials_manager = SpotifyClientCredentials() # implicitly uses SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET env vars!!
    client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    print("---------------")
    print("CLIENT:", type(client)) #> <class 'spotipy.client.Spotify'>
    print(dir(client))
    search_term = "Springsteen on Broadway"
    print("---------------")
    print("SEARCH:", search_term)
    response = client.search(q=search_term, limit=20)
    print("---------------")
    print("RESPONSE:", type(response))
    songs = response["tracks"]["items"]
    print("---------------")
    print(f"SONGS ({len(songs)}):", type(response))
    for i, song in enumerate(songs):
        print(f"  {i}) {song['name']}")

# requires user interaction to get a token to auth on their behalf (auth token)
# do this initially to get a valid token,
# then store that token in an env var SPOTIFY_USER_AUTH_TOKEN
# to enable future programmatic usage
def get_token():
    # looks like scope can be a list, see: https://github.com/plamere/spotipy/blob/master/spotipy/oauth2.py#L225
    # AUTH_SCOPE = ["playlist-read-private", "playlist-modify-private"] #> see https://developer.spotify.com/documentation/general/guides/scopes/#playlist-modify-private
    AUTH_SCOPE = "playlist-read-private" # trying this for now, simplest step forward
    token = util.prompt_for_user_token(USERNAME, AUTH_SCOPE)
    # might need to use this kind of approach instead...
    #user_credentials_filepath = os.path.join(os.path.dirname(__file__), "..", "credentials", "spotify_user.json")
    #token = util.prompt_for_user_token(USERNAME, AUTH_SCOPE, cache_path=user_credentials_filepath)
    return token

# requires user auth token
def get_playlists():
    #token = get_token()
    client = spotipy.Spotify(auth=AUTH_TOKEN)
    print("---------------")
    print("CLIENT:", type(client)) #> <class 'spotipy.client.Spotify'>
    print(dir(client))
    print("---------------")
    print("GETTING PLAYLISTS...")
    playlists = []
    #playlists = client.user_playlists("spotify") # hmm there are > 900 playlists and I needed to quit the program... need to try a different request
    response = client.current_user_playlists() #> requests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://api.spotify.com/v1/me/playlists?limit=50&offset=0
    while response:
        print(type(response))
        for i, playlist in enumerate(response['items']):
            print(f"{i + 1 + response['offset']} {playlist['uri']} {playlist['name']}")
            playlists.append(playlist)
        if response["next"]:
            response = client.next(response)
        else:
            response = None
    return playlists

# requires user auth token
def create_playlist():
    client = spotipy.Spotify(auth=AUTH_TOKEN)
    print("---------------")
    print("PLAYLIST EXISTS?")

    playlists = get_playlists()

    breakpoint()

    print("---------------")
    print("CREATING PLAYLIST...")
    #playlists = client.user_playlists("spotify") # hmm there are > 900 playlists and I needed to quit the program... need to try a different request
    playlists = client.current_user_playlists()

if __name__ == "__main__":

    #get_springsteen_songs()

    #get_token()

    get_playlists()

    create_playlist()
