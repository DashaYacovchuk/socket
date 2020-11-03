import select
import socket

SERVER_ADDRESS = ('localhost', 8686)

MAX_CONNECTIONS = 15
numbers_server = {1,2,3}
in_ = list()
out_ = list()


def get_non_blocking_server_socket():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(0)
    server.bind(SERVER_ADDRESS)
    server.listen(MAX_CONNECTIONS)
    return server


def readables(read, server):
    for resource in read:
        if resource is server:
            connection, client_address = resource.accept()
            connection.setblocking(0)
            in_.append(connection)
            print("new connection from {address}".format(address=client_address))
        else:
            data = ""
            try:
                global res
                data = resource.recv(1024)
                data = data.decode('utf-8')
            except ConnectionResetError:
                pass
            if data:
                set1 = set(data.split())
                for i in list(set1):
                    if i == " ":
                        set1.discard(i)
                set2 = set(map(int, set1))
                for i in list(set2):
                    if i > 55:
                        set2.discard(i)
                fin = set2.union(numbers_server)
                fin = sorted(fin)
                res = str(fin)
                if resource not in out_:
                    out_.append(resource)
            else:
                clear(resource)


def clear(resource):
    if resource in out_:
        out_.remove(resource)
    if resource in in_:
        in_.remove(resource)
    resource.close()
    print('closing connection ' + str(resource))


def writables(write):
    for resource in write:
        try:
            global res
            resource.send(str(res).encode())
        except OSError:
            clear(resource)


if __name__ == '__main__':
    server_socket = get_non_blocking_server_socket()
    in_.append(server_socket)
    print("server is running, please, press ctrl+c to stop")
    try:
        while in_:
            read, write, exceptional = select.select(in_, out_, in_)
            readables(read, server_socket)
            writables(write)
    except KeyboardInterrupt:
        clear(server_socket)
        print("Server stopped! Thank you for using!")