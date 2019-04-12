# Credits, Notes, and Reference

## Pandora

### Pandora API

  + https://6xq.net/pandora-apidoc/json
  + https://6xq.net/pandora-apidoc/json/partners/#partners

### The `pydora` Package

  + https://github.com/mcrute/pydora
  + https://github.com/mcrute/pydora/blob/master/pandora/client.py#L160-L164
  + https://github.com/mcrute/pydora/blob/master/pandora/clientbuilder.py#L77-L114
  + https://github.com/mcrute/pydora/blob/master/pandora/errors.py
  + https://github.com/mcrute/pydora/blob/master/pandora/models/pandora.py#L366-L369
  + https://github.com/mcrute/pydora/blob/master/pandora/models/__init__.py#L91-L177
  + https://github.com/mcrute/pydora/blob/master/pandora/transport.py#L27
  + https://github.com/mcrute/pydora/blob/master/tests/test_pandora/test_clientbuilder.py

FYI: to import the `pandora` module you may first have to import the `pydora` module.

## Spotify

### Spotify API

  + https://developer.spotify.com/documentation/web-api/
  + https://developer.spotify.com/console/post-playlist-tracks/
  + https://developer.spotify.com/documentation/web-api/reference/playlists/add-tracks-to-playlist/
  + https://developer.spotify.com/documentation/web-api/reference/playlists/get-a-list-of-current-users-playlists/

### The `spotipy` Package

  + https://github.com/plamere/spotipy
  + https://spotipy.readthedocs.io/en/latest/
  + https://github.com/s2t2/my-spotify-app-py/blob/master/list_songs.py
  + https://spotipy.readthedocs.io/en/latest/#client-credentials-flow
  + https://github.com/plamere/spotipy/blob/master/spotipy/client.py
  + https://github.com/plamere/spotipy/blob/master/spotipy/util.py

### Spotify Auth

  + https://developer.spotify.com/documentation/general/guides/authorization-guide/#authorization-flows
  + https://developer.spotify.com/documentation/general/guides/authorization-guide/#authorization-code-flow

"This flow is suitable for long-running applications in which the user grants permission only once. It provides an access token that can be refreshed. Since the token exchange involves sending your secret key, perform this on a secure location, like a backend service, and not from a client such as a browser or from a mobile app."

"Have your application request authorization (GET https://accounts.spotify.com/authorize)"

  + https://spotipy.readthedocs.io/en/latest/#authorization-code-flow
  + https://developer.spotify.com/documentation/general/guides/scopes/
  + https://developer.spotify.com/documentation/general/guides/scopes/#playlist-read-private
  + https://developer.spotify.com/documentation/general/guides/scopes/#playlist-modify-private
  + `SpotipyOauth`: https://github.com/plamere/spotipy/blob/master/spotipy/oauth2.py#L93-L264


One time method to get a token prompts user to login, then sends user to a redirect url and appends an auth code into the url params. The terminal asks for me to input the entire URL, and returns an access token.

This also seems to add a file called `.cache-USERNAME` to the root directory of the repo. it looks like this:

```json
{
    "access_token": "_____",
    "token_type": "Bearer",
    "expires_in": 3600,
    "refresh_token": "______",
    "scope": "playlist-read-private",
    "expires_at": 1554651631
}
```

Moving it to "credentials/spotify_user.json" in case we need it later. And gitignoring it. Obviously.

Here is the source of what's going on with that file, and how to customize its location:

  + https://github.com/plamere/spotipy/blob/master/spotipy/oauth2.py#L123-L130
  + https://github.com/plamere/spotipy/blob/master/spotipy/util.py#L9-L51

Looks like scope can be a list, see:

  + https://github.com/plamere/spotipy/blob/master/spotipy/oauth2.py#L225


## Pytest

  + https://stackoverflow.com/questions/38442897/how-do-i-disable-a-test-using-py-test

## Travis CI

  + https://docs.travis-ci.com/user/environment-variables/#default-environment-variables

## Python

Pretty Printing Reference:

```py
import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint("HELLO")
```
