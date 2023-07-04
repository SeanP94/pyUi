import logging
import datetime
import os

cpath = os.path.dirname(os.path.realpath(__file__))

# Set config
logging.basicConfig(filename=cpath + '/requestsError.log', encoding='utf-8', level=logging.ERROR)

def logError(formatedString : str):
    '''
    Simply logs the error in file.

    TODO:
        As project is built, determine how to log better :)
    '''
    now = datetime.datetime.now()
    logging.error(f"[{now}] : {formatedString}")
