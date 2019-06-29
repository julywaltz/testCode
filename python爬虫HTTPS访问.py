#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-06-29 14:40:57
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-06-29 14:48:45
# @Email: julywaltz77@hotmail.com

from urllib.request import Request, urlopen
import ssl

request = Request('https://www.12306.cn/mormhweb/')
request.add_header(
    'User-agent',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
)

context = ssl._create_default_https_context()  # 忽略ssl证书信任报错

with urlopen(request, context=context) as res:
    print(res._method)
    print(res.read())
