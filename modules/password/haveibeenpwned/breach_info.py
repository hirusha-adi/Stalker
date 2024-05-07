import requests
from tabulate import tabulate
from utils import errors

@errors.handle_errors
def start(breach_name):
    """Get information about a specific breach."""
    print(f"Getting information about breach: {breach_name}...")
    response = requests.get(f"https://haveibeenpwned.com/api/v3/breach/{breach_name}")
    data = response.json()

    if data:
        headers = ["Breach", "Domain", "Date", "Pwn Count", "Fabricated", "Verified", "Retired", "Spam", "Description"]
        breach_info = [[
            data.get("Title", ""), data.get("Domain", ""), data.get("BreachDate", ""),
            data.get("PwnCount", ""), data.get("IsFabricated", ""),
            data.get("IsVerified", ""), data.get("IsRetired", ""), data.get("IsSpamList", ""),
            data.get("Description", "")
        ]]
        print(tabulate(breach_info, headers=headers, tablefmt="grid"))
    else:
        print("Breach not found.")
