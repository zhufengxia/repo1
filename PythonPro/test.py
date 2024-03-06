import efinance as ef 
import csv
from os.path import join
k=ef.stock.get_quote_history(stock_codes="000571",beg="20230101",end="20231215",klf=60)
# k.to_csv(f'000571.json',encoding="UTF-8-sig",index=None)
# 写入csv文件
# k.to_json("000571.json",index=None,force_ascii=False)
# 写入json文件
k.to_excel("E:\PythonPro\000571.xlsx",index=False)

"""""
data = {'玩具':['车','飞机','轮船'], '数量':[3,2,5], '价格':[100,90,80]} 
df_data = DataFrame(data)
df_data['数量'] = df_data['数量'].apply(str)
print(df_data)
"""
"""""
import requests
ssion=requests.session()
headers={"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
data = {"email":"mr_mao_hacker@163.com","password":"alarmchime"}
ssion.post("http://www.renren.com/PLogin.do",data=data)
response=ssion.get('http://www.renren.com/410043129/profile')
print(response.request.headers)
#print(response.encoding)
#print(response.url)
print(response.status_code)
print(response.text)
"""
'''from urllib.parse import urlencode
wd = "张三同学"
encode_res = urlencode({'k': wd}, encoding='utf-8')
# keyword = encode_res.split('=')[1]
print(encode_res)'''
"""
import requests
import re
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
response = requests.get('https://www.zhihu.com/explore', headers=headers)
result = re.findall("(ExploreSpecialCard-contentTitle|ExploreRoundtableCardquestionTitle).*?>(.*?)</a>", response.text)
print([i[1] for i in result])"""

