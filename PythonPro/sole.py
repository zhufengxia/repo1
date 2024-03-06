import requests
import pandas as pd

code=input('请输入外汇代码')
url='https://push2.eastmoney.com/api/qt/stock/get?'
columns=['code','name','Latest_price','range','Price_limit','Today_open','The_highest','minimum','Yesterday_closing']
headers={
    'Accept':'*/*',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Connection':'keep-alive',
'Cookie':'qgqp_b_id=fa53fd3ad7eb8a13d75b11161280c247; websitepoptg_api_time=1709087222925; st_si=25161761244081; st_asi=delete; HAList=ty-119-JPYNZD-100%u65E5%u5143%u5151%u65B0%u897F%u5170%u5143%2Cty-119-USDNZD-%u7F8E%u5143%u5151%u65B0%u897F%u5170%u5143%2Cty-119-ZARCHF-%u5357%u975E%u5170%u7279%u5151%u745E%u90CE%2Cty-119-USDPLN-%u7F8E%u5143%u5151%u6CE2%u5170%u5179%u7F57%u63D0%2Cty-1-601166-%u5174%u4E1A%u94F6%u884C%2Cty-1-603004-N%u9F0E%u9F99%2Cty-1-605599-%u83DC%u767E%u80A1%u4EFD%2Cty-1-601096-C%u5B8F%u76DB%2Cty-1-688032-%u79BE%u8FC8%u80A1%u4EFD%2Cty-116-02302-%u4E2D%u6838%u56FD%u9645; st_pvi=30703821769824; st_sp=2023-12-13%2021%3A30%3A16; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=21;',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

params={
    'invt': '2',
    'fltt': '1',
    'fields': 'f57,f58,f43,f169,f170,f46,f44,f45,f60',
    'secid':f'119.{code}',
    'ut': 'fa5fd1943c7b386f172d6893dbfba10b',
    'wbp2u':'0|0|0|web'
}
def to_df(v):
    if isinstance(v, list):
        return pd.DataFrame(data=v,columns = columns)
    elif isinstance(v, dict):
        return pd.DataFrame(data=[v,],columns = columns)
    else:
        return pd.DataFrame(data=[{'value': v}],columns = columns)

data_list=[]
respons=requests.get(url=url,headers=headers,params=params)
respons_data=respons.json()['data']
data_dict={'code':respons_data['f57'],'name':respons_data['f58'],'Latest_price':respons_data['f43'],'range':respons_data['f169'],'Price_limit':respons_data['f170'],
           'Today_open':respons_data['f46'],'The_highest':respons_data['f44'],'minimum':respons_data['f45'],'Yesterday_closing':respons_data['f60']}
data_list.append(data_dict)
data=to_df(data_list)
print(data)




