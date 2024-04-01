import os
import typing as t


class Vars:
    history_folder_path: t.Union[str, os.PathLike] = os.path.join(
        os.getcwd(), "history"
    )

    username_folder_path: t.Union[str, os.PathLike] = os.path.join(
        history_folder_path, "usernames"
    )

    history: t.List[dict] = []


def init() -> None:
    if not os.path.isdir(Vars.username_folder_path):
        os.makedirs(Vars.username_folder_path)
