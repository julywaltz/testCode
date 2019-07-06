#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-07-06 21:20:41
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-07-07 00:06:37
# @Email: julywaltz77@hotmail.com

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from lxml import etree
from time import sleep
import csv
import os

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)


# 获取糯米城市id,创建城市id文件
def get_nuomi_city_id(driver):
    file_name = 'nuomu_city_id.csv'
    if file_name not in os.listdir(os.getcwd()):
        url = 'https://dianying.nuomi.com/home/citylist'
        driver.get(url)
        sleep(3)
        tree = etree.HTML(driver.page_source)
        ids = tree.xpath('//ul[@class="cities fl"]/li/a/@data-id')
        cities_id = {}
        for id in ids:
            city = tree.xpath(
                '//ul[@class="cities fl"]/li/a[@data-id={}]/text()'.format(
                    id))[0].strip()
            cities_id[city] = id
        print(cities_id, type(cities_id))
        with open('nuomu_city_id.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in cities_id.items():
                writer.writerow([key, value])
        driver.quit()
    else:
        pass


# 获取淘票票城市id,创建城市id文件,城市链接
def get_taopiaopiao_city_id(driver):
    file_name = 'taopiaopiao_city_id.csv'
    if file_name not in os.listdir(os.getcwd()):
        url = 'https://dianying.taobao.com'
        wait = WebDriverWait(driver, 10)
        driver.get(url)
        city_link = wait.until(
            expected_conditions.element_to_be_clickable((By.ID, 'cityName')))
        city_link.click()
        sleep(1)
        with open('test.html', 'w', encoding='utf8') as f:
            f.write(driver.page_source)
        tree = etree.HTML(driver.page_source)
        ids = tree.xpath(
            '//div[@class="M-cityList scrollStyle"]/ul/li/a/@data-id')
        cities_id = {}
        for id in ids:
            city = tree.xpath(
                '//div[@class="M-cityList scrollStyle"]/ul/li/a[@data-id="{}"]/text()'.format(id)
            )[0].strip()
            cities_id[city] = id
        print(cities_id, type(cities_id))
        with open(file_name, 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in cities_id.items():
                writer.writerow([key, value])
        driver.quit()
    else:
        pass


