import pathlib

from config import BASE_DIR


def helper_add(func):
    def wrapper(*args, **kwargs):
        from_path = args[0]
        name = pathlib.Path(from_path).name

        if not pathlib.Path(from_path).exists():
            print(f"file not found {from_path}")
            exit(0)

        if pathlib.Path(f"{BASE_DIR}{name}").exists():
            print(f"File system already has {from_path}")
            exit(0)


        func(from_path)

    return wrapper