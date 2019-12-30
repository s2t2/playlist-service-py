
from pprint import pprint
import os
import pandas

from app import EXPORTS_DIR
from app.spotify_service import SpotifyService

CSV_FILEPATH = os.path.join(EXPORTS_DIR, "spotify", "tracks.csv")

def to_row(result):
    track = result["track"]
    album = track["album"]
    artist = track["artists"][0] # there can be many artists per track

    return {
        "album_id": album["id"],
        "album_name": album["name"],
        "album_release_date": album["release_date"],
        "album_art": album["images"][0]["url"],
        "artist_id": artist["id"],
        "artist_name": artist["name"],
        "duration_ms": track["duration_ms"],
        "explicit": track["explicit"],
        "isrc_id": track["external_ids"]["isrc"],
        "id": track["id"],
        "name": track["name"],
        "popularity": track["popularity"]
    }

def row_sort(row):
    return [row["artist_name"], row["album_name"], row["name"]]

if __name__ == "__main__":


    service = SpotifyService()

    #tracks = service.client.current_user_saved_tracks()
    ##> *** spotipy.client.SpotifyException: http status: 403, code:-1 - https://api.spotify.com/v1/me/tracks?limit=20&offset=0:
    ##> Insufficient client scope

    service.get_playlists()

    if input("List playlists? (Y/N, default=N): ").upper() == "Y":
        print("USER PLAYLISTS:")
        pprint([p["name"] for p in service.playlists])

    default_playlist_name = "Your Top Songs 2019"
    playlist_name = input(f"Please enter a playlist name (default: '{default_playlist_name}'): ") \
        or default_playlist_name # handles empty strings ... ("" or "hello") --> "hello"

    playlist = service.get_playlist(playlist_name)

    if playlist:
        tracks = service.get_tracks(user_id=playlist["owner"]["id"], playlist_id=playlist["id"])
        print("TRACKS", len(tracks))

        data = [to_row(track) for track in tracks]
        data = sorted(data, key=row_sort)

        df = pandas.DataFrame(data)
        df.index.rename("id", inplace=True) # assigns a column label "id" for the index column
        df.index += 1 # starts ids at 1 instead of 0
        print("EXPORTING SPOTIFY TRACKS TO CSV...", os.path.abspath(CSV_FILEPATH))
        print(df.head())
        df.to_csv(CSV_FILEPATH)
    else:
        print("OOPS, Please try a different playlist name.")
