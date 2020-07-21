from socket import *

udpSocket=socket(AF_INET,SOCK_DGRAM)
udpSocket.bind(("",7788))

num=1
while True:
    recvData=udpSocket.recvfrom(1024)
    udpSocket.sendto(recvData[0],recvData[1])

    print("已经将接收的第%d个数据返回给对方,内容为：%s"%(num,recvData[0]))
    num+=1

udpSocket.close()
