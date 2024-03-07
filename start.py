import os
import sys

import modules
from utils import texts

if os.name == "nt":
    sys.exit("Not supported on windows!")

texts.banner_home()
while True:
    i_main: str = input(">> ").strip()

    if i_main == "help":
        texts.help_home()

    elif i_main == "usernames":
        modules.username_lookup.start()

    elif i_main in ["exit", "quit"]:
        print("Quitting!")
        sys.exit()

    else:
        print("[!] Command not found!")
