import os
from utils import errors


@errors.handle_errors
def start(email: str, color=False, clear=False) -> None:
    try:
        import holehe  
    except ImportError:
        os.system("pip install holehe" if os.name == 'nt' else "pip3 install holehe")
    
    os.system(f"holehe {'--no-color' if not color else ''} {'--no-clear' if not clear else ''} {email}")
