#!/usr/bin/env python
# -*- coding=utf-8 -*-
'''
@Author: Julywaltz
@Date: 2019-06-15 14:39:46
@LastEditors: Julywaltz
@LastEditTime: 2019-06-15 14:39:47
@Version: $Id$
'''
import requests
from lxml import etree
from time import sleep
import datetime

ISOTIMEFORMAT = '%H:%M:%S'
theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
print('程序开始', theTime)

urls = []
req = requests.get('https://www.qiushibaike.com/text/')
html = req.text
root = etree.HTML(html)
page_number = root.xpath('//span[@class="page-numbers"]/text()')[-1]
urls = []
for i in range(1, int(page_number) + 1):
    url = 'https://www.qiushibaike.com/text/page/' + str(i) + '/'
    req_1 = requests.get(url)
    html_1 = req_1.text
    root = etree.HTML(html_1)
    first = root.xpath('//div[@class="col1"]/div/a/@href')
    for url in first:
        url = 'https://www.qiushibaike.com' + url
        if urls != []:
            if url != urls[-1]:
                urls.append(url)
        else:
            urls.append(url)
print('地址获取完成')
theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
print('程序开始', theTime)
print(len(urls))
t = 1
for url in urls:
    theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    print('第%d个段子读取成功' % t, theTime)
    t += 1
    text = []
    req = requests.get(url)
    html = req.text
    root = etree.HTML(html)
    word = root.xpath('//div[@class="word"]/div/text()')
    word = '\n'.join(word)
    auther = '\n作者:' + root.xpath('//span[@class="side-user-name"]/text()')[0]
    number = '\n好笑数：' + \
        root.xpath('//i[@class = "number"]/text()')[0] + '\n' + '\n'
    text.append(word)
    text.append(auther)
    text.append(number)
    print('第%d个段子写入开始' % t)
    for line in text:
        with open('qiushibaike.txt', 'a', encoding='utf8') as f:
            f.write(line)
    print('第%d个段子写入完成' % t)
    theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    print('写入完成', theTime)
    sleep(1)
print('全部写入完成')
