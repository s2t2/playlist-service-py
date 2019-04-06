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

## Usage

Retrieve a list of bookmarks from Pandora:

```sh
python app/pandora_service.py
```

## Testing

Install the `pytest` package (first time only):

```sh
pip install pytest
```

Run tests:

```sh
pytest
```
