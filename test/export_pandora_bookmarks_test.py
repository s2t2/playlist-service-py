
from datetime import datetime

from pandora.models.bookmark import Bookmark

from app.exports.pandora.bookmarks import to_row

def test_to_row(pandora_bookmark):
    assert isinstance(pandora_bookmark, Bookmark)

    row = to_row(pandora_bookmark)

    isinstance(row["artist_name"], str)
    isinstance(row["album_name"], str)
    isinstance(row["song_name"], str)
    isinstance(row["art_url"], str)
    isinstance(row["date_created"], datetime)
