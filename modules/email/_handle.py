from .specific_sites import chess_com
from .specific_sites import deezer
from .specific_sites import duolingo
from .specific_sites import github
from .specific_sites import gravatar
from .specific_sites import imgur
from .specific_sites import instagram
from .specific_sites import pinterest
from .specific_sites import pornhub
from .specific_sites import spotify
from .specific_sites import strava
from .specific_sites import twitter

def handler(sub_modules, args, is_interactive=True):
    
    sub_modules_str = "/".join(sub_modules)
    if sub_modules_str == "specific/chess_com":
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
    
    elif sub_modules_str == "specific/duolingo":
        if is_interactive:
            email = input("[?] Email: ")
        else:
            email = args[0]
        print(f"[*] Using Email: {email}")
        duolingo.start(email=email)
        
    elif sub_modules_str == "specific/github":
        if is_interactive:
            email = input("[?] Email: ")
        else:
            email = args[0]
        print(f"[*] Using Email: {email}")
        github.start(email=email)
    
    elif sub_modules_str == "specific/gravatar":
        if is_interactive:
            email = input("[?] Email: ")
        else:
            email = args[0]
        print(f"[*] Using Email: {email}")
        gravatar.start(email=email)
    
    elif sub_modules_str == "specific/imgur":
        if is_interactive:
            email = input("[?] Email: ")
        else:
            email = args[0]
        print(f"[*] Using Email: {email}")
        imgur.start(email=email)
    
    elif sub_modules_str == "specific/instagram":
        if is_interactive:
            email = input("[?] Email: ")
        else:
            email = args[0]
        print(f"[*] Using Email: {email}")
        instagram.start(email=email)
        
    elif sub_modules_str == "specific/pinterest":
        if is_interactive:
            email = input("[?] Email: ")
        else:
            email = args[0]
        print(f"[*] Using Email: {email}")
        pinterest.start(email=email)
    
    elif sub_modules_str == "specific/pornhub":
        if is_interactive:
            email = input("[?] Email: ")
        else:
            email = args[0]
        print(f"[*] Using Email: {email}")
        pornhub.start(email=email)
        
    elif sub_modules_str == "specific/spotify":
        if is_interactive:
            email = input("[?] Email: ")
        else:
            email = args[0]
        print(f"[*] Using Email: {email}")
        spotify.start(email=email)

    elif sub_modules_str == "specific/strava":
        if is_interactive:
            email = input("[?] Email: ")
        else:
            email = args[0]
        print(f"[*] Using Email: {email}")
        strava.start(email=email)
    
    elif sub_modules_str == "specific/twitter":
        if is_interactive:
            email = input("[?] Email: ")
        else:
            email = args[0]
        print(f"[*] Using Email: {email}")
        twitter.start(email=email)
