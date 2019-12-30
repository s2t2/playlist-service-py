import os
import pytest
#from datetime import datetime
#from pandora.models.bookmark import Bookmark

from app.pandora_service import PandoraService
from app.spotify_service import SpotifyService

CI_ENV = os.environ.get("CI", "OOPS") == "true" # expect default environment variable setting of "CI=true" on Travis CI, see: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables
SKIP_REASON = "to avoid configuring credentials on, and issuing requests from, the CI server"

@pytest.fixture(scope="module")
def pandora_service():
    return PandoraService(login=True)

@pytest.fixture(scope="module")
def spotify_service():
    return SpotifyService(login=True)

@pytest.fixture(scope="module")
def pandora_bookmark(pandora_service):
    # TODO: assemble a mock bookmark if possible
    # Bookmark(
    #    album_name='Nirvana',
    #    art_url='http://mediaserver-cont-usc-mp1-1-v4v6.pandora.com/images/public/int/0/9/7/2/800042790_500W_500H.jpg',
    #    artist_name='Sam Smith',
    #    bookmark_token='430238419315403744',
    #    date_created=datetime.datetime(2019, 12, 21, 5, 58, 35, 240000),
    #    music_token='S2440851', sample_gain='-6.45',
    #    sample_url='http://www.pandora.com/favorites/getSample.jsp?token=MY_TOKEN&allowExplicit=true',
    #    song_name='Latch (Acoustic)'
    #) #> __init__() got an unexpected keyword argument 'album_name'

    #options = {
    #    "album_name":'Nirvana',
    #    "art_url":'http://mediaserver-cont-usc-mp1-1-v4v6.pandora.com/images/public/int/0/9/7/2/800042790_500W_500H.jpg',
    #    "artist_name":'Sam Smith',
    #    "bookmark_token":'430238419315403744',
    #    "date_created": datetime(2019, 12, 21, 5, 58, 35, 240000),
    #    "music_token": 'S2440851',
    #    #"sample_gain"='-6.45',
    #    "sample_url": 'http://www.pandora.com/favorites/getSample.jsp?token=MY_TOKEN&allowExplicit=true',
    #    "song_name": 'Latch (Acoustic)'
    #}
    #bookmark = Bookmark(options)
    #print(bookmark.song_name) # hmm these values are all None though...

    bookmarks = pandora_service.get_bookmarked_songs()
    return bookmarks[0]
