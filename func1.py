import logging
logger = logging.getLogger(__name__)

def func_with_logger():
    logger.info("This is a info message from func2.func_with_logger()")
    logger.debug("This is a debug message from func2.func_with_logger()")