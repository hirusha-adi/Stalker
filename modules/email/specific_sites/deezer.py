import requests

def start(email: str):
    try:
        s = requests.Session()

        r = s.post("https://www.deezer.com/ajax/gw-light.php?method=deezer.getUserData&input=3&api_version=1.0&api_token=&cid=")
        token = r.json()['results']['checkForm']

        params = {
            'method': 'deezer.emailCheck',
            'input': 3,
            'api_version': 1.0,
            'api_token': token,
        }

        data = '{"EMAIL":"' + email + '"}'

        api = s.post("https://www.deezer.com/ajax/gw-light.php", params=params, data=data)

        if api.json()['results']['availability'] == True:
            print(f"[-] Account not found in deezer")

        elif api.json()['results']['availability'] == False:
            print(f"[+] Account found in deezer")

        s.close()

    except Exception as e:
        print("An error occurred:", e)
        s.close()
