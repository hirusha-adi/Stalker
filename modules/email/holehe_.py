import os
from utils import errors


@errors.handle_errors
def start(email: str, no_color=False, no_clear=False):
    try:
        import holehe # make sure this is installed
    except ImportError:
        os.system("pip install holehe" if os.name == 'nt' else "pip3 install holehe")
        
    os.system(f"holehe {'--no-color' if no_color else ''} {'--no-clear' if no_clear else ''} {email}")
    