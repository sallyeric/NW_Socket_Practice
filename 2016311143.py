# keep alive
import os
import time
import threading
import socket

#확장자 나누기 + threading
def http(client_socket) :
    data = client_socket.recv(65535)
    data = data.decode()
    print(data)

    try:    
        headers = data.split("\r\n")
        file_name = headers[0].split(" ")[1]
        print(file_name)
        # file_name2 = headers[0].split(" ")[1]
        _, extension = os.path.splitext(file_name)

        hypertext = ['.html', '.htm']
        image = ['.jpg', '.jpeg', '.png', '.bmp']

        if os.path.isfile('.'+ file_name):
            if extension in hypertext:
                file = open('.'+file_name, 'rt', encoding='utf-8')
                data = file.read()
                header = 'HTTP/1.1 200 0K\r\n\r\n'
                client_socket.send((header+data).encode('utf-8'))
            elif extension in image:
                client_socket.send('HTTP/1.1 200 OK\r\n'.encode())
                client_socket.send("Content-Type: image/png\r\n".encode())
                client_socket.send("Accept-Ranges: bytes\r\n\r\n".encode())
                with open('.' + file_name, 'rb') as sourceFile:
                    while True:
                        data = sourceFile.read(10000)
                        if not data:
                            break
                        client_socket.send(data)
            else:
                header = 'HTTP/1.0 404 File Not Found\r\n\r\n'
                client_socket.send((header+html).encode('utf-8'))
        else:
            header = 'HTTP/1.0 404 File Not Found\r\n\r\n'
            client_socket.send((header+html).encode('utf-8'))
    except Exception as e:
        print(e)
    client_socket.close()



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('192.168.0.100', 10080))
server_socket.listen(0)
print('listening...')

while True :
    client_socket, addr = server_socket.accept()
    print('accepting')
    t = threading.Thread(target=http, args=(client_socket,))
    t.start()