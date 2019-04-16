
from app.spotify_service import client_auth

from flask import Blueprint, request, render_template, redirect

auth_routes = Blueprint("auth_routes", __name__)

@auth_routes.route("/")
def index():
    print("INDEX PAGE")
    return "You have visited the homepage. Try visiting /auth/spotify/login"

# GET /auth/spotify/login
@auth_routes.route("/auth/spotify/login")
def spotify_login():
    print("SPOTIFY LOGIN...")
    auth_url = client_auth().get_authorize_url() #> 'https://accounts.spotify.com/authorize?client_id=_____&response_type=code&redirect_uri=________&scope=playlist-modify-private+playlist-read-private'
    return redirect(auth_url)

# GET /auth/spotify/callback
# GET /auth/spotify/callback?code=xyz123
@auth_routes.route("/auth/spotify/callback")
def spotify_callback(code=None):
    print("SPOTIFY CALLBACK")
    print("REQUEST PARAMS:", dict(request.args))

    if "code" in request.args:
        code = request.args["code"]
        message = f"CODE: {code}"
    else:
        message = "OOPS, UNABLE TO GET CODE"

    #print(message)
    #token_info = client_auth.get_access_token(code)
    #token = token_info["access_token"]
    #print("ACCESS TOKEN:", token)

    return message
