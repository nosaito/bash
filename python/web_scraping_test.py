#!/usr/bin/env python
# -*- coding: sjis -*-

# web scraping test
# http://qiita.com/dtakkiy/items/4feb89868587161ee0b5?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items


import requests
from bs4 import BeautifulSoup

target_url = 'http://collab.micron.com/mfg/Fab4/opcdfm/Lists/trackDFM/Active1.aspx'  #example.co.jp�͉ˋ�̃h���C���B�C�ӂ�url�ɕύX����
r = requests.get(target_url)         #requests���g���āAweb����擾
soup = BeautifulSoup(r.text, 'lxml') #�v�f�𒊏o

for a in soup.find_all('a'):
    print(a.get('href'))         #�����N��\��
