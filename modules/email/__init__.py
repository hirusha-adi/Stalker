"""
Module Name: `email`

Modules List
------------

Sub-modules ->
    email/specific/github - Users/Organizations associated with emails


Modules Help
------------

email/specific/github
    - Description
        Use GitHub's official API to get accounts and organizations
        associated with the given email address.
    - Usage
        python stalker.py "email/specific/github" <email>
    - Example
        python stalker.py "email/specific/github" "johndoe@gmail.com"
        python stalker.py "email/specific/github" "janedoe@protonmail.com"

"""

from ._handle import handler
