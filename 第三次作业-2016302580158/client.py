import socket

host = 'localhost'
port = 8000

cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cl.connect((host, port))
print("若想关闭连接，请输入#")
while True:
    client_input = input("请输入想要发送的消息：")
    cl.send(client_input.encode())
    re_data = cl.recv(1024)
    print("来自服务器的回应：" + re_data.decode())
    if client_input == '#':
        cl.close()
        break
