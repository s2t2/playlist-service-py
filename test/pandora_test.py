
import datetime
import os
from dotenv import load_dotenv
import pydora
import pandora
import pytest

from app.pandora_service import (
    CLIENT_SETTINGS, PANDORA_USERNAME, PANDORA_PASSWORD,
    configured_client, authenticated_client, get_bookmarks
)

def test_configured_client():
    # it should be a Pandora API client:
    client = configured_client()
    assert isinstance(client, pandora.client.APIClient)

    # it should be configured with provided settings:
    assert client.partner_user == CLIENT_SETTINGS["PARTNER_USER"]
    assert client.device == CLIENT_SETTINGS["DEVICE"]

    # it should be able to login:
    assert "login" in dir(client)

CI_ENV = os.environ.get("CI", "OOPS") == "true" # expect default environment variable setting of "CI=true" on Travis CI, see: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables

SKIP_REASON = "to avoid configuring credentials on, and issuing requests from, the CI server"

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_authenticated_client():
    # it should be a Pandora API client:
    client = authenticated_client()
    assert isinstance(client, pandora.client.APIClient)

    # it should be authenticated with user credentials:
    assert client.username == PANDORA_USERNAME
    assert client.password == PANDORA_PASSWORD

    # it should be able to get my bookmarks:
    assert "get_bookmarks" in dir(client)

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_bookmarks():
    songs = get_bookmarks()
    assert isinstance(songs, list)
    assert len(songs) > 0

    song = songs[0]
    assert isinstance(song, pandora.models.pandora.Bookmark)
    assert isinstance(song.date_created, datetime.datetime)
    assert isinstance(song.artist_name, str)
    assert isinstance(song.song_name, str)
    assert isinstance(song.album_name, str)
