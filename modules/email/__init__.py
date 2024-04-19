"""
Module Name: `email`

Modules List
------------

Sub-modules ->
    email/specific/github - Users/Organizations associated with the email
    email/specific/chess_com - Check if account exists under this email
    email/specific/deezer - Check if account exists under this email


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

email/specific/chess_com
    - Description
        CHeck if an account exists for the given email address
    - Usage
        python stalker.py "email/specific/chess_com" <email>
    - Example
        python stalker.py "email/specific/chess_com" "johndoe@gmail.com"
        python stalker.py "email/specific/chess_com" "janedoe@protonmail.com"

email/specific/deezer
    - Description
        CHeck if an account exists for the given email address
    - Usage
        python stalker.py "email/specific/deezer" <email>
    - Example
        python stalker.py "email/specific/deezer" "johndoe@gmail.com"
        python stalker.py "email/specific/deezer" "janedoe@protonmail.com"

"""

from ._handle import handler
