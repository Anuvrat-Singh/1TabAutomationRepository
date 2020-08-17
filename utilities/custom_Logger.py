import inspect
import logging


def customLogger(logLevel=logging.DEBUG):
    # get the name of the class/method which is invoking the logger
    loggerName = inspect.stack()[1][3]

    # create a logger and get the loggername
    logger = logging.getLogger(loggerName)

    # log all the information if log level is not passed
    logger.setLevel(logging.DEBUG)

    # define a file handler if logs are to be written on a file otherwise console handler
    fileHandler = logging.FileHandler("AutomationRun.log", mode='a')

    # set the filehandler's log level
    fileHandler.setLevel(logLevel)

    # create a formatter of file handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')

    # add the formatter in the filehandler
    fileHandler.setFormatter(formatter)

    # add the filehandler to the logger
    logger.addHandler(fileHandler)

    # return the logger
    return logger
