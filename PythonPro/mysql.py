from pymysql import Connection
conn=None
try:
    conn=Connection(
        host="localhost",   #主机名
        port=3306,          #端口
        user="root",        #链接方式
        password="123456"   #密码
        # database='xxx'    #指定数据库
        # autocommit        #设置自动提交
    )
    # 创建游标对象
    cursor=conn.cursor()
    # 定义一个建表SQL语句
    sql="""
    alter table python_sql add column sex varchar(2);
    """
    # 选择要操作的数据库
    conn.select_db("db_python")
    # 使用游标对象，执行SQL
    # cursor.execute(sql)
    # 查询数据
    # cursor.execute('select *from python_sql')
    # cursor.execute("insert into python_sql values(null,'小明',19,'男')")
    # 查询插入的主键id
    # print("主键id=",conn.insert_id)
    # 更新数据
    # cursor.execute("update python_sql set age=24 where id=1")
    # 删除数据
    # cursor.execute("delete from python_sql where id=1")
    # 调用存储过程
    cursor.execute("call xxx(1,2,@x)")
    cursor.execute("select @x")
    result=cursor.fetchone()
    conn.commit()
except Exception as e:
    print("异常:",e)
finally:
    conn.close()