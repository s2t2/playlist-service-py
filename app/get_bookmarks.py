
import os
import time
import requests

BASE_URL = "https://tuner.pandora.com/services/json"

def bookmarks_url():
    method = "user.getBookmarks"
    request_url = os.path.join(BASE_URL, f"?method={method}")

    partner_id = "ABC" # TODO: https://6xq.net/pandora-apidoc/json/authentication/#auth-partnerlogin
    request_url += f"&partner_id={partner_id}"

    auth_token = "TODO" # TODO: https://6xq.net/pandora-apidoc/json/authentication/#auth-userlogin
    request_url += f"&userAuthToken={auth_token}"

    current_time = int(round(time.time() * 1000))
    diff = 0 # TODO: (time of Partner login request – syncTime from Partner login response)
    sync_time = current_time + diff
    request_url += f"&syncTime={sync_time}"

    return request_url

request_url = bookmarks_url()

print("REQUEST URL:", request_url)

response = requests.get(request_url)

print("STATUS:", response.status_code) #> 200
print("BODY:", response.text) #> '{"stat":"fail","message":"An unexpected error occurred","code":9}'

#breakpoint()
