import os
import json
import typing as t
from concurrent.futures import ThreadPoolExecutor

import requests
from urllib.parse import urlparse
from urllib.parse import ParseResult

def extract_main_url(input_url: str) -> str:
    try:
        parsed_url: ParseResult = urlparse(input_url)
        main_url = f"{parsed_url.scheme}://{parsed_url.netloc}/"
        return main_url
    except:
        return input_url
    
def check_username_on_site(site: dict, username: str, session: requests.sessions.Session) -> None:
    uri: str = site.get("uri_check", "")
    method: str = site.get("method", "GET")
    payload: t.Union[str, dict] = site.get("post_body", {})
    headers: dict = site.get("headers", {})

    if uri == "":
        print("[!!] No URI")
        return

    try:
        if method == "GET":
            final_url = uri.format(account=username)
            response = session.get(final_url, headers=headers, timeout=10)
        elif method == "POST":
            final_url = uri
            response = session.post(final_url, data=payload, headers=headers, timeout=10)

        response.raise_for_status()

        if response.status_code == site["e_code"] and site["e_string"] in response.text:
            print(f"""
[+] Found {username} on {site.get("name")}:
    - Username: {username}
    - Platform Name: {site.get("name")}
    - Platform URL: {extract_main_url(final_url)}
    - User Profile URL: {final_url}
    - Exists: Claimed
    - HTTP Status: {response.status_code}
    - Response Time (s): {response.elapsed.total_seconds():.3f}
                  """)
            
        elif (response.status_code == site["m_code"] and site["m_string"] in response.text):
            print("None")

    except requests.exceptions.RequestException as req_err:
        print(f"Error occurred for {site['name']} - {req_err}")
    
def start(username: str) -> None:
    support_file = os.path.join(os.getcwd(), "support", "wmn-data.json")
    if not os.path.isfile(support_file):
        try:
            response = requests.get("https://raw.githubusercontent.com/WebBreacher/WhatsMyName/main/wmn-data.json")
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Request exception occurred: {req_err}")
        else:
            if response.status_code == 200:
                with open(support_file, "wb") as f:
                    f.write(response.content)
                print(f"File downloaded and saved to: {support_file}")
            else:
                print(f"Unexpected response status code: {response.status_code}")

    with open(support_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    with ThreadPoolExecutor() as executor, requests.Session() as session:
        futures = [
            executor.submit(check_username_on_site, site, username, session)
            for site in data["sites"]
        ]
        results = [future.result() for future in futures]

    if not any(results):
        print(f"[-] Username {username} not found on any site.")
