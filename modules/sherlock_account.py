"""
from modules import sherlock_account

username = "hirushaadi"
data = sherlock_account.getSherlock(username=username)
sherlock_account.showSherlock(data=data)
"""

import csv
from utils.constants import *
from utils.support import *
from tabulate import tabulate


def getSherlock(username: str) -> dict:
    # clone repo and run
    # os.system("git clone https://github.com/sherlock-project/sherlock.git")
    # os.chdir("sherlock") # inside: /sherlock
    # os.system(f"{python} sherlock --verbose --no-color --nsfw --csv {username}")
    # os.chdir("../") # inside: /

    # move files to work dir
    # os.system(f"mv ./sherlock/{username}.* ./session/{username}/")
    # os.chdir("../") # inside: ./session/username

    # open and parse data from .csv saved from sherlock
    csv_file = f"{sanitize_username(username)}.csv"
    data = {}
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            username = row["username"]
            name = row["name"]
            # url_main = row["url_main"]
            url_user = row["url_user"]
            exists = row["exists"]
            http_status = int(row["http_status"])
            response_time = float(row["response_time_s"][:3])

            if username not in data:
                data[username] = []

            data[username].append({
                "name": name,
                # "url_main": url_main,
                "url_user": url_user,
                "exists": exists,
                "http_status": http_status,
                "response_time_s": response_time
            })

        return data


def showSherlock(data: dict) -> None:
    for username, services in data.items():
        print(f"Username: {username}")
        headers = services[0].keys()
        rows = [list(service.values()) for service in services]
        print(tabulate(rows, headers, tablefmt="pretty"))


if __name__ == "__main__":
    username = "hirushaadi"
    x = getSherlock(username=username)
    showSherlock(data=x)
