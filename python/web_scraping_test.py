#!/usr/bin/env python
# -*- coding: sjis -*-

# web scraping test
# http://qiita.com/dtakkiy/items/4feb89868587161ee0b5?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items


import requests
from bs4 import BeautifulSoup

target_url = 'http://collab.micron.com/mfg/Fab4/opcdfm/Lists/trackDFM/Active1.aspx'  #example.co.jpは架空のドメイン。任意のurlに変更する
r = requests.get(target_url)         #requestsを使って、webから取得
soup = BeautifulSoup(r.text, 'lxml') #要素を抽出

for a in soup.find_all('a'):
    print(a.get('href'))         #リンクを表示
