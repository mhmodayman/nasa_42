

def set_Inp_IPC_config():
    OutfileName = '../Tx/Inp_IPC.txt'
    outfile = open(OutfileName, 'w')

    outfile.write('<<<<<<<<<<<<<<< 42: InterProcess Comm Configuration File >>>>>>>>>>>>>>>>\n')
    outfile.write('1                                       ! Number of Sockets\n')
    outfile.write('**********************************  IPC 0   *****************************\n')
    outfile.write('Tx                                     ! IPC Mode (OFF,TX,RX,TXRX,ACS,WRITEFILE,READFILE)\n')
    outfile.write('0                                       ! AC.ID for ACS mode\n')
    outfile.write('"State00.42"                            ! File name for WRITE or READ\n')
    outfile.write('SERVER                                  ! Socket Role (SERVER,CLIENT,GMSEC_CLIENT)\n')
    outfile.write('localhost     10001                     ! Server Host Name, Port\n')
    outfile.write('TRUE                                    ! Allow Blocking (i.e. wait on RX)\n')
    outfile.write('TRUE                                    ! Echo to stdout\n')
    outfile.write('5                                       ! Number of TX prefixes\n')
    outfile.write('"Orb[0].PosN"				! Prefix 0\n')
    outfile.write('"Orb[0].VelN"				! Prefix 1\n')
    outfile.write('"SC[0].A_B"				! Prefix 2\n')
    outfile.write('"SC[0].Q_B"				! Prefix 3\n')
    outfile.write('"SC[0].wbl_B"				! Prefix 4\n')

    outfile.write('\n')
    outfile.close()
