import socket

UDP_IP = "35.161.72.250"
UDP_PORT = 8080

while True:
    message = intput("Enter your message: ")
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.sendto(message, (UDP_IP, UDP_PORT))
