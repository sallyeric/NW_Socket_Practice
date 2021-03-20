from socket import *

serverIP = '192.168.0.104'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))

msg = input('Input lowercase sentence: ')
clientSocket.send(msg.encode())

newMsg = clientSocket.recv(1024)
print('From Server: ', newMsg.decode())
clientSocket.close()