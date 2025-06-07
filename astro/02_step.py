from astro.core.config import your_star_dec, your_star_pmdec, your_star_pmra, your_star_parallax, your_star_ra, your_star_t, near_star_filepath
from astro.core.logger_settings import logger
from astro.algorithm import (
    all_for_your_star,
    finding_between_d,
    finding_d,
    finding_l,
    finding_true_answer,
    finding_true_coord,
    get_data_from_csv
)


def main():
    ra0, dec0, d0 = all_for_your_star(
        ra=your_star_ra,
        dec=your_star_dec,
        parallax=your_star_parallax,
        pmra=your_star_pmra,
        pmdec=your_star_pmdec,
        t=your_star_t
    )

    near_stars = get_data_from_csv(near_star_filepath)
    stars_true_coord = finding_true_coord(
        stars=near_stars,
        t=your_star_t
    )
    stars_with_l = finding_l(
        stars=stars_true_coord,
        ra0=ra0,
        dec0=dec0
    )
    stars_with_d = finding_d(stars=stars_with_l)
    answer = finding_between_d(
        stars=stars_with_d,
        d0=d0
    )
    answer.sort()
    true_answer = finding_true_answer(answer=answer)
    for item in true_answer:
        print('%.2f' % item)


if __name__ == '__main__':
    logger.info('Start script 02_step.py')
    main()
    logger.info('End script 02_step.py')
