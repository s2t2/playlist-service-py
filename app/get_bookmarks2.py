# https://github.com/mcrute/pydora
# https://github.com/mcrute/pydora/blob/master/tests/test_pandora/test_clientbuilder.py
# https://6xq.net/pandora-apidoc/json/partners/#partners
# https://github.com/mcrute/pydora/blob/f6d1613deb7ec23d38b3d7d2c20b065f3457c8b8/pandora/clientbuilder.py#L77-L114
# https://github.com/mcrute/pydora/blob/f6d1613deb7ec23d38b3d7d2c20b065f3457c8b8/pandora/transport.py#L27

import pydora.pandora.clientbuilder as cb

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
client = cb.SettingsDictBuilder(settings).build()

breakpoint()

client.login("username", "password")
#client.login(PANDORA_USERNAME, PANDORA_PASSWORD)
