student_list=[]

def main():
    while True:
        menu()#输出主页面
        button=int(input("请输入功能的代号"))
        if button==1:
            add()#增加学生信息
        elif button==2:
            Delete()#删除学生信息
        elif button==3:
            Locat()#查询学生信息
        elif button==4:
            Change()#改变学生信息
        elif button==0:
            print("退出学生信息管理系统")
            choose=input("输入y or Y")
            if choose=='y'or'Y':
                break
            else:
                continue

def menu():
    print("*******************************")
    print("******欢迎进入学生管理系统*******")
    print("*******************************")
    print(" ")
    print("*******************************")
    print("***** 0:退出学生信息管理系统*****")
    print("***** 1:增加学生信息************")
    print("***** 2:删除学生信息************")
    print("***** 3:查询学生信息************")
    print("***** 4:改变学生信息************")
    print("*******************************")

def add():
    global student_list
    while True:
        id=int(input("输入学生id"))
        name=input("输入学生姓名")
        try:
            chinese=int(input("输入语文成绩"))
            match=int(input("输入数学成绩"))
            english=int(input("输入英语成绩"))
        except:
            print("非法输入")
            continue
        for stu in student_list:
            if stu['name']==name:
                print("学生已存在")
                return
            if stu['id']==id:
                print("学生已存在")
                return 
        student={'id':id,'name':name,'chinese':chinese,'match':match,'english':english}
        student_list.append(student)
        answer=input("是否继续输入 y or Y")
        if answer=='y'or answer=='Y':
            continue
        else:
            break
    print("学生信息录入完毕")

def Delete():
    global student_list
    while True:
        mode=int(input("输入删除的的模式 0:学号， 1:姓名"))
        if mode==0:
            num=int(input("输入要删除学生的学号"))
            for number in student_list:
                if number['id']==num:
                    student_list.remove(number)
            print("输入的学生不存在")
        elif mode==1:
            name=input("输入学生的姓名")
            for student in student_list:
                if student==name:
                    student_list.remove(student)
            print("输入的学生id不存在")
        return None

def Locat():
    global student_list
    while True:
        mode=int(input("选择要查询的模式 0:学号， 1:姓名"))
        if mode==0:
            num=int(input("输入要查询学生的学号"))
            for number in student_list:
                if num==number['id']:
                    print(number)
            print("输入的学生学号不存在")
            return None
        elif mode==1:
            name=input("输入要查询学生的姓名")
            for student in student_list:
                if name==student['name']:
                    student_list.remove(student)
                    return 0
        print("输入的学生姓名不存在")
        return None

def Change():
    global student_list
    while True:
        name=input("输入要改变的学生的姓名")
        for student in student_list:
            if name==student['name']:
                student_list['chinese']=int(input("输入语文成绩"))
                student_list['match']=int(input("输入数学成绩"))
                student_list['english']=int(input("输入英语成绩"))
                print("修改成功")
                return 0
        print("输入的学生姓名不存在")
        return None
def show():
    print("id\tname\tchinese\tmatch\tenglish")
    print(" ")
    for student in student_list:
        print(f"{student['id']}\t{student['name']}\t{student['chinese']}\t{student['match']}\t{student['english']}")

main()
show() 