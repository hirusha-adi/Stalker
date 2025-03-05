import requests
from utils import decorators


@decorators.handle_errors
def start(email: str):
    params = {
        "source_url": "/",
        "data": '{"options": {"email": "' + email + '"}, "context": {}}',
    }
    url = "https://www.pinterest.fr/resource/EmailExistsResource/get/"
    response = requests.get(url, params=params)

    if response.json()["resource_response"]["data"]:
        print("[+] Account found in pinterest.")
    else:
        print("[-] Account not found in pinterest.")
