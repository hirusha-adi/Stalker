import os
import sys
from utils import banners

if os.name == "nt":
    sys.exit("Not supported on windows!")

banners.home()
while True:
    i_main = input(">> ").strip()
    if i_main == "help":
        print("""username lookup""")
    elif i_main == "username lookup":
        print()
    else:
        print("[!] Command not found!")
