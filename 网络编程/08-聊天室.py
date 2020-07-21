from socket import *

def main():
    #创建一个套接字
    udpSocket=socket(AF_INET,SOCK_DGRAM)

    #绑定一个端口
    udpSocket.bind(("",7788))

    #接收数据
    while True:
        data=udpSocket.recvfrom(1024)
        print("[%s]:%s"%(str(data[1]),data[0].decode("gb2312")))   


if __name__=="__main__":
     main()
