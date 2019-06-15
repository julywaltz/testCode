#!/usr/bin/env python
# -*- coding=utf-8 -*-
'''
@Author: Julywaltz
@Date: 2019-06-15 14:29:02
@LastEditors: Julywaltz
@LastEditTime: 2019-06-15 14:35:04
@Version: $Id$
'''
from bs4 import BeautifulSoup
import requests
from lxml import etree
import threading


def html_text(url):
    req = requests.get(url)
    return req.text


def down_pic(url, filename):
    pic = requests.get(url)
    print(filename, '下载中')
    with open('pics\\' + filename, 'wb') as f:
        f.write(pic.content)
    print(filename, '下载完成')


page_number = 1
while page_number < 9782:
    url = 'https://pixabay.com/images/search/?pagi=' + str(page_number)
    page_number += 1
    html = html_text(url)
    soup = BeautifulSoup(html, 'lxml')
    result = soup.find_all('div', class_='item')
    for link in result:
        link = 'https://pixabay.com' + link.find('a').get('href')
        html = html_text(link)
        url = etree.HTML(html).xpath('//img[@itemprop="contentURL"]/@srcset'
                                     )[0].split('1x')[0].strip(' ')
        filename = url.split('/')[-1]
        t = threading.Thread(target=down_pic, args=(url, filename))
        t.start()
