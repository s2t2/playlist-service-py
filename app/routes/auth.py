from flask import Blueprint, request, render_template

auth_routes = Blueprint("auth_routes", __name__)

@auth_routes.route("/")
def index():
    print("VISITING THE INDEX PAGE")
    return "You have visited the homepage"
    #return render_template("index.html")

# GET /auth/spotify/callback
# GET /auth/spotify/callback?code=xyz123
@auth_routes.route("/auth/spotify/callback")
def hello(code=None):
    print("CALLBACK")
    print("REQUEST PARAMS:", dict(request.args))

    if "code" in request.args:
        code = request.args["code"]
        message = f"AUTH CODE: {code}"
    else:
        message = "OOPS, UNABLE TO GET AUTH CODE"

    return message
