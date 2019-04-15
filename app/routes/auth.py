#import os
#from dotenv import load_dotenv
import spotipy
#from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import spotipy.util as util
#load_dotenv()
from app.spotify_service import USERNAME, AUTH_SCOPE





from flask import Blueprint, request, render_template

auth_routes = Blueprint("auth_routes", __name__)

@auth_routes.route("/")
def index():
    print("VISITING THE INDEX PAGE")
    return "You have visited the homepage"
    #return render_template("index.html")

@auth_routes.route("/auth/spotify/login")
def spotify_login():
    print("LOGGING IN TO SPOTIFY...")
    token = util.prompt_for_user_token(USERNAME, AUTH_SCOPE)
    return f"THE TOKEN IS: {token}"
    #return render_template("index.html")

# GET /auth/spotify/callback
# GET /auth/spotify/callback?code=xyz123
@auth_routes.route("/auth/spotify/callback")
def spotify_callback(code=None):
    print("CALLBACK")
    print("REQUEST PARAMS:", dict(request.args))

    if "code" in request.args:
        code = request.args["code"]
        message = f"AUTH CODE: {code}"
    else:
        message = "OOPS, UNABLE TO GET AUTH CODE"

    return message
