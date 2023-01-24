import logging
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config

logger = logging.getLogger('examples.artist_recommendations')
logging.basicConfig(level='INFO')

client_id = config.CLIENT_ID
client_secret = config.CLIENT_SECRET

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_artist(name):
    """
    get artist information by searching using artist name.

    example:
        >> get_artist('Tobe Nwigwe')
        >> {'external_urls': {'spotify':
            'https://open.spotify.com/artist/3Qh89pgJeZq6d8uM1bTot3'}, 'followers': {'href': None, 'total': 277309},
            'genres': ['christian hip hop', 'houston rap'], ...
            'name': 'Tobe Nwigwe', 'popularity': 56, 'type': 'artist', 'uri': 'spotify:artist:3Qh89pgJeZq6d8uM1bTot3'}

    :param name:
        name of an artist
    :return:
        dict: artist metadata
    """
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None


def show_recommendations_for_artist(artists):
    """
    returns list of recommended artist/songs based on list input of artist IDs

    :param artists:
        list of artist IDs
    :return:
        dict: artist metadata
    """
    results = sp.recommendations(seed_artists=artists)

    return results['tracks']
