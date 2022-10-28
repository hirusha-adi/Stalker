import os
import typing as t

class _Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    
    

def cprint(*texts, c: t.Optional[t.AnyStr] = None):
    """
    Description
        Print Texts to console with style
        
    Parameters
        *texts -> Any
            Values to print to the console
        c -> str
            Color/Style of text,
            should be either: "red", "green", "cyan", "yellow", "bold"
    Examples
        cprint("hi", "hello", c="red")
        cprint("hi", "hello", c="green")
        cprint("hi", "hello", c="cyan")
        cprint("hi", "hello", c="yellow")
        cprint("hi", "hello", c="bold")
    """
    colors = ("red", "green", "yellow", "cyan", "bold")
    if ("NO_COLOR" in os.environ or "ANSI_COLORS_DISABLED" in os.environ) or not(c in colors):
        for text in texts:
            print(text, end=" ")
    else:
        c = c.lower()
        if c == "red":
            for text in texts:
                print(f"{_Colors.RED}{text}", end=f" ")
            print(f"{_Colors.RESET}")
        elif c == "green":
            for text in texts:
                print(f"{_Colors.GREEN}{text}", end=f" ")
            print(f"{_Colors.RESET}")
        elif c == "cyan":
            for text in texts:
                print(f"{_Colors.CYAN}{text}", end=f" ")
            print(f"{_Colors.RESET}")
        elif c == "yellow":
            for text in texts:
                print(f"{_Colors.YELLOW}{text}", end=f" ")
            print(f"{_Colors.RESET}")
        elif c == "bold":
            for text in texts:
                print(f"{_Colors.BOLD}{text}", end=f" ")
            print(f"{_Colors.RESET}")

