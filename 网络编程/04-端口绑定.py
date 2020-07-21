from socket import *

udpSocket=socket(AF_INET,SOCK_DGRAM)

#udpSocket.bind(("192.168.0.105",7788))
udpSocket.bind(("",7788))
#udpSocket.sendto(b"hahaha",("10.1.10.232",8080))


udpSocket.sendto(b"hahaha",("192.168.0.104",8080))
