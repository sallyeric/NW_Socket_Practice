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
- Wait for next client connection (serverSocket still opened)


### 2. Client
- Create clientSocket
- Request connection to server
```
clientSocket.connect(x,y) # x: Server IP, y: Server Port
```
- Send request using clientSocket
- Read reply from clientSocket
- Close clientSocket