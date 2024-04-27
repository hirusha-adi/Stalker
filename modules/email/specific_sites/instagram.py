import requests
from utils import errors


@errors.handle_errors
def start(email: str):
    url = "https://www.instagram.com/accounts/emailsignup/"
    response = requests.get(url)
    csrf_token = response.cookies["csrftoken"]

    data = {"email": email, "first_name": "", "username": "", "opt_into_one_tap": False}
    url = "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/"
    headers = {"x-csrftoken": csrf_token}
    response = requests.post(url, headers=headers, data=data)

    code = response.json()["errors"]["email"][0]["code"]
    if code == "email_is_taken":
        print("[+] Account found in Instagram.")
    else:
        print("[-] Account not found in Instagram.")
