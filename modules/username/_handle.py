from .search import lookup
from .search import directory
from .specific_sites import amazon
from .specific_sites import github
from utils.help import username_help as show_help

module_functions = {
    "search/lookup": lookup.start,
    "specific/amazon": amazon.start,
    "specific/github": github.start
}

def handler(sub_modules, args, is_interactive=True):
    
    sub_modules_str = "/".join(sub_modules)
    
    if sub_modules_str in module_functions:
        if is_interactive:
            username = input("[?] Username: ")
        else:
            username = args[0]
        print(f"[*] Using Username: {username}")
        module_functions[sub_modules_str](username=username)

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
    
    
    # Use this as a template to extend in the future if required.
    # -----
    # elif sub_modules_str == "specific/module":
    #     if is_interactive:
    #         username = input("[?] Username: ")
    #     else:
    #         username = args[0]
    #     print(f"[*] Using Username: {username}")
    #     module.start(username=username)
    # -----
    
    else:
        print("Invalid sub_module provided.")
        show_help()
