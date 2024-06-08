import inspect
import logging
def customLogger(logLevel=logging.DEBUG):
    #gets the name of the class/ method from where the method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    #by default, log all messages
    logger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger