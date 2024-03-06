import requests 
import re 
import os 
from lxml import etree
url='https://v26-web.douyinvod.com/42eddff13ccebb068f2ef6c63c3ca094/659d0e98/video/tos/cn/tos-cn-ve-15/e0d1729e968d435796474c54565cc9bf/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=689&bt=689&cs=0&ds=3&ft=LjhJEL998xl8uEemD0P5H4eaciDXtLN5o_QEeuJtiNLD1Inz&mime_type=video_mp4&qs=0&rc=ZDc7aTdnNDRnZzxoO2Y2O0BpMzdoOXB0bWU7MzMzPGkzM0BiXzExNmJfX18xYjUzYmM2YSNvZDVwZmlib2lgLS1jLTBzcw%3D%3D&btag=e00010000&dy_q=1704788089&l=20240109161448F29E1A2FED059F05C204'

headers={
    'Accept':'*/*',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
   'Sec-Ch-Ua':
'"Not_A Brand";v="8", '"Chromium"';v="120", "Microsoft Edge";v="120"',
'Sec-Ch-Ua-Mobile':
'?0',
'Sec-Ch-Ua-Platform':
'"Windows"',
'Sec-Fetch-Dest':
'video'
}

respons=requests.get(url=url,headers=headers).text
