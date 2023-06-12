import socket
from read_and_ack import read_and_ack
from parser import parse_all
from Inp_IPC_for_Tx import set_Inp_IPC_config


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

    """
    See Nomenclature.pdf file
    See mathkit.c file
    See 42types.h file

    SC.B[0]:       is the main body frame, L is LVLH, and N is inertial (Newtonian)

    SC[0].wln:     Angular velocity of L in N, expressed in N
    SC[0].B[0].wn: Angular velocity of B in N, expressed in B

    SC[0].wbl_B:   Angular velocity of B in L, expressed in B

    SC[0].A_B      euler angles [Roll_B, Pitch_B, Yaw_B] of B in L (rad) (expressed in B)
    SC[0].Q_B      quaternion of B in L (expressed in B), scalar part is the last element in the vector

    SC[0].CLN:     DCM of L in N (or from N in L)
    SC.B[0].CN:    DCM of B in N (or from N to B)

    World 0:       is sun
    World 3:       is earth

    GN:            Joint between N and B[0]

    line 0      -->         TIME
    line 1      -->         Orb[0].PosN      Position, [[m]], expressed in N [~=~]
    line 2      -->         Orb[0].VelN      Velocity, [[m/sec]], expressed in N [~=~]
    line 3      -->         SC[0].A_B        Euler angles [Roll_B, Pitch_B, Yaw_B] of B in L (expressed in B) [rad]
    line 3      -->         SC[0].Q_B        Euler angles [Roll_B, Pitch_B, Yaw_B] of B in L (expressed in B) [rad]
    line 4      -->         SC[0].wbl_B      Angular velocity of B in L (expressed in B) [rad/s]
    """

    try:
        read_bytes = read_and_ack(client_socket)
        parse_all(read_bytes)

    except socket.timeout:
        print('WARNING - timeout on receiving bytes from ethernet')
        break

client_socket.close()
