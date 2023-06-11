def parse_time_instance(time_bytes: bytearray):
    """
    _summary_

    Args:
        time_bytes (bytearray): Ex: b'TIME 2014-172-00:00:00.200000000'

    Returns:
        year    int:
        day     int:
        hour    int:
        minute  int:
        second  float:
    """

    TIME   = time_bytes[5:].split('-')
    year   = int(TIME[0])
    day    = int(TIME[1])
    HMS    = TIME[2].split(':')
    hour   = int(HMS[0])
    minute = int(HMS[1])
    second = float(HMS[2])

    print(f"year is {year}, day is {day}, hour is {hour}, minute is {minute}, second is {second}")

    return year, day, hour, minute, second
