from socket import *

udpSocket=socket(AF_INET,SOCK_DGRAM)

udpSocket.sendto(b"hhehe",("10.1.10.232",8080))

udpSocket.sendto(b"hahaha",("10.1.10.232",8080))
