import os
import json
import typing as t
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from urllib.parse import urlparse, ParseResult
from tqdm import tqdm


def extract_main_url(input_url: str) -> str:
    try:
        parsed_url: ParseResult = urlparse(input_url)
        main_url = f"{parsed_url.scheme}://{parsed_url.netloc}/"
        return main_url
    except:
        return input_url


def check_username_on_site(
    site: dict, username: str, session: requests.sessions.Session
) -> None:
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
            response = session.post(
                final_url, data=payload, headers=headers, timeout=10
            )

        response.raise_for_status()

        if response.status_code == site["e_code"] and site["e_string"] in response.text:
            print(
                f"""
[+] Found {username} on {site.get("name")}:
    - Username: {username}
    - Platform Name: {site.get("name")}
    - Platform URL: {extract_main_url(final_url)}
    - User Profile URL: {final_url}
    - Exists: Claimed
    - HTTP Status: {response.status_code}
    - Response Time (s): {response.elapsed.total_seconds():.3f}
                  """
            )

        elif (
            response.status_code == site["m_code"] and site["m_string"] in response.text
        ):
            return None  # Not found

    except requests.exceptions.RequestException:
        return None  # Handle request failure


def start(username: str) -> None:
    support_file = os.path.join(os.getcwd(), "support", "wmn-data.json")
    if not os.path.isfile(support_file):
        try:
            response = requests.get(
                "https://raw.githubusercontent.com/WebBreacher/WhatsMyName/main/wmn-data.json"
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as req_err:
            print(f"Request exception occurred: {req_err}")
            return
        else:
            with open(support_file, "wb") as f:
                f.write(response.content)

    with open(support_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    sites = data["sites"]

    with ThreadPoolExecutor() as executor, requests.Session() as session, tqdm(
        total=len(sites), desc="Checking sites", unit="site"
    ) as progress_bar:
        futures = {executor.submit(
            check_username_on_site, site, username, session): site for site in sites}

        for future in as_completed(futures):
            future.result()  # Wait for completion
            progress_bar.update(1)  # Update tqdm progress

    print(f"[-] Username {username} not found on any site.")
