import socket


# create a socket object
UDP_CLIENT = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# get local machine name
server_info = ("127.0.0.1", 9999)
MESSAGE = b"hello"
BUFFER_SIZE = 1024


UDP_CLIENT.sendto(MESSAGE, server_info)
msg = UDP_CLIENT.recvfrom(BUFFER_SIZE)
print(msg[0].decode())

