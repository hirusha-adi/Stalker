import pwnedpasswords
from utils import decorators

@decorators.handle_errors
def start(password: str) -> None:
    x = pwnedpasswords.check(password)
    if x == 0:
        print("[+] Your password has not been breached.")
    else:
        print(f"[-] Password has been breached. k={x}")
        