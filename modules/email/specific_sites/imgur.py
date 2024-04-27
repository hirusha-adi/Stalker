import requests


def start(target: str):

    r = requests.post(
        "https://imgur.com/signin/ajax_email_available", data={"email": target}
    )

    try:

        if r.json()["data"]["available"] == False:
            print("[+] Account found in Imgur.")

        # elif r.json()["data"]["available"] == True:
        else:
            print("[-] Account not found in Imgur.")

    except Exception as e:
        print("An error occurred:", e)
