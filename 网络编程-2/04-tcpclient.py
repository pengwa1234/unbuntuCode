from socket import *

#创建套接字
clientSocket=socket(AF_INET,SOCK_STREAM)

#连接服务器
clientSocket.connect(("192.168.0.105",8989))

#向服务器发送数据 
#1.tcp客户端已经连接好了服务器，所以在以后的数据发送中，不需要
#填写接收方的ip和port
clientSocket.send("haha".encode("gb2312"))

#接收数据
recvData=clientSocket.recv(1024)

print("recvData:%s"%recvData.decode("gb2312"))


#关闭套接
clientSocket.close()
