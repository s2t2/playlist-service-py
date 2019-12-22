
from app.pandora_service import PandoraService
from app.spotify_service import SpotifyService

if __name__ == "__main__":

    spotify_service = SpotifyService()

    # RESET PLAYLIST

    playlist = spotify_service.find_or_create_playlist() # TODO: destroy_and_create_playlist()
    print("--------------------------------")
    print("PLAYLIST: ", playlist["id"], playlist["name"])

    playlist_id = playlist["id"]

    # LIST BOOKMARKED SONGS

    pandora_service = PandoraService()

    songs = pandora_service.get_bookmarked_songs()
    print("--------------------------------")
    print(f"BOOKMARKS ({len(songs)}):")
    for song in songs:

        # SEARCH FOR MATCHING SONG

        search_term = f"{song.song_name} {song.artist_name}"
        print("--------------------------------")
        print(f"SONG SEARCH TERM: '{search_term}'")

        tracks = spotify_service.song_search(search_term)
        print(f"SEARCH RESULTS ({len(tracks)}):")

        for track in tracks:
            print(f"  + {track['uri']} '{track['name']}' by {track['artists'][0]['name']}")

        try:
            track = tracks[0] # consider allowing user to select
            print("SELECTED:", track["uri"])

            track_ids = [track["uri"]]

            # ADD SONG TO PLAYLIST

            parsed_response = spotify_service.add_tracks(playlist_id, track_ids)
            print(f"ADDED! SNAPSHOT:", parsed_response["snapshot_id"])

        except IndexError as e:
            print("N/A - NONE FOUND")
