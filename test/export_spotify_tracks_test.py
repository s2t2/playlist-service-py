

from app.exports.spotify.tracks import row_sort, to_row

playlist_attrs = {
    'collaborative': False,
    'description': 'The songs you loved most this year, all wrapped up.',
    'external_urls': {'spotify': 'https://open.spotify.com/playlist/PLAYLIST_ID'},
    'href': 'https://api.spotify.com/v1/playlists/PLAYLIST_ID',
    'id': 'PLAYLIST_ID',
    'images': [{
        'height': None,
        'url': 'https://lineup-images.scdn.co/your-top-songs-2019_DEFAULT-en.jpg',
        'width': None
    }],
    'name': 'Your Top Songs 2019',
    'owner': {
        'display_name': 'Spotify',
        'external_urls': {'spotify': 'https://open.spotify.com/user/spotify'},
        'href': 'https://api.spotify.com/v1/users/spotify',
        'id': 'spotify',
        'type': 'user',
        'uri': 'spotify:user:spotify'
    },
    'primary_color': None,
    'public': False,
    'snapshot_id': 'SNAPSHOT_ID==',
    'tracks': {
        'href': 'https://api.spotify.com/v1/playlists/PLAYLIST_ID/tracks',
        'total': 100
    },
    'type': 'playlist',
    'uri': 'spotify:playlist:PLAYLIST_ID'
}

track_attrs = {
    'added_at': '2019-12-12T19:57:17Z',
    'added_by': {
        'external_urls': {'spotify': 'https://open.spotify.com/user/'},
        'href': 'https://api.spotify.com/v1/users/',
        'id': '',
        'type': 'user',
        'uri': 'spotify:user:'
    },
    'is_local': False,
    'primary_color': None,
    'track': {
        'album': {
            'album_type': 'single',
            'artists': [{
                'external_urls': {'spotify': 'https://open.spotify.com/artist/7eBDae8nEzoq5GThrBTpRP'},
                'href': 'https://api.spotify.com/v1/artists/7eBDae8nEzoq5GThrBTpRP',
                'id': '7eBDae8nEzoq5GThrBTpRP',
                'name': 'MTNS',
                'type': 'artist',
                'uri': 'spotify:artist:7eBDae8nEzoq5GThrBTpRP'
            }],
            'available_markets': [],
            'external_urls': {'spotify': 'https://open.spotify.com/album/7FEnMscWH7GGd69UYx65iu'},
            'href': 'https://api.spotify.com/v1/albums/7FEnMscWH7GGd69UYx65iu',
            'id': '7FEnMscWH7GGd69UYx65iu',
            'images': [
                {'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b27345447e1fa9626283b24a6703', 'width': 640},
                {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e0245447e1fa9626283b24a6703', 'width': 300},
                {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d0000485145447e1fa9626283b24a6703', 'width': 64}],
            'name': 'Salvage',
            'release_date': '2013-11-22',
            'release_date_precision': 'day',
            'total_tracks': 5,
            'type': 'album',
            'uri': 'spotify:album:7FEnMscWH7GGd69UYx65iu'
        },
        'artists': [{
            'external_urls': {'spotify': 'https://open.spotify.com/artist/7eBDae8nEzoq5GThrBTpRP'},
            'href': 'https://api.spotify.com/v1/artists/7eBDae8nEzoq5GThrBTpRP',
            'id': '7eBDae8nEzoq5GThrBTpRP',
            'name': 'MTNS',
            'type': 'artist',
            'uri': 'spotify:artist:7eBDae8nEzoq5GThrBTpRP'
        }],
        'available_markets': [],
        'disc_number': 1,
        'duration_ms': 257669,
        'episode': False,
        'explicit': False,
        'external_ids': {'isrc': 'AU5Q11300057'},
        'external_urls': {'spotify': 'https://open.spotify.com/track/7kFljFrvjmu5WhhVUE2H3x'},
        'href': 'https://api.spotify.com/v1/tracks/7kFljFrvjmu5WhhVUE2H3x',
        'id': '7kFljFrvjmu5WhhVUE2H3x',
        'is_local': False,
        'name': 'Fears',
        'popularity': 34,
        'preview_url': None,
        'track': True,
        'track_number': 2,
        'type': 'track',
        'uri': 'spotify:track:7kFljFrvjmu5WhhVUE2H3x'
    },
    'video_thumbnail': {'url': None}
}

def test_to_row():
    row = to_row(track_attrs)
    assert row["album_id"] == "7FEnMscWH7GGd69UYx65iu"
    assert row["album_name"] == "Salvage"
    assert row["album_release_date"] == "2013-11-22"
    assert row["album_art"] == "https://i.scdn.co/image/ab67616d0000b27345447e1fa9626283b24a6703"
    assert row["artist_id"] == "7eBDae8nEzoq5GThrBTpRP"
    assert row["artist_name"] == "MTNS"
    assert row["duration_ms"] == 257669
    assert row["explicit"] == False
    assert row["isrc_id"] == "AU5Q11300057"
    assert row["id"] == "7kFljFrvjmu5WhhVUE2H3x"
    assert row["name"] == "Fears"
    assert row["popularity"] == 34

def test_row_sort():
    assert row_sort(to_row(track_attrs)) == ["MTNS", "Salvage", "Fears"]
