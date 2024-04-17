import os
import sys

args =  sys.argv[:]

try:
    module = args[1]
except IndexError:
    print("[!!] No module selected!")
    # display_help()
    sys.exit()

try:
    args_to_pass = args[2:]
    if len(args_to_pass) == 0:
        raise IndexError
except IndexError:
    print("[+] No arguments passed, starting interactive mode")

