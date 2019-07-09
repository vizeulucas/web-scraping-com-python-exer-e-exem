from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError:
        return None
    else:
        return title


title = getTitle('http://www.pythonscraping.com/pages/page1.html')

if title == None:
    print('Titulo não encontrado')
else:
    print(title)
