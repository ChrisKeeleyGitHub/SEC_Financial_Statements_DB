# Logging tool

import logging


def get_logger():

    logger_level = logging.INFO
    fmt = "%(asctime)s [FILE: %(filename)10s() | FUNC: %(funcName)15s() | LINE #:%(lineno)4s] %(levelname)s: %(message)s"
    log = logging.getLogger('root')
    logging.basicConfig(format=fmt)

    log.setLevel(logger_level)

    return log


