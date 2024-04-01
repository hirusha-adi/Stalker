def banner_home() -> None:
    print(
        """
 ╔═╗┌┬┐┌─┐┬  ┬┌─┌─┐┬─┐
 ╚═╗ │ ├─┤│  ├┴┐├┤ ├┬┘
 ╚═╝ ┴ ┴ ┴┴─┘┴ ┴└─┘┴└─
  Welcome to Stalker!
 
Type help for more info
"""
    )


def help_home() -> None:
    print(
        """
Available modules:
    usernames

Available commands:
    exit
    
Global commands:
    quit
        """
    )


def help_usernames() -> None:
    print(
        """
Available commands:
    lookup <username>
    open <username>
    list <username>
    save <username> [txt/json/csv]
    history
    history show <username> [i=interactive]
        """
    )
