import time 
from multiprocessing.dummy import Pool
def get_page(str):
    print("正在下载 :",str)
    time.sleep(2)
    print("下载成功 :",str)
name_list=['蔡徐坤','鸡你太美','两年半']

start_time=time.time()

pool=Pool(3)
pool.map(get_page,name_list)

end_time=time.time()

print('%d'%(end_time-start_time))

