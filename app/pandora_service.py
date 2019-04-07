
import os
from dotenv import load_dotenv
import pydora
import pandora.clientbuilder as cb # PREREQUISITE: import pydora

load_dotenv()

PANDORA_USERNAME = os.environ.get("PANDORA_USERNAME", "OOPS")
PANDORA_PASSWORD = os.environ.get("PANDORA_PASSWORD", "OOPS")
CLIENT_SETTINGS = {
    "DECRYPTION_KEY": "R=U!LH$O2B#",
    "ENCRYPTION_KEY": "6#26FRL$ZWD",
    "PARTNER_USER": "android",
    "PARTNER_PASSWORD": "AC7IBG09A3DTSYM4R41UJWL07VLN8JI7",
    "DEVICE": "android-generic"
} # FYI: these are generic public device settings (not personal or private), see: https://6xq.net/pandora-apidoc/json/partners/#partners)

def authenticated_client():
    client = cb.SettingsDictBuilder(CLIENT_SETTINGS).build()
    login_response = client.login(PANDORA_USERNAME, PANDORA_PASSWORD)
    return client

if __name__ == "__main__":

    print("---------------------------")
    print("GETTING BOOKMARKS...")

    client = authenticated_client()

    bookmarks_response = client.get_bookmarks()
    print(type(bookmarks_response))

    print(f"FOUND {len(bookmarks_response.songs)} BOOKMARKS:")
    for song in bookmarks_response.songs:
        song_info = {
            "bookmarked_on": song.date_created.strftime("%Y-%m-%d"),
            "artist": song.artist_name,
            "title": song.song_name,
            "album": song.album_name
        }
        print(song_info)
