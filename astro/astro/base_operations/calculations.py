import math


def hms_to_radians(hours: int or float, minutes: int or float = 0, seconds: int or float = 0) -> float:
    """
    Method convert hours, minutes and seconds to radians

    Args:
        hours: Hours
        minutes: Minutes
        seconds: Seconds

    Returns:
        Returns the value of the hour angle in radians
    """
    negative_flag = False
    if hours < 0:
        hours = abs(hours)
        negative_flag = True
    decimal_degrees = (hours + minutes / 60 + seconds / 3600) * 15
    radians = math.radians(decimal_degrees)
    return -radians if negative_flag else radians


def dms_to_radians(degrees: int or float, minutes: int or float = 0, seconds: int or float = 0) -> float:
    """
    Method convert degrees, minutes and seconds to radians

    Args:
        degrees: Degrees
        minutes: Minutes
        seconds: Seconds

    Return:
        Returns the angle value in radians
    """
    negative_flag = False
    if degrees < 0:
        degrees = abs(degrees)
        negative_flag = True
    decimal_degrees = degrees + minutes / 60 + seconds / 3600
    radians = math.radians(decimal_degrees)
    return -radians if negative_flag else radians


def radians_to_hms(rad: float) -> tuple:
    """
    Method convert radians to hours, minutes and seconds

    Args:
        rad: Angle in radians

    Returns:
        Returns the tuple with hours, minutes and seconds
    """
    negative_flag = False
    if rad < 0:
        rad = abs(rad)
        negative_flag = True
    hours = rad * 12 / math.pi
    minutes, seconds = divmod(hours * 3600, 60)
    hours, minutes = divmod(minutes, 60)
    return (int(-hours), int(minutes), seconds) if negative_flag else (int(hours), int(minutes), seconds)


def radians_to_dms(rad: float) -> tuple:
    """
        Method convert radians to degrees, minutes and seconds

        Args:
            rad: Angle in radians

        Returns:
            Returns the tuple with degrees, minutes and seconds
    """
    negative_flag = False
    if rad < 0:
        rad = abs(rad)
        negative_flag = True
    degrees = math.degrees(rad)
    minutes, seconds = divmod(degrees * 3600, 60)
    degrees, minutes = divmod(minutes, 60)
    return (int(-degrees), int(minutes), seconds) if negative_flag else (int(degrees), int(minutes), seconds)


def radians_to_hms_str(rad: float) -> str:
    """
    Method converts radians to hours, minutes and seconds for accurate string output

    Args:
        rad: Angle in radians

    Returns:
        Returns a formatted string
    """
    angle = radians_to_hms(rad)
    out = f'{angle[0]}h {angle[1]}m {angle[2]}s'
    return out


def radians_to_dms_str(rad: float) -> str:
    """
    Method converts radians to degrees, minutes and seconds for accurate string output

    Args:
        rad: Angle in radians

    Returns:
        Returns a formatted string
    """
    angle = radians_to_dms(rad)
    out = f'{angle[0]}° {angle[1]}\' {angle[2]}"'
    return out


def calculate_distance(ra1: float, dec1: float, plx1: float, ra2: float, dec2: float, plx2: float) -> float:
    """
    Для использования этой функции необходимо передать значения восхождения, склонения и параллакса двух звезд в градусах. Функция возвращает расстояние между звездами в парсеках.
    """
    
    # TODO: надо сделать перевод для парралакса, потому что на входе другие единицы измерения 


    # Преобразование восхождения и склонения в радианы
    ra1 = math.radians(ra1)
    dec1 = math.radians(dec1)
    ra2 = math.radians(ra2)
    dec2 = math.radians(dec2)

    # Еще надо подумать по поводу перегрузки функции, но это уже можно будет оставить на доработку
    # Можно сразу получать значения в радианах

    # Преобразование параллакса в расстояние в парсеках
    d1 = 1 / (plx1 / 1000)
    d2 = 1 / (plx2 / 1000)

    # Вычисление декартовых координат звезд
    x1 = d1 * math.cos(dec1) * math.cos(ra1)
    y1 = d1 * math.cos(dec1) * math.sin(ra1)
    z1 = d1 * math.sin(dec1)

    x2 = d2 * math.cos(dec2) * math.cos(ra2)
    y2 = d2 * math.cos(dec2) * math.sin(ra2)
    z2 = d2 * math.sin(dec2)

    # Вычисление евклидова расстояния
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    return dist


if __name__ == '__main__':
    print(radians_to_hms_str(math.pi))
    print(radians_to_hms_str(-math.pi))
    print(radians_to_dms_str(math.pi))
    print(radians_to_dms_str(-math.pi))
    print(hms_to_radians(12))
    print(hms_to_radians(-12))
    print(dms_to_radians(180))
    print(dms_to_radians(-180))