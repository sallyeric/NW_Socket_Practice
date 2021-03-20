from socket import *

serverIP = 'IP주소' #wsl에서 ifconfig의 inet
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))

msg = input('Input lowercase sentence: ')
clientSocket.send(msg.encode())

newMsg = clientSocket.recv(1024)
print('From Server: ', newMsg.decode())
clientSocket.close()