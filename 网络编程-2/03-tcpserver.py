from socket import *

serverSocket=socket(AF_INET,SOCK_STREAM)

#绑定任何一个电脑上的ip，端口是8899
serverSocket.bind(("",8899))

#服务器最多可以同时接收5个客户端发送的数据
serverSocket.listen(5)

print("--------1--------")

clientSocket,clientInfo=serverSocket.accept()
print("-----2-----------")
#clientSocket表示新的客户端
#clientInfo表示新的客户端的ip及port

print(clientSocket,clientInfo)
recvData=clientSocket.recv(1024)

print("--------3---------")
print("%s:%s"%(str(clientInfo),recvData.decode("gb2312")))

clientSocket.close()
serverSocket.close()
