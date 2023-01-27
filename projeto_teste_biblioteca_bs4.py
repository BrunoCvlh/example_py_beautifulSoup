# -*- coding: utf-8 -*-
"""Projeto Teste biblioteca BS4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GwmVi02BzmLtQ9KQeIRHCabSeXuLUZIt
"""

from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/'
r= requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

soup.find('div', class_='small-widget')

soup.find('div', attrs={'class' : 'small-widget'})

soup.find('div', class_ = 'small-widget').h2

soup.find('div', class_ = 'small-widget').h2.text

soup.find('div', class_ = 'small-widget').p

soup.find('div', class_ = 'small-widget').h2.next_element

soup.find('div', class_ = 'small-widget').h2.next_sibling

soup.find('div', class_ = 'small-widget').h2.next_sibling.next_sibling

soup.find_all('div', class_ = 'small-widget')[3].h2.text

elementos = soup.find_all('div', class_ = 'small-widget')

for elemento in elementos:
  print(elemento.h2.text)