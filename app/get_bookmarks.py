
import os
import time
import requests

BASE_URL = "https://tuner.pandora.com/services/json"
#INT_BASE_URL = "https://internal-tuner.pandora.com/services/json"

def check_url():
    return f"{BASE_URL}/?method=test.checkLicensing"

def partner_login_url():
    # https://6xq.net/pandora-apidoc/json/authentication/#partner-login
    # https://6xq.net/pandora-apidoc/json/partners/#partners
    # decrypt_pw = "R=U!LH$O2B#"
    # encrypt_pw = "6#26FRL$ZWD"
    # device_id = "android-generic"
    username = "android"
    password = "AC7IBG09A3DTSYM4R41UJWL07VLN8JI7"
    device_model = "android-generic"
    version = "5"
    url = f"{BASE_URL}/?method=auth.partnerLogin"
    url += f"&username={username}"
    url += f"&password={password}"
    url += f"&deviceModel={device_model}"
    url += f"&version={version}"
    return url

def partner_login():
    # https://6xq.net/pandora-apidoc/json/authentication/#partner-login
    # https://6xq.net/pandora-apidoc/json/partners/#partners
    request_url = f"{BASE_URL}/?method=auth.partnerLogin"
    body = {
        "username": "pandora one",
        "password": "TVCKIBGS9AO9TSYLNNFUML0743LH82D",
        "deviceModel": "D01",
        "version": "5"
    }
    response = requests.post(request_url, data=body)
    return response

def user_login_url():
    partner_id = 123 # TODO
    url = f"{BASE_URL}/?method=auth.userLogin"
    url += f"&partner_id={partner_id}"
    return url

def bookmarks_url():
    url = f"{BASE_URL}/?method=user.getBookmarks"

    partner_id = "ABC" # TODO: https://6xq.net/pandora-apidoc/json/authentication/#auth-partnerlogin
    url += f"&partner_id={partner_id}"

    auth_token = "TODO" # TODO: https://6xq.net/pandora-apidoc/json/authentication/#auth-userlogin
    url += f"&userAuthToken={auth_token}"

    current_time = int(round(time.time() * 1000))
    diff = 0 # TODO: (time of Partner login request – syncTime from Partner login response)
    sync_time = current_time + diff
    url += f"&syncTime={sync_time}"

    return url

if __name__ == "__main__":

    response = partner_login()
    print("STATUS:", response.status_code) #> 200
    print("BODY:", response.text) #> '{"stat":"fail","message":"An unexpected error occurred","code":9}'

    #breakpoint()
