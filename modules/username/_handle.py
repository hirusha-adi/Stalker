from .search import lookup
from .search import directory

def handler(sub_modules, args, is_interactive=True):
    
    sub_modules_str = "/".join(sub_modules)
    
    if sub_modules_str == "search/lookup":
        if is_interactive:
            username = input("[?] Username: ")
        else:
            username = args[0]
        print(f"[*] Using username: {username}")
        lookup.start(username=username)
    
    elif sub_modules_str == "search/directory":
        if is_interactive:
            name = input("[?] Username: ")
            first_or_last = input("[?] First or Last name? [^first/last]: ")
        else:
            name = args[0]
            first_or_last = args[1]
        print(f"[*] Using name: {name}")
        print(f"[*] Using name as {first_or_last} name")
        directory.start(name=name, first_or_last=first_or_last)
        
        