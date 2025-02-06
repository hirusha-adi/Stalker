import requests
from utils import errors


@errors.handle_errors
def start(email: str):
    url = f"https://spclient.wg.spotify.com/signup/public/v1/account?validate=1&email={email}"
    response = requests.get(url)

    if response.json()["status"] == 20:
        print("[+] Account found in Spotify.")
    else:
        print("[-] Account not found in Spotify.")
