#!/usr/bin/env python3

print("Upracme Slovensko scrapper uklidme česko")

from urllib.parse import urlparse, urljoin

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

from pathlib import Path
# import webbrowser

SOURCE_URL = "http://www.uklidmecesko.cz"

destination = Path().cwd() / 'src/html'

html = urlopen(SOURCE_URL)
bsObj = BeautifulSoup(html.read(), 'lxml')


def retrieve(zdroj, cil):
    dir = cil.parent
    dir.mkdir(parents=True, exist_ok = True)
    urlretrieve(zdroj, cil)


styly = bsObj.findAll("link", {"rel": "stylesheet"})
for styl in styly:
    href = styl['href']
    url = urlparse(href)
    # print(url)
    if url.netloc is '':
        zdroj = urljoin(SOURCE_URL, href)
        print(zdroj)
        # webbrowser.open(zdroj)
        retrieve(zdroj, destination / href.lstrip('/'))
        

skripty = bsObj.findAll("script")

for skript in skripty:
    
    if not 'src' in skript.attrs:
        continue
    src = skript['src']
    url = urlparse(src)
    
    if url.netloc is '':
        zdroj = urljoin(SOURCE_URL, src)
        print(zdroj)
    #     # webbrowser.open(zdroj)
        retrieve(zdroj, destination / src.lstrip('/'))

obrazky = bsObj.findAll("img")
# print(obrazky)
for obrazek in obrazky:
    
    if not 'src' in obrazek.attrs:
        continue
    src = obrazek['src']
    url = urlparse(src)
    
    if url.netloc is '':
        zdroj = urljoin(SOURCE_URL, src)
        print(zdroj)
    #     # webbrowser.open(zdroj)
        retrieve(zdroj, destination / src.lstrip('/'))