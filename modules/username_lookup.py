import os
import sys
import json
import typing as t
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

from matplotlib import is_interactive
import requests
from tabulate import tabulate
from urllib.parse import urlparse
from urllib.parse import ParseResult

from utils import texts
from utils.vars import Vars


def extract_main_url(input_url: str) -> str:
    try:
        parsed_url: ParseResult = urlparse(input_url)
        main_url = f"{parsed_url.scheme}://{parsed_url.netloc}/"
        return main_url
    except:
        return input_url


def check_username_on_site(
    site: dict, username: str, session: requests.sessions.Session, final_data: dict
) -> bool:
    uri: str = site.get("uri_check", "")
    method: str = site.get("method", "GET")
    payload: t.Union[str, dict] = site.get("post_body", {})
    headers: dict = site.get("headers", {})

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
            final_data["status"]["total"] += 1
            final_data["accounts"].append(
                {
                    "id": final_data["status"]["total"],
                    "username": username,
                    "name": site.get("name"),
                    "url_main": extract_main_url(final_url),
                    "url_user": final_url,
                    "exists": "Claimed",
                    "http_status": response.status_code,
                    "response_time_s": f"",
                }
            )
            print(
                f"""
Found {username} on {site.get("name")}:
    ID: {final_data["status"]["total"]}
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


def start() -> None:
    while True:
        inp: str = input("[usernames] >> ").strip()

        if inp == "help":
            texts.help_usernames()

        elif inp.startswith("history show"):
            is_interactive = False
            username = inp.split("show")[-1].strip()
            try:
                last_arg = username.split(" ")
                if last_arg[-1] in ("i", "interactive"):
                    is_interactive = True
                    username = last_arg[0]
            except IndexError:
                pass

            print(f"Results for: {username}")
            i = 0
            for his in Vars.history:
                print(
                    his["status"]["name"],
                    username,
                    (his["status"]["name"] == username),
                    is_interactive,
                )
                if his["status"]["name"] == username:
                    i += 1
                    print(f"Displaying result {i}.\n")
                    print(
                        tabulate(
                            data, headers=["Name", "Total", "Time"], tablefmt="grid"
                        )
                    )
                    if is_interactive:
                        print("\nPress [ENTER] to go to next account!")
                    for acc in his["accounts"]:
                        print(
                            f"""
Found {username} on {acc['name']}:
    ID: {acc['id']}
    Username: {acc['username']}
    Platform Name: {acc['name']}
    Platform URL: {acc['url_main']}
    User Profile URL: {acc['url_user']}
    Exists: {acc['exists']}
    HTTP Status: {acc['http_status']}
    Response Time (s): {acc['response_time_s']}"""
                        )
                        if is_interactive:
                            input("")

        elif inp == "history":
            files = os.listdir(Vars.username_folder_path)
            if len(files) == 0:
                print("No history!")
            else:
                for filename in files:
                    with open(
                        os.path.join(Vars.username_folder_path, filename),
                        "r",
                        encoding="utf-8",
                    ) as file:
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
                print(
                    tabulate(data, headers=["Name", "Total", "Time"], tablefmt="grid")
                )

        elif inp.startswith("lookup"):
            username = inp[7:]
            final_data = {
                "status": {"name": username, "total": 0, "time": f"{datetime.now()}"},
                "accounts": [],
            }
            support_file = os.path.join(os.getcwd(), "support", "wmn-data.json")
            if not os.path.isfile(support_file):
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
                        print(
                            f"Unexpected response status code: {response.status_code}"
                        )

            with open(support_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            with ThreadPoolExecutor() as executor, requests.Session() as session:
                futures = [
                    executor.submit(
                        check_username_on_site, site, username, session, final_data
                    )
                    for site in data["sites"]
                ]
                results = [future.result() for future in futures]

            if not any(results):
                print(f"Username {username} not found on any site.")
            else:
                file_path = os.path.join(Vars.username_folder_path, f"{username}.json")
                try:
                    with open(file_path, "w") as json_file:
                        json.dump(final_data, json_file, indent=4)
                    print(
                        f"Found accounts have been saved temporarily in: {file_path} for the history functionality."
                    )
                except Exception as e:
                    print(f"Error occurred while saving JSON data: {e}")

        elif inp == "exit":
            break
        elif inp == "quit":
            print("Quitting!")
            sys.exit()
        else:
            pass
    return
