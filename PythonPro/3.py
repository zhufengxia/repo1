import socket
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
while True:
    data:str=conn.recv(1024).decode("UTF-8")
    print(f"客户端发来的信息是,{data}")
    msg=input("请输入你要和客户端回复的信息:")
    if msg=='exit':
        break
    conn.send(msg.encode("UTF-8"))
conn.close()
socket_server.close()
