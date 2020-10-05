import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8086       # Port to listen on (non-privileged ports are > 1023)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'Hi server',(HOST,PORT))