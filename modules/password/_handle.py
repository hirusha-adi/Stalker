from . import haveibeenpwned
from . import pastebin
from utils.help import password_help as show_help

module_functions = {
    "pastebin": pastebin.start,
    "haveibeenpwned/check": haveibeenpwned.check.start,
    "haveibeenpwned/range": haveibeenpwned.range_.start,
}

def handler(sub_modules, args, is_interactive=True):
    
    sub_modules_str = "/".join(sub_modules)
    
    if sub_modules_str in module_functions:
        if is_interactive:
            breach_name = input("[?] Password: ")
        else:
            breach_name = args[0]
        print(f"[*] Using Password: {breach_name}")
        module_functions[sub_modules_str](password=breach_name)

    elif sub_modules_str == "haveibeenpwned/breach_info":
        if is_interactive:
            breach_name = input("[?] Breach Name: ")
        else:
            breach_name = args[0]
        print(f"[*] Using Breach Name: {breach_name}")
        haveibeenpwned.breach_info.start(password=breach_name)
    
    elif sub_modules_str == "haveibeenpwned/domain_check":
        if is_interactive:
            domain = input("[?] Domain Name: ")
        else:
            domain = args[0]
        print(f"[*] Using Domain Name: {domain}")
        haveibeenpwned.domain_check.start(domain=domain)
    
    elif sub_modules_str == "haveibeenpwned/domain_list":
        haveibeenpwned.domains_list.start()
        
    elif sub_modules_str in "haveibeenpwned/filtered_check":
        if is_interactive:
            email = input("[?] Email: ")
            domain = input("[?] Domain Name: ")
        else:
            email = args[0]
            domain = args[1]
        print(f"[*] Using Email: {email}")
        print(f"[*] Using Domain Name: {domain}")
        haveibeenpwned.filtered_check.start(email=email, domain=domain)

    # Use this as a template to extend in the future if required.
    # -----
    # elif sub_modules_str == "specific/module":
    #     if is_interactive:
    #         password = input("[?] Password: ")
    #     else:
    #         password = args[0]
    #     print(f"[*] Using Password: {password}")
    #     module.start(password=password)
    # -----
    
    else:
        print("Invalid sub_module provided.")
        show_help()
