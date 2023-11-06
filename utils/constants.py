import os

if os.name == 'nt':
    python = 'python'
    pip = 'pip'
else:
    python = 'python3'
    pip = 'pip3'


class Path:
    home = os.getcwd()
    session = os.path.join(home, 'session')
