"""i="小美喜欢我"
k=input("输入内容")
if k==i:
    j=input("有多喜欢？")
    if j=="很喜欢":
        print("明天就去表白")
    elif j=="一点点":
        print("舔🐕")
else:
    print("🤡")
"""
"""import random
num=random.randint(1,100)
k=int(input("输入一个你要猜的数"))
i=0
while k!=num:
    if i>=1:
        k=int(input("再次输入你要猜的数"))
    i+=1
    if k>num:
        print("大了")
    else:
        print("小了")
    if k==num:
        print("恭喜你第%d次就猜中了"%i)
        break
"""
"""i=1
while i<=9:
    j=1
    while j<=i:
        print(f"{j}*{i}={j*i}\t",end=' ')
        j+=1
    i+=1
    print()
"""
"""number="666"
for x in number:
    print(x)
"""
"""num=100
num1=1
conut=0
"""
"""for x in range(num1,num):
    if x%2==0:
        conut+=1
print(conut)
"""

"""for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end=' ')
    print()
"""
"""import random
money=1*10**4
gongzi=1*10**3
for number in range(1,21):
    jixiao=random.randint(1,10)
    if money<=0:
        print(f"员工{number}没钱了叼毛")
    elif jixiao>=3:
        print(f"员工{number},绩效分{jixiao},发放工资{gongzi}")
        money-=gongzi
    else:
        print("天天摸鱼还想要钱?ya屎啦你")
"""

"""def my_len(data):
    conut=0
    for x in data:
        conut+=1
    return conut
str="666666666"
k=my_len(str)
print(k)

def say_hi():
    print("Hi 叼毛")
say_hi()
"""

"""def add(x,y):
    resulf=x+y
    print(f"x+y={resulf}")
x=int(input("输入x"))
y=int(input("输入y"))
add(x,y)
"""

"""def check_age(age):
    if age>=18:
        return "SUCCESS"
    else:
        return None
resulf=check_age(18)
if not resulf:
    print("小屁孩")
else:
    print("大叼毛")
"""
"""num=100

def test_a(number):
    global num
    num=666
    print(f"test_a:{num}")
test_a(num)
print(num)
"""

"""my_list=[1,2,3,666,666,666]
print(my_list)
i=len(my_list)
my_list.remove(666)
print(my_list)
my_list.extend([1,2,3])
print(my_list)
Count=my_list.count(666)
print(Count)
my_list.clear()
print(my_list)
print(i)
"""
"""mylist=[]
for x in range(10):
    mylist.append(x)
for i in range(10):
    print(mylist[i],end=' ')
    """

"""t1=('我是你爹',16,['football','music'])
print(t1.index(16),t1[0])
print(t1)
del t1[2][0]
t1[2].append('coding')
print(t1)
"""
"""mystr="itzhufeng it"
num=mystr.count('it')
new_mystr=mystr.replace(' ','|')
print(num,new_mystr)
new_mystr1=mystr.split("|")
print(new_mystr1,type(new_mystr1))
"""
"""my_list=[0,1,2,3,4,5,6]
resulf=my_list[::]
print(resulf)
"""
"""my_set_empty={"我是你爹","我是你爷"}
print(my_set_empty)
my_set_empty.add("我是你祖宗")
my_set={"我是你祖宗","我是你爹"}
my_set_empty.difference_update(my_set)
set3=my_set_empty.union(my_set)
print(my_set_empty,my_set,set3,len(set3))
for element in my_set_empty:
    print(element)
"""

"""my_list=['我是你爹','我是你爷','我是你祖宗']
my_set=set()
for element in my_list:
    print(element,end=' ')
for temp in my_list:
    my_set.add(temp)
for p in my_set:
    print(p,end=' ')
"""

"""my_dict={'我是你爹':{'语文':99,'数学':99,'英语':99},'我是你爷':{'语文':99,'数学':99,'英语':99},'我是你祖宗':{'语文':99,'数学':99,'英语':99}}
print(my_dict["我是你爹"]['数学'])
"""

"""my_dict=dict()
my_dict['我是你爹']=666
print(my_dict)
my_dict['我是你爷']=999
print(my_dict)
my_dict['我是你爹']=666666
print(my_dict)
k=my_dict.pop('我是你爹')
print(my_dict,k)
j=len(my_dict)
print(j)
print(my_dict.keys())
print(my_dict.values())
"""
"""lambda x,y:x+y
def text_func(compute):
    resulf=compute(1,2)
    print(resulf)
def compute(x,y):
    return x*y
text_func(lambda x,y:x+y)
"""

"""f=open("E:/.text","r",encoding="UTF-8")
print(f"读取五个字节的结果是{f.read(5)}")
"""
"""f=open("E:/text.txt","r",encoding="UTF-8")
print(f"读取二十个字节的结果是{f.read(20)}")
"""

