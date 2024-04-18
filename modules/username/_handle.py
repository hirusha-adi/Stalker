from . import lookup

def handler(sub_modules, args, is_interactive=True):
    
    sub_modules_str = "/".join(sub_modules)
    
    if sub_modules_str == "lookup":
        if is_interactive:
            username = input("[?] Username: ")
        else:
            username = args[0]
        print(f"[*] Using username: {username}")
        lookup.start(username=username)
        