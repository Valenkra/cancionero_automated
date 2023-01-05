import json
import math
import requests
from secrets import user_id, playlist_id
from refresh import Refresh

class SaveSongs:
    def __init__(self):
        self.user_id = user_id
        self.tracks = []
        self.token = ""
        self.playlist_id = playlist_id

    def call_refresh(self):
        refreshCaller = Refresh()
        self.token = refreshCaller.refresh()
        self.tracks = self.find_songs()

    def find_songs(self):
        offset = 0
        list_songs = []
        query = "https://api.spotify.com/v1/playlists/{0}/tracks?limit=50&offset={1}".format(playlist_id, offset)
        response = requests.get(query, headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(self.token)})

        response_json = response.json()

        offset_max = math.ceil(response_json["total"] / 50)

        num = 1

        for getting_tracks in range(offset_max):
            for i in response_json["items"]:
                # print(f'{num}: {i["track"]["name"]} - {i["track"]["artists"][0]["name"]}')
                list_songs.append((f'{i["track"]["name"]} {i["track"]["artists"][0]["name"]}').replace(" ", "+"))
                num += 1

            offset = 50 * (getting_tracks + 1)

            query = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks?limit=50&offset={offset}'
            response = requests.get(query,
                                    headers={"Content-Type": "application/json",
                                             "Authorization": "Bearer {}".format(self.token)})

            response_json = response.json()

        return list_songs
