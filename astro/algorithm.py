import re
import csv

from astro.core.config import *
from astro.core.logger_settings import logger
from astro.base_operations.calculations import *


gaia = near_star_filepath

ra0 = 283.2125563242885 # пересчитанные координаты для базовой звезды
dec0 = 45.34969376631197
d0 = 0.3011193895835285

# ra0 = 283.21255717679503 # начальные коодринаты для базовой звезды
# dec0 = 45.349694823151324


def test():
    # Наше с Лехой
    ra = 283.21255717679503
    dec = 45.349694823151324

    # Данил
    # ra = 176.26370021831409
    # dec = 0.005412190339654384

    # Ильи и Максима
    # ra = 293.6137418404033
    # dec = 47.83893574320811

    ra_rad = dms_to_radians(ra)
    dec_rad = dms_to_radians(dec)

    dm = (0, 1, 0)

    print(f'ra minus: {radians_to_degrees(ra_rad - dms_to_radians(*dm))}\nra plus: {radians_to_degrees(ra_rad + dms_to_radians(*dm))}\ndec minus: {radians_to_degrees(dec_rad - dms_to_radians(*dm))}\ndec plus: {radians_to_degrees(dec_rad + dms_to_radians(*dm))}')


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


def main():
    global ra0
    global dec0

    # Данил
    # ra = 176.26370021831409
    # dec = 0.005412190339654384

    dev = (0, 1, 0)
    print_interval(ra0, dec0, dev)


def get_data_from_csv(
        path: str
) -> list:
    with open(path) as table:
        reader = csv.reader(table, delimiter=',', quotechar='\n')
        rows = list(reader)
        new_rows = []

        for row in rows:
            new_row = []
            for item in row:
                if re.search(r'\d+\.\d+', item) or re.search(r'\d+', item):
                    new_row.append(float(item))
            if new_row != [] and len(new_row) > 3:
                new_rows.append(new_row)

        # for row in rows:
        #     print(f'{row=}')

    return new_rows


def finding_true_coord(
        stars: list
) -> list:
    new_stars = []
    t = 7
    for i in range(len(stars)):
        global ra0
        global dec0

        name = stars[i][0]
        ra = stars[i][1]
        dec = stars[i][2]
        parallax = stars[i][3]
        pmra = stars[i][4]
        pmdec = stars[i][5]
        new_ra = dms_to_radians(ra) + dms_to_radians(0, 0, pmra / 1000) * t
        new_dec = dms_to_radians(dec) + dms_to_radians(0, 0, pmdec / 1000) * t
        new_stars.append([name, radians_to_degrees(new_ra), radians_to_degrees(new_dec), parallax])
    return new_stars


def finding_l(
        stars: list
) -> list:
    new_stars = []
    t = 7
    for i in range(len(stars)):
        global ra0
        global dec0

        name = stars[i][0]
        ra = stars[i][1]
        dec = stars[i][2]
        parallax = stars[i][3]
        l = math.acos(math.sin(dms_to_radians(dec)) * math.sin(dms_to_radians(dec0))
                      + math.cos(dms_to_radians(dec)) * math.cos(dms_to_radians(dec0)) * math.cos(dms_to_radians(ra0) - dms_to_radians(ra)))
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


def all_for_main_star(
) -> list:
    global ra0
    global dec0

    pmra = -25.12029842069031
    pmdec = -31.141251994948167
    parallax = 3.3209419074044937
    t = 7

    ra = ra0 + dms_to_radians(0, 0, pmra / 1000) * t
    dec = dec0 + dms_to_radians(0, 0, pmdec / 1000) * t
    d = 1 / parallax
    return [ra, dec, d]


def finding_between_d(
        stars: list
) -> list:
    global ra0
    global dec0
    global d0
    answer = []
    for i in range(len(stars)):
        name = stars[i][0]
        ra = stars[i][1]
        dec = stars[i][2]
        l = stars[i][3]
        d = stars[i][4]
        new_d = pow(d0, 2) + pow(d, 2) - 2 * d * d0 * math.cos(l)
        # print(new_d)
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


if __name__ == '__main__':
    logger.info('Application is running')
    main()
    stars = get_data_from_csv(gaia)

    # for row in stars:
    #     print(row)

    new_stars = finding_true_coord(stars)
    new_new_stars = finding_l(new_stars)
    new_new_new_stars = finding_d(new_new_stars)
    # print(all_for_main_star())
    answer = finding_between_d(new_new_new_stars)
    # print(answer)
    answer.sort()
    true_answer = finding_true_answer(answer)

    for item in true_answer:
        print('%.2f' % item)
    # print(answer)



    # for item in new_new_new_stars:
    #     print(item)

    # kepler = kepler_filepath
    # print_csv(kepler)

    logger.info('Application has terminated')
