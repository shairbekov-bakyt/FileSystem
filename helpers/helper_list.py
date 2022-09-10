import pathlib

from config import BASE_DIR


def helper_list(func):
    def wrapper(*args, **kwargs):
        if len(args) != 0:
            print("command list not take any arguments")
            exit(0)

        if not pathlib.Path(BASE_DIR).exists():
            print("File system not initialized")
            exit(0)

        func()

    return wrapper