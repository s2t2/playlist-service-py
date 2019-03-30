# System Planning and Requirements Document

## Problem Statement

As someone who listens to songs on multiple music services, I'd like a way to automate the process of updating a playlist on one service to reflect the feedback I provide to another service about what songs I have "liked" or "bookmarked". I currently perform this process manually, on an ad-hoc basis, and not as consistently as I'd like. This lack of consistency across platforms leads to a music listening experience that has room for improvement.

Automatically "synchronizing" my music preferences across services will provide me with a better listening experience overall, and will save me time it would have otherwise taken to manually update playlists across various music services.

### Current State Process

TODO











<hr>

## Proposed Solution

The proposed solution is called the "Playlist Sync Service" because it will seamlessly automate the process of updating the user's song playlists across multiple music services (i.e. [Pandora](https://www.pandora.com) and[Spotify]([Spotify](https://www.spotify.com))).

The solution will include application software written in the Python programming language.

### Future State Process

TODO

### System Objectives

The system's primary objective is to perform a one-directional sync of playlist information from the Pandora service to the Spotify service. By doing so, the system should provide value to the user in the form of **time savings** and **improved music listening experience**.

### User Interface Requirements

For now, the users will interface with the application through a **command-line interface (CLI)**. In the future, perhaps the scope will expand to allow users to also access the application through a GUI web interface.

## User Experience Requirements

Ultimately, the user should be able to continue to use the Pandora and Spotify music services as usual, without any additional interactions, interruptions, or disruptions.

After successful execution of the playlist synchronization, **the user should be able to see their Pandora "bookmarks" in a Spotify playlist called "Pandora Bookmarks", so they can continue listening to their favorite songs**.












































### Information Requirements

Data Flow Diagram:

![a sketch of a data flow diagram, depicting a system icon in the middle, with information flows from the Pandora service into the system, and information outflows from the system to Spotify service](/planning/dfd-sketch.jpg)

Information Inputs:

  + **Bookmarked Songs List** (a list of songs I've "bookmarked" on Pandora)

Information Outputs:

  + **Playlist Update Request** (a request to add bookmarked songs to a playlist on Spotify)

### Functionality Requirements

  1. Bookmark Retrieval Process
  2. Playlist Update Process

### Bookmark Retrieval Process

The system should get my bookmarked songs from Pandora.

### Playlist Update Process

The system should add bookmarked songs to a playlist on Spotify.

> NICE TO HAVE: The system should send me email with the results of its playlist update attempts. It should report on whether or not it was successful, and if successful it should say which songs it has added to the playlist.














### Technology Requirements

The application can be installed and run on a personal computer (i.e. in a "development" environment), or on an application server managed via the Heroku platform (i.e. in a "production" environment).

The computer should allow installation of Python version 3.7 and various third-party Python packages. The computer should also have an Internet connection to facilitate the programmatic communication HTTP access to the Pandora and Spotify APIs.

The source code will be installed or "deployed" onto a Heroku server. The server will be configured to execute the service at scheduled intervals.
