#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-07-03 23:57:47
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-07-03 23:58:01
# @Email: julywaltz77@hotmail.com
from selenium import webdriver
from urllib import parse
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from time import sleep
import re
"""构建url"""
base_url = 'https://sh.zu.fang.com/house/a018-s31/'
d = {'key': '闵行'}
u = parse.urlencode(d)
url = '{}?{}'.format(base_url, u)
"""初始化浏览器"""
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
sleep(3)
"""获取网页租房信息"""
for i in range(1, 6):
    soup = BeautifulSoup(driver.page_source, 'lxml')
    house_info = soup.find_all('dl', class_="list hiddenMap rel")
    for info in house_info:
        info_1 = info.find("dt", class_="img rel floatl")
        info_2 = info.find("dd", class_="info rel")
        if info_1 != None and info != None:
            price = info_2.find("span", class_="price").get_text()
            address = info_2.find("p", class_="gray6 mt12").get_text()
            name = "{}-{}.jpg".format(address, price)
            url = info.img.get("onerror")[17:-2]
            pic = requests.get(url)
            with open(name, 'wb') as f:
                f.write(pic.content)
                print(j, name, "下载完成")
                j += 1
    driver.find_element_by_link_text("下一页").click()
