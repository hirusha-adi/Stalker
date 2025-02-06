import requests
from utils import decorators


@decorators.handle_errors
def start(email: str):

    r = requests.get(
        "https://www.duolingo.com/2017-06-30/users", params={"email": email}
    )
    
    if """{"users":[]}""" in r.text:
        print("[-] Account not found in doulingo.")

    else:
        username = r.json()["users"][0]["username"]
        if username is not None and username != "":
            print("[+] Account found in duolingo, with username: {username}")
        else:
            print("[-] Account not found in duolingo.")

