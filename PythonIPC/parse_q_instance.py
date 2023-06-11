def parse_q_instance(q_bytes: bytearray):
    """
    _summary_

    Args:
        quaternion_bytes (bytearray): Ex: b'SC[0].Q_B = 3.988104041961e-02 -1.093784192349e-02 1.498945602886e-02 9.990321228254e-01'

    Returns:
    """

    qb = q_bytes[12:].split(' ')

    print('Quaternion, scalar is last element, of B in L (expressed in B) ::       ', [float(x) for x in qb])
