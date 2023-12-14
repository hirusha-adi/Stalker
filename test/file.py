import requests
import json
from concurrent.futures import ThreadPoolExecutor

found_accounts = []

from urllib.parse import urlparse

def extract_main_url(input_url):
    try:
        parsed_url = urlparse(input_url)
        main_url = f"{parsed_url.scheme}://{parsed_url.netloc}/"
        return main_url
    except:
        return input_url 

def check_username_on_site(site, username):
    uri = site.get("uri_check")
    method = site.get("method", "GET")
    payload = site.get("post_body", {})
    headers = site.get("headers", {})

    try:
        if method == "GET":
            final_url = uri.format(account=username)
            response = requests.get(final_url, headers=headers, timeout=10)
        elif method == "POST":
            final_url = uri
            response = requests.post(final_url, data=payload, headers=headers, timeout=10)

        response.raise_for_status()  # Raise HTTPError for bad responses

        if response.status_code == site["e_code"] and site["e_string"] in response.text:
            account_info = {
                "id": len(found_accounts) + 1,
                "username": username,
                "name": site.get("name"),
                "url_main": extract_main_url(final_url),
                "url_user": final_url,
                "exists": "Claimed",
                "http_status": response.status_code,
                "response_time_s": f"{response.elapsed.total_seconds():.3f}",
            }
            found_accounts.append(account_info)
            print(f"Username {username} found on {site['name']} ({site['cat']} category)")
            return True
        elif response.status_code == site["m_code"] and site["m_string"] in response.text:
            print(f"Username {username} not found on {site['name']} ({site['cat']} category)")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Request timed out: {timeout_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

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
