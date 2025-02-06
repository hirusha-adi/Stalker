import requests
from utils import errors


@errors.handle_errors
def start(email: str):
    r = requests.get(f"https://api.github.com/search/users?q={email}+in:email")

    data = r.json()
    total_count = data.get("total_count", 0)

    if total_count == 0:
        print("[-] Account not found in Github")
    else:
        print(f"[+] Accounts found in GitHub: {total_count}")
        print("----------")
        for item in data.get("items", []):
            print("Username:", item.get("login"))
            print("ID:", item.get("id"))
            print("Node ID:", item.get("node_id"))
            print("Avatar URL:", item.get("avatar_url"))
            print("Gravatar ID:", item.get("gravatar_id"))
            print("Profile URL:", item.get("html_url"))
            print("Followers URL:", item.get("followers_url"))
            print("Following URL:", item.get("following_url"))
            print("Gists URL:", item.get("gists_url"))
            print("Starred URL:", item.get("starred_url"))
            print("Subscriptions URL:", item.get("subscriptions_url"))
            print("Organizations URL:", item.get("organizations_url"))
            print("Repos URL:", item.get("repos_url"))
            print("Events URL:", item.get("events_url"))
            print("Received Events URL:", item.get("received_events_url"))
            print("Type:", item.get("type"))
            print("Site Admin:", item.get("site_admin"))
            print("Score:", item.get("score"))
            print("----------")
