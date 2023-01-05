from googlesearch import search
import requests_html
from main import SaveSongs
from scraper import GoogleScraper
from secrets import allowedSites

tituloYartista = SaveSongs()
tituloYartista.call_refresh()
canciones = []

# Buscar Lyrics y eliminar los inexistentes
f = open('readme.txt', 'w')
f.write(f'Lista de canciones que no se han encontrado en la base de datos...\n')

bad_index = []
for i in range(len(tituloYartista.tracks)):
	canciones.append(tituloYartista.tracks[i])
	canciones[i] = GoogleScraper(canciones[i])
	if canciones[i].lyrics == []:
		bad_index.append(i)
		f.write(f'  - {canciones.tracks[i].replace("+", " ")} \n' )
bad_index.reverse()
for i in range(len(bad_index)):
	canciones.pop(bad_index[i])
	tituloYartista.tracks.pop(bad_index[i])

f.close()

class findChords:
	def __init__(self,songInfo):
		self.query = f'{songInfo.replace("+", " ")} acordes'
		self.sites = self.findSites()

	def findSites(self):
		sites = []
		for response in search(self.query, tld="co.in", num=10, stop=10, pause=2):
			for site in allowedSites:
				if(response.find(site) != -1):
					sites.append(response)

		return sites

acordes = []
for x in range(3):#range(len(canciones.tracks)):
	acordes.append(findChords(tituloYartista.tracks[x]))
	acordes[x].findSites()
	print(acordes[x].sites)
#print(acordes)
	#session = requests_html.HTMLSession()
	#r = session.get('https://www.cifraclub.com/paulo-londra/chica-paranormal/')

	#lyrics = r.html.xpath('//*[@id="js-w-content"]/div[3]/div[1]/div[1]/div[1]/div/div/pre')[0].text.split()
	#print(lyrics)


