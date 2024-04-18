from utils import google_search

def start(username: str):
    google_search(f'site:amazon.com "{username}"')
        