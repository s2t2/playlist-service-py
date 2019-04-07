
import pydora
import pandora # PREREQUISITE: import pydora

from app.pandora_service import CLIENT_SETTINGS, authenticated_client

# so yes these tests are going to make real live requests
# which is generally something we should avoid
# but at this time this repo is more for instructional purposes
# so this is a reasonable thing students might do
# and I remember doing it as a junior developer
# so its ok.
# here we go...
# oh, in order for these to work on the CI server, its environment variables need configuring
# which is something else we should avoid
# so TODO: look up simple / student-learnable mocking examples
# here we go...
#

def test_client_settings():
    assert CLIENT_SETTINGS == {
        "DECRYPTION_KEY": "R=U!LH$O2B#",
        "ENCRYPTION_KEY": "6#26FRL$ZWD",
        "PARTNER_USER": "android",
        "PARTNER_PASSWORD": "AC7IBG09A3DTSYM4R41UJWL07VLN8JI7",
        "DEVICE": "android-generic"
    } # FYI: these are generic public device settings (not personal or private), see: https://6xq.net/pandora-apidoc/json/partners/#partners)

def test_client():
    client = authenticated_client()
    assert isinstance(client, pandora.client.APIClient)
