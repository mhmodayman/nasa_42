def parse_Pos_instance(Pos_bytes: bytearray):
    """
    _summary_

    Args:
        Pos_bytes (bytearray): Ex: b'Orb[0].PosN = 6.978144836285e+06 8.452605838528e+02 1.253150349842e+03'

    Returns:
    """

    posn = Pos_bytes[14:].split(' ')

    print('Inertial position ::             ', [float(x) for x in posn])
