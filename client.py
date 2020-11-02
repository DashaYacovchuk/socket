import socket

MAX_CONNECTIONS = 20
address_to_server = ('localhost', 8686)

clients = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(MAX_CONNECTIONS)]
for client in clients:
    client.connect(address_to_server)
for i in range(MAX_CONNECTIONS):
    clients[i].send(bytes("10 73 52 31 82" + str(i), encoding='UTF-8'))

for client in clients:
    data = client.recv(1024)
    result = data.decode('utf-8')
    print(result)