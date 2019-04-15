# Contributor's Guide

## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

## Installation

Install application from [GitHub source](https://github.com/s2t2/playlist-service-py), and navigate there from the command-line:

```sh
git clone git@github.com:s2t2/playlist-service-py.git # or use HTTPS address
cd playlist-service-py
```

Create a virtual environment called "playlist-env" and activate it:

```sh
conda create -n playlist-env
conda activate playlist-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Setup

Follow the instructions below to obtain credentials and configure environment variables. See also the [example .env file](/.example.env).

### Pandora Credentials

Obtain your Pandora username and password, and store them in environment variables  called `PANDORA_USERNAME` and `PANDORA_PASSWORD`, respectively.

### Spotify Credentials

Set an environment variable called `SPOTIFY_USERNAME` to denote your Spotify username.

Create a [Spotify Client application](https://developer.spotify.com/dashboard/applications/), then store its configuration information in environment variables `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and `SPOTIPY_REDIRECT_URL`.

The first time you use the app via the command line, it will prompt you to login, and will store a resulting credentials file called `.cache-SPOTIFY_USERNAME` to the root directory of the repo. Subsequent requests will look for the credentials file at this location to prevent additional user logins.

## Usage

List Pandora bookmarks:

```sh
python app/pandora_service.py
```

List songs in the corresponding Spotify playlist:

```sh
python app/spotify_service.py
```

Add all Pandora bookmarks to the corresponding Spotify playlist:

```sh
python app/sync_service.py
```

## Testing

Install the `pytest` package (first time only):

```sh
pip install pytest
```

Run tests:

```sh
pytest --disable-pytest-warnings
```
