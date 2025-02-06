import requests
from utils import errors


@errors.handle_errors
def start(email: str):
    url = f"https://api.twitter.com/i/users/email_available.json?email={email}"
    response = requests.get(url)
    if response.json()["taken"]:
        print("[+] Account found in Twitter.")
    else:
        print("[+] Account not found in Twitter.")
