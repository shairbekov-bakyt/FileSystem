import pathlib

from config import BASE_DIR


def helper_delete(func):
    def wrapper(*args, **kwargs):
        if len(args) != 1:
            print("del command wait argument")
            exit()

        name = args[0]

        if not pathlib.Path(f"{BASE_DIR}{name}").exists():
            print(f"file {name} not exists")
            exit(0)

        func(name)

    return wrapper