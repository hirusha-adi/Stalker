import sys

from utils import help
from modules import username
from modules import email
from modules import password

args =  sys.argv[:]

try:
    module = args[1]
except IndexError:
    print("[!!] No module selected!")
    # display_help()
    sys.exit()

is_interactive = False
try:
    args_to_pass = args[2:]
    if len(args_to_pass) == 0:
        raise IndexError
except IndexError:
    is_interactive = True
    print("[+] No arguments passed, starting interactive mode")

modules = module.split("/")
main_module = modules[0]
sub_modules = modules[1:]

if main_module == "help":
    help.main_help()
    
elif main_module == "username":
    username.handler(sub_modules=sub_modules, args=args_to_pass, is_interactive=is_interactive)

elif main_module == "email":
    email.handler(sub_modules=sub_modules, args=args_to_pass, is_interactive=is_interactive)

elif main_module == "password":
    password.handler(sub_modules=sub_modules, args=args_to_pass, is_interactive=is_interactive)
