# -*- coding: utf-8 -*-
from shiva.media import MediaDir, MimeType

SERVER_URI = ''
SECRET_KEY = 'senior design project 342635778331321'  # Set this to something secret.
MEDIA_DIRS = (
        MediaDir(root='.', dirs=('/media',), url='http://xstream.azurewebsites.net'),
    # Examples.
    # MediaDir(root='/srv/http', dirs=('/music',), url='http://127.0.0.1/'),
    # MediaDir('/home/fatmike/music/shiva'),
    # If in doubt, read the source.
)
# Add your own mimetypes here.
# MIMETYPES = (
#     MimeType(type='audio', subtype='mp3', extension='mp3',
#              acodec='libmp3lame'),
#     MimeType(type='audio', subtype='ogg', extension='ogg',
#              acodec='libvorbis'),
# )
LASTFM_API_KEY = ''
SCRAPERS = {
    'lyrics': (
        'azlyrics.AZLyrics',
        'metrolyrics.MetroLyrics',
        'letrascanciones.MP3Lyrics',
    ),
}
METROLYRICS_API_KEY = '1234567890123456789012345678901234567890'
BANDSINTOWN_APP_ID = 'SHIVA_APP_ID'
# Here you can redefine anything you set in your settings.project file, like
# the database URI.
