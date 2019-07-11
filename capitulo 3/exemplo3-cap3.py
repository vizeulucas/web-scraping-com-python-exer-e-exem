from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re


random.seed(datetime.datetime.now()) #inicia o gerador de numeros randomicos com base no horario atual do sistema


def get_links(article_url):
    html = urlopen('http://en.wikipedia.org{}'.format(article_url)) #pega o html do artigo da wikipedia
    bs = BeautifulSoup(html, 'lxml') #transforma o html num objeto bs
    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    #retorna uma lista contendo todos os links para artigos da wikipedia encontrados na url passada como argumento


links = get_links('/wiki/Kevin_Bacon') #artigo exemplo

while len(links) > 0:
    new_article = links[random.randint(0, len(links)-1)].attrs['href'] #escolhe um artigo aleatorio da lista
    print(new_article)
    links = get_links(new_article) #reinicia o ciclo com o novo artigo escolhido anteriormente
