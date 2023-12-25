import os
import time

class Constants:
    # Basic Stuff
    # ----------------------------------------------------
    HOME_FOLDER = os.getcwd()
    DATE_TIME = time.strftime("%d%m%Y_%H%M%S")
    
    # Logging Stuff
    # ----------------------------------------------------
    MADE_ONCE = False
    LOG_FOLDER = os.path.join(HOME_FOLDER, 'logs')
    LOG_FILENAME = f"{DATE_TIME}.log"
    LOG_TO_FILE = True

