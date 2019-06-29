#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-06-27 22:44:59
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-06-27 23:13:51
# @Email: julywaltz77@hotmail.com

from urllib.request import Request, urlopen
from urllib.parse import urlencode
import simplejson

url = 'http://httpbin.org/post'

data = urlencode({'name': '张三，@=/￥*', 'age': '6'})
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
req = Request(url, headers={'User-agent': ua})
with urlopen(req, data=data.encode()) as response:  #post方法，data不能为None
    text = response.read()
    d = simplejson.loads(text)
    print(d)
    print(type(d))