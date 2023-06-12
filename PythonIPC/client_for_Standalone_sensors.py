import socket
from read_and_ack import read_and_ack
from parser import parse_all
from Inp_IPC_for_Standalone_sensors import set_Inp_IPC_config


set_Inp_IPC_config()
client_port = 10001
client_host = "127.0.0.1"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)  # AF_INET: IPv4, SOCK_DGRAM: UDP, SOCK_STREAM: TCP
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

    except socket.timeout:
        print('WARNING - timeout on receiving bytes from ethernet')
        break

client_socket.close()
