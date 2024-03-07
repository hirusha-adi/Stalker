def banner_home():
    print(
        """
 ╔═╗┌┬┐┌─┐┬  ┬┌─┌─┐┬─┐
 ╚═╗ │ ├─┤│  ├┴┐├┤ ├┬┘
 ╚═╝ ┴ ┴ ┴┴─┘┴ ┴└─┘┴└─
  Welcome to Stalker!
 
Type help for more info
"""
    )


def help_home():
    print(
        """
Available modules:
    accounts

Available commands:
    exit
    
Global commands:
    quit
        """
    )


def help_usernames():
    print(
        """
Available commands:
    lookup <username>
    open <username>
    list <username>
    save <username> [txt/json/csv]
    history
        """
    )
