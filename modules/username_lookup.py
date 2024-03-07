import os
import sys
import json
import typing as t

from tabulate import tabulate

from utils import texts


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

        elif inp == "exit":
            break
        elif inp == "quit":
            print("Quitting!")
            sys.exit("")
        else:
            pass
    return
