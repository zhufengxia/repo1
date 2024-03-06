import requests 
import json
import csv

url='https://push2.eastmoney.com/api/qt/stock/details/get'

headers={
    'Accept':'*/*',
    'Accept-Language':'Accept-Language:en-US,en;q=0.9',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

params={
    'fields1': 'f1,f2,f3,f4',
'fields2': 'f51,f52,f53,f54,f55',
'secid': '1.601096',
}

respons_json=requests.get(url=url,headers=headers,params=params).text 
res_list=json.loads(respons_json)['data']['details']
fp=open("Real_time.csv",'a',encoding="UTF-8",newline='')

for i in range(0,len(res_list)):
    data=res_list[i].split(',')
    data_csv=csv.writer(fp)
    data_csv.writerow(data)
