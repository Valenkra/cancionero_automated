import requests
'''
client_id = 45fde2d5971b4eb18880e347910a49ea
client_secret = 6059e7d9ef474ce390816c4c7d95425f

https://accounts.spotify.com/authorize?client_id=45fde2d5971b4eb18880e347910a49ea&response_type=code&redirect_uri=https%3A%2F%2Fgithub.com%2Fvalenvug&scope=playlist-modify-private%20playlist-modify-public


curl -H "Authorization: Basic NDVmZGUyZDU5NzFiNGViMTg4ODBlMzQ3OTEwYTQ5ZWE6NjA1OWU3ZDllZjQ3NGNlMzkwODE2YzRjN2Q5NTQyNWY=" -d grant_type=authorization_code -d code=AQCZz-2PoFzONg8cMyNe1z3zRDrd4q3In88jE8rBWopIlZ6jvduQx3eqZLMN9V1VZJl-rqzlpGhGPOd8zSofdkJLrifh7HR7UVsKUfhj69Wv2CM1Cxd3AbwLskRgUf-BgDcxV2e6-4DZmWm4Uxi0m2kUK-1mtYYW2oaN1J1iKKvRJGyPR9gbtyduZqN1tFROrtqtqWjIJQnyKPkGs_t4Oei38zDW4yYeUg7p8Dio1lQ -d redirect_uri=https%3A%2F%2Fgithub.com%2Fvalenvug https://accounts.spotify.com/api/token
'''
#{"access_token":"BQA6hK3yphgtZmwAdRHvNZzvX7J5LMgrHzg6BH6furzgflSmLR0m9aYzOL4ZOrlYI9toOE6MIIMX1ceeVRymgBtaxb7TX9TVQ1jqDefTLNosQR4AQEAzdLqZWuvP3bLH5XSC3MoqMctOjV9uiuhSmCDRYKgcIZeBmwO-7ut5XaDSXYz102pvgqQ9yR9MLipO9J77i006j1z5-9gH35h8OCymFTRpovJgHm7c-vuZ","token_type":"Bearer","expires_in":3600,"refresh_token":"AQA3D0Z0juLxBSu-svToUO-jE2QcnAH6k0YXneaPtKFWAWWj9NAbNljMVw0Xg2vbVhJ3CKso1ulQFiryNHuDQ96VTyQtj5sLV569FFve4d1IknD8Fb_YYBGmPusWMHk1oAQ","scope":"playlist-modify-private playlist-modify-public"}

token = "BQA6hK3yphgtZmwAdRHvNZzvX7J5LMgrHzg6BH6furzgflSmLR0m9aYzOL4ZOrlYI9toOE6MIIMX1ceeVRymgBtaxb7TX9TVQ1jqDefTLNosQR4AQEAzdLqZWuvP3bLH5XSC3MoqMctOjV9uiuhSmCDRYKgcIZeBmwO-7ut5XaDSXYz102pvgqQ9yR9MLipO9J77i006j1z5-9gH35h8OCymFTRpovJgHm7c-vuZ"
user_id = "valen_vu"
playlist_id = "1QC2XMVeR0Sjd7V5LWUCG7"
refresh_token = "AQA3D0Z0juLxBSu-svToUO-jE2QcnAH6k0YXneaPtKFWAWWj9NAbNljMVw0Xg2vbVhJ3CKso1ulQFiryNHuDQ96VTyQtj5sLV569FFve4d1IknD8Fb_YYBGmPusWMHk1oAQ"
base64 = "NDVmZGUyZDU5NzFiNGViMTg4ODBlMzQ3OTEwYTQ5ZWE6NjA1OWU3ZDllZjQ3NGNlMzkwODE2YzRjN2Q5NTQyNWY="

allowedSites = [
                'https://www.cifraclub.com/',
                'https://www.ultimate-guitar.com',
                'https://acordes.lacuerda.net'
]

