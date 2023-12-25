import os
import logging
import inspect
from datetime import datetime

class CustomLogger:
    def __init__(self, logger_name):
        # variables
        self.logger_name = logger_name

        # logs folder
        os.makedirs('logs', exist_ok=True)
        
        # logging setup
        log_filename = os.path.join('logs', datetime.now().strftime('%Y-%m-%d') + '.log')
        logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        
    def parse_structure(self):
        frame = inspect.currentframe()
        filename = inspect.getframeinfo(frame.f_back).filename
        current_function_name = inspect.currentframe().f_back.f_code.co_name
        current_class_name = None

        # is the function is a method inside a class
        if 'self' in frame.f_back.f_locals:
            current_class_name = frame.f_back.f_locals['self'].__class__.__name__

        log_message = f"[{self.logger_name}] [{filename}]"
        if current_class_name:
            log_message += f" [{current_class_name}]"
        log_message += f" [{current_function_name}()]"

        return log_message

    def debug(self, msg):
        print(f"{self.parse_structure()} {msg}")
        logging.debug(f"{self.parse_structure()} {msg}")
    
    def info(self, msg):
        logging.info(f"{self.parse_structure()} {msg}")
