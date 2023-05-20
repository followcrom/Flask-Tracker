import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

# print("------------------------------------------------------------------------")


def get_artist(results):
    artist_lst = []
    for item in results["items"]:
        track = item["track"]
        artist_solo = track["artists"][0]["name"]
        artistes = track["artists"]
        if len(artistes) > 1:
            artist_lst_2 = [d["name"] for d in artistes]
            group = str()
            for art_name in artist_lst_2:
                if art_name == artist_lst_2[0]:
                    group = art_name
                else:
                    group = group + ", " + art_name
            artist_lst.append(group)
        else:
            artist_lst.append(artist_solo)
    return artist_lst


# print("------------------------------------------------------------------------")


def get_song(results):
    song_lst = []
    for item in results["items"]:
        track = item["track"]
        song = track["name"]
        song_lst.append(song)
    return song_lst


# print("------------------------------------------------------------------------")


def get_popularity(results):
    popularity_lst = []
    for item in results["items"]:
        track = item["track"]
        popularity = track["popularity"]
        popularity_lst.append(popularity)
    return popularity_lst


# print("------------------------------------------------------------------------")


def get_track_id(results):
    track_id_lst = []
    for item in results["items"]:
        track = item["track"]
        track_id = track["id"]
        track_id_lst.append(track_id)
    return track_id_lst


# print("------------------------------------------------------------------------")


def get_external_url(results):
    external_url_lst = []
    for item in results["items"]:
        track = item["track"]
        external_url = track["external_urls"]["spotify"]
        external_url_lst.append(external_url)
    return external_url_lst


print("------------------------------------------------------------------------")


def get_tracks(results):
    long_artist_lst = []
    long_song_lst = []
    long_popularity_lst = []
    long_external_url_lst = []

    long_artist_lst.extend(get_artist(results))
    long_song_lst.extend(get_song(results))
    long_popularity_lst.extend(get_popularity(results))
    long_external_url_lst.extend(get_external_url(results))

    top_10_dict = {
        "artist": long_artist_lst,
        "song": long_song_lst,
        "popularity": long_popularity_lst,
        "Link": long_external_url_lst,
    }

    return top_10_dict
