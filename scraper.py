import requests_html
from main import SaveSongs

class GoogleScraper:
    def __init__(self, cancion):
        self.session  = requests_html.HTMLSession()
        self.r = self.session.get(f'https://www.google.com/search?q={cancion}+lyrics')
        self.lyrics = self.find_lyrics()

    def find_lyrics(self):
        i = 1
        lyrics = []
        running = True
        while running:
            try:
                lyrics.append(self.r.html.xpath(f'//*[@id="kp-wp-tab-default_tab:kc:/music/recording_cluster:lyrics"]/div[1]/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div[{i}]')[0].text)
                i+=1
            except IndexError:
                running = False

        return lyrics

'''
canciones = SaveSongs()
canciones.call_refresh()
songs = []

#f = open('readme.txt', 'w')
#f.write(f'Lista de canciones que no se han encontrado en la base de datos...\n')

for i in range(len(canciones.tracks)):
    songs.append(canciones.tracks[i])
    songs[i] = GoogleScraper(songs[i])
    if songs[i].lyrics == []:
        pass
        #f.write(f'  - {canciones.tracks[i].replace("+", " ")} \n' )

#f.close()

'''