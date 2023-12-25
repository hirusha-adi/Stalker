import os
import inspect
from datetime import datetime
from utils.constants import Constants

# Folder
# ----------------------------------------------------
if not Constants.MADE_ONCE:
    os.makedirs('logs', exist_ok=True)
    Constants.MADE_ONCE = True
    
    
# File
# ----------------------------------------------------
log_filename = os.path.join(Constants.LOG_FOLDER, Constants.LOG_FILENAME)
if Constants.LOG_TO_FILE:
    if not os.path.isfile(log_filename):
        with open(log_filename, 'w', encoding='utf-8') as _file:
            _file.write(
                f'[{datetime.now()}] [DEBUG] [ModuleManager] -> Log File Created')
    
def parse_structure(level):
    frame = inspect.currentframe()
    filename = inspect.getframeinfo(frame.f_back).filename
    current_function_name = inspect.currentframe().f_back.f_code.co_name
    current_class_name = None
    
    # is the function is a method inside a class
    if 'self' in frame.f_back.f_locals:
        current_class_name = frame.f_back.f_locals['self'].__class__.__name__
        
    log_message = f"[{datetime.now()}] [{level}] [{filename}]"
    if current_class_name:
        log_message += f" [{current_class_name}]"
    log_message += f" [{current_function_name}()]"
    
    return log_message


def log(level, *args) -> None:
    final = f"{parse_structure(level=level)} -> {' '.join(args)}"
    print(final)
    if Constants.LOG_TO_FILE:
        with open(log_filename, 'a', encoding='utf-8') as file:
            file.write(f"\n{final}")
                
    
def debug(msg):
    log("DEBUG", msg)

def error(msg):
    log("ERROR", msg)
    
def success(msg):
    log("SUCCESS", msg)
    
def info(msg):
    log("INFO", msg)

def warning(msg):
    log("WARNING", msg)