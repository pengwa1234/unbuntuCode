from socket import *
import sys

#给飞秋广播
dest=("<broadcast>",2425)

#创建套接字
udpSocket=socket(AF_INET,SOCK_DGRAM)

#创建允许发送广播的地址
udpSocket.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

#发送广播的内容
udpSocket.sendto("收到消息了吗？")

print("等待对方回复(按ctl+c退出))

while True:
    (buf,address)=udpSocket.recvfrom(2048)
    print("Recevied from %s:%s"%(buf,address))

