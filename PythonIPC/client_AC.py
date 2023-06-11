import socket
from read_and_ack import read_and_ack
from parser import parse_all


client_port = 10001
client_host = "127.0.0.1"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM , 0)  # AF_INET: IPv4, SOCK_DGRAM: UDP, SOCK_STREAM: TCP
client_socket.setblocking(False)
client_socket.settimeout(10)


while True:
    try:
        client_socket.connect((client_host, client_port))
        break
    except OSError:
        pass

while True:
    try:
        read_bytes = read_and_ack(client_socket)
        parse_all(read_bytes)

        client_socket.send(b'SC[0].AC.Whl[0].Tcmd = 0.0001 \n[EOF]')
        print(client_socket.recv(4))  # receive ack on sent command (b'Ack\n')

        read_bytes = read_and_ack(client_socket)
        parse_all(read_bytes)

        client_socket.send(b'SC[0].AC.Whl[1].Tcmd = 0.0002 \n[EOF]')
        print(client_socket.recv(4))  # receive ack on sent command (b'Ack\n')

    except socket.timeout:
        print('WARNING Timedout on receiving bytes from ethernet')
        break

client_socket.close()
