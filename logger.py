import sys
import logging


def setLogger(name):
    logger = logging.getLogger("test")

    stdoutHandler = logging.StreamHandler(stream=sys.stdout)
    fileHandler = logging.FileHandler("/tmp/test.log.txt")


    fmt = logging.Formatter(
            "%(name)s: %(asctime)s | %(levelname)s | %(filename)s%(lineno)s | %(process)d >>> %(message)s"
        )

    stdoutHandler.setFormatter(fmt)
    fileHandler.setFormatter(fmt)

    logger.addHandler(stdoutHandler)
    logger.addHandler(fileHandler)

    logger.setLevel(logging.INFO)

    return logger