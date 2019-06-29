#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-06-29 13:54:57
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-06-29 14:19:11
# @Email: julywaltz77@hotmail.com

from urllib.parse import urlencode
from urllib.request import urlopen, Request
import simplejson
from time import sleep

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
jurl = 'https://movie.douban.com/j/search_subjects'

print('开始')
for y in range(0, 100, 10):
    sleep(2)
    print(y)
    d = {'type': 'movie', 'tag': '热门', 'page_limit': 10, 'page_start': y}
    req = Request('{}?{}'.format(jurl, urlencode(d)),
                  headers={'User-agent': ua})
    with urlopen(req) as res:
        subjects = simplejson.loads(res.read())
        for line in subjects['subjects']:
            with open('filem.txt', 'a', encoding='utf8') as f:
                f.write(str(line) + '\n' + '-' * 30+'\n')
print('结束')
