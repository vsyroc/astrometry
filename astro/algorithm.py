import re
import csv

from astro.core.config import *
from astro.core.logger_settings import logger
from astro.base_operations.calculations import *


def print_interval(
        ra: float,
        dec: float,
        dev: int or float or tuple
) -> None:
    print(f'ra: {ra}\ndec: {dec}')
    if isinstance(dev, int) or isinstance(dev, float):
        print(f'deviation: {dev}°')
    elif isinstance(dev, tuple):
        print(f'deviation: {dev[0]}° {dev[1]}\' {dev[2]}"')
    ra_minus, ra_plus = finding_an_interval(ra, deviation=dev)
    dec_minus, dec_plus = finding_an_interval(dec, deviation=dev)
    print(
        f'ra minus: {ra_minus}\nra plus: {ra_plus}\ndec minus: {dec_minus}\ndec plus: {dec_plus}')


def get_data_from_csv(
        path: str
) -> list:
    with open(path) as table:
        reader = csv.reader(table, delimiter=',', quotechar='\n')
        rows = list(reader)
        new_rows = []
        source_id = your_star_source_id

        for row in rows:
            new_row = []
            for item in row:
                if re.search(r'\d+\.\d+', item) or re.search(r'\d+', item):
                    new_row.append(float(item))
            if new_row != [] and len(new_row) > 3 and new_row[0] != source_id:
                new_rows.append(new_row)
    return new_rows


def finding_true_coord(
        stars: list,
        t: int
) -> list:
    new_stars = []
    for i in range(len(stars)):
        name = stars[i][0]
        ra = stars[i][1]
        dec = stars[i][2]
        parallax = stars[i][3]
        pmra = stars[i][4]
        pmdec = stars[i][5]
        new_ra = dms_to_radians(ra) + dms_to_radians(0, 0, pmra / 1000) * t
        new_dec = dms_to_radians(dec) + dms_to_radians(0, 0, pmdec / 1000) * t
        new_stars.append([name, radians_to_degrees(new_ra),
                         radians_to_degrees(new_dec), parallax])
    return new_stars


def finding_l(
        stars: list,
        ra0: float,
        dec0: float,
) -> list:
    new_stars = []
    for i in range(len(stars)):
        name = stars[i][0]
        ra = stars[i][1]
        dec = stars[i][2]
        parallax = stars[i][3]
        l = math.acos(math.sin(dms_to_radians(dec)) * math.sin(dec0)
                      + math.cos(dms_to_radians(dec)) * math.cos(dec0) * math.cos(ra0 - dms_to_radians(ra)))
        new_stars.append([name, ra, dec, parallax, l])
    return new_stars


def finding_d(
        stars: list
) -> list:
    new_stars = []
    for i in range(len(stars)):
        name = stars[i][0]
        ra = stars[i][1]
        dec = stars[i][2]
        parallax = stars[i][3]
        l = stars[i][4]
        d = 1 / parallax
        new_stars.append([name, ra, dec, l, d])
    return new_stars


def all_for_your_star(
        ra: float,
        dec: float,
        parallax: float,
        pmra: float,
        pmdec: float,
        t: int
) -> list:
    new_ra = dms_to_radians(ra) + dms_to_radians(0, 0, pmra / 1000) * t
    new_dec = dms_to_radians(dec) + dms_to_radians(0, 0, pmdec / 1000) * t
    d = 1 / parallax
    return [new_ra, new_dec, d]


def finding_between_d(
        stars: list,
        d0: float
) -> list:
    answer = []
    for i in range(len(stars)):
        l = stars[i][3]
        d = stars[i][4]
        new_d = math.sqrt(pow(d0, 2) + pow(d, 2) - 2 * d * d0 * math.cos(l))
        answer.append(new_d)
    return answer


def finding_true_answer(
        answer: list
) -> list:
    arr = answer[:10]
    new_arr = []
    d = arr[0]
    for item in arr:
        new_arr.append(item / d)
    return new_arr
