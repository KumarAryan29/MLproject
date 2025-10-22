import sys
import logging
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    _, _ , exc_tb = error_detail.exc_info() # This variable will tell in which line the exception has occured, on which file exception has occured, etc.
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number[{1}] error message[{2}]".format(
    file_name, exc_tb.tb_lineno, str(error))

    return error_message


'''
Parameters:

error: This is the actual error message or exception object that was raised.

error_detail: A sys object (which provides system-specific parameters and functions). The exc_info() function from this module is used to extract details about the most recent exception.

exc_info(): This function returns a tuple containing three values:

The exception type (not used here).

The exception value (not used here).

The traceback object (exc_tb), which contains information about the exception like where it occurred.

exc_tb.tb_frame.f_code.co_filename: Extracts the filename where the exception occurred.

exc_tb.tb_lineno: Extracts the line number where the exception occurred.

str(error): Converts the error message into a string.

error_message: A formatted string that provides details of the error, including:

The filename where the error occurred.

The line number where the error occurred.

The error message itself.

The function returns the formatted error message.
'''





class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

'''
Inheritance: CustomException inherits from Python’s built-in Exception class. This means CustomException can be used as a regular exception but adds additional functionality.

Constructor (__init__):

The constructor takes two parameters:

error_message: The message associated with the error.

error_detail: A sys object (used to get the traceback details).

The super().__init__(error_message) calls the constructor of the base Exception class to initialize the exception with the error_message.

self.error_message: The error message is processed by the error_message_detail function (defined above) to include additional information like the file and line number where the error occurred. This message is stored in the error_message attribute.

__str__ method:

This method returns the custom error message when the exception is raised or printed. It ensures that when CustomException is used, the detailed error message (including the file and line number) is shown.
'''


# For checking the code
'''
if __name__ == "__main__":

    try:
        a = 1/0
    except Exception as e:
        logging.info("Devide By Zero Error")
        raise CustomException(e, sys)
    
'''