import traceback
import functools
from datetime import datetime
import inspect
import time

def handle_errors(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred in {func.__name__}: {e}")
            traceback.print_exc() 
            return None 

    return wrapper

def show_function_info(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        signature = str(inspect.signature(func))
        frame = inspect.currentframe().f_back

        print(f"[DEBUG] Running: {func_name}")
        print(f"[DEBUG] Signature: {signature}")
        print(f"[DEBUG] Arguments: Positional: {args}, Keyword: {kwargs}")
        print(f"[DEBUG] Time: {datetime.now()}")

        start_time = time.time()
        # ---
        result = func(*args, **kwargs)
        # ---
        end_time = time.time()
        execution_time = end_time - start_time

        print(f"[DEBUG] Execution time: {execution_time:.4f} seconds")

        return result
    
    return wrapper
