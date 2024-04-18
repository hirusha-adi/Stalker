import re

import requests
from bs4 import BeautifulSoup

def request_page(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        ul_tag = soup.find('ul', class_='limheight')
        if ul_tag:
            li_tags = ul_tag.find_all('li')
            for li_tag in li_tags:
                name_text = li_tag.text.strip()
                name_text = re.sub(r'\d', '', name_text)
                print(name_text)

    else:
        print(f"[!!] Failed to fetch data from the website. Visit {url}")
        return None

def start(name: str, first_or_last: str):
    if first_or_last.lower() == "first":
        url = f"https://namesdir.com/F_{name}"
    elif first_or_last.lower() == "last":
        url = f"https://namesdir.com/S_{name}"
    else:
        print("[!!] Invalid arguments passed for `name_type`")
        return
        
    request_page(url=url)
