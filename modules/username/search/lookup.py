import os
import json
import typing as t
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from urllib.parse import urlparse, ParseResult
from tqdm import tqdm


HITS: t.List[str] = []


def extract_main_url(input_url: str) -> str:
    try:
        parsed_url: ParseResult = urlparse(input_url)
        main_url = f"{parsed_url.scheme}://{parsed_url.netloc}/"
        return main_url
    except:
        return input_url


def check_username_on_site(
    site: dict, username: str, session: requests.sessions.Session, progress_bar: tqdm
) -> None:
    global HITS

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
            # Temporarily stop the progress bar updates
            progress_bar.set_postfix({"Found": site["name"]}, refresh=True)
            progress_bar.set_description(f"Found on {site['name']}")
            progress_bar.update(1)

            HITS.append(f"""[+] Found {username} on {site.get("name")}:
\t- Username: {username}
\t- Platform Name: {site.get("name")}
\t- Platform URL: {extract_main_url(final_url)}
\t- User Profile URL: {final_url}
\t- Exists: Claimed
\t- HTTP Status: {response.status_code}
\t- Response Time (s): {response.elapsed.total_seconds():.3f}\n""")

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
            check_username_on_site, site, username, session, progress_bar): site for site in sites}

        for future in as_completed(futures):
            future.result()
            progress_bar.update(1)

    if HITS:
        print(f"[+] Username {username} found on the following sites:")
        print(f"="*30)
        for hit in HITS:
            print(hit)
    else:
        print(f"[-] Username {username} not found on any site.")
