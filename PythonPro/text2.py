import requests
import json
import csv
import time
while True:
    url='https://push2.eastmoney.com/api/qt/stock/details/get'
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        'Accept':'*/*',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    }
    params={
        'fields1':'f1,f2,f3,f4',
        'fields2':'f51,f52,f53,f54,f55',
        'pos':'-11',
        'secid': '1.600630',
        'ut': 'fa5fd1943c7b386f172d6893dbfba10b'
    }
    result=requests.get(url=url,headers=header,params=params)
    res_json=result.text
    with open('data1.csv','w',encoding='UTF-8')as fp:
        fp.write(res_json+'\n')
    time.sleep(5)
    