from astro.core.config import *
from astro.core.logger_settings import logger
from astro.algorithm import (
    all_for_your_star,
    get_data_from_csv
)


def main():
    your_star = all_for_your_star(
        ra=your_star_ra,
        dec=your_star_dec,
        parallax=your_star_parallax,
        pmra=your_star_pmra,
        pmdec=your_star_pmdec,
        t=your_star_t
    )
    ra0 = your_star[0]
    dec0 = your_star[1]
    d0 = your_star[2]

    near_stars = get_data_from_csv(near_star_filepath)

    for star in near_stars:
        print(star)
    print(len(near_stars))


if __name__ == '__main__':

    main()
