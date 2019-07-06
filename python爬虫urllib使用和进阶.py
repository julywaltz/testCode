#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-06-26 22:43:17
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-07-06 22:20:11
# @Email: julywaltz77@hotmail.com

from urllib.request import urlopen, Request

url = 'https://dianying.taobao.com/index.htm'
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'

req = Request(url, headers={'User-agent': ua})
response = urlopen(req)  # get方法

print(response.closed)
with response:
    print(type(response))  # http.client.HTTPresponse类文件对象
    print(response.status)  # 状态
    print(response.geturl())  # 返回真正的url
    print(response.info())  # headers
    #print(response.read())  # 读取返回的内容
"""
上述代码等价于：
try:
    response
finally:
    print(type(response))  #http.client.HTTPresponse类文件对象
    print(response.status)  #状态
    print(response.get(url))  #返回真正的url
    print(response.info())  #headers
    print(response.read())  #读取返回的内容
    respones.close()
print(response.closed)
"""
print('-' * 30)
print(req.get_header('User-agent'))
print(response.closed)