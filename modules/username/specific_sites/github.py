import requests
from utils import errors


@errors.handle_errors
def start(username):
    response = requests.get(f"https://api.github.com/users/{username}/events/public")

    if response.status_code == 200:
        data = response.json()
        for event in data:
            print("Event Type:", event["type"])
            print("Actor:")
            print("  ID:", event["actor"]["id"])
            print("  Login:", event["actor"]["login"])
            print("  Avatar URL:", event["actor"]["avatar_url"])
            print("Repository:")
            print("  ID:", event["repo"]["id"])
            print("  Name:", event["repo"]["name"])
            print("Payload:")
            payload = event.get("payload", {})
            if payload:
                print("  Size:", payload.get("size", "N/A"))
                print("  Ref:", payload.get("ref", "N/A"))
                print("  Head:", payload.get("head", "N/A"))
                print("  Before:", payload.get("before", "N/A"))
                commits = payload.get("commits", [])
                print("  Commits:")
                for commit in commits:
                    print("    Commit SHA:", commit["sha"])
                    print("    Author:", commit["author"]["name"])
                    print("    Message:", commit["message"])
                    print("    URL:", commit["url"])
                    print()
            else:
                print("  No payload available.")
            print("Public:", event["public"])
            print("Created At:", event["created_at"])
            print("-" * 50)
    else:
        print(
            f"Failed to fetch data from the GitHub API. Status code: {response.status_code}"
        )
