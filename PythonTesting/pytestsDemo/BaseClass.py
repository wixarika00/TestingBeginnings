import inspect
import logging
from typing import Any


class BaseClass:
    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.get_logger(loggerName)  # catches file name
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(
            fileHandler)  # filehandler (file location) object  - in which file I have to print, and in which format
        # setting level (to see what to display)
        logger.setLevel(logging.DEBUG)
        return logger

