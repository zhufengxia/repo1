import requests
import re,csv
import pandas as pd
data_list=[]
for number in range(1,10):
    url='https://93.push2.eastmoney.com/api/qt/clist/get?'

    headers={
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection':'keep-alive',
        'Cookie':'qgqp_b_id=fa53fd3ad7eb8a13d75b11161280c247; websitepoptg_show_time=1703853645734; HAList=ty-1-601166-%u5174%u4E1A%u94F6%u884C%2Cty-1-603004-N%u9F0E%u9F99%2Cty-1-605599-%u83DC%u767E%u80A1%u4EFD%2Cty-1-601096-C%u5B8F%u76DB%2Cty-1-688032-%u79BE%u8FC8%u80A1%u4EFD%2Cty-116-02302-%u4E2D%u6838%u56FD%u9645%2Cty-0-200029-%u6DF1%u6DF1%u623F%uFF22%2Cty-1-900906-%u4E2D%u6BC5%u8FBEB%2Cty-0-200056-%u7687%u5EADB%2Cty-0-430510-%u4E30%u5149%u7CBE%u5BC6; websitepoptg_api_time=1708865488228; st_si=72021486140528; st_asi=delete; st_pvi=30703821769824; st_sp=2023-12-13%2021%3A30%3A16; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=5; st_psi=20240225205920850-113200301321-9614971811',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
        }
    columns=['number','code','name','Latest_price','range','Price_limit','tody_open','tody_up','ody_low','yesterday_clos']

    params={
        'pn': number,
        'pz': '20',
        'po': '1',
        'np': '1',
        'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
        'fltt': '2',
        'invt': '2',
        'wbp2u': '|0|0|0|web',
        'fid': 'f3',
        'fs': 'm:119,m:120,m:133',
        'fields': 'f12,f14,f2,f4,f3,f15,f16,f17,f18'
        }
    respons=requests.get(headers=headers,params=params,url=url)
    respons_json=respons.json()
    # print(respons_json['data']['diff'])
    for x in respons_json['data']['diff']:
        code=x['f12']
        name=x['f14']
        Latest_price=x['f2']
        range=x['f4']
        Price_limit=str(x['f3'])+'%'
        tody_open=x['f15']
        tody_up=x['f16']
        tody_low=x['f17']
        yesterday_clos=x['f18']
        data_dict1={'code':code,'name':name,'Latest_price':Latest_price,'range':range,'Price_limit':Price_limit,'tody_open':tody_open,'tody_up':tody_up,'tody_low':tody_low,'yesterday_clos':yesterday_clos}
        data_list.append(data_dict1)

def to_df(v):
    if isinstance(v, list):
        return pd.DataFrame(data=v,columns = columns)
    elif isinstance(v, dict):
        return pd.DataFrame(data=[v,],columns = columns)
    else:
        return pd.DataFrame(data=[{'value': v}],columns = columns)

data_pd=to_df(data_list)
print(data_pd)



