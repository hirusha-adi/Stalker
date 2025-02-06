import requests
import hashlib
from utils import decorators


@decorators.handle_errors
def start(email: str):
    encoded_email = email.lower().encode("utf-8")
    hashed_email = hashlib.sha256(encoded_email).hexdigest()
    r = requests.get(f"https://en.gravatar.com/{hashed_email}.json")

    if "User not found" in r.text:
        print("[-] Account not found in Gravatar.")

    else:
        print(
            f"[+] Account found in Gravar, with username: {r.json()['entry'][0]['displayName']}"
        )
