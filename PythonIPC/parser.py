from parse_time_instance import parse_time_instance
from parse_w_instance import parse_w_instance
from parse_a_instance import parse_a_instance
from parse_q_instance import parse_q_instance
from parse_Pos_instance import parse_Pos_instance
from parse_Vel_instance import parse_Vel_instance


def parse_all(read_bytes):
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


    read_str = read_bytes.decode('UTF-8').split('\n')

    parse_time_instance(read_str[0])
    parse_Pos_instance(read_str[1])
    parse_Vel_instance(read_str[2])
    parse_a_instance(read_str[3])
    parse_q_instance(read_str[4])
    parse_w_instance(read_str[5])

    print('\n ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: \n')
