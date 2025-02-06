import requests
from utils import errors


@errors.handle_errors
def start(email: str):

    r = requests.post(
        "https://imgur.com/signin/ajax_email_available", data={"email": email}
    ).json()
    
    if r["data"]["error"]:
        print("[!!] Error:", r["data"]["error"])
    elif r["data"]["available"] == False:
        print("[+] Account found in Imgur.")
    else:
        print("[-] Account not found in Imgur.")
