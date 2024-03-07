import os
import sys
import json
import typing as t
from concurrent.futures import ThreadPoolExecutor

import requests
from tabulate import tabulate
from urllib.parse import urlparse
from urllib.parse import ParseResult

from utils import texts


def extract_main_url(input_url: str) -> str:
    try:
        parsed_url: ParseResult = urlparse(input_url)
        main_url = f"{parsed_url.scheme}://{parsed_url.netloc}/"
        return main_url
    except:
        return input_url


def check_username_on_site(
    site: dict, username: str, session: requests.sessions.Session
) -> bool:
    uri: str = site.get("uri_check", "")
    method: str = site.get("method", "GET")
    payload: t.Union[str, dict] = site.get("post_body", {})
    headers: dict = site.get("headers", {})
    found_accounts = []

    if uri == "":
        return False

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
            account_info = {
                "id": len(found_accounts) + 1,
                "username": username,
                "name": site.get("name"),
                "url_main": extract_main_url(final_url),
                "url_user": final_url,
                "exists": "Claimed",
                "http_status": response.status_code,
                "response_time_s": f"",
            }
            found_accounts.append(account_info)
            print(
                f"""
Found {username} on {site.get("name")}:
    ID: ...
    Username: {username}
    Platform Name: {site.get("name")}
    Platform URL: {extract_main_url(final_url)}
    User Profile URL: {final_url}
    Exists: Claimed
    HTTP Status: {response.status_code}
    Response Time (s): {response.elapsed.total_seconds():.3f}
                  """
            )
            return True
        elif (
            response.status_code == site["m_code"] and site["m_string"] in response.text
        ):
            return False

    except requests.exceptions.RequestException as req_err:
        print(f"Error occurred for {site['name']} - {req_err}")

    return False


class Vars:
    username_folder_path: t.Union[str, os.PathLike] = os.path.join(
        os.getcwd(), "history", "usernames"
    )
    history: t.List[dict] = []


def init() -> None:
    if not os.path.isdir(Vars.username_folder_path):
        os.makedirs(Vars.username_folder_path)


def start() -> None:
    while True:
        inp: str = input("[usernames] >> ").strip()

        if inp == "help":
            texts.help_usernames()

        elif inp == "history":
            files = os.listdir(Vars.username_folder_path)
            if len(files) == 0:
                print("No history!")
            else:
                for filename in files:
                    with open(filename, "r", encoding="utf-8") as file:
                        Vars.history.append(json.load(file))
                data = []
                for dat in Vars.history:
                    data.append(
                        [
                            dat["status"]["name"],
                            dat["status"]["total"],
                            dat["status"]["time"],
                        ]
                    )
                headers = ["Name", "Total", "Time"]
                print(tabulate(data, headers=headers, tablefmt="grid"))

        elif inp.startswith("lookup"):
            username = inp[7:]
            final_data = {
                "status": {"name": username, "total": 0, "time": 0},
                "accounts": [],
            }
            support_file = os.path.join(os.getcwd(), "support", "wmn-data.json")
            try:
                response = requests.get(
                    "https://raw.githubusercontent.com/WebBreacher/WhatsMyName/main/wmn-data.json"
                )
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
                print(f"Username {username} not found on any site.")
            else:
                # SAVE HISTORY JSON
                print(f"Found accounts have been saved temporarily in:")

        elif inp == "exit":
            break
        elif inp == "quit":
            print("Quitting!")
            sys.exit("")
        else:
            pass
    return
