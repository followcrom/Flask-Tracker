import spotipy
from spotipy.oauth2 import SpotifyOAuth
from django.conf import settings

# Specify the scopes you want to use, separated by a space
scopes = "user-top-read user-modify-playback-state"


def get_spotipy_client():
    sp_oauth = SpotifyOAuth(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIFY_REDIRECT_URI,
        scope=scopes,
        show_dialog=True,
        cache_path="../.cache",
    )
    return spotipy.Spotify(auth_manager=sp_oauth)


# Initialize once and use throughout the application
sp = get_spotipy_client()
