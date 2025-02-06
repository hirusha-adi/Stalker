import requests
from utils import errors

@errors.handle_errors
def start():
    """Fetch and display a list of breached domains."""
    print("Fetching List of Breached Domains...\n")
    response = requests.get("https://haveibeenpwned.com/api/v3/breaches")
    data = response.json()

    if data:
        for item in data:
            domain_name = item.get('Domain')
            if domain_name:
                print(domain_name)
        print(f"\nTotal: {len(data)}")
    else:
        print("No breached domains found.")
