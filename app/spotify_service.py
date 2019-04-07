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

# requires user interaction
# do this initially to get a valid token, then store that token in an env var to enable programmatic usage
def get_token():
    # looks like scope can be a list, see: https://github.com/plamere/spotipy/blob/master/spotipy/oauth2.py#L225
    # AUTH_SCOPE = ["playlist-read-private", "playlist-modify-private"] #> see https://developer.spotify.com/documentation/general/guides/scopes/#playlist-modify-private
    AUTH_SCOPE = "playlist-read-private" # trying this for now, simplest step forward
    token = util.prompt_for_user_token(USERNAME, AUTH_SCOPE)
    return token

# requires user auth
def get_my_playlists():
    token = get_token()

    client = spotipy.Spotify(auth=token)

    #client_credentials_manager = SpotifyClientCredentials() # implicitly uses SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET env vars!!
    #client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    print("---------------")
    print("CLIENT:", type(client)) #> <class 'spotipy.client.Spotify'>
    print(dir(client))

    print("---------------")
    print("GETTING PLAYLISTS...")

    #playlists = client.user_playlists("spotify") # hmm there are > 900 playlists and I needed to quit the program... need to try a different request
    playlists = client.current_user_playlists() #> requests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://api.spotify.com/v1/me/playlists?limit=50&offset=0

    while playlists:
        print(type(playlists))

        for i, playlist in enumerate(playlists['items']):
            print(f"{i + 1 + playlists['offset']} {playlist['uri']} {playlist['name']}")

        if playlists["next"]:
            playlists = client.next(playlists)
        else:
            playlists = None

if __name__ == "__main__":

    #get_springsteen_songs()

    get_token()
    #get_my_playlists()