from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as erro:
    print(erro)
except URLError as erro:
    print(erro)
else:
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs.h1)
