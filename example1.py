import logging
from logger import setup_logger
from func1 import func_with_logger
from func2 import func_with_logging
from func3 import func_with_print

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # export log messages to console and file
    setup_logger(log_dir="./output", log_file="example1.log", log_level=logging.DEBUG)

    # print test
    print("This is a print message from main.py.")

    # logger test, **prefer**
    logger.info("This is a info message from main.logger.info()")
    logger.debug("This is a debug message from main.logger.debug()")
    logger.warning("This is a warning message from main.logger.warning()")

    # logging test
    logging.info("This is a info message from main.logging.info()")
    logging.debug("This is a debug message from main.logging.debug()")

    # function test
    func_with_logger()  # **prefer**
    func_with_logging()
    func_with_print()