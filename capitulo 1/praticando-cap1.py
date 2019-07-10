from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


def getDiv(url):
    try:
        html = urlopen(url)
    except HTTPError as erro:
        print(erro)
        return None
    except URLError as erro:
        print(erro)
        return None

    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        div = bs.div
    except AttributeError:
        print('Erro, Atributo Inexistente')
        return None
    else:
        return div


url = 'http://pythonscraping.com/pages/page1.html'
print(getDiv(url))
