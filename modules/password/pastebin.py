from utils import search_google
from utils import decorators


@decorators.handle_errors
def start(password: str):
    search_google(f'site:pastebin.com "{password}"')
    
