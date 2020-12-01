import socket
import random
MAX_CONNECTIONS = 10
address_to_server = ('localhost', 8686)
clients = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(MAX_CONNECTIONS)]
for client in clients:
    client.connect(address_to_server)
for i in range(MAX_CONNECTIONS):
    numbers_client = [random.randint(10, 100) for k in range(10)]
    listToStr = ' '.join([str(elem) for elem in numbers_client])
    print(listToStr)
    clients[i].send(bytes(listToStr, encoding='UTF-8'))

for client in clients:
    data = client.recv(1024)
    result = data.decode('utf-8')
    print(result, '\n')