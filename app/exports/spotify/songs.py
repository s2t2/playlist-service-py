
import os
import pandas

from app import EXPORTS_DIR
from app.spotify_service import SpotifyService

CSV_FILEPATH = os.path.join(EXPORTS_DIR, "spotify", "songs.csv")

if __name__ == "__main__":

    print("EXPORTING SPOTIFY SONGS TO CSV...", os.path.abspath(CSV_FILEPATH))

    service = SpotifyService()

    playlist_name = input("Please enter a playlist name (default: 'Your Top Songs 2019'): ")
    if playlist_name == "":
        playlist_name = "Your Top Songs 2019"

    playlist = service.get_playlist(playlist_name)
    if playlist:

        breakpoint()
        tracks = service.get_bookmarked_songs()
        #data = [to_dict(bookmark) for bookmark in bookmarks]
        #data = sorted(data, key=bookmark_sort)

        #df = pandas.DataFrame(data)
        #df.index.rename("id", inplace=True) # assigns a column label "id" for the index column
        #df.index += 1 # starts ids at 1 instead of 0
        #print(df.head())
        #df.to_csv(CSV_FILEPATH)
    else:
        print("OOPS, try another")
