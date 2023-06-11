MAX_MSG_SIZE = 4096  # bytes

def read_and_ack(client_socket):
    # number of bytes to receive from socket depends of decimal points
    read_bytes = client_socket.recv(MAX_MSG_SIZE)
    client_socket.send(b'Ack \n')  # send ack on received data

    return read_bytes
