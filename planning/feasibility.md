# Feasibility Analysis

## Spotify Integration

### Spotify API

They have an API. I've used it before.

  + https://developer.spotify.com/documentation/web-api/
  + https://developer.spotify.com/console/post-playlist-tracks/
  + https://developer.spotify.com/documentation/web-api/reference/playlists/add-tracks-to-playlist/

### Spotify Python Packages

There is a good package called `spotipy` that I've briefly used before.

  + https://github.com/plamere/spotipy
  + https://spotipy.readthedocs.io/en/latest/
  + https://github.com/s2t2/my-spotify-app-py/blob/master/list_songs.py

## Pandora Integration

### Pandora API

Wait Pandora doesn't have an API? But there seems to be some "unofficial" API documentation:

  + https://6xq.net/pandora-apidoc/json/
  + https://6xq.net/pandora-apidoc/rest/
  + https://6xq.net/pandora-apidoc/rest/authentication/
  + https://6xq.net/pandora-apidoc/json/bookmarks/#retrieve-bookmarks
  + https://6xq.net/pandora-apidoc/json/implementations/
  + https://6xq.net/pandora-apidoc/json/methods/
  + https://6xq.net/pandora-apidoc/json/errorcodes/

Is this credible? It seems to want username and password auth, which is not ideal. I wonder if there is another way to obtain an access token? I read not all requests use HTTPS? This might be a security concern and requires further investigation...

### Pandora Python Packages

Not sure about these packages:

  + https://github.com/mcrute/pydora (seems like more of a client app)
  + https://github.com/rectalogic/mopidy-pandora (seems to be part of a client app)
  + https://github.com/pithos/pithos (seems to be part of a client app)

Might have to use the `requests` package to directly issue requests to the unofficial API.

  + http://docs.python-requests.org/en/master/user/quickstart/
  + https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/requests.md

Looking at parts of pydora again:

  + https://github.com/mcrute/pydora/blob/9e49c086a86deff4ae85d802e9d57278f1ac4636/pandora/client.py#L160-L164
  + https://github.com/mcrute/pydora/blob/9e49c086a86deff4ae85d802e9d57278f1ac4636/pandora/models/pandora.py#L366-L369
  + https://github.com/mcrute/pydora/blob/f6d1613deb7ec23d38b3d7d2c20b065f3457c8b8/pandora/models/__init__.py#L91-L177

[Attempt using requests package](/app/get_bookmarks.py) not successful after a few tries.

[Attempt using pydora package](/app/get_bookmarks2.py) was successful after a few tries!

Helpful pydora source code:

  + https://github.com/mcrute/pydora
  + https://github.com/mcrute/pydora/blob/master/tests/test_pandora/test_clientbuilder.py
  + https://6xq.net/pandora-apidoc/json/partners/#partners
  + https://github.com/mcrute/pydora/blob/f6d1613deb7ec23d38b3d7d2c20b065f3457c8b8/pandora/clientbuilder.py#L77-L114
  + https://github.com/mcrute/pydora/blob/f6d1613deb7ec23d38b3d7d2c20b065f3457c8b8/pandora/transport.py#L27
  + https://github.com/mcrute/pydora/blob/f6d1613deb7ec23d38b3d7d2c20b065f3457c8b8/pandora/errors.py
