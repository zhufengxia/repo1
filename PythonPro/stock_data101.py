import requests
import csv
# class Stock_his_data():

#     def __init__(self,time):
#         pass

def get_his_data(code:str,time:str):
    '''
    code是股票代码如'300059',
    time多少分钟数据1是一分钟数据,5是五分钟,15是十五分钟,30是三十分钟,60是六十分钟,101是日数据,102是周数据,103月数据
    '''
    market=['0','1','2','5','23']  #股票一部分市场,若不够可添加
    '''用来看看是哪个市场 若市场不对则不会有数据'''
    for i in range(len(market)):
            id=market[i]+'.'+code
            url = 'https://push2his.eastmoney.com/api/qt/stock/kline/get'
            params={
                    'fqt':'1',
                    'klt':time,
                    'fields2':'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63',
                    'fields1':'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13',
                    'secid':id,
                    'beg':20230101,
                    'end':20500101,
                    'rtntype':'6'
                }

            header= {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                        'Accept': '*/*',
                        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                    }
            result=requests.get(url=url,headers=header,params=params).text
            print(result)
#             try:
#                 res=result.split('"klines":')
#                 res=res[1]
#                 res=res[2:-4]
#                 res=res.split('","')
#                 filename=code+'.csv'
#                 fp=open(filename,'a',encoding='utf-8',newline="")
#                 csv_writer=csv.writer(fp)
#                 cs=csv_writer.writerow([" 时间 ","  open","close","high","low","amount","volume","振幅","涨幅","涨跌","换手率","未知一","时间戳"])
#                 for i in range(len(res)):
#                     res1=res[i].split(',')
#                     for j in res1:
#                         csv_writer=csv.writer(fp)
#                         csv_writer.writerow([res1[0],res1[1],res1[2],res1[3],res1[4],res1[5],res1[6],res1[7],res1[8],res1[9],res1[10],res1[11],res1[12]])
#             except:
#                 pass

#     fp.close()
#     print('ok')
# if __name__=='__main__':
#      get_his_data('003009',101)