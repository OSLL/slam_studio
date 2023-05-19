import logging
from config import get_filename


class Logger:
    _instance = None

    @staticmethod
    def get_instance():
        if not Logger._instance:
            Logger._instance = Logger()
        return Logger._instance.logger

    def __init__(self):
        if not Logger._instance:
            self.logger = logging.getLogger("Slam studio")
            self.logger.setLevel(logging.DEBUG)
            filename = get_filename()
            file_handler = logging.FileHandler(filename, 'w')
            formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)



