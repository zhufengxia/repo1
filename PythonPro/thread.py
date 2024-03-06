from multiprocessing.dummy import Pool
import time 
import requests 
import json
import re

all_shanghai_stock_url='https://4.push2.eastmoney.com/api/qt/clist/get'

header={
    'Accept':'*/*',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

params={
    'pn': '1',
'pz': '20',
'po': '1',
'np': '1',
'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
'fltt': '2',
'invt': '2',
'wbp2u':' |0|0|0|web',
'fid': 'f3',
'fs': 'm:0 t:6,m:0 t:80',
'fields': 'f12'
}
respons=requests.get(url=all_shanghai_stock_url,headers=header,params=params).text
print(respons)

