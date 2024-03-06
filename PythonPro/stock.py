import requests 


def stock(code:str,time:str):
    url='https://push2his.eastmoney.com/api/qt/stock/kline/get'
    headers={
        'Accept':'*/*',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
    designation={'0','1'}
    for designa in len(designation):
        params={
            'secid':designation[designa]+'.'+code,
            'ut': 'fa5fd1943c7b386f172d6893dbfba10b',
            'fields1':' f1,f2,f3,f4,f5,f6',
            'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61',
            'klt': time,
            'fqt': '1',
            'bge':'0',
            'end': '20500101',
            'lmt': '120'
           }
        respons=requests.get(url=url,headers=headers,params=params).text
        print(respons)


stock('601096','5')
