import os
import logging
import inspect
from datetime import datetime
from utils.constants import Constants

class CustomLogger:
    def __init__(self, module_name):
        # Module Related
        # ----------------------------------------------------
        self.module_name = module_name

        # Folder
        # ----------------------------------------------------
        if not Constants.MADE_ONCE:
            os.makedirs('logs', exist_ok=True)
            Constants.MADE_ONCE = True
        
        # File
        # ----------------------------------------------------
        self.log_filename = os.path.join(Constants.LOG_FOLDER, Constants.LOG_FILENAME)
        if Constants.LOG_TO_FILE:
            if not os.path.isfile(self.log_filename):
                with open(self.log_filename, 'w', encoding='utf-8') as _file:
                    _file.write(
                        f'[{datetime.now()}] [DEBUG] [ModuleManager] -> Log File Created')
    
    def parse_structure(self, level):
        frame = inspect.currentframe()
        filename = inspect.getframeinfo(frame.f_back).filename
        current_function_name = inspect.currentframe().f_back.f_code.co_name
        current_class_name = None

        # is the function is a method inside a class
        if 'self' in frame.f_back.f_locals:
            current_class_name = frame.f_back.f_locals['self'].__class__.__name__

        log_message = f"[{datetime.now()}] [{level}] [{self.module_name}] [{filename}]"
        if current_class_name:
            log_message += f" [{current_class_name}]"
        log_message += f" [{current_function_name}()]"

        return log_message


    def log(self, level, *args) -> None:
        final = f"{self.parse_structure(level=level)} -> {' '.join(args)}"
        print(final)
        if Constants.LOG_TO_FILE:
            with open(self.log_filename, 'a', encoding='utf-8') as file:
                file.write(f"\n{final}")
                
    
    def debug(self, msg):
        self.log("DEBUG", msg)
    
    def info(self, msg):
        print(f"{self.parse_structure()} -> {msg}")
