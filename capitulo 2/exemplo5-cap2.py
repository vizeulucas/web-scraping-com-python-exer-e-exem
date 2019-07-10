from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'lxml')

images = bs.find_all('img', {'src': re.compile('\.\.\/img/gifts/img.*\.jpg')})
for img in images:
    print(img['src'])
