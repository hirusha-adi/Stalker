import requests
from utils import decorators


@decorators.handle_errors
def start(email: str):
    r = requests.get(f"https://www.chess.com/callback/email/available?email={email}")

    if r.json()["isEmailAvailable"] == True:
        print(f"[-] Account not found in chess.com.")
    elif r.json()["isEmailAvailable"] == False:
        print(f"[+] Account found in chess.com.")
