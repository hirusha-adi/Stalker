
from .phoneinfoga import dorks
from .phoneinfoga import search

module_functions = {
    "phoneinfoga/dorks": dorks.start,
    "phoneinfoga/search": search.start
}

def handler(sub_modules, args, is_interactive=True):
    sub_modules_str = "/".join(sub_modules)
    
    if sub_modules_str in module_functions:
        if is_interactive:
            phone_number = input("[?] Phone number: ")
        else:
            phone_number = args[0]
        print(f"[*] Using Phone number: {phone_number}")
        module_functions[sub_modules_str](email=phone_number)
    
    # Use this as a template to extent in the future if required.
    # -----
    # elif sub_modules_str == "specific/module":
    #     if is_interactive:
    #         phone_number = input("[?] Phone number: ")
    #     else:
    #         phone_number = args[0]
    #     print(f"[*] Using Phone number: {phone_number}")
    #     module.start(phone_number=phone_number)
    # -----
    
    else:
        print("Invalid sub_module provided.")
