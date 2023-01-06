import markdown
import requests
import requests_html

url=f'https://www.cifraclub.com/oasis/dont-look-back-in-anger/'
session= requests_html.HTMLSession()
r= session.get(url)
print(r.html.xpath(f'//*[@id="js-w-content"]/div[3]/div[1]/div[1]/div[1]/div/div/pre')[0].text)

'''
markdown_string = '# Hello World'

with open('sample.md', 'w') as f:
    f.write(markdown_string)
    f.close()

# 2
html_string = markdown.markdown(markdown_string)
print(html_string)
'''