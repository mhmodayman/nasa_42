def parse_Vel_instance(Vel_bytes: bytearray):
    """
    _summary_

    Args:
        Vel_bytes (bytearray): Ex: b'Orb[0].VelN = -1.637147642420e+00 4.226301845533e+03 6.265750157340e+03'

    Returns:
    """

    veln = Vel_bytes[14:].split(' ')

    print('Inertial velocity ::             ', [float(x) for x in veln])
