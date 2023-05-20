from flask import Flask, render_template, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from spotty import get_tracks
import os

application = Flask(__name__)

client_id = os.environ["SPOTIPY_CLIENT_ID"]
client_secret = os.environ["SPOTIPY_CLIENT_SECRET"]
redirect_uri = os.environ["SPOTIPY_REDIRECT_URI"]


@application.route("/")
def liked_songs():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-library-read"))
    results = sp.current_user_saved_tracks(offset=0, limit=10)
    name = "10 Latest Liked Songs"
    tracks = get_tracks(results)
    return render_template("index.html", name=name, tracks=tracks)


if __name__ == "__main__":
    application.run(debug=True)
