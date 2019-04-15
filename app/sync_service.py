
from spotify_service import find_or_create_playlist
from pandora_service import get_bookmarks

if __name__ == "__main__":

    playlist = find_or_create_playlist() # TODO: consider getting all playlists and asking the user to choose one
    print("PLAYLIST: ", playlist["id"], playlist["name"])

    songs = get_bookmarks()
    print(f"BOOKMARKS ({len(songs)}):")
    for song in songs:
        print({
            "bookmarked_on": song.date_created.strftime("%Y-%m-%d"),
            "artist": song.artist_name,
            "title": song.song_name,
            #"album": song.album_name
        })

        #if song.song_name not in playlist_song_names:
        #    parsed_response = add_tracks(playlist_id, track_uris)
        #    print("ADDED TRACKS, SNAPSHOT:", parsed_response["snapshot_id"])
