import requests
from bs4 import BeautifulSoup
from utils import errors


@errors.handle_errors
def start(email: str):
    try:
        session = requests.Session()
        response = session.get("https://fr.pornhub.com/signup")
        soup = BeautifulSoup(response.text, "html.parser")
        token = soup.find(attrs={"name": "token"}).get("value")
        params = {"token": token}
        data = {"check_what": "email", "email": email}
        api_response = session.post(
            "https://fr.pornhub.com/user/create_account_check", params=params, data=data
        )

        if api_response.json()["email"] == "create_account_failed":
            print("[+] Account found in Pornhub.")
        # if api_response.json()["email"] == "create_account_passed":
        else:
            print("[+] Account not found in Pornhub.")

    finally:
        session.close()
