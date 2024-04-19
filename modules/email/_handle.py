from .specific_sites import github
from .specific_sites import chess_com
from .specific_sites import deezer

def handler(sub_modules, args, is_interactive=True):
    
    sub_modules_str = "/".join(sub_modules)
    if sub_modules_str == "specific/github":
        if is_interactive:
            email = input("[?] Email: ")
        else:
            email = args[0]
        print(f"[*] Using Email: {email}")
        github.start(email=email)
    
    elif sub_modules_str == "specific/chess_com":
        if is_interactive:
            email = input("[?] Email: ")
        else:
            email = args[0]
        print(f"[*] Using Email: {email}")
        chess_com.start(email=email)
    
    elif sub_modules_str == "specific/deezer":
        if is_interactive:
            email = input("[?] Email: ")
        else:
            email = args[0]
        print(f"[*] Using Email: {email}")
        deezer.start(email=email)
