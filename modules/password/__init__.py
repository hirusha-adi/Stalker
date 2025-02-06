"""
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
        python stalker.py "pastebin" "admin"
        python stalker.py "pastebin" admin123
        python stalker.py "pastebin" "admin123%$686%^&"

haveibeenpwned/check
    - Description
        Check how many times your password has been breached
        using the API of haveibeenpawned.com
    - Usage
        python stalker.py "haveibeenpwned/check" <password>
    - Examples
        python stalker.py "haveibeenpwned/check" "admin"
        python stalker.py "haveibeenpwned/check" admin123
        python stalker.py "haveibeenpwned/check" "admin123%$686%^&"
    
haveibeenpwned/range
    - Description
        Use google dorks to find information about the given amazon username.
    - Usage
        python stalker.py "haveibeenpwned/range" <password>
    - Examples
        python stalker.py "haveibeenpwned/range" "admin"
        python stalker.py "haveibeenpwned/range" admin123
        python stalker.py "haveibeenpwned/range" "admin123%$686%^&"

"""

from ._handle import handler
