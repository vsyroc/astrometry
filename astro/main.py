import re
import csv

from astro.core.location_settings import gaia_filepath
from astro.core.logger_settings import logger
# from alive_progress import alive_bar
from astro.base_operations.calculations import (
    calculate_distance,
    radians_to_dms,
    radians_to_hms,
    dms_to_radians,
    hms_to_radians,
    radians_to_degrees,
    dms_to_degree,
    finding_an_interval
)


gaia = gaia_filepath


def main() -> None:
    with open(gaia) as table:
        reader = csv.reader(table, delimiter=',', quotechar='\n')
        rows = list(reader)

        stars = []

        for i in range(10):
            print(rows[i])

        # with alive_bar(len(rows)) as bar:
        #     # pattern = re.compile(r'^\d+(\.\d+)?$')
        #     # При использовании паттерна почему-то теряется 4 звезды, так что пока оставим через try. Вроде пока что производительность позволяет
        #     for row in rows:
        #         if row[8] != '':
        #             # if re.search(pattern, row[4]) and re.search(pattern, row[6]) and re.search(pattern, row[8]):
        #             try:
        #                 stars.append(
        #                     [float(row[4]), float(row[6]), float(row[8])])
        #             except:
        #                 pass
        #         bar()

        # print(f'Total stars: {len(stars)}')
        # # print(stars[0])
        # # print(stars[1])

        # distanse = calculate_distance(
        #     stars[0][0],
        #     stars[0][1],
        #     stars[0][2],
        #     stars[1][0],
        #     stars[1][1],
        #     stars[1][2],
        #     )

        # print(f'Distanse between star[0] and star[1]: {distanse} parsec')

        # for row in rea]der:
        #     if row[8] != '':
        #         # print(row)
        #         # print(row[4], row[6], row[8], sep='|')
        #         counter += 1
        #     bar()
        #         # if counter == 2:
        #             # break
        # # print(counter)


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


if __name__ == '__main__':
    logger.info('Application is running')

    ra = 283.21255717679503
    dec = 45.349694823151324
    dev = (0, 1, 0)
    print_interval(ra, dec, dev)

    logger.info('Application has terminated')
