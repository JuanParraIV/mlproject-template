import logging
import sys


def error_message_detail(error, error_detail: sys) -> str:
    """
    Constructs a detailed error message including the file name, line number, and error message.

    Args:
      error (Exception): The exception object containing the error details.
      error_detail (sys): The sys module, used to extract traceback information.

    Returns:
      str: A formatted string containing the file name, line number, and error message where the error occurred.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] error message: [{str(error)}]".format()
    return error_message


class CustomException(Exception):
    """
    Custom exception class for handling and formatting error messages.

    Attributes:
      error_message (str): The error message describing the exception.
      error_detail (sys): The system-specific details related to the exception.

    Methods:
      __init__(error_message: str, error_detail: sys):
        Initializes the CustomException instance with a formatted error message.
    """

    def __init__(self, error_message: str, error_detail: sys) -> None:
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message
