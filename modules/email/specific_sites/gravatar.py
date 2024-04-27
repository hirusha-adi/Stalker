import requests
import hashlib


def start(target: str):

    encoded_email = target.lower().encode("utf-8")
    hashed_email = hashlib.sha256(encoded_email).hexdigest()

    r = requests.get(f"https://en.gravatar.com/{hashed_email}.json")

    try:
        if "User not found" in r.text:
            print("[-] Account not found in Gravatar.")

        else:
            print(
                f"[+] Account found in Gravar, with username: {r.json()['entry'][0]['displayName']}"
            )

    except Exception as e:
        print("An error occurred:", e)
