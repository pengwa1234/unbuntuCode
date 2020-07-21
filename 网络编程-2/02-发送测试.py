import struct
from socket import *

udpSocket=socket(AF_INET,SOCK_DGRAM)

#data=struct.pack('!H8sb5sb',1,'test.png',0,'octet',0)

data=struct.pack("!H8sb5sb",1,"test.png".encode("utf-8"),0,"octet".encode("utf-8"),0)

udpSocket.sendto(data,("192.168.0.102",69))

#udpSocket.sendto(data,("10.1.10.232",69))
udpSocket.close()
