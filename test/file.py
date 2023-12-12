import requests
import json
from concurrent.futures import ThreadPoolExecutor

found_accounts = []

def check_username_on_site(site, username):
    uri = site.get("uri_check")
    method = site.get("method", "GET")
    payload = site.get("post_body", {})
    headers = site.get("headers", {})

    if method == "GET":
        response = requests.get(uri.format(account=username), headers=headers)
    elif method == "POST":
        response = requests.post(uri, data=payload, headers=headers)

    if response.status_code == site["e_code"] and site["e_string"] in response.text:
        account_info = {
            "id": len(found_accounts) + 1,
            "username": username,
            "name": site.get("name"),
            "url_main": site.get("url_main", ""),
            "url_user": site.get("url_user", ""),
            "exists": "Claimed",
            "http_status": response.status_code,
            "response_time_s": f"{response.elapsed.total_seconds():.3f}",
        }
        found_accounts.append(account_info)
        print(f"Username {username} found on {site['name']} ({site['cat']} category)")
        return True
    elif response.status_code == site["m_code"] and site["m_string"] in response.text:
        print(f"Username {username} not found on {site['name']} ({site['cat']} category)")
    return False

def check_username(username):
    with open('wmn-data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(check_username_on_site, site, username) for site in data["sites"]]
        results = [future.result() for future in futures]

    if not any(results):
        print(f"Username {username} not found on any site.")
    else:
        print("\nFound Accounts:")
        for account_info in found_accounts:
            print(account_info)

if __name__ == "__main__":
    username_to_check = input("Enter the username to check: ")
    check_username(username_to_check)
