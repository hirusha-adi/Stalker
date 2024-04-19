import requests

def chess(url: str):

    r = requests.get(url)

    if r.json()['isEmailAvailable'] == True:
        print(f"[-] No account found in chess.com")
    elif r.json()['isEmailAvailable'] == False:
        print(f"[+] Account found in chess.com")

def start(email: str):
    url = f"https://www.chess.com/callback/email/available?email={email}"
    chess(url=url)
