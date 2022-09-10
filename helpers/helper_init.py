import pathlib

from config import BASE_DIR


def helper_init(func):
    def wrapper(*args, **kwargs):
        if pathlib.Path(BASE_DIR).exists():
            print("File system already initialized")
            exit(0)

        func()

    return wrapper