#!/usr/bin/env python3

# from lxml.etree import parse, tostring
from lxml.html import parse, tostring, fragment_fromstring

# from bs4 import BeautifulSoup

from pathlib import Path

template_dir = Path(__file__).parent / 'src/html/templates'

for template_file in template_dir.glob('*.php'):
    print(template_file)
    source = template_file.read_text()
    # bsObj = BeautifulSoup(source, 'lxml')
    # tree = parse(template_file.open(encoding = 'utf-8'))
    tree = fragment_fromstring(template_file.read_text(encoding = 'utf-8'))
    # print(tree)
    # print(bsObj)
    # root = tree.getroot()
    # print(tostring(root))
    # print(root.tag)