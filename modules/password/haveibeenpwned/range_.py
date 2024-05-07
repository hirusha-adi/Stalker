import pwnedpasswords
from tabulate import tabulate
from utils import errors

@errors.handle_errors
def start(password: str) -> None:
    x = pwnedpasswords.range(password)
    print(tabulate(x.items(), headers=['SHA-1 Hash Suffix', 'Frequency']))
    