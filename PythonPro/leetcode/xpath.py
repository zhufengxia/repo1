from lxml import etree 
import xpath
import requests 
url='https://pic.netbian.com/4kmeinv/'

headers={
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

respons_text=requests.get(url=url,headers=headers).text
tree=etree.HTML(respons_text)
li_list=tree.xpath('//div[@class="slist"]/ul[@class="clearfix"]/li')
fp=open("./picture.jpg","wb")
for li in li_list:
   picture_url=li.xpath('./a/img/@src')[0]
   pictrue_url='https://pic.netbian.com'+picture_url
   respons=requests.get(url=pictrue_url,headers=headers).content
   fp.write(respons)
fp.close()