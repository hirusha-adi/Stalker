import requests
from tabulate import tabulate
from utils import decorators

@decorators.handle_errors
def start(email, domain):
    """Check if the email address has been breached for a specific domain."""
    print(f"Checking Breach status for {email}...")
    response = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}?domain={domain}")
    data = response.json()

    if data:
        headers = ["Breach", "Domain", "Date", "Breached Info", "Fabricated", "Verified", "Retired", "Spam"]
        breach_info = [[
            item.get("Title", ""), item.get("Domain", ""), item.get("BreachDate", ""),
            ", ".join(item.get("DataClasses", [])), item.get("IsFabricated", ""),
            item.get("IsVerified", ""), item.get("IsRetired", ""), item.get("IsSpamList", "")
        ] for item in data]
        print(tabulate(breach_info, headers=headers, tablefmt="grid"))
    else:
        print("No breaches found.")
