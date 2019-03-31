
import os
import time

import requests

BASE_URL = "https://tuner.pandora.com/services/json"
method = "user.getBookmarks"
auth_token = "TODO"
sync_time = int(round(time.time() * 1000)) #> 1554041027885
request_url = os.path.join(BASE_URL, f"?method={method}&userAuthToken={auth_token}&syncTime={sync_time}")
print("REQUEST URL:", request_url)

response = requests.get(request_url)

print(response.status_code) #> 200
print(response.text) #> '{"stat":"fail","message":"An unexpected error occurred","code":9}'

breakpoint()























# UNOFFICIAL PANDORA API DOCS
# https://6xq.net/pandora-apidoc/json/
# https://tuner.pandora.com/services/json
# https://internal-tuner.pandora.com/services/json
#> https://tuner.pandora.com/services/json/?method=user.getBookmarks
#> https://tuner.pandora.com/services/json/?method=auth.userLogin&partner_id=123

# User auth token if available, partner auth token or empty if neither is known yet.
# auth_token = "_____"

# Partner id obtained by Partner login or empty
# https://6xq.net/pandora-apidoc/json/authentication/#auth-partnerlogin
# partner_id = ""

# User id as obtained by User login or empty
# https://6xq.net/pandora-apidoc/json/authentication/#auth-userlogin
# user_id = ""

# string User auth token, see User login
# auth_token = "_______"

# int Synchonized time.
# Calculation: current time + (time of Partner login request – syncTime from Partner login response).
# This is a protection against replay-attacks.
# sync_time = 0
