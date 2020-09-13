import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd
from re import search
import os.path
from os import path

with open('../secret/credentials.json') as f:
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

pID = input("Spotify playlist ID: ")

result = spotify.playlist(pID, fields="tracks,albums,next")

tracks = result["tracks"]

show_tracks(tracks)
while tracks['next']:
    tracks = spotify.next(tracks)
    show_tracks(tracks)

df = pd.DataFrame({'track_name': track_name, 'artist_name': artist_name})

print(df)

path = input("Specify the path to save the .csv file to. If empty, will save to current folder. ")
fileName = input("Specify the file name. If left empty, file will be named Tracks.csv. ")
if path == "":
    if fileName == "":
        csv = df.to_csv('Tracks.csv', index = True)
    else:
        csv = df.to_csv(fileName, index=True)
elif path != "":
    if fileName == "":
        csv = df.to_csv(rf'{path}Tracks.csv', index = True)
    else:
        csv = df.to_csv(rf'{path}{fileName}.csv', index = True)
print(csv)