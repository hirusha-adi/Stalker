"""
Module Name: `phonenumber`

Modules List
------------

Sub-modules ->
    phonenumber/phoneinfoga/dorks - get a list of google droks
    phonenumber/phoneinfoga/search - get a list of google droks and search it


Modules Help
------------

phonenumber/phoneinfoga/dorks
    - Description
        Get a list of google dorks queries containing the given phone number
    - Usage
        python stalker.py "phonenumber/phoneinfoga/dorks" <phone_number>
    - Example
        python stalker.py "phonenumber/phoneinfoga/dorks" "+94099889888"

phonenumber/phoneinfoga/search
    - Description
        Get a list of google dorks queries containing the given phone number
        and google search it, and get the result URLs
    - Usage
        python stalker.py "phonenumber/phoneinfoga/search" <phone_number>
    - Example
        python stalker.py "phonenumber/phoneinfoga/search" "+94099889888"
"""

from ._handle import handler
