def parse_a_instance(a_bytes: bytearray):
    """
    _summary_

    Args:
        angles_bytes (bytearray): Ex: b'SC[0].A_B = -1.741719449276e-04 -2.136206927920e-04 1.121205523335e-04'

    Returns:
    """

    ab = a_bytes[12:].split(' ')

    print('Euler angles of B in L (expressed in B) ::       ', [float(x) for x in ab])
