import json
import requests

from bs4 import BeautifulSoup

WEBSITE_URL = 'https://www.hardmob.com.br/forums/407-Promocoes'

def get_promocoes(event = None, context = None):

    r = requests.get(WEBSITE_URL)

    if not r.status_code == requests.codes.ok:
        raise

    soup = BeautifulSoup(r.text, 'lxml')
    div_links = soup.select('#threadlist')[0]
    links = div_links.select('.title')

    i = 0
    for link in links:
        if i > 1:
            print(link.text, ' -> ', 'https://www.hardmob.com.br/' + link['href'])
        i = i+1



if __name__ == '__main__':
    get_promocoes()
