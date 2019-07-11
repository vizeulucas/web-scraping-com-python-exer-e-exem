from urllib.request import urlopen
from bs4 import BeautifulSoup


html_doc = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html_doc, 'lxml')

for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
