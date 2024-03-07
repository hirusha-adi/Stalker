import os
import sys
import json

from tabulate import tabulate

from utils import texts


class Vars:
    username_folder_path = os.path.join(os.getcwd(), "history", "usernames")
    history = []


def init():
    if not os.path.isdir(Vars.username_folder_path):
        os.makedirs(Vars.username_folder_path)


def start():
    while True:
        inp = input("[usernames] >> ")

        if inp == "help":
            texts.help_usernames()

        elif inp == "history":
            for filename in os.listdir(Vars.username_folder_path):
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
