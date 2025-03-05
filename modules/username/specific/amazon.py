from utils import search_google
from utils import decorators


@decorators.handle_errors
def start(username: str):
    search_google(f'site:amazon.com "{username}"')
