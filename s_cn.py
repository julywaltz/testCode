from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import requests
from lxml import etree
import csv
import threading

# 名鞋网商品爬取程序
# 获取商品链接


def get_goodslinks(link, chrome_options, goods_links):
    req = requests.get(link)
    html = req.text
    tree = etree.HTML(html)
    page_list = tree.xpath('//td[@class="pagernum"]/a/text()')
    page_soup = BeautifulSoup(html, 'lxml')
    url_id = page_soup.find('a', href="//www.s.cn/list")
    url_id = url_id.get('url_id')
    i = 1
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(link)
    time.sleep(1.5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    goods_list = soup.find_all('a', class_='big_pic')
    for good_link in goods_list:
        good_link = 'https:' + good_link.get('href')
        print(i, good_link)
        i += 1
        goods_links.append(good_link)
    driver.quit()
    for page in page_list[1:]:
        link = 'https://www.s.cn/list/' + url_id + '-pg' + page
        print(link)
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(link)
        time.sleep(1.5)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        goods_list = soup.find_all('a', class_='big_pic')
        for good_link in goods_list:
            good_link = 'https:' + good_link.get('href')
            print(i, good_link)
            i += 1
            goods_links.append(good_link)
        driver.quit()
    return goods_links

# 获取商品信息


def get_goodsinfo(goods_link):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(goods_link)
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    name = soup.find('h1', class_='goodsname').get_text()
    price = soup.find('span', class_='price1 salePrice_big').get_text()
    info = soup.find('div', class_='proshow-canshu').get_text()
    print(name, 'done')
    all_goods.append([name, url, price, info])
    driver.quit()


# 获取品牌连接
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

url = 'https://www.s.cn/list'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'lxml')
brand_list = soup.find_all('dl', id="brand_dl")[0]
brand_links = brand_list.find_all('a')
goods_links = []
for link in brand_links:
    link = 'https:' + link.get('href')
    print(link)
    goods_link = get_goodslinks(link, chrome_options, goods_links)
    goods_links += goods_link
print('商品链接获取完成')

global all_goods
all_goods = []
for goods_link in goods_links:
    threading.Thread(target=get_goodsinfo, args=(goods_link,)).start()
    while threading.active_count() > 4:
        time.sleep(2)
print('商品信息下载完成')
with open('www.s.cn_goods.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['商品名', '商品链接', '价格', '商品信息'])
    for line in all_goods:
        writer.writerow(line)
print('商品信息文件以生成')
