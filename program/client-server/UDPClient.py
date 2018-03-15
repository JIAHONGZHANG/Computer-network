import socket
import time

serverName = '192.168.43.185'
serverPort = 12000
socket.setdefaulttimeout(1)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#message = input('Please input lowercase sentence: ')
for i in range(26):
    message = chr(97 + i)
    T = time.time()
    clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        newT = time.time()
        print(modifiedMessage.decode('utf-8'), end = ' ')
        print(f'trt = {round((newT - T) * 1000)} ms\r\n')
    except socket.timeout:
        print(f'{message} Response timeout!')
clientSocket.close()
