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
