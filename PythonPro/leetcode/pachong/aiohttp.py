import asyncio 
import time 
import aiohttp

start=time.time()
urls=[]

async def get_page(url):
    async with aiohttp.ClientSession() as session:
        # get(),post()
        # headers,params/data,proxy='http://ip:port'
        async with await session.get(url) as response:
            # text()返回字符形式的响应数据
            # read()返回的二进制形式的响应数据
            # json返回的是json对象的响应数据
            # 注意:获取响应数据之前一定要使用await进行手动挂起
            page_text=await response.text()
            print(page_text)

tasks=[]

for url in urls:
    c=get_page(url)
    task=asyncio.ensure_future(c)
    task.append(task)