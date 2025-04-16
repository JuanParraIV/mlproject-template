import logging
import os
from datetime import datetime

"""
This module sets up a logging configuration for the application.

The logger writes log messages to a file named with the current timestamp
in the format 'YYYY_MM_DD_HH_MM_SS.log'. The log files are stored in a 
'logs' directory located in the current working directory. If the 'logs' 
directory does not exist, it will be created automatically.

Attributes:
  LOG_FILE (str): The name of the log file, generated using the current timestamp.
  log_path (str): The full path to the directory where the log file will be stored.
  LOG_FILE_PATH (str): The full path to the log file.

Logging Configuration:
  - Log messages are written to the file specified by LOG_FILE_PATH.
  - Log format: "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
  - Log level: INFO
"""
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(log_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

