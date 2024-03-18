# Log Everything

## Overview

This module provides a custom logger that enables simultaneous logging to the **console** and to a **file**, capturing output from both `print` statements and the Python `logging` library (`logging.info()`, `logger.info()`, etc.). It's designed for easy integration into Python projects to enhance logging capabilities.

## Features

- Captures and redirects `print` output to both console and file.
- Integrates with the Python `logging` library to log messages at various levels (INFO, DEBUG, etc.).
- Configurable to output logs both console and file, or to console only.
- Automatically generates a new log file with a timestamp if the specified log file already exists, preventing overwrites.
- Easy to integrate with existing Python scripts or projects.

## Setup and Usage

### Basic Setup

1. Place `logger.py` in your project directory.
2. Import the `setup_logger` function from the logger module in your main script:

   ```python
   from logger import setup_logger
   ```

3. Initialize the logger at the beginning of your main script:

   ```python
   setup_logger(log_file="logger.log", log_dir="./output", log_level=logging.DEBUG)
   ```

   - `log_file`: Name of the file where logs will be written. If `None`, logs will only be printed to the console.
   - `log_dir`: Directory where the log file will be stored.
   - `log_level`: Minimum level of messages to be logged. Can be DEBUG, INFO, WARNING, ERROR, or CRITICAL.

### Usage Examples

In this example, all messages will be logged to both the console and a specified log file.

```python
import logging
from logger import setup_logger

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # set log_file to None to log only to console
    setup_logger(log_file="logger.log", log_dir="./output", log_level=logging.DEBUG)
    logger.info("This is a info message from logger.info()")
    logger.debug("This is a debug message from logger.debug()")
```

- Excute `example1.py` to see the output in the console and the log file.
   - The example output can be found in the `output` directory.
- Excute `example2.py` to see the output in the console only.


### Integration with Custom Functions

You can also use the logger in custom functions within your project. Here is how you can integrate it:

1. Import the logging library and the logger module in your custom function file.

   ```python
   import logging
   logger = logging.getLogger(__name__)

   def func_with_logger():
       logger.info("This is an info message from func_with_logging()")
       logger.debug("This is a debug message from func_with_logging()")
   ```

3. Call your functions from the main script where the logger has been set up.

   ```python
   from func1 import func_with_logger

   if __name__ == "__main__":
       # Logger setup must be done before calling functions
       setup_logger(log_file="logger.log", log_dir="./output", log_level=logging.DEBUG)

       # Function call
       func_with_logger()
   ```