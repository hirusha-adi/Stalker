import requests


def start(email: str):

    r = requests.get(
        "https://www.duolingo.com/2017-06-30/users", params={"email": email}
    )

    try:
        if """{"users":[]}""" in r.text:
            print("> Duolingo")

        else:
            username = r.json()["users"][0]["username"]

            if username is not None and username != "":
                print("[+] Account found in duolingo, with username: {username}")

            else:
                print("[-] Account not found in duolingo.")

    except Exception as e:
        print("An error occurred:", e)
