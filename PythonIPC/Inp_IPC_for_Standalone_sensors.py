

def set_Inp_IPC_config():
    OutfileName = '../Standalone/Inp_IPC.txt'
    outfile = open(OutfileName, 'w')

    outfile.write('<<<<<<<<<<<<<<< 42: InterProcess Comm Configuration File >>>>>>>>>>>>>>>>\n')
    outfile.write('1                                       ! Number of Sockets\n')
    outfile.write('**********************************  IPC 0   *****************************\n')
    outfile.write('ACS                                     ! IPC Mode (OFF,TX,RX,TXRX,ACS,WRITEFILE,READFILE)\n')
    outfile.write('0                                       ! AC.ID for ACS mode\n')
    outfile.write('"State00.42"                            ! File name for WRITE or READ\n')
    outfile.write('SERVER                                  ! Socket Role (SERVER,CLIENT,GMSEC_CLIENT)\n')
    outfile.write('localhost     10001                     ! Server Host Name, Port\n')
    outfile.write('TRUE                                    ! Allow Blocking (i.e. wait on RX)\n')
    outfile.write('TRUE                                    ! Echo to stdout\n')
    outfile.write('1                                       ! Number of TX prefixes\n')
    outfile.write('"SC[0].AC.Gyro[0].Rate"			! Prefix 0\n')

    outfile.write('\n')
    outfile.close()