"""from time import *
print("你好")
sleep(10)
print("我好")
"""

"""import niubi2
niubi2.text(6,6)
"""
"""list=[1,2,3,4,5,6,7,8,9]
print(max(list),min(list))
"""
"""from niubi2 import*
text_a(1,2)
text_b(2,1)
"""

"""import json
data=[{"name":"老王","age":16},{"name":"张三","age":20}]
data=json.dumps(data,ensure_ascii=False)
print(data)
data=json.loads(data)
print(data)
"""

"""class student:
    name=None
    gender=None
    nationality=None
    native_place=None
    age=None
    def __init__(self,name,gender,nationality,native_place,age):
        self.name=name
        self.gender=gender
        self.nationality=nationality
        self.native_place=native_place
        self.age=age
    def __str__(self):
        return f"{self.name},{self.gender},{self.nationality},{self.native_place},{self.age}"
    def __lt__(self,other):
        return self.age<other.age
    def __le__(self,other):
        return self.age<=other
    def __eq__(self,other):
        return self.age==other.age
stu=student("蔡徐坤","男","鸡国","鸡村","2.5")
stu_1=student("鸡哥","男","鸡国","鸡城","2.5")
print(str(stu))
print(stu.age<stu_1.age)
print(stu.age<=stu_1.age)
print(stu.age==stu_1.age)
"""

"""class Phone:
    __current_voltage=0
    def __keep_single_core(self):
        print("让CPU以单核模式运行")
    def call_by_5g(self):
        if self.__current_voltage>=1:
            print("5g通话已开启")
        else:
            print(f"电量不足,{str(self.__keep_single_core)}")
phone=Phone()
phone.call_by_5g()
"""

"""class phone:
    IMET=None
    producer=None

    def call_by_4g(self):
        print("4g通话")

class phone2022(phone):
    face_id=True

    def call_by_5g(self):
        print("2022最新5g通话")
"""

"""def add(x:int,y:int):
    return x+y
def func(data:list)->list:
    return data

from typing import Union
my_list:list[Union(int,str)]=[1,2,"坤"]
"""

# def account_create(initial_amount=0):
#         def atm(num,deposit=True):
#             nonlocal initial_amount
#             if deposit:
#                 initial_amount+=num
#                 print(f"存款+{num},账户余额{initial_amount}")
#             else:
#                 initial_amount-=num
#                 print(f"取款{num},账户余额{initial_amount}")
#         return atm

# fn=account_create()
# fn(10000)
# fn(20000)
# fn(100,False)


"""def outer(func):
    def inner():
        print("晚安,玛卡巴卡")
        func()
        print("起身啦,全世界!")
    return inner

@outer
def sleep():
    import random
    import time
    print("睡眠中...")
    time.sleep(random.randint(1,5))

sleep()
"""

"""class Person:
    pass
class Woeker(Person):
    pass

class Student(Person):
    pass
class Teacher(Person):
    pass
class PersonFactory:
    def get_person(self,p_type):
        if p_type=='w':
            return Woeker()
        elif p_type=='s':
            return Student()
        elif p_type=='t':
            return Teacher()
pf=PersonFactory()
woke=pf.get_person('w')
stu=pf.get_person('s')
tea=pf.get_person('t')
"""
"""import time
def sing(mag):
    while True:
        print(mag)
        time.sleep(1)
def dance(mag):
    while True:
        print(mag)
        time.sleep(1)

import threading

sing_thread=threading.Thread(target=sing,args=("我在唱歌,哈哈哈...",))
dance_thread=threading.Thread(target=dance,kwargs={"mag":"我在跳舞,啦啦啦..."})
sing_thread.start()
dance_thread.start()
"""

"""import socket
socket_server=socket.socket()
socket_server.bind(("localhost",8888))
socket_server.listen(1)
# resulf:tuple=socket_server.accept()
# conn=resulf[0]
# address=resulf[1]
conn,address=socket_server.accept()
#accept方法返回的是二元元组(链接对象，客户端地址信息)
#可以通过 变量 1 变量 2 =socket_server.accept()的形式,直接接受二元元组的两个元素
#accept()方法,是阻塞的方法,等待客户端的连接,如果没有客户端的连接会一直卡在这一行
print(f"接收到了客户端的连接,客户端的信息是:{address}")
data:str=conn.recv(1024).decode("UTF-8")
print(f"客户端发来的信息是,{data}")
msg=input("请输入你要和客户端回复的信息:").encode("UTF-8")
conn.send(msg)
conn.close()
socket_server.close()
"""


"""import re
s="python 666"
#resulf=re.match("python",s)
#print(resulf.group())

# resulf=re.search("python",s)
# print(resulf.group())

resulf=re.findall("python",s)
print(resulf)
"""

import re
s="wdnmd 666 !!"
resulf=re.findall(r'\d',s)
print(resulf)