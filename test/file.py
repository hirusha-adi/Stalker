import requests
import json
from concurrent.futures import ThreadPoolExecutor

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

if __name__ == "__main__":
    username_to_check = input("Enter the username to check: ")
    check_username(username_to_check)
