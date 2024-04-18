from utils import search_google

def start(username: str):
    search_google(f'site:amazon.com "{username}"')
        