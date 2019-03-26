import socket

host = '0.0.0.0'
port = 8000
so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
so.bind((host, port))
so.listen(1)

con, address = so.accept()
print("开始一个新的连接，客户端地址是：", address)
while True:
        data = con.recv(1024)
        if not data:
            break
        ans = bytes("已接受来信：", encoding='utf-8')
        con.send(ans+data)
        print("收到客户端(%s,%s)的消息: " % address + data.decode())
so.close()

