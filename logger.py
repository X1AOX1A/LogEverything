import os
import sys
import time
import errno
import logging

__all__ = ["Logger", "setup_logger"]


class Logger:
    """A logger that can also log to file and console.

    Args:
        fpath (str, optional): If specified, log will be written to this file.
    """

    def __init__(self, fpath=None):
        self.console = sys.stdout
        self.file = None
        if fpath is not None:
            mkdir_if_missing(os.path.dirname(fpath))
            self.file = open(fpath, "w")

    def __del__(self):
        self.close()

    def __enter__(self):
        pass

    def __exit__(self, *args):
        self.close()

    def write(self, msg):
        self.console.write(msg)
        if self.file is not None:
            self.file.write(msg)

    def flush(self):
        self.console.flush()
        if self.file is not None:
            self.file.flush()
            os.fsync(self.file.fileno())

    def close(self):
        self.console.close()
        if self.file is not None:
            self.file.close()

    def setup_logging(self, level=logging.INFO):
        """Set up logging to capture with the same file handler and also log to console."""
        log_format = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(name)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # Set up the file handler or console handler for logging messages
        handlers = []
        if self.file:
            file_handler = logging.StreamHandler(self.file)
            file_handler.setFormatter(log_format)
            handlers.append(file_handler)
        
        # Set up the console handler for logging messages
        console_handler = logging.StreamHandler(self.console)
        console_handler.setFormatter(log_format)
        handlers.append(console_handler)

        # Get the root logger and set the level (default is INFO)
        root_logger = logging.getLogger()
        root_logger.setLevel(level)

        # If the logger already has handlers, remove them to prevent duplicate logs
        if root_logger.handlers:
            for handler in root_logger.handlers:
                root_logger.removeHandler(handler)

        # Add our custom handlers to the root logger
        for handler in handlers:
            root_logger.addHandler(handler)


def mkdir_if_missing(dirname):
    """Create dirname if it is missing."""
    if not os.path.exists(dirname):
        try:
            os.makedirs(dirname)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise


def setup_logger(log_file=None, log_dir="./output", log_level=logging.INFO):
    """Setup the logger.
    Args:
        log_file (str, optional): log file name. If None, logs only to console.
        log_dir (str): directory to save logging file.
        log_level (int): logging level, e.g. logging.INFO or logging.DEBUG.
    """
        
    log_path = None
    if log_file:
        mkdir_if_missing(log_dir)
        log_path = os.path.join(log_dir, log_file)

        if os.path.exists(log_path):
            # Make sure the existing log file is not over-written
            time_string = time.strftime("-%Y-%m-%d-%H-%M-%S")
            basename, ext = os.path.splitext(log_path)
            log_path = basename + time_string + ext

    # Set up stdout redirection
    log_instance = Logger(log_path)
    sys.stdout = log_instance

    # Set up logging redirection
    log_instance.setup_logging(level=log_level)


if __name__ == "__main__":
    log_dir = "./output"
    setup_logger(log_dir)
    print("This is a message.")
    logging.info("This is a logging.info message.")