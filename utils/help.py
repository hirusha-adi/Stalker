
def main_help():
    print("""
Program usage: 
    python3 stalker.py <module> [arguments]
          """)

def username_help():
    print("""
Module Name: `username`

Modules List
------------

Sub-modules ->
    username/search/lookup - Username search engine
    username/search/directory - Names directory
    username/specific/amazon - Amazon username search
    username/specific/github - Github username search


Modules Help
------------

username/search/lookup
    - Description
        Made using the WebBreacher/WhatsMyName list. 
        Provides a similar functionality to https://whatsmyname.app/ using Python.
    - Usage
        python stalker.py "username/search/lookup" <username>
    - Examples
        python stalker.py "username/search/lookup" "hirusha-adi"

username/search/directory
    - Description
        Name Directory. 
        Will scrape https://namesdir.com/ and print the names list.
    - Usage
        python stalker.py "username/search/directory" <name> <name_type>
    - Examples
        python stalker.py "username/search/directory" John first
        python stalker.py "username/search/directory" Doe last
    
username/specific/amazon
    - Description
        Use google dorks to find information about the given amazon username.
    - Usage
        python stalker.py "username/specific/amazon" <username>
    - Examples
        python stalker.py "username/specific/amazon" "hirusha-adi"

username/specific/github
    - Description
        Use GitHub's API to get the past events of a given username.
    - Usage
        python stalker.py "username/specific/github" <username>
    - Examples
        python stalker.py "username/specific/github" "hirusha-adi"
""")
    
    
def password_help():
    print("""
Module Name: `password`

Modules List
------------

Sub-modules ->
    pastebin - Search for pastebin dumps
    haveibeenpwned/check - Check if pawned?
    haveibeenpwned/range - List pawned sha-1 suffixes.


Modules Help
------------

pastebin
    - Description
        Scan for public password dumps in pastebin
        Utilizing google dorks  
    - Usage
        python stalker.py "pastebin" <password>
    - Examples
        python stalker.py "pastebin" "admin123%$686%^&"

haveibeenpwned/check
    - Description
        Check how many times your password has been breached
        using the API of haveibeenpawned.com
    - Usage
        python stalker.py "haveibeenpwned/check" <password>
    - Examples
        python stalker.py "haveibeenpwned/check" "admin123%$686%^&"
    
haveibeenpwned/range
    - Description
        Use google dorks to find information about the given amazon username.
    - Usage
        python stalker.py "haveibeenpwned/range" <password>
    - Examples
        python stalker.py "haveibeenpwned/range" "admin123%$686%^&"
""")