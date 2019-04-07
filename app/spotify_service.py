import os
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv() # load environment variables

CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID", "OOPS")
CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET", "OOPS")

if __name__ == "__main__":

    client_credentials_manager = SpotifyClientCredentials() # implicitly uses SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET env vars!!
    client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    print("---------------")
    print("CLIENT:", type(client)) #> <class 'spotipy.client.Spotify'>
    print(dir(client))

    #
    # EXAMPLE SEARCH
    #
    #search_term = "Springsteen on Broadway"
    #print("---------------")
    #print("SEARCH:", search_term)
#
    #response = client.search(q=search_term, limit=20)
    #print("---------------")
    #print("RESPONSE:", type(response))
#
    #songs = response["tracks"]["items"]
    #print("---------------")
    #print(f"SONGS ({len(songs)}):", type(response))
#
    #for i, song in enumerate(songs):
    #    print(f"  {i}) {song['name']}")


    #
    # GET PLAYLISTS
    # ... adapted from: https://spotipy.readthedocs.io/en/latest/#client-credentials-flow
    #

    playlists = client.user_playlists("spotify") # hmm there are > 900 playlists and I needed to quit the program... need to try a different request

    while playlists:
        print(type(playlists))

        for i, playlist in enumerate(playlists['items']):
            print(f"{i + 1 + playlists['offset']} {playlist['uri']} {playlist['name']}")

        if playlists["next"]:
            playlists = client.next(playlists)
        else:
            playlists = None
