import pathlib

from config import BASE_DIR


def helper_init(func):
    def wrapper(*args, **kwargs):
        if args != 0:
            print("command init not take any arguments")
            exit(0)

        if pathlib.Path(BASE_DIR).exists():
            print("File system already initialized")
            exit(0)

        func()

    return wrapper