#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-06-29 15:39:05
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-06-29 15:46:35
# @Email: julywaltz77@hotmail.com
import requests
ua = ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
urls = [
    'https://www.baidu.com/s?wd=chengyili',
    'https://www.baidu.com/s?wd=chengyili'
]
session = requests.Session()
with session:
    for url in urls:
        response = session.get(url, headers={'User-Agent': ua})
    with response:
        print(response.text[:50])
        print('~' * 50)
        print(response.cookies)  # 状态码
        print('~' * 50)
        print(response.headers, '~~~~~~~~~~~~~~~~~')
        print(response.request.headers)
