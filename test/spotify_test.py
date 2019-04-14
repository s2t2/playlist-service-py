

from app.spotify_service import authenticated_client
import spotipy

import os
import pytest

CI_ENV = os.environ.get("CI", "OOPS") == "true" # expect default environment variable setting of "CI=true" on Travis CI, see: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables
SKIP_REASON = "to avoid issuing requests from the CI server"

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_authenticated_client():
    client = authenticated_client()
    assert isinstance(client, spotipy.client.Spotify)
    assert "current_user_playlists" in dir(client)
    assert "next" in dir(client)
    assert "search" in dir(client)
    assert "user_playlist_create" in dir(client)
    assert "user_playlist_add_tracks" in dir(client)
