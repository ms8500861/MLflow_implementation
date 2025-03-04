import sys

class customexception(Exception):
    def __init__(self, error_message, error_details: sys):
        _, _, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.error_message = "Error occurred in python script name[{0}] line number[{1}] error message[{2}]".format(self.file_name, self.lineno, str(error_message))

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        raise customexception(e, sys)
