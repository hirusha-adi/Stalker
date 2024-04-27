import requests


def start(email: str):
    url = f"https://www.strava.com/athletes/email_unique?email={email}"
    response = requests.get(url)
    try:
        if "false" in response.text:
            print("[+] Account found in Strava.")
        # elif "true" in response.text:
        else:
            print("[+] Account not found in Strava.")
    except Exception as e:
        print("An error occurred:", e)
