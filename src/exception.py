import sys
import logging

# Ensure the logger is set up correctly by importing the logger configuration
from src.logger import logging  # Import the logger configuration

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script [{0}] at line number [{1}] with error message [{2}]".format(
        filename, exc_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        detailed_error_message = error_message_detail(error_message, error_detail)
        super().__init__(detailed_error_message)
        self.error_message = detailed_error_message

    def __str__(self):
        return self.error_message

'''
if __name__ == "__main__":
    try:
        logging.info("Attempting to divide by zero.")
        a = 1 / 0
    except Exception as e:
        logging.error("An exception occurred.", exc_info=True)
        raise CustomException(e, sys) from e
'''