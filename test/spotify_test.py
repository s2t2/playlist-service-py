

import os
import pytest
import spotipy

from app.spotify_service import (
    USERNAME,
    PLAYLIST_NAME,
    get_token,
    authenticated_client,
    find_or_create_playlist,
    add_tracks
)

def test_playlist_name():
    assert PLAYLIST_NAME == "My Pandora Bookmarks III"

CI_ENV = os.environ.get("CI", "OOPS") == "true" # expect default environment variable setting of "CI=true" on Travis CI, see: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables
SKIP_REASON = "to avoid issuing requests from the CI server"

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_get_token():
    credentials_filepath = os.path.join(os.path.dirname(__file__), "..", f".cache-{USERNAME}")
    assert os.path.isfile(credentials_filepath) == True # right now this test requires a pre-existing credentials file

    #if os.path.isfile(credentials_filepath):
    #    os.remove(credentials_filepath)
    #assert os.path.isfile(credentials_filepath) == False

    token = get_token()
    assert os.path.isfile(credentials_filepath) == True
    assert isinstance(token, str)
    # consider reading the json file to compare the auth token value

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_authenticated_client():
    client = authenticated_client()
    assert isinstance(client, spotipy.client.Spotify)
    assert "current_user_playlists" in dir(client)
    assert "next" in dir(client)
    assert "search" in dir(client)
    assert "user_playlist_create" in dir(client)
    assert "user_playlist_add_tracks" in dir(client)

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_find_or_create_playlist():
    parsed_response = find_or_create_playlist()
    assert isinstance(parsed_response, dict)
    assert parsed_response["name"] == PLAYLIST_NAME

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_add_track():
    track_ids = ["spotify:track:4912tpbfCZEcSqPvmQVu1W"]
    parsed_response = add_tracks(track_ids)
    assert isinstance(parsed_response, dict)
    assert isinstance(parsed_response["snapshot_id"], str)
