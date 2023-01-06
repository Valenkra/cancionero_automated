import markdown
import requests
import requests_html
from markdownify import markdownify
from lxml import html

from bs4 import BeautifulSoup
import urllib.request

adress = 'https://www.cifraclub.com/oasis/dont-look-back-in-anger/'
response = urllib.request.urlopen(adress)
html = response.read()

soup = BeautifulSoup(html,features="lxml")
pre = soup.find_all('pre')
print(pre)

