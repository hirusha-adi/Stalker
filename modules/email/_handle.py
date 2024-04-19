from .specific_sites import github

def handler(sub_modules, args, is_interactive=True):
    
    sub_modules_str = "/".join(sub_modules)
    
    if sub_modules_str == "specific_sites/github":
        if is_interactive:
            email = input("[?] Email: ")
        else:
            email = args[0]
        print(f"[*] Using Email: {email}")
        github.start(email=email)
