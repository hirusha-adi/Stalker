from . import haveibeenpwned
from utils.help import password_help as show_help

module_functions = {
    "haveibeenpwned/check": haveibeenpwned.check.start,
    "haveibeenpwned/range": haveibeenpwned.range_.start,
}

def handler(sub_modules, args, is_interactive=True):
    
    sub_modules_str = "/".join(sub_modules)
    
    if sub_modules_str in module_functions:
        if is_interactive:
            password = input("[?] Password: ")
        else:
            password = args[0]
        print(f"[*] Using Password: {password}")
        module_functions[sub_modules_str](password=password)

    # Use this as a template to extend in the future if required.
    # -----
    # elif sub_modules_str == "specific/module":
    #     if is_interactive:
    #         password = input("[?] Password: ")
    #     else:
    #         password = args[0]
    #     print(f"[*] Using Password: {email}")
    #     module.start(password=password)
    # -----
    
    else:
        print("Invalid sub_module provided.")
        show_help()
