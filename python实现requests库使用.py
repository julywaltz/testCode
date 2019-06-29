#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-06-29 15:25:37
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-06-29 15:31:31
# @Email: julywaltz77@hotmail.com

import requests
from urllib.parse import urlencode

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
jurl = 'https://movie.douban.com/j/search_subjects'

d = {'type': 'movie', 'tag': '热门', 'page_limit': 10, 'page_start': 10}

url = '{}?{}'.format(jurl, urlencode(d))

response = requests.request('GET', url, headers={'User-agent': ua})
with response:
    print(type(response))
    print(response.text)
    print(response.status_code)  # 状态码
    print(response.url)
    print(response.request)
