
from app.pandora_service import PandoraService

if __name__ == "__main__":

    service = PandoraService()
     print(type(service))

    songs = service.get_bookmarked_songs()
    print(f"MY BOOKMARKED SONGS {len(songs)}:")
    for song in songs:
        song_info = {
            "bookmarked_on": song.date_created.strftime("%Y-%m-%d"),
            "artist": song.artist_name,
            "title": song.song_name,
            #"album": song.album_name
        }
        print(song_info)
