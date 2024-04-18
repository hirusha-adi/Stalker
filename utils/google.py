from googlesearch import search

def search_google(query: str) -> None:
    for item in search(f"{query}", advanced=True):
            print(f"""
[+] Result:
    Title: {item.title}
    URL: {item.description}
    Description: {item.url}
                """)