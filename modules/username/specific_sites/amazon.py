from utils import search_google
from utils import errors


@errors.handle_errors
def start(username: str):
    search_google(f'site:amazon.com "{username}"')
