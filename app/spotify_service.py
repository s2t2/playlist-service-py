import os
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv() # load environment variables

CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID", "OOPS")
CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET", "OOPS")

def example_search(client):
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

def get_my_playlists(client):
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

    client_credentials_manager = SpotifyClientCredentials() # implicitly uses SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET env vars!!
    client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    print("---------------")
    print("CLIENT:", type(client)) #> <class 'spotipy.client.Spotify'>
    print(dir(client))

    example_search(client)

    get_my_playlists(client)
