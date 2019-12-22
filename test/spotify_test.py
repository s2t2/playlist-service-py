

import os
import pytest
import spotipy

from app.spotify_service import SpotifyService, CLIENT_ID, CLIENT_SECRET, USERNAME, PLAYLIST_NAME, AUTH_SCOPE, REDIRECT_URL
from conftest import CI_ENV, SKIP_REASON

def test_config():
    assert CLIENT_ID is not "OOPS"
    assert CLIENT_SECRET is not "OOPS"
    assert REDIRECT_URL is not "OOPS"
    assert USERNAME is not "OOPS"
    assert AUTH_SCOPE == "playlist-read-private playlist-modify-private"
    assert PLAYLIST_NAME is not "OOPS"

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_song_search():
    spotify_service = SpotifyService(login=False)
    songs = spotify_service.song_search("Springsteen on Broadway")
    assert len(songs) == 20

    song = songs[0]
    assert "id" in song.keys() # song["id"] == "7G7UNs17d0Grqk63M2MAwu"
    assert "name" in song.keys() # song["name"] == "My Hometown - Springsteen on Broadway"
    assert "uri" in song.keys() # song["uri"] == "spotify:track:7G7UNs17d0Grqk63M2MAwu"

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_get_token(spotify_service):
    credentials_filepath = os.path.join(os.path.dirname(__file__), "..", f".cache-{USERNAME}")
    assert os.path.isfile(credentials_filepath) == True # right now this test requires a pre-existing credentials file

    #if os.path.isfile(credentials_filepath):
    #    os.remove(credentials_filepath)
    #assert os.path.isfile(credentials_filepath) == False

    token = spotify_service.get_token()
    assert os.path.isfile(credentials_filepath) == True
    assert isinstance(token, str)
    # consider reading the json file to compare the auth token value

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_authenticated_client(spotify_service):
    client = spotify_service.client
    assert isinstance(client, spotipy.client.Spotify)
    assert "current_user_playlists" in dir(client)
    assert "next" in dir(client)
    assert "search" in dir(client)
    assert "user_playlist_create" in dir(client)
    assert "user_playlist_add_tracks" in dir(client)

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_find_or_create_playlist(spotify_service):
    parsed_response = spotify_service.find_or_create_playlist()
    assert isinstance(parsed_response, dict)
    assert parsed_response["name"] == PLAYLIST_NAME

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_add_tracks(spotify_service):
    playlist = spotify_service.find_or_create_playlist()
    playlist_id = playlist["id"]

    track_ids = ["spotify:track:4912tpbfCZEcSqPvmQVu1W"]
    parsed_response = spotify_service.add_tracks(playlist_id, track_ids)
    assert isinstance(parsed_response, dict)
    assert isinstance(parsed_response["snapshot_id"], str)
