import pwnedpasswords

def start(password: str) -> None:
    x = pwnedpasswords.range(password)
    print(x)
    # if x == 0:
    #     print("[+] Password ")
    # else:
    #     print(f"[-] Password has been breached. k={x}")
    