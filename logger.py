import logging
from config import get_filename


def get():
    logger = logging.getLogger("slam studio")
    logger.setLevel(logging.DEBUG)
    filename = get_filename()
    file_handler = logging.FileHandler(filename, 'w')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger



