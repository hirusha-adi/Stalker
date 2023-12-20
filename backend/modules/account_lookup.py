import requests
import json
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

class AccountLookup:
    def __init__(self) -> None:
        self.found_accounts = []
    
    def extract_main_url(self, input_url):
        try:
            parsed_url = urlparse(input_url)
            main_url = f"{parsed_url.scheme}://{parsed_url.netloc}/"
            return main_url
        except:
            return input_url 
    
    def check_username_on_site(self, site, username, session):
        uri = site.get("uri_check")
        method = site.get("method", "GET")
        payload = site.get("post_body", {})
        headers = site.get("headers", {})

        try:
            if method == "GET":
                final_url = uri.format(account=username)
                response = session.get(final_url, headers=headers, timeout=10)
            elif method == "POST":
                final_url = uri
                response = session.post(final_url, data=payload, headers=headers, timeout=10)

            response.raise_for_status()

            if response.status_code == site["e_code"] and site["e_string"] in response.text:
                account_info = {
                    "id": len(self.found_accounts) + 1,
                    "username": username,
                    "name": site.get("name"),
                    "url_main": self.extract_main_url(final_url),
                    "url_user": final_url,
                    "exists": "Claimed",
                    "http_status": response.status_code,
                    "response_time_s": f"{response.elapsed.total_seconds():.3f}",
                }
                self.found_accounts.append(account_info)
                return True
            elif response.status_code == site["m_code"] and site["m_string"] in response.text:
                return False

        except requests.exceptions.RequestException as req_err:
            print(f"Error occurred for {site['name']} - {req_err}")

        return False

    def check_username(self, username):
        with open('wmn-data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        with ThreadPoolExecutor() as executor, requests.Session() as session:
            futures = [executor.submit(self.check_username_on_site, site, username, session) for site in data["sites"]]
            results = [future.result() for future in futures]

        if not any(results):
            print(f"Username {username} not found on any site.")
        else:
            print("\nFound Accounts:")
            for account_info in self.found_accounts:
                print(account_info)

