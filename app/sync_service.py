
from pandora_service import get_bookmarks
from spotify_service import find_or_create_playlist, song_search, add_tracks

if __name__ == "__main__":

    # RESET PLAYLIST

    playlist = find_or_create_playlist() # TODO: destroy_and_create_playlist()
    print("--------------------------------")
    print("PLAYLIST: ", playlist["id"], playlist["name"])

    playlist_id = playlist["id"]

    # LIST BOOKMARKED SONGS

    songs = get_bookmarks()
    print("--------------------------------")
    print(f"BOOKMARKS ({len(songs)}):")
    for song in songs[0:2]:

        # SEARCH FOR MATCHING SONG

        search_term = f"{song.song_name} {song.artist_name}"
        print("--------------")
        print(f"SONG SEARCH TERM: {search_term}")

        tracks = song_search(search_term)
        print(f"SEARCH RESULTS ({len(tracks)}):")
        for track in tracks:
            print(f"  + {track['uri']} '{track['name']}' by {track['artists'][0]['name']}")

        track = tracks[0] # consider allowing user to select
        print("SELECTED TRACK:", track["uri"])

        track_ids = [track["uri"]]

        # ADD SONG TO PLAYLIST

        parsed_response = add_tracks(playlist_id, track_ids)
        print("ADDED TRACK, SNAPSHOT:", parsed_response["snapshot_id"])
