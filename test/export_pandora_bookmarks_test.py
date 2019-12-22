#import datetime
#from pandora.models.bookmark import Bookmark
#
#from app.pandora_service import PandoraService
#
#def test_bookmark_to_dict():
#    #Bookmark(
#    #    album_name='Nirvana',
#    #    art_url='http://mediaserver-cont-usc-mp1-1-v4v6.pandora.com/images/public/int/0/9/7/2/800042790_500W_500H.jpg',
#    #    artist_name='Sam Smith',
#    #    bookmark_token='430238419315403744',
#    #    date_created=datetime.datetime(2019, 12, 21, 5, 58, 35, 240000),
#    #    music_token='S2440851', sample_gain='-6.45',
#    #    sample_url='http://www.pandora.com/favorites/getSample.jsp?token=MY_TOKEN&allowExplicit=true',
#    #    song_name='Latch (Acoustic)'
#    #) #> __init__() got an unexpected keyword argument 'album_name'
#
#    service = PandoraService(login=False)
#    bookmark_attrs = {
#        "album_name": 'Nirvana',
#        "art_url": 'http://mediaserver-cont-usc-mp1-1-v4v6.pandora.com/images/public/int/0/9/7/2/800042790_500W_500H.jpg',
#        "artist_name": 'Sam Smith',
#        #"bookmark_token": 'MY_TOKEN',
#        "date_created": datetime.datetime(2019, 12, 21, 5, 58, 35, 240000),
#        #"music_token": 'S2440851',
#        #"sample_gain": '-6.45',
#        #"sample_url": 'http://www.pandora.com/favorites/getSample.jsp?token=MY_TOKEN&allowExplicit=true',
#        "song_name": 'Latch (Acoustic)'
#    }
#
#    breakpoint()
#    #mock_bookmark = bookmark = Bookmark()
#    bookmark = Bookmark.from_json(api_client=service.client, data=bookmark_attrs)
#
#    assert bookmark.album_name == "Nirvana"
#
