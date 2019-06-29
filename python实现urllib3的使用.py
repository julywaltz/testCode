#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-06-29 15:04:20
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-06-29 15:24:42
# @Email: julywaltz77@hotmail.com

import urllib3
from urllib.parse import urlencode

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
jurl = 'https://movie.douban.com/j/search_subjects'

d = {'type': 'movie', 'tag': '热门', 'page_limit': 10, 'page_start': 10}
# 连接池管理器
with urllib3.PoolManager() as http:
    response = http.request('GET',
                            '{}?{}'.format(jurl, urlencode(d)),
                            headers={'User-agent': ua})
    print(type(response))
    # response: HTTPResponse = HTTPResponse()
    print(response.status)
    print(response.data)
