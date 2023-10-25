from astro.core.logger_settings import logger
from astro.algorithm import print_interval
from astro.core.config import *


def main():
    # Надо указать отклонение в (градусах, минутах, секундах)
    deviation = (0, 1, 0)
    print_interval(
        ra=your_star_ra,
        dec=your_star_dec,
        dev=deviation
    )


if __name__ == '__main__':
    logger.info('Start 02_step.py script')
    main()
    logger.info('End 02_step.py script')
