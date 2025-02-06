import requests
from utils import errors

@errors.handle_errors
def start(domain):
    """Check if the specified domain has been breached."""
    print(f"Checking Breach status for Domain: {domain}...")
    response = requests.get(f"https://haveibeenpwned.com/api/v3/breaches?domain={domain}")
    data = response.json()

    if data:
        for item in data:
            print(f"Breach: {item.get('Title')}, Domain: {item.get('Domain')}")
    else:
        print("Domain not found in any breaches.")
