from markdownify import markdownify
from bs4 import BeautifulSoup
import urllib.request

adress = 'https://www.cifraclub.com/oasis/dont-look-back-in-anger/'
response = urllib.request.urlopen(adress)
html = response.read()

soup = BeautifulSoup(html, features="lxml")
pre = soup.find_all('pre')
pre = str(pre)
pre = pre[6:]
pre = pre[:-7]
pre = pre.replace(" ", "&nbsp;")

file = markdownify(pre, heading_style="ATX")
with open('samples.md', 'w') as f:
    f.write(file)
    f.close()
'''
with open('samples.md', 'r+') as f:
    for line in f.readlines():
        if line.find('*') != -1:
            line.replace(' ', '&nbsp;')
            print(line)

    f.close()'''

# Read in the file
with open('samples.md', 'r') as file:
  filedata = file.readlines()

# Replace the target string
for x in range(len(filedata)):
    line = filedata[x]
    if line.find('*') != -1:
        pass
        #filedata[x] = filedata[x].replace(" ", '&nbsp;')

    if line != "\n" and line.find(']') == -1:
        filedata[x] = filedata[x][:-1] + '  \n'

        print(line)

# Write the file out again
with open('samples.md', 'w') as file:
  file.writelines(filedata)



