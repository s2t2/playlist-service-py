
import os
import pprint
from dotenv import load_dotenv
import pydora # allows importing of the "pandora" sub-package
import pandora.clientbuilder as cb

load_dotenv()

PANDORA_USERNAME = os.environ.get("PANDORA_USERNAME", "OOPS")
PANDORA_PASSWORD = os.environ.get("PANDORA_PASSWORD", "OOPS")


if __name__ == "__main__":

    pp = pprint.PrettyPrinter(indent=4)

    client_settings = {
        "DECRYPTION_KEY": "R=U!LH$O2B#",
        "ENCRYPTION_KEY": "6#26FRL$ZWD",
        "PARTNER_USER": "android",
        "PARTNER_PASSWORD": "AC7IBG09A3DTSYM4R41UJWL07VLN8JI7",
        "DEVICE": "android-generic"
    } # FYI: these are generic public device settings (not personal or private), see: https://6xq.net/pandora-apidoc/json/partners/#partners)
    client = cb.SettingsDictBuilder(client_settings).build()
    print("---------------------------")
    print("CLIENT:", type(client)) #> <class 'pandora.client.APIClient'>
    pp.pprint(dir(client))

    print("---------------------------")
    print("LOGGING IN...")
    login_response = client.login(PANDORA_USERNAME, PANDORA_PASSWORD)
    pp.pprint(login_response)

    print("---------------------------")
    print("GETTING BOOKMARKS...")
    bookmarks_response = client.get_bookmarks()
    print(type(bookmarks_response))
    pp.pprint(dir(bookmarks_response))

    print(f"FOUND {len(bookmarks_response.songs)} BOOKMARKS:")
    for song in bookmarks_response.songs:
        song_info = {
            "title": song.song_name,
            "artist": song.artist_name,
            "album": song.album_name,
            "bookmarked_on": song.date_created.strftime("%Y-%m-%d")
        }
        pp.pprint(song_info)
