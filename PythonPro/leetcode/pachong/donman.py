import requests 
from lxml import etree 

url='https://ac.qq.com/Comic/comicInfo/id/531040'

headers={
    'Cookie':
'qq_domain_video_guid_verify=575f8e9b1d722c91; _qimei_uuid42=18109101b091006f83472891f5a4b8d2e2308cc407; _qimei_fingerprint=63cdc74b5ee8ca3f649c5ac65b0006a8; pgv_pvid=321249732; _qimei_q36=; _qimei_h38=936f093983472891f5a4b8d20200000eb18109; nav_userinfo_cookie=; ac_wx_user=; Hm_lvt_f179d8d1a7d9619f10734edb75d482c4=1704847204; __BEACON_deviceId=bsdNZ500hwQDX24Fmd9YkbfZ3FzzPJ8a; theme=dark; readLastRecord=%5B%5D; roastState=0; _qpsvr_localtk=0.36710082256680443; readRecord=%5B%5B531040%2C%22%E6%96%97%E7%A0%B4%E8%8B%8D%E7%A9%B9%22%2C1%2C%2201%22%2C1%5D%2C%5B505430%2C%22%E8%88%AA%E6%B5%B7%E7%8E%8B%22%2C1%2C%22%E7%AC%AC1%E8%AF%9D%20ROMANCE%20DAWN%20%E5%86%92%E9%99%A9%E7%9A%84%E5%BA%8F%E5%B9%95%22%2C1%5D%5D; Hm_lpvt_f179d8d1a7d9619f10734edb75d482c4=1704850105',
'Sec-Ch-Ua':
'"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
'Sec-Ch-Ua-Mobile':
'?0',
'Sec-Ch-Ua-Platform':
'"Windows"',
'Sec-Fetch-Dest':
'document',
'Sec-Fetch-Mode':
'navigate',
'Sec-Fetch-Site':
'none',
'Sec-Fetch-User':
'?1',
'Upgrade-Insecure-Requests':
'1',
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

respons=requests.get(url=url,headers=headers).text 
respons_html=etree.HTML(respons)
em_list=respons_html.xpath('//div[3]//div[@class="works-chapter-list-wr ui-left"]/ol[1]/li[1]/p[1]/span[1]/a/@href')
li_url='https://ac.qq.com'+em_list[0]
manhua_li_text=requests.get(url=li_url,headers=headers).text
manhua_html=etree.HTML(manhua_li_text)
manhua_list=manhua_html.xpath('./div')
print(manhua_list)