
import os
import pandas

from app import EXPORTS_DIR
from app.pandora_service import PandoraService

CSV_FILEPATH = os.path.join(EXPORTS_DIR, "pandora", "bookmarks.csv")

def to_dict(bookmark):
    """
    bookmark (pandora.models.bookmark.Bookmark)
    """
    return {
        "artist_name": bookmark.artist_name,
        "album_name": bookmark.album_name,
        "song_name": bookmark.song_name,
        "art_url": bookmark.art_url,
        "date_created": bookmark.date_created,
    }

def bookmark_sort(bookmark_attrs):
    """
    bookmark_attrs (dict)
    """
    return [bookmark_attrs["artist_name"], bookmark_attrs["album_name"], bookmark_attrs["song_name"]]

if __name__ == "__main__":

    service = PandoraService()

    bookmarks = service.get_bookmarked_songs()
    data = [to_dict(bookmark) for bookmark in bookmarks]
    data = sorted(data, key=bookmark_sort)

    df = pandas.DataFrame(data)
    df.index.rename("id", inplace=True) # assigns a column label "id" for the index column
    df.index += 1 # starts ids at 1 instead of 0
    print("EXPORTING PANDORA BOOKMARKS TO CSV...", os.path.abspath(CSV_FILEPATH))
    print(df.head())
    df.to_csv(CSV_FILEPATH)
