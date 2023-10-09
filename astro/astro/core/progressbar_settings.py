# Тут надо будет написать какой-нибудь свой прогресс бар, а то мне сторонние не особо понравились.
# Заодно и можно будет настройки свои тут оставить. Только надо подумать, что взять за основу

# На форуме писали о alive_progress. Надо посмотреть на него документацию

# https://github.com/rsalmei/alive-progress

import time

from alive_progress import alive_bar


if __name__ == '__main__':
    with alive_bar(100) as bar:
        for i in range(100):
            bar()
            time.sleep(0.1)