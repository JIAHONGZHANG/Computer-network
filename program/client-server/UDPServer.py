from socket import *

while 1:
    serverPort = 13000
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    message, clientAddress = serverSocket.recvfrom(2048)
    serverSocket.sendto(message.encode('utf-8'), clientAddress)