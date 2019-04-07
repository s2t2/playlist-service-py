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

Create a [Spotify Client application](https://developer.spotify.com/dashboard/applications/), and note its credentials, then store them in environment variables called `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET`, respectively.


## Usage

List bookmarked songs on Pandora:

```sh
python app/pandora_service.py
```

List songs in the "Pandora Bookmarks" playlist on Spotify:

```sh
python app/spotify_service.py
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
