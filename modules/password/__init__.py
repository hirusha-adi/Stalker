"""
Module Name: `username`

Modules List
------------

Sub-modules ->
    username/search/lookup - Username search engine
    username/search/directory - Names directory
    username/specific/amazon - Amazon username search
    username/specific/github - Github username search

Not implemented yet (To-DO) ->
    username/specific/tinder - Tinder username search
    username/specific/pgp - MIT PGP Key Server

Modules Help
------------

username/search/lookup
    - Description
        Made using the WebBreacher/WhatsMyName list. 
        Provides a similar functionality to https://whatsmyname.app/ using Python.
    - Usage
        python stalker.py "username/search/lookup" <username>
    - Examples
        python stalker.py "username/search/lookup" hirusha-adi
        python stalker.py "username/search/lookup" hirusha_adi
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
        python stalker.py "username/specific/amazon" hirusha-adi
        python stalker.py "username/specific/amazon" hirusha_adi
        python stalker.py "username/specific/amazon" "hirusha-adi"

username/specific/github
    - Description
        Use GitHub's API to get the past events of a given username.
    - Usage
        python stalker.py "username/specific/github" <username>
    - Examples
        python stalker.py "username/specific/github" hirusha-adi
        python stalker.py "username/specific/github" hirusha_adi
        python stalker.py "username/specific/github" "hirusha-adi"
"""

from ._handle import handler
