
import os
from pprint import pprint

from dotenv import load_dotenv
import pydora
import pandora.clientbuilder as cb

load_dotenv()

PANDORA_USERNAME = os.environ.get("PANDORA_USERNAME", "OOPS")
PANDORA_PASSWORD = os.environ.get("PANDORA_PASSWORD", "OOPS")

CLIENT_SETTINGS = {
    "DECRYPTION_KEY": "R=U!LH$O2B#",
    "ENCRYPTION_KEY": "6#26FRL$ZWD",
    "PARTNER_USER": "android",
    "PARTNER_PASSWORD": "AC7IBG09A3DTSYM4R41UJWL07VLN8JI7",
    "DEVICE": "android-generic"
} # FYI: these are generic public device settings (not personal or private), see: https://6xq.net/pandora-apidoc/json/partners/#partners

class PandoraService():
    """Uses the unofficial Pandora API to act on behalf of the authenticated user."""

    def __init__(self, login=True):
        self.client = cb.SettingsDictBuilder(CLIENT_SETTINGS).build()
        if login:
            self.client.login(PANDORA_USERNAME, PANDORA_PASSWORD)

    def get_bookmarked_songs(self):
        """Fetches the user's bookmarked songs."""
        response = self.client.get_bookmarks()
        return response.songs

if __name__ == "__main__":

    service = PandoraService()

    songs = service.get_bookmarked_songs()
    #print(f"MY BOOKMARKED SONGS {len(songs)}:")
    for song in songs:
        song_info = {
            "bookmarked_on": song.date_created.strftime("%Y-%m-%d"),
            "artist": song.artist_name,
            "title": song.song_name,
            #"album": song.album_name
        }
        print(song_info)
