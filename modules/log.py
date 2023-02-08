import logging


FILENAME = "log.log"
FORMAT = "%(funcName)s(%(asctime)s)\n%(message)s\n"
DATE_FORMAT = "%d/%m/%Y %H:%M:%S"


LOGGER = logging.getLogger("personal")
LOGGER.setLevel(logging.DEBUG)

LOGGER_FILE_HANDLER = logging.FileHandler("log.log")
LOGGER_FILE_HANDLER.setFormatter(
    logging.Formatter(FORMAT, DATE_FORMAT)
)

LOGGER.addHandler(
    LOGGER_FILE_HANDLER
)
