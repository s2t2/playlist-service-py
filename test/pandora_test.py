
import pytest

from datetime import datetime
import pydora
from pandora.client import APIClient
from pandora.models.bookmark import Bookmark

from app.pandora_service import PandoraService, CLIENT_SETTINGS, PANDORA_USERNAME, PANDORA_PASSWORD

from conftest import CI_ENV, SKIP_REASON

def test_configured_client():
    pandora_service = PandoraService(login=False)
    # it should be a Pandora API client:
    client = pandora_service.client
    assert isinstance(client, APIClient)

    # it should be configured with provided settings:
    assert client.partner_user == CLIENT_SETTINGS["PARTNER_USER"]
    assert client.device == CLIENT_SETTINGS["DEVICE"]

    # it should be able to login and issue requests:
    assert "login" in dir(client)
    assert "get_bookmarks" in dir(client)

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_authenticated_client(pandora_service):
    # it should be a Pandora API client:
    client = pandora_service.client
    assert isinstance(client, APIClient)
    #assert client.username == None
    #assert client.password == None
    #
    #pandora_service.authenticate()

    # it should be authenticated with user credentials:
    assert client.username == PANDORA_USERNAME
    assert client.password == PANDORA_PASSWORD

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_get_bookmarks(pandora_service):
    songs = pandora_service.get_bookmarked_songs()
    assert isinstance(songs, list)
    assert len(songs) > 0

    song = songs[0]
    assert isinstance(song, Bookmark)
    assert isinstance(song.date_created, datetime)
    assert isinstance(song.artist_name, str)
    assert isinstance(song.song_name, str)
    assert isinstance(song.album_name, str)
