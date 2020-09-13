import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd
from re import search

with open('./credentials.json') as f:
    data = json.load(f)

cid = data['spotify_cid']
secret = data['spotify_token']

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_name = []
track_name = []

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        if search(' ver', track['name'].lower()):
            track_name.append(track['name'])
            artist_name.append(track['artists'][0]['name'])
            print(
                "   %d %32.32s %s" %
                (i, track['artists'][0]['name'], track['name']), end = "\r")
        else:
            None

def getlist(dict):
    return dict.keys()

pID = input("Spotify playlist ID: ")

result = spotify.playlist(pID, fields="tracks,albums,next")

#print(getlist(result))

tracks = result["tracks"]

show_tracks(tracks)
while tracks['next']:
    tracks = spotify.next(tracks)
    show_tracks(tracks)

df = pd.DataFrame({'track_name': track_name, 'artist_name': artist_name})

print(df)
csv = df.to_csv('Tracks.csv', index = True)
print(csv)