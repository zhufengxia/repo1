import requests 
import json

url="https://fanyi.baidu.com/sug"

headers={
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

data={
    'kw':"submission" 
}

res=requests.post(url=url,headers=headers,data=data)
print(res.json())