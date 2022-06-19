import logging

def test_logging_demo():
    logger = logging.getLogger(__name__)  # catches file name

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # filehandler (file location) object  - in which file I have to print, and in which format
    # setting level (to see what to display)
    logger.setLevel(logging.DEBUG)

    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happend")
    logger.critical("Critical issue")
