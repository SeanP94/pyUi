import logging
import datetime

from pathlib import Path
cpath = Path(__file__).resolve().parent

# Set config
logging.basicConfig(filename=str(cpath/'requestsError.log'), encoding='utf-8', level=logging.ERROR)

def logError(formatedString : str):
    '''
    Simply logs the error in file.

    TODO:
        As project is built, determine how to log better :)
    '''
    now = datetime.datetime.now()
    logging.error(f"[{now}] : {formatedString}")
