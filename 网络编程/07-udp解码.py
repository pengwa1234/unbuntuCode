from socket import *

udpSocket=socket(AF_INET,SOCK_DGRAM)

udpSocket.bind(("192.168.0.108",7788))
recvData=udpSocket.recvfrom(1024)

print(recvData)

#content,destInfo=recvData

#print(a.decode("gb2312"))

#print(b.decode("utf-8"))
