from bs4 import BeautifulSoup
import requests 


url='https://www.shicimingju.com/book/sanguoyanyi.html'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

page_text=requests.get(url=url,headers=headers).text
soup=BeautifulSoup(page_text,'lxml')
li_list=soup.select('.book-mulu > ul > li')
fp=open('./sangguoyanyi.text','w',encoding="UTF-8")
for li in li_list:
    detail_url='https://www.shicimingju.com'+li.a['href']
    detail_page_text=requests.get(url=detail_url,headers=headers).text 
    detail_soup=BeautifulSoup(detail_page_text,'lxml')
    title=detail_soup.find('h1').string
    div_tag=detail_soup.find('div',class_='chapter_content')
    content=div_tag.text 
    fp.write(title+':'+content+'\n') 
fp.close()