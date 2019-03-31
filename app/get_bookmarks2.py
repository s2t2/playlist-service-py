# https://github.com/mcrute/pydora
# https://github.com/mcrute/pydora/blob/master/tests/test_pandora/test_clientbuilder.py
# https://6xq.net/pandora-apidoc/json/partners/#partners
# https://github.com/mcrute/pydora/blob/f6d1613deb7ec23d38b3d7d2c20b065f3457c8b8/pandora/clientbuilder.py#L77-L114
# https://github.com/mcrute/pydora/blob/f6d1613deb7ec23d38b3d7d2c20b065f3457c8b8/pandora/transport.py#L27
# https://github.com/mcrute/pydora/blob/f6d1613deb7ec23d38b3d7d2c20b065f3457c8b8/pandora/errors.py

import os
import pprint

from dotenv import load_dotenv
import pydora # source of "pandora" sub-package
#from pandora.client import APIClient
import pandora.clientbuilder as cb

pp = pprint.PrettyPrinter(indent=4)

load_dotenv()

PANDORA_USERNAME = os.environ.get("PANDORA_USERNAME", "OOPS")
PANDORA_PASSWORD = os.environ.get("PANDORA_PASSWORD", "OOPS")

client_settings = {
    # tuner.pandora.com
    "android": {
        "DECRYPTION_KEY": "R=U!LH$O2B#",
        "ENCRYPTION_KEY": "6#26FRL$ZWD",
        "PARTNER_USER": "android",
        "PARTNER_PASSWORD": "AC7IBG09A3DTSYM4R41UJWL07VLN8JI7",
        "DEVICE": "android-generic"
    },
    "ios": {
        "DECRYPTION_KEY": "20zE1E47BE57$51",
        "ENCRYPTION_KEY": "721^26xE22776",
        "PARTNER_USER": "iphone",
        "PARTNER_PASSWORD": "P2E4FC0EAD3*878N92B2CDp34I0B1@388137C",
        "DEVICE": "IP01"
    },
    # internal-tuner.pandora.com
    "desktop": {
        "DECRYPTION_KEY": "U#IO$RZPAB%VX2",
        "ENCRYPTION_KEY": "2%3WCL*JU$MP]4",
        "PARTNER_USER": "pandora one",
        "PARTNER_PASSWORD": "TVCKIBGS9AO9TSYLNNFUML0743LH82D",
        "DEVICE": "D01",
    }
}

settings = client_settings["android"]

client = cb.SettingsDictBuilder(settings).build() #> <class 'pandora.client.APIClient'>
# pp.pprint(dir(client))

breakpoint()

#client.login("username", "password") #> invalid partner login
client.login(PANDORA_USERNAME, PANDORA_PASSWORD)
#> {
#   'hasAudioAds': False,
#   'isCapped': False,
#   'username': '______',
#   'canListen': True,
#   'subscriptionHasExpired': False,
#   'userId': '1234567',
#   'listeningTimeoutMinutes': '1440',
#   'zeroVolumeNumMutedTracks': 1,
#   'zeroVolumeAutoPauseEnabledFlag': True,
#   'maxStationsAllowed': 250,
#   'listeningTimeoutAlertMsgUri': '/mobile/still_listening.vm',
#   'userProfileUrl': 'https://www.pandora.com/login?auth_token=ABC123&target=DEF456',
#   'userAuthToken': '____________'
# }

response = client.get_bookmarks()
print(type(response)) #> <class 'pandora.models.pandora.BookmarkList'>
print(type(response.songs)) #> <class 'list'>

len(response.songs) #> 83
