from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page1.html')
bs_html_parser = BeautifulSoup(html.read(), 'html.parser') #utilizando o html. parser como parser
bs_lxml_parser = BeautifulSoup(html.read(), 'lxml') #utilizando o lxml como parser
bs_html5lib_parser = BeautifulSoup(html.read(), 'html5lib') #utilizando o html5lib como parser

#desativar dois dos três parsers acima e dois prints abaixo para funcionar
print(bs_html_parser.h1)
print(bs_lxml_parser.h1)
print(bs_html5lib_parser.h1)
