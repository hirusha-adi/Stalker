import os
import logging
import inspect
from datetime import datetime

LOG_FOLDER = 'logs'
LOG_FILENAME = 'app.log'
LOG_TO_FILE = True

if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)

log_filename = os.path.join(LOG_FOLDER, LOG_FILENAME)

if LOG_TO_FILE and not os.path.isfile(log_filename):
    with open(log_filename, 'w', encoding='utf-8') as file:
        file.write(f'[{datetime.now()}] [DEBUG] [ModuleManager] -> Log File Created')

logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s [%(levelname)s] [%(filename)s] [%(name)s] [%(funcName)s()] -> %(message)s')

def log(level, *msg):
    logger = logging.getLogger(__name__)
    current_frame = inspect.currentframe()
    filename = inspect.getframeinfo(current_frame.f_back).filename
    current_function_name = current_frame.f_back.f_code.co_name
    current_class_name = current_frame.f_back.f_locals.get('self', None).__class__.__name__ if 'self' in current_frame.f_back.f_locals else None

    log_message = f"[{datetime.now()}] [{level}] [{filename}]"
    log_message += f" [{current_class_name}]" if current_class_name else ""
    log_message += f" [{current_function_name}()]"
    log_message += f" -> {' '.join(msg)}"

    logger.log(getattr(logging, level.upper()), log_message)

# Example usage:
log('debug', 'This is a debug message.')
log('info', 'This is an info message.')
log('warning', 'This is a warning message.')
log('error', 'This is an error message.')
log('critical', 'This is a critical message.')
