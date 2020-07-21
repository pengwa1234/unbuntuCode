from socket import *
import struct

#创建套接字连接
udpSocket=socket(AF_INET,SOCK_DGRAM)

#发送给服务器的数据格式
data=struct.pack('!H8sb5sb'.encode("utf-8"),1,'test.png'.encode("utf-8"),0,'octet'.encode("utf-8"),0)
#ip,port="10.1.10.232",69

ip,port="192.168.0.102",69
#向服务器发送一个下载请求:tftp服务的端口是69
udpSocket.sendto(data,(ip,port))


f=open("test.png","wb")


#如果文件接收完，就退出程序，如果没有就继续将文件写入创建的文件中

while True:

    #从服务器接收数据
    recvData=udpSocket.recvfrom(1024)
    data,ip_port=recvData
    print(ip_port)
    #提取操作码和块编码数据
    flag,block=struct.unpack("!HH",data[:4])
    if flag==5:
        print("服务器没有该文件！")
        break
    elif flag==3:
        filedata=data[4:]    
        if len(filedata)<512: 
            print("数据传输完毕！")    
            break
        else:
            f.write(filedata)
            ackData=struct.pack("!HH",4,block)
            print("收到(%s)的数据"%block)
            udpSocket.sendto(ackData,ip_port)

f.close()
udpSocket.close()



