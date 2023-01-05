from secrets import refresh_token, base64
import requests
import json

class Refresh:
    def __init__(self):
        self.refresh_token = refresh_token
        self.base64 = base64

    def refresh(self):
        query = "https://accounts.spotify.com/api/token"
        response = requests.post(query,
                                 data={"grant_type": "refresh_token",
                                       "refresh_token": refresh_token},
                                 headers={"Authorization": f'Basic {base64}'})

        return response.json()["access_token"]