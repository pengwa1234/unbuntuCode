from socket import *
import struct


#创建一个udp连接
udpSocket=socket(AF_INET,SOCK_DGRAM)

fileLen=len('01-tftp-下载文件.py')
#发送个服务器的数据格式
sendData=struct.pack('!H%ssb5sb'%fileLen,2,'01-tftp-下载文件.py'.encode('utf-8'),0,'octet'.encode('utf-8'),0)

ip_port=('192.168.0.102',69)
#发送数据给服务器
udpSocket.sendto(sendData,ip_port)

#打开一个文件，读取里面的内容
f=open('01-tftp-下载文件.py','rb')

#本地块序号
local_num=1

while True:
   # 从服务器接收到数据
    recvData=udpSocket.recvfrom(1024)
    #获取到数据和ip部分
    data,ip_port=recvData
    
    #将数据按照大端的格式分解出确认码和块编号
    flag,block=struct.unpack('!HH',data[:4])

    if flag==5:
        print("异常发生，无法上传文件")
        break
    elif flag==4:
        #构建发送的数据包
        bagData=f.read(512)
        sendData=struct.pack('!HH512s',3,local_num,bagData)
        
        if len(sendData)<=0:
            print("数据传输完毕")
            break
        udpSocket.sendto(sendData,ip_port)
        
        if local_num<65535:
            local_num+=1
        else:
            local_num=1

f.close()
udpSocket.close()

           

