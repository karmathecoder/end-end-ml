import sys
import logging

def error_messege_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    error_msg = "Error Occoured In Python Script Name  [{0}] Line Number [{1}] Error Message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_msg


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_messege_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

# if __name__ == '__main__':
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by 0 error")
#         raise CustomException(e,sys)    