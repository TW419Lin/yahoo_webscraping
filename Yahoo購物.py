# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:48:03 2020

@author: ASUS
"""
import requests
from bs4 import BeautifulSoup

header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36','cookie': 'SID=6QbWDvnYDiLfTqhNdOknQlfH_CM0eOmeq6ruxezl6scIGsWltAzfZKOeXjzYd662NHzifg.; HSID=AuhbSSlD-qvzbQ5br; SSID=ApAIdEuzdOenN30rh; APISID=FkTm8PRj5nzuvZAx/AjK4xYXNhB5F2oUmt; SAPISID=PcsAbgbI-Q-bgzXy/A5F5NzEuqBrCrt1UM; CONSENT=YES+TW.zh-CN+'}
param = {'p':'switch'}
search = input('SEARCH ITEM:')
param['p']=search

url = "https://tw.buy.yahoo.com/search/product"

data = requests.get(url, params=param, headers=header).text
content = BeautifulSoup(data, 'html.parser')
goods = content.find('div', class_='ResultList_resultList_IpWJt')
items = goods.find_all('li', class_='BaseGridItem__grid___2wuJ7 BaseGridItem__multipleImage___37M7b')
print (items)
print('------------------------------------------------')  
# for row in items:
#     link = row.find('a').get('href')
#     print('Link:', link)
#     title = row.find('span', class_='BaseGridItem__title___2HWui').text
#     print('Title:',title)
#     price = row.find('em', class_='BaseGridItem__price___31jkj').text
#     print('Price:',price)
    
      
allvalue = list(row.stripped_strings)
print(allvalue)
    # title = allvalue[2]
    # price = allvalue[3]
    # price=price.replace('$','')
    # price=price.replace(',','')
    # print(title)
    # print(price)
    # print()
