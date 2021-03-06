# NW_Socket_Practice

## [SWE3022] Basic Socket Programming

### Application Layer -- [Socket] -- Transport Layer(TCP)

### 1. Server
- Create serverSocket
- Wait for client connection request 
- If client requests for connection, accept() and create connectionSocket
- Read request from connectionSocket
- Write reply to connectionSocket
- Close connectionSocket
- Wait for next client connection (serverSocket still open)

![image](https://user-images.githubusercontent.com/55427886/111873856-b903b780-89d5-11eb-9d27-8edc16219b60.png)


### 2. Client
- Create clientSocket
- Request connection to server
```
clientSocket.connect(x,y) # x: Server IP, y: Server Port
```
- Send request using clientSocket
- Read reply from clientSocket
- Close clientSocket

![image](https://user-images.githubusercontent.com/55427886/111873830-9ec9d980-89d5-11eb-9264-8eaedcee0162.png)
