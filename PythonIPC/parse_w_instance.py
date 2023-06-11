def parse_w_instance(w_bytes: bytearray):
    """
    _summary_

    Args:
        w_bytes (bytearray): Ex: b'SC[0].wbl_B = -1.741719449276e-04 -2.136206927920e-04 1.121205523335e-04'

    Returns:
    """

    wb = w_bytes[14:].split(' ')

    print('Angular velocity of B in L (expressed in B) ::    ', [float(x) for x in wb])
