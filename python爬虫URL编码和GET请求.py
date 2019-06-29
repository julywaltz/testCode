#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-06-26 23:35:16
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-06-29 14:48:35
# @Email: julywaltz77@hotmail.com

from urllib import parse
from urllib.request import urlopen, Request

base_url = 'https://cn.bing.com/search'
d = {'q': '程一栗'}
u = parse.urlencode(d)
url = '{}?{}'.format(base_url, u)
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'

req = Request(url, headers={'User-agent': ua})
response = urlopen(req)  # get方法
with response:
    with open('d:/bing.html', 'wb+') as f:
        f.write(response.read())
        f.flush
