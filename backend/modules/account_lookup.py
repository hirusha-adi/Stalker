import requests
import json
import os
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

class AccountLookup:
    def __init__(self, username):
        """
        Initialize an AccountLookup instance with the given username.

        Parameters:
        - username (str): The username to search for on various sites.
        """
        self.username = username
        self.found_accounts = []
        
        """
        {
            status: {
                error: false,
                error_desc: [],
                show_accounts_custom: false,
                total_accounts: 0,
            },
            found_accounts: [
                {
                  id: 1,
                  username: "hirushaadi",
                  name: "Anilist",
                  url_main: "https://anilist.co/",
                  url_user: "https://anilist.co/user/hirushaadi/",
                  exists: "Claimed",
                  http_status: "200",
                  response_time_s: "4.281000000000859",
                },
            ],
        }
        """
        
        self.final_data = {
            'status': {
                'error': False,
                'error_desc': [],
                'show_accounts_custom': True,
                'total_accounts': 0,
            },
            'found_accounts': [],
        }

    def extract_main_url(self, input_url):
        """
        Extract the main URL from a given input URL.

        Parameters:
        - input_url (str): The URL to extract the main URL from.

        Returns:
        - str: The main URL.
        """
        try:
            parsed_url = urlparse(input_url)
            main_url = f"{parsed_url.scheme}://{parsed_url.netloc}/"
            return main_url
        except Exception:
            return input_url

    def check_username_on_site(self, site, session):
        """
        Check if the given username exists on a specific site.

        Parameters:
        - site (dict): Information about the site to check, including URI, method, payload, etc.
        - session (requests.Session): A session object for making HTTP requests.

        Returns:
        - dict or None: Information about the found account or None if not found.
        """
        uri = site.get("uri_check")
        method = site.get("method", "GET")
        payload = site.get("post_body", {})
        headers = site.get("headers", {})

        try:
            if method == "GET":
                final_url = uri.format(account=self.username)
                response = session.get(final_url, headers=headers, timeout=10)
            elif method == "POST":
                final_url = uri
                response = session.post(final_url, data=payload, headers=headers, timeout=10)

            response.raise_for_status()

            if response.status_code == site["e_code"] and site["e_string"] in response.text:
                account_info = {
                    "id": len(self.found_accounts) + 1,
                    "username": self.username,
                    "name": site.get("name"),
                    "url_main": self.extract_main_url(final_url),
                    "url_user": final_url,
                    "exists": "Claimed",
                    "http_status": response.status_code,
                    "response_time_s": f"{response.elapsed.total_seconds():.3f}",
                }
                self.found_accounts.append(account_info)
                return account_info 
            elif response.status_code == site["m_code"] and site["m_string"] in response.text:
                return None

        except requests.exceptions.RequestException as req_err:
            print(f"Error occurred for {site['name']} - {req_err}")
        
        except Exception as e:
            self.final_data['status']['error'] = True
            self.final_data['status']['error_desc'].append(f"Error occurred for {site['name']}: {e}")

        return None

    def run(self):
        """
        Run the account lookup process.

        Returns:
        - dict: Final data containing information about found accounts and status.
        """
        wmn_data_filename = os.path.join('support', 'wmn-data.json')
        with open(wmn_data_filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        with ThreadPoolExecutor() as executor, requests.Session() as session:
            futures = [executor.submit(self.check_username_on_site, site, session) for site in data["sites"]]
            results = [future.result() for future in futures]

        found_accounts = [account_info for account_info in results if account_info is not None]

        if not found_accounts:
            print(f"Username {self.username} not found on any site.")
            self.final_data['status']['error'] = True
            self.final_data['status']['error_desc'].append(f"Username {self.username} not found on any site.")
            self.final_data['status']['show_accounts_custom'] = False
        else:
            self.final_data['status']['show_accounts_custom'] = True
            self.final_data['found_accounts'] = found_accounts
            self.final_data['status']['total_accounts'] = len(found_accounts)
            
            print("\nFound Accounts:")
            for account_info in found_accounts:
                print(account_info)

        return self.final_data
