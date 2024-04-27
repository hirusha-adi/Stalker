import requests


def start(email: str):
    url = f"https://api.twitter.com/i/users/email_available.json?email={email}"
    response = requests.get(url)
    try:
        if response.json()["taken"]:
            print("[+] Account found in Twitter.")
        else:
            print("[+] Account not found in Twitter.")
    except Exception as e:
        print("An error occurred:", e)
