# System Planning and Requirements Document

## Problem Statement

As someone who listens to songs on multiple music services, I'd like a way to automate the process of updating a playlist on one service to reflect the feedback I provide to another service about what songs I have "liked" or "bookmarked". I currently perform this process manually, on an ad-hoc basis, and not as consistently as I'd like. This lack of consistency across platforms leads to a music listening experience that has room for improvement.



### Current State Process

TODO











<hr>

## Proposed Solution

The proposed solution is called the "Playlist Sync Service" because it will seamlessly automate the process of updating the user's song playlists across multiple music services (i.e. [Pandora](https://www.pandora.com) and [Spotify](https://www.spotify.com)).

### Hypothesis

Automatically "synchronizing" the user's music preferences across services will provide the user with a better listening experience overall, and will save the user time it would have otherwise taken to manually update playlists on each of the various services.

### System Objectives

The system's primary objective is to perform a one-directional sync of playlist information from the Pandora service to the Spotify service. By doing so, the system should provide value to the user in the form of time savings and improved music listening experience.

### User Experience Requirements

Ultimately, the user should be able to continue to use the Pandora and Spotify music services as usual, without any additional interactions, interruptions, or disruptions.

Additionally, the user should see a Spotify playlist which contains all songs recently bookmarked on Pandora. Existence of this playlist and accuracy of its song contents will lead to an improved listening experience.

### Information Requirements

Data Flow Diagram:

![a sketch of a data flow diagram, depicting a system icon in the middle, with information flows from the Pandora service into the system, and information outflows from the system to Spotify service](/planning/dfd-sketch.jpg)

Information Inputs:

  + Bookmarked Songs List (a list of songs I've "bookmarked" on Pandora)

Information Outputs:

  + Playlist Update Request (a request to add songs to a Spotify playlist)

### Functionality Requirements (Features)

  1. Bookmark Retrieval
  2. Playlist Updating

#### Bookmark Retrieval

The user should be able to continue to "bookmark" their favorite songs in Pandora, as usual, without interruption.

On a scheduled or ad-hoc basis, the system should automatically get a list of the user's bookmarked songs from Pandora.

#### Playlist Updating

The system should automatically add a user's Pandora bookmarks to a Spotify playlist called "Pandora Bookmarks".

> NICE TO HAVE: The system should send me email with the results of its playlist update attempts. It should report on whether or not it was successful, and if successful it should say which songs it has added to the playlist.

The user should be able to see their favorite songs in the designated Spotify playlist so they can continue listening.

### User Interface Requirements

For now, users will interface with the application through a command-line interface (CLI).

In the future, perhaps the scope will expand to allow users to also access the application through a GUI web interface.

### Technology Requirements

The application can be installed and run on a personal computer (i.e. "development" environment), or a Heroku application server (i.e. "production" environment).

Regardless of the operating environment, the computer should allow installation of Python 3.7 and various third-party Python packages. The computer should also have an Internet connection to facilitate the programmatic communication HTTP access to the Pandora and Spotify APIs.

The production environment should have scheduling capabilities to execute Python scripts at specified intervals.
