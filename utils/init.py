import os
import sys


def initializse():
    try:
        if not os.path.isdir('session'):
            os.mkdir('session')
    except Exception as e:
        print(e)
        sys.exit()
