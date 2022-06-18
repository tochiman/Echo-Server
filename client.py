import socket
import sys

class Main():
    def __init__(self) -> None: 
        self.host = 'localhost'
        self.port = 8080
        self.server_address = (self.host, self.port)
        self.recv_size = 1024

    def content_send(self,message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(self.server_address)
            client_socket.send(message.encode('utf-8'))

            data = client_socket.recv(self.recv_size)

            print(data.decode('utf-8'))

if '__main__' == __name__:
    main = Main()
    message = sys.argv[1]

    if message == 'loop':
        while True:
            message = input("Please enter the words you want to send")
            if message == 'break':
                break
            else:
                main.content_send(message=message)
    else:
        main.content_send(message=message)

