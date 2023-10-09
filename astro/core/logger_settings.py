from loguru import logger


logger.add(
    'file.log',
    format='{level} {message} {time}'
)