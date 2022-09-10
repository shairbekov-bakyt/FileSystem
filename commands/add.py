import shutil

from config import BASE_DIR
from helpers.helper_add import helper_add


@helper_add
def add_file(from_path: str) -> None:
    shutil.copy(from_path, BASE_DIR)
    print(f"file {from_path} successfully copied")
